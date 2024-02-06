# coding:utf-8
import requests
import json
import argparse
import subprocess
from pathlib import Path
import logging

LOG_FORMAT: str = '[%(asctime)s][%(levelname)s] - %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)

WORKDIR: Path = Path(__file__).parent
"""工作目录"""
DOCKERHUB_USERNAME: str = None
"""docker hub 用户名"""
DOCKERHUB_PASSWORD: str = None
"""docker hub 密码"""
DEBUG_MODE: bool = False
"""DEBUG 模式"""
OWNER: str = 'viacooky'


class Github:
    @staticmethod
    def get_release_by_tag(owner: str, repo: str, tag: str = 'latest') -> str:
        """github api 获取 tagname

        Args:
            owner (str): owner
            repo (str): repo
            tag (str, optional): v0.0.1. Defaults to 'latest'.

        Returns:
            str: tagname
        """
        url = f'https://api.github.com/repos/{owner}/{repo}/releases/{tag}'
        rs = requests.get(url)
        data = json.loads(rs.text)
        return str(data['tag_name'])


class DockerBuildX:
    @staticmethod
    def build(repo: str, tag: str, namespace: str = OWNER, platform: str = 'linux/arm64,linux/amd64', cwd: str = None) -> None:
        """build 命令

        Args:
            repo (str): 仓库
            tag (str): tag
            namespace (str, optional): 命名空间. Defaults to OWNER.
            platform (str, optional): 平台. Defaults to 'linux/arm64,linux/amd64'.
            cwd (str, optional): 当前工作目录. Defaults to None.
        """
        cmd = f'docker buildx build -t {namespace}/{repo}:{tag} --platform={platform} --push .'
        logging.info(f'[{repo}] exec: {cmd}')
        if (cwd):
            subprocess.check_call(cmd, shell=True, cwd=f'{cwd}')
        else:
            subprocess.check_call(cmd, shell=True)


class DockerHub:
    @staticmethod
    def login() -> None:
        """Docker hub 登录
        """
        logging.info(f'Docker Hub Login')
        cmd = f'echo {DOCKERHUB_PASSWORD} | docker login --username {DOCKERHUB_USERNAME} --password-stdin'
        subprocess.check_call(cmd, shell=True)

    @staticmethod
    def logout() -> None:
        """Docker hub 登出
        """
        logging.info(f'Docker Hub Logout')
        subprocess.check_call(f'docker logout', shell=True)

    @staticmethod
    def push(repository: str, tag: str, namespace: str = OWNER) -> None:
        """推送

        Args:
            repository (str): 仓库
            tag (str): tag
            namespace (str, optional): 命名空间. Defaults to OWNER.
        """
        logging.info(f'Docker Hub push')

        cmd = f'docker push {namespace}/{repository}:{tag}'
        logging.info(f'exec: {cmd}')
        subprocess.check_call(cmd, shell=True)

    @staticmethod
    def check_repository_tag(repo: str, tag: str, namespace: str = OWNER) -> bool:
        """检查仓库和tag是否存在

        Args:
            repository (str): 仓库名
            tag (str): tag
            namespace (str, optional): 命名空间. Defaults to OWNER.

        Returns:
            bool: 
        """
        url = f'https://hub.docker.com/v2/namespaces/{namespace}/repositories/{repo}/tags/{tag}'
        response = requests.get(url)
        return response.status_code == 200


class Tools:
    @staticmethod
    def write_file(file: str, text: str) -> None:
        with open(file, mode="w", encoding='utf-8') as f:
            f.write(text)

    @staticmethod
    def read_file(file: str) -> None:
        with open(file, mode='r', encoding='utf-8') as f:
            return f.read()


def arg_parser():
    """命令行参数解析
    """
    parser = argparse.ArgumentParser(description='Dockerfile 构建发布脚本')
    parser.add_argument('-u', '--username',
                        help='docker hub 的 用户名', required=True)
    parser.add_argument('-p', '--password',
                        help='docker hub 的 密码', required=True)
    parser.add_argument('--debug', action='store_true', help='DEBUG 模式')

    arg = parser.parse_args()

    global DOCKERHUB_USERNAME
    global DOCKERHUB_PASSWORD
    global DEBUG_MODE
    DOCKERHUB_USERNAME = arg.username
    DOCKERHUB_PASSWORD = arg.password
    DEBUG_MODE = arg.debug

    return arg


def ddns_dnspod() -> None:
    """ddns-dnspod 检查更新并构建镜像
    """
    repo = 'ddns-dnspod'
    repo_dir = WORKDIR.joinpath(repo)
    docker_file = repo_dir.joinpath('Dockerfile')
    docker_file_tmpl = repo_dir.joinpath('data', 'Dockerfile.tmpl')
    app_file = repo_dir.joinpath('data', 'app.py')

    logging.info(f'[{repo}] 正在检查更新...')
    cmd = f'python3 {app_file} -v'
    logging.info(f'[{repo}] exec: {cmd}')
    latest_ver = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()

    if DockerHub.check_repository_tag(repo, latest_ver):
        logging.info(f'[{repo}] {OWNER}/{repo}:{latest_ver} 已存在，无需更新')
        return

    new_text = Tools.read_file(docker_file_tmpl).replace('__VERSION__', latest_ver)
    Tools.write_file(docker_file, new_text)
    logging.info(f'[{repo}] Dockerfile 更新完成 {docker_file}')

    DockerBuildX.build(repo, tag=latest_ver, cwd=repo_dir)
    DockerBuildX.build(repo, tag='latest', cwd=repo_dir)


