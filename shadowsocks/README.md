# Shadowsocks docker images

![](https://img.shields.io/docker/automated/viacooky/shadowsocks.svg?style=flat-square) ![](https://img.shields.io/docker/build/viacooky/shadowsocks.svg?style=flat-square) ![](https://img.shields.io/microbadger/image-size/viacooky/shadowsocks.svg?style=flat-square)

## What is this?

[Shadowsocks](https://github.com/shadowsocks/shadowsocks) docker version

## Try

[![Try in PWD](https://github.com/play-with-docker/stacks/raw/master/assets/images/button.png)](https://labs.play-with-docker.com/?stack=https://raw.githubusercontent.com/viacooky/Dockerfiles/master/shadowsocks/pwd-stack.yml)

## Dockerfile

[Github Repository](https://github.com/viacooky/Dockerfiles/tree/master/shadowsocks)

## 镜像使用

### 直接使用

- 默认启用端口：
  - 8989

`docker run --rm -p <your port>:8989 viacooky/shadowsocks`

### 自定义配置文件

`docker run --rm -v <your file>:/app/config.json -p <your port>:8989 viacooky/shadowsocks`

## 配置

### 默认配置

```
端口：8989
密码：ss123456
加密方法：aes-256-cfb
```

默认 config.json

`https://github.com/viacooky/Dockerfiles/blob/master/shadowsocks/config.json`

## 关于 shadowsocks

[shadowsocks wiki](https://github.com/shadowsocks/shadowsocks/wiki)

[shadowsocks Configuration](https://github.com/shadowsocks/shadowsocks/wiki/Configuration-via-Config-File)
