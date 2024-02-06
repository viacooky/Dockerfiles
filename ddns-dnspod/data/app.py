# coding:utf-8
import logging
import os
import requests
import json
import argparse
import pathlib
import time
from dataclasses import dataclass

VERSION = '0.0.1'
LOG_FORMAT = '[%(asctime)s][%(levelname)s] - %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)


@dataclass()
class Cfg(object):
    dnspod_id: str = None
    """DNSPOD ID"""
    dnspod_token: str = None
    """dnspod token"""
    domain: str = None
    """默认 域名  格式 domain.com"""
    sub_domain: str = None
    """子域名 格式 www"""
    internal: int = 30
    """最小执行间隔 (秒)"""
    email: str = None
    """邮箱 格式 my@email.com"""
    record_ip: str = None
    """DNSPOD 记录IP"""
    record_id: str = None
    """DNSPOD 记录ID，接口返回"""
    last_update_time: int = 0
    """上次更新时间戳，系统生成"""

    def __init__(self, cfg_file: str = None):
        super().__init__()
        # 初始化
        self.__read_from_env()
        if cfg_file:
            self.__read_from_file(cfg_file)
        self.check_cfg()

    def __read_from_env(self) -> None:
        """从环境变量读取配置
        """
        logging.info('从环境变量读取配置')
        self.dnspod_id = os.getenv('DNSPOD_ID')
        self.dnspod_token = os.getenv('DNSPOD_TOKEN')
        self.domain = os.getenv('DOMAIN')
        self.sub_domain = os.getenv('SUB_DOMAIN')
        self.internal = int(os.getenv('INTERNAL')) if os.getenv('INTERNAL') else 30
        self.email = os.getenv('EMAIL')

    def __read_from_file(self, cfg_file: str) -> None:
        """从文件读取配置
        """
        if not pathlib.Path.exists(cfg_file):
            logging.info(f'找不到文件 {cfg_file}')
            return
        logging.info(f'从文件读取配置 {cfg_file}')
        text = ''
        with open(cfg_file, 'r') as file:
            text = file.read()
        data = json.loads(text)
        self.dnspod_id = data['dnspod_id']
        self.dnspod_token = data['dnspod_token']
        self.domain = data['domain']
        self.sub_domain = data['sub_domain']
        self.internal = int(data['internal'])
        self.email = data['email']

    def check_cfg(self) -> None:
        """检查配置项
        """
        try:
            if (not (self.dnspod_id)):
                raise Exception('配置参数异常：dnspod_id 为空')
            if (not (self.dnspod_token)):
                raise Exception('配置参数异常：dnspod_token 为空')
            if (not (self.domain)):
                raise Exception('配置参数异常：domain 为空')
            if (not (self.sub_domain)):
                raise Exception('配置参数异常：sub_domain 为空')
            if (not (self.internal)):
                raise Exception('配置参数异常：internal 为空')
            if (not (self.email)):
                raise Exception('配置参数异常：email 为空')
        except Exception as ex:
            logging.error(f'配置校验失败! {ex}')
            logging.error('退出')
            exit(1)


class IpHelper(object):
    @staticmethod
    def get_public_ip_httpbin() -> str:
        """获取公网IP  httpbin

        Raises:
            Exception: 获取公网IP失败

        Returns:
            str: ip
        """
        url = 'http://www.httpbin.org/ip'
        rs = requests.get(url, verify=False)
        if rs.status_code() != 200:
            raise Exception('公网IP获取失败 [httpbin]')
        data = json.loads(rs.text)
        return str(data['origin'])


