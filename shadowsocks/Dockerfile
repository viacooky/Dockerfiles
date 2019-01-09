FROM alpine

# 名称/描述/源代码/使用/作者
LABEL org.label-schema.name="shadowsocks" \
    org.label-schema.description="shadowsocks docker version" \
    org.label-schema.vendor="viacooky" \
    org.label-schema.vcs-url="https://github.com/viacooky/Dockerfiles/tree/master/shadowsocks" \
    org.label-schema.usage="https://github.com/viacooky/Dockerfiles/blob/master/shadowsocks/README.md"

EXPOSE 8989
WORKDIR /app
COPY ./config.json .
RUN apk add --no-cache --update python curl \
    && curl -sSL -o "/tmp/get-pip.py" "https://bootstrap.pypa.io/get-pip.py" \
    && python "/tmp/get-pip.py" \
    && pip install --upgrade pip \
    && pip install --no-cache-dir shadowsocks \
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


CMD [ "/usr/bin/ssserver", "-c", "config.json"]
