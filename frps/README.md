# FRPS docker images

![](https://img.shields.io/docker/automated/viacooky/frps.svg) ![](https://img.shields.io/docker/build/viacooky/frps.svg) ![](https://img.shields.io/microbadger/image-size/viacooky/frps.svg) ![](https://images.microbadger.com/badges/version/viacooky/frps.svg)

## What is this?

[FRP](https://github.com/fatedier/frp) server docker version

update to **v0.22.0**

## Dockerfile

[Github Repository](https://github.com/viacooky/Dockerfiles/tree/master/frps)

## Try

[![Try in PWD](https://github.com/play-with-docker/stacks/raw/master/assets/images/button.png)](https://labs.play-with-docker.com/?stack=https://raw.githubusercontent.com/viacooky/Dockerfiles/master/frps/docker-compose.yml)

## Usage

### Simple

Default expose port:

- 7000 (Frps server)
- 7500 (Dashboard）

Dashboard default:

- username: admin
- password: admin

`docker run --rm -p <your port>:7000 -p <your port>:7500 -p 20000-30000:20000-30000 viacooky/frps`

- you can use command `docker run -p 20000-30000` , publish ports 20000-30000 to hosted

### Custom configuration file

`docker run --rm -v <your file>:/app/frps.ini -p <your port>:7000 -p <your port>:7500 viacooky/frps`
