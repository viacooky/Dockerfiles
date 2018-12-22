FROM alpine

WORKDIR /downloads
# COPY ./get_info.py .
RUN apk --update --no-cache add python3 curl \
    && if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi \
    && curl -sSLO https://raw.githubusercontent.com/viacooky/Dockerfiles/master/frps/get_info.py \
    && tag_name=`python get_info.py` \
    && echo frp最新版本:${tag_name} \
    && curl -sSLO https://github.com/fatedier/frp/releases/download/v${tag_name}/frp_${tag_name}_linux_amd64.tar.gz \
    && echo 下载完成 \
    && tar -zxvf frp_${tag_name}_linux_amd64.tar.gz \
    && echo 解压完成 \
    && mkdir -p /app \
    && curl -sSLO https://github.com/viacooky/Dockerfiles/raw/master/frps/frps.ini \
    && mv frp_${tag_name}_linux_amd64/frps /app \
    && mv frps.ini /app \
    && echo 开始清理 \
    && apk del curl \
    && rm -rf /etc/apk \
    && rm -rf /lib/apk \
    && rm -rf /root/.cache \
    && rm -rf /sbin/apk \
    && rm -rf /share/apk \
    && rm -rf /var/cache \
    && echo 清理完成


WORKDIR /app
CMD [ "./frps", "-c", "frps.ini" ]
