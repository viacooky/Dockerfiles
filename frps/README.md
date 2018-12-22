# FRPS 镜像

## What is this?

将[**FRP**](https://github.com/fatedier/frp)项目的服务端打包为 Docker 镜像，方便部署

## 镜像使用

### 直接使用

- 默认启用端口：
  - 7000 (Frps server)
  - 7500 (Dashboard）

`docker run --rm -p <your port>:7000 -p <your port>:7500 viacooky/frps`

### 自定义配置文件

`docker run --rm -v <your file>:/app/frps.ini -p <your port>:7000 -p <your port>:7500 viacooky/frps`
