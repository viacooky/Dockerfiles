# FRPS 镜像

## What is this?

[FRP](https://github.com/fatedier/frp) server docker version

[Github Repository](https://github.com/viacooky/Dockerfiles/tree/master/frps)

## 镜像使用

### 直接使用

- 默认启用端口：
  - 7000 (Frps server)
  - 7500 (Dashboard）

`docker run --rm -p <your port>:7000 -p <your port>:7500 -p 20000-30000:20000-30000 viacooky/frps`

- 可以使用 `docker run -p 20000-30000` 命令，发布 20000-30000 端口到宿主机，供 frpc 客户端发布远程端口

### 自定义配置文件

`docker run --rm -v <your file>:/app/frps.ini -p <your port>:7000 -p <your port>:7500 viacooky/frps`

### FRP 版本更新

`Dockerfile`默认拉取最新版本的 FRP，若 Dockerhub 官方仓库中镜像的 FRP 版本更新不及时，可 clone 本仓库后自行构建

```bash
git clone https://github.com/viacooky/Dockerfiles.git
cd Dockerfiles/frps
docker build . -t <image name>:<tag>
```
