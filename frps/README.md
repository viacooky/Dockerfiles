# frps

# 简介
基于 [fatedier/frp](https://github.com/fatedier/frp) 的Docker 镜像

* [中文文档](https://gofrp.org/zh-cn/)

# 使用

## Docker Run

```bash
docker run -d --name=frps --restart=always --network=host viacooky/frps:latest
```

或指定 `frps.toml`

```bash
docker run -d --name=frps --restart=always --network=host \
    -v /Dockerfiles/frps/data/frps.toml:/app/frps.toml \
    viacooky/frps:latest
```

## Docker Compose


``` bash
# 具体参考 `/frps/docker-compose.yml`
cd frps/
docker-compose up -d
```