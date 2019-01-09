# FRPS docker images

![](https://img.shields.io/docker/automated/viacooky/frps.svg) ![](https://img.shields.io/docker/build/viacooky/frps.svg) ![](https://img.shields.io/microbadger/image-size/viacooky/frps.svg) ![](https://images.microbadger.com/badges/version/viacooky/frps.svg)

## What is this?

[FRP](https://github.com/fatedier/frp) server docker version

## Dockerfile

[Github Repository](https://github.com/viacooky/Dockerfiles/tree/master/frps)

## Try

[![Try in PWD](https://github.com/play-with-docker/stacks/raw/master/assets/images/button.png)](https://labs.play-with-docker.com/?stack=https://raw.githubusercontent.com/viacooky/Dockerfiles/master/frps/docker-compose.yml)

## Usage

### Simple

Default expose port:

- 7000 (Frps server)
- 7500 (Dashboard）

`docker run --rm -p <your port>:7000 -p <your port>:7500 -p 20000-30000:20000-30000 viacooky/frps`

- 可以使用 `docker run -p 20000-30000` 命令，发布 20000-30000 端口到宿主机，供 frpc 客户端发布远程端口

### Custom configuration file

`docker run --rm -v <your file>:/app/frps.ini -p <your port>:7000 -p <your port>:7500 viacooky/frps`

### Update FRPS

`Dockerfile`默认拉取最新版本的 FRP，若 Dockerhub 官方仓库中镜像的 FRP 版本更新不及时，可 clone 本仓库后自行构建

```bash
git clone https://github.com/viacooky/Dockerfiles.git
cd Dockerfiles/frps
docker build . -t <image name>:<tag>
```
