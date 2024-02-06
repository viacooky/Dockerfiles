FROM node:16.16 as builder

RUN git clone https://github.com/Bowen7/regex-vis.git \
    && cd regex-vis \
    && npm i -g pnpm \
    && pnpm install \
    && pnpm run build 


FROM nginx:1.21-alpine
LABEL description="regex-vis" \
    author="viacooky" \
    github="https://github.com/viacooky/Dockerfiles" \
    original_repository="https://github.com/Bowen7/regex-vis"


ENV VERSION 0.0.0
ENV TZ Asia/Shanghai
ENV PLATFORM amd64
ENV OS linux

RUN if [ "$(uname -m)" = "x86_64" ]; then export PLATFORM=x86_64 ; else if [ "$(uname -m)" = "aarch64" ]; then export PLATFORM=arm64 ; fi fi \
    && echo ============== 当前系统 ${OS} 当前架构 ${PLATFORM} \
    && ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && echo ============== 设置时区 ${TZ} \
    && echo 开始清理 \
    && rm -rf /etc/apk \
    && rm -rf /lib/apk \
    && rm -rf /root/.cache \
    && rm -rf /sbin/apk \
    && rm -rf /share/apk \
    && rm -rf /var/cache \
    && echo 清理完成


COPY --from=builder /regex-vis/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]