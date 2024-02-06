# ddns-go

# 简介
基于 [jeessy2/ddns-go](https://github.com/jeessy2/ddns-go) 制作的Docker 镜像


# 使用

## docker run

使用 `--net=host` 模式，默认端口 `9876`

可把 /ddns-go 替换为你主机任意目录, 配置文件为隐藏文件 `.ddns_go_config.yaml`

```bash
docker run -d --name=ddns-go --restart=always -v /ddns-go:/root --network=host viacooky/ddns-go:latest
```

或使用端口映射模式

```bash
docker run -d --name=ddns-go --restart=always -v /ddns-go:/root -p 9876:9876 viacooky/ddns-go:latest
```

## docker-compose


``` bash
cd ddns-go/
docker-compose up -d
```