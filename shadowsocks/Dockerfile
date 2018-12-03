FROM alpine
LABEL description="Shadowsocks 镜像" \
    version="1.0" \
    maintainer="viacooky@gmail.com"

# 安装依赖
RUN apk add --no-cache --update \
    python \
    curl

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "/tmp/get-pip.py"
RUN python "/tmp/get-pip.py"
RUN pip install --upgrade pip
RUN pip install --no-cache-dir shadowsocks

COPY config.json ./
CMD [ "/usr/bin/ssserver", "-c", "config.json"]
EXPOSE 8989