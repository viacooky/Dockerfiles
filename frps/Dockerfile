FROM alpine

# 名称/描述/源代码/使用/作者
LABEL org.label-schema.name="frps" \
    org.label-schema.description="frp server v0.24.1" \
    org.label-schema.vendor="viacooky" \
    org.label-schema.vcs-url="https://github.com/viacooky/Dockerfiles/tree/master/frps" \
    org.label-schema.usage="https://github.com/viacooky/Dockerfiles/blob/master/frps/README.md"



WORKDIR /downloads
COPY ./get_info.py .
RUN apk --update --no-cache add curl \
    # && if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi \
    && tag_name='0.24.1' \
    && echo frp最新版本:${tag_name} \
    && curl -sSLO https://github.com/fatedier/frp/releases/download/v${tag_name}/frp_${tag_name}_linux_amd64.tar.gz \
    && echo 下载完成 \
    && tar -zxvf frp_${tag_name}_linux_amd64.tar.gz \
    && echo 解压完成 \
    && mkdir -p /app \
    && mv frp_${tag_name}_linux_amd64/frps /app\
    && echo 开始清理 \
    && apk del curl \
    && rm -rf /etc/apk \
    && rm -rf /lib/apk \
    && rm -rf /root/.cache \
    && rm -rf /sbin/apk \
    && rm -rf /share/apk \
    && rm -rf /var/cache \
    && rm -rf /downloads \
    && echo 清理完成

EXPOSE 20000-30000
WORKDIR /app
COPY ./frps.ini .
CMD [ "./frps", "-c", "frps.ini" ]
