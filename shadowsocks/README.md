# Shadowsocks docker version

![](https://img.shields.io/docker/automated/viacooky/shadowsocks.svg) ![](https://img.shields.io/docker/build/viacooky/shadowsocks.svg) ![](https://img.shields.io/microbadger/image-size/viacooky/shadowsocks.svg) ![](https://images.microbadger.com/badges/version/viacooky/shadowsocks.svg)

## What is this?

[Shadowsocks](https://github.com/shadowsocks/shadowsocks) docker version

## Dockerfile

[Github Repository](https://github.com/viacooky/Dockerfiles/tree/master/shadowsocks)

## Try

[![Try in PWD](https://github.com/play-with-docker/stacks/raw/master/assets/images/button.png)](https://labs.play-with-docker.com/?stack=https://raw.githubusercontent.com/viacooky/Dockerfiles/master/shadowsocks/docker-compose.yml)

## Usage

### Simple

Defrult expose ports：

- 8989

`docker run --rm -p <your port>:8989 viacooky/shadowsocks`

### Custom configuration file

`docker run -d -v <your file>:/app/config.json -p <your port>:8989 viacooky/shadowsocks`

## Configuration

### Default

```
port: 8989
password: ss123456
encryption method: aes-256-cfb
```

default config.json

`https://github.com/viacooky/Dockerfiles/blob/master/shadowsocks/config.json`

```JSON
{
  "server": "0.0.0.0",
  "server_port": 8989,
  "local_address": "0.0.0.0",
  "local_port": 1080,
  "password": "ss123456",
  "timeout": 600,
  "method": "aes-256-cfb",
  "verbose ": "-3",
  "log-file": "/shadowsocks/logs"
}
```

## About shadowsocks project

[shadowsocks wiki](https://github.com/shadowsocks/shadowsocks/wiki)

[shadowsocks Configuration](https://github.com/shadowsocks/shadowsocks/wiki/Configuration-via-Config-File)
