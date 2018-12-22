FROM alpine
LABEL description="Shadowsocks 镜像" \
    version="1.0" \
    maintainer="viacooky@gmail.com"

WORKDIR /app
RUN apk add --no-cache --update python curl \
    && curl -sSL -o "/tmp/get-pip.py" "https://bootstrap.pypa.io/get-pip.py" \
    && python "/tmp/get-pip.py" \
    && pip install --upgrade pip \
    && pip install --no-cache-dir shadowsocks \
    && curl -sSLO https://github.com/viacooky/Dockerfiles/raw/master/shadowsocks/config.json \
    && echo 开始清理 \
    && apk del curl \
    && rm -rf /etc/apk \
    && rm -rf /lib/apk \
    && rm -rf /root/.cache \
    && rm -rf /sbin/apk \
    && rm -rf /share/apk \
    && rm -rf /var/cache \
    && rm -rf /tmp \
    && rm -rf /usr/share/apk \
    && rm -rf /usr/bin/easy_install \
    && rm -rf /usr/bin/easy_install-2.7 \
    && rm -rf /usr/bin/pip \
    && rm -rf /usr/bin/pip2 \
    && rm -rf /usr/bin/pip2.7 \
    && rm -rf /usr/bin/pydoc \
    && echo 清理完成

EXPOSE 8989
CMD [ "/usr/bin/ssserver", "-c", "/app/config.json"]