def frps() -> None:
    """frps 检查更新并构建镜像
    """
    repo = 'frps'
    repo_dir = WORKDIR.joinpath(repo)
    docker_file = repo_dir.joinpath('Dockerfile')
    docker_file_tmpl = repo_dir.joinpath('data', 'Dockerfile.tmpl')

    logging.info(f'[{repo}] 正在检查更新...')
    latest_ver = Github.get_release_by_tag('fatedier', 'frp')[1:]

    if DockerHub.check_repository_tag(repo, latest_ver):
        logging.info(f'[{repo}] {OWNER}/{repo}:{latest_ver} 已存在，无需更新')
        return

    new_text = Tools.read_file(docker_file_tmpl).replace('__VERSION__', latest_ver)
    Tools.write_file(docker_file, new_text)
    logging.info(f'[{repo}] Dockerfile 更新完成 {docker_file}')

    DockerBuildX.build(repo, tag=latest_ver, cwd=repo_dir)
    DockerBuildX.build(repo, tag='latest', cwd=repo_dir)


def caddy_cloudflare() -> None:
    repo = 'caddy-cloudflare'
    repo_dir = WORKDIR.joinpath(repo)
    docker_file = repo_dir.joinpath('Dockerfile')
    docker_file_tmpl = repo_dir.joinpath('data', 'Dockerfile.tmpl')

    logging.info(f'[{repo}] 正在检查更新...')
    latest_ver = Github.get_release_by_tag('caddyserver', 'caddy')[1:]
    logging.info(f'[caddyserver] latest: {latest_ver}')

    # 检查镜像
    if DockerHub.check_repository_tag(repo, latest_ver):
        logging.info(f'[{repo}] {OWNER}/{repo}:{latest_ver} 已存在，无需更新')
        return

    new_text = Tools.read_file(docker_file_tmpl).replace('__CADDY_VER__', latest_ver)
    Tools.write_file(docker_file, new_text)
    logging.info(f'[{repo}] Dockerfile 更新完成 {docker_file}')

    DockerBuildX.build(repo, tag=latest_ver, cwd=repo_dir)
    DockerBuildX.build(repo, tag='latest', cwd=repo_dir)


def ddns_go() -> None:
    """ddns-go 检查更新并构建镜像
    """
    repo = 'ddns-go'
    repo_dir = WORKDIR.joinpath(repo)
    docker_file = repo_dir.joinpath('Dockerfile')
    docker_file_tmpl = repo_dir.joinpath('data', 'Dockerfile.tmpl')

    logging.info(f'[{repo}] 正在检查更新...')
    latest_ver = Github.get_release_by_tag('jeessy2', 'ddns-go')[1:]
    logging.info(f'[{repo}] latest: {latest_ver}')

    if DockerHub.check_repository_tag(repo, latest_ver):
        logging.info(f'[{repo}] {OWNER}/{repo}:{latest_ver} 已存在，无需更新')
        return

    new_text = Tools.read_file(docker_file_tmpl).replace('__VERSION__', latest_ver)
    Tools.write_file(docker_file, new_text)
    logging.info(f'[{repo}] Dockerfile 更新完成 {docker_file}')

    DockerBuildX.build(repo, tag=latest_ver, cwd=repo_dir)
    DockerBuildX.build(repo, tag='latest', cwd=repo_dir)


def regex_vis() -> None:
    """regex-vis 检查更新并构建镜像
    """
    repo = 'regex-vis'
    repo_dir = WORKDIR.joinpath(repo)
    docker_file = repo_dir.joinpath('Dockerfile')
    docker_file_tmpl = repo_dir.joinpath('data', 'Dockerfile.tmpl')

    latest_ver = '0.0.1'

    if DockerHub.check_repository_tag(repo, latest_ver):
        logging.info(f'[{repo}] {OWNER}/{repo}:{latest_ver} 已存在，无需更新')
        return
    new_text = Tools.read_file(docker_file_tmpl).replace('__VERSION__', latest_ver)
    Tools.write_file(docker_file, new_text)
    logging.info(f'[{repo}] Dockerfile 更新完成 {docker_file}')

    DockerBuildX.build(repo, tag=latest_ver, cwd=repo_dir)
    DockerBuildX.build(repo, tag='latest', cwd=repo_dir)


if __name__ == '__main__':
    arg = arg_parser()

    if not DEBUG_MODE:
        try:
            DockerHub.login()
            frps()
            ddns_go()
            # ddns_dnspod()
            regex_vis()
            caddy_cloudflare()
        finally:
            DockerHub.logout()
    else:
        # frps()
        # ddns_dnspod()
        # caddy_cloudflare()
        # ddns_go()
        pass