class DNSPod(object):

    @staticmethod
    def __get_headers(email: str) -> dict[str, str]:
        """构建请求的Headers

        Args:
            email (str): 邮箱

        Returns:
            dict[str, str]: headers
        """
        api_name = 'Dnspod-Api'
        api_version = '0.0.2'
        return {
            'User-Agent': f'{api_name}/{api_version}({email})',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

    @staticmethod
    def record_get(cfg: Cfg) -> dict[str, str]:
        """获取记录
            使用：https://dnsapi.cn/Record.List

        Args:
            cfg (Cfg): 配置

        Raises:
            Exception: 接口请求失败相关

        Returns:
            dict[str,str]: 
        """

        url = 'https://dnsapi.cn/Record.List'

        headers = DNSPod.__get_headers(cfg.email)
        data = {
            'login_token': f'{cfg.dnspod_id},{cfg.dnspod_token}',
            'format': 'json',
            'lang': 'cn',
            'error_on_empty': 'no',
            'record_type': 'A',
            'domain': cfg.domain,
            'sub_domain': cfg.sub_domain
        }

        response = requests.post(url=url, data=data, headers=headers, timeout=10)
        if (response.status_code != 200):
            raise Exception(f'httpcode:{response.status_code} 请求失败 {url}')
        result = json.loads(response.text)
        if (int(result['status']['code']) != 1):
            raise Exception('获取记录操作失败', result)
        records = [{'id': r['id'], 'value': r['value']} for r in result['records'] if str(r['name']) == cfg.sub_domain and int(r['enabled']) == 1]
        if (len(records) < 1):
            raise Exception(f'没有找到子域名[{cfg.sub_domain}]相关记录，请先前往dnspod进行添加', result)
        return records[0]

    @staticmethod
    def record_update(cfg: Cfg) -> None:
        """更新记录
            使用 https://dnsapi.cn/Record.Modify

        Args:
            cfg (Cfg): 配置
        """

        url = 'https://dnsapi.cn/Record.Modify'

        headers = DNSPod.__get_headers(cfg.email)
        data = {
            'login_token': f'{cfg.dnspod_id},{cfg.dnspod_token}',
            'format': 'json',
            'lang': 'cn',
            'error_on_empty': 'no',
            'domain': cfg.domain,
            'sub_domain': cfg.sub_domain,
            'record_type': 'A',
            'record_line': '默认',
            'record_id': cfg.record_id,
            'value': cfg.record_ip
        }

        response = requests.post(url=url, data=data, headers=headers, timeout=10)
        if (response.status_code != 200):
            raise Exception(f'httpcode:{response.status_code} 请求失败 {url}')
        result = json.loads(response.text)
        if (int(result['status']['code']) != 1):
            raise Exception('更新记录操作失败', result)
        logging.info(f'更新记录操作成功:{cfg.sub_domain}.{cfg.domain} => {cfg.record_ip}')


def arg_parser():
    """解析命令行参数

    Returns:
        Namespace: 解析结果
    """
    parser = argparse.ArgumentParser(description='DDNS - DNSPOD')
    parser.add_argument('-c', '--config',
                        type=pathlib.Path,
                        help='配置文件')
    parser.add_argument('-v', '--version',
                        action='version', version=VERSION,
                        help='版本')

    return parser.parse_args()


def run(cfg: Cfg) -> None:
    curr_time = int(round(time.time() * 1000))
    is_timeout = (curr_time - cfg.last_update_time) > 600000  # 10分钟

    # 初始化获取记录
    if is_timeout or (not cfg.record_ip):
        record = DNSPod.record_get(cfg)
        cfg.record_ip = record['value']
        cfg.record_id = record['id']
        cfg.last_update_time = int(round(time.time() * 1000))

    public_ip = IpHelper.get_public_ip_httpbin()
    logging.info(f'当前IP： {public_ip}')
    if (cfg.record_ip == public_ip):
        logging.info(f'无需更新')
        return
    cfg.record_ip = public_ip
    DNSPod.record_update(cfg)


if __name__ == '__main__':
    arg = arg_parser()
    cfg = Cfg(arg.config)

    logging.info('开始启动')
    while True:
        try:
            run(cfg)
        except Exception as ex:
            logging.exception(ex)
        time.sleep(cfg.internal)
