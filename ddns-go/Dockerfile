FROM alpine:latest
LABEL description="ddns-go" \
    author="viacooky" \
    github="https://github.com/viacooky/Dockerfiles" \
    original_repository="https://github.com/jeessy2/ddns-go"

ENV VERSION 6.5.0
ENV TZ Asia/Shanghai

ENV PLATFORM x86_64
ENV OS linux

RUN if [ "$(uname -m)" = "x86_64" ]; then export PLATFORM=x86_64 ; else if [ "$(uname -m)" = "aarch64" ]; then export PLATFORM=arm64 ; fi fi \
    && echo ============== 当前系统${OS} 当前架构${PLATFORM} \
    && apk add --no-cache tzdata \
    && ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && echo ddns-go 版本:${VERSION} \
    && wget --no-check-certificate https://github.com/jeessy2/ddns-go/releases/download/v${VERSION}/ddns-go_${VERSION}_${OS}_${PLATFORM}.tar.gz \
    && echo 下载完成 \
    && mkdir -p /app \
    && tar -zxvf ddns-go_${VERSION}_${OS}_${PLATFORM}.tar.gz -C /app \
    && echo 解压完成 \
    && echo 开始清理 \
    && rm -rf /etc/apk \
    && rm -rf /lib/apk \
    && rm -rf /root/.cache \
    && rm -rf /sbin/apk \
    && rm -rf /share/apk \
    && rm -rf /var/cache \
    && cd .. \
    && rm -rf *.tar.gz \
    && echo 清理完成

EXPOSE 9876
ENTRYPOINT ["/app/ddns-go"]
CMD ["-l", ":9876", "-f", "300"]