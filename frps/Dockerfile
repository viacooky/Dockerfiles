FROM alpine:latest
LABEL description="frp Server" \
    author="viacooky" \
    github="https://github.com/viacooky/Dockerfiles" \
    original_repository="https://github.com/fatedier/frp"

ENV FRP_VER 0.62.1

ENV TZ Asia/Shanghai
ENV PLATFORM amd64
ENV OS linux

RUN if [ "$(uname -m)" = "x86_64" ]; then export PLATFORM=amd64 ; else if [ "$(uname -m)" = "aarch64" ]; then export PLATFORM=arm64 ; fi fi \
    && echo ============== 当前架构${PLATFORM} \
    && apk add --no-cache tzdata \
    && ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && echo frp最新版本:${FRP_VER} \
    && wget --no-check-certificate https://github.com/fatedier/frp/releases/download/v${FRP_VER}/frp_${FRP_VER}_${OS}_${PLATFORM}.tar.gz \
    && echo 下载完成 \
    && tar -zxvf frp_${FRP_VER}_${OS}_${PLATFORM}.tar.gz \
    && echo 解压完成 \
    && mkdir -p /app \
    && cd frp_${FRP_VER}_${OS}_${PLATFORM} \
    && mv frps /app\
    && mv frps.toml /app\
    && echo 开始清理 \
    && rm -rf /etc/apk \
    && rm -rf /lib/apk \
    && rm -rf /root/.cache \
    && rm -rf /sbin/apk \
    && rm -rf /share/apk \
    && rm -rf /var/cache \
    && cd .. \
    && rm -rf *.tar.gz frp_* \
    && echo 清理完成

EXPOSE 7000 7500
CMD [ "/app/frps", "-c", "/app/frps.toml" ]