# caddy-cloudflare

# 简介
基于 [caddyserver/caddy](https://github.com/caddyserver/caddy) 的Docker 镜像，加入了 [caddy-dns/cloudflare](https://github.com/caddy-dns/cloudflare) 插件

* [官网](https://caddyserver.com/) 
* [文档](https://caddyserver.com/docs/) 
* [Caddyfile文档](https://caddyserver.com/docs/caddyfile)

# 使用

## Caddyfile

在 `caddyfile` 中加入以下配置
```
tls {
	dns cloudflare {env.CF_API_TOKEN}
}
```
可以替换 `{env.CF_API_TOKEN}` 为你的TOKEN，这样将依赖于配置文件而不是环境变量

## docker run

```bash
docker run -d --name caddy \
  -p 80:80 \
  -p 443:443 \
  -v caddy_data:/data \
  -v caddy_config:/config \
  -v $PWD/data/Caddyfile:/etc/caddy/Caddyfile \
  -e CF_API_TOKEN=12345 \
  viacooky/caddy-cloudflare:latest
```


## docker-compose


``` bash
cd caddy-cloudflare/
docker-compose up -d
```

# 一些使用示例

## 使用 Caddyfile

```
docker run --rm -it \
-p 80:80 \
-p 443:443 \
-v $(pwd)/data/Caddyfile:/etc/caddy/Caddyfile \
viacooky/caddy-cloudflare:latest
```

## 文件服务器 - 文件列表形式

* 示例 [Caddyfile](./data/example/Caddyfile.FileServer)
```
docker run --rm -it \
-p 80:80 \
-p 443:443 \
-v $(pwd)/data/example/Caddyfile.FileServer:/etc/caddy/Caddyfile \
-v $(pwd)/data/example/site/:/usr/share/caddy/ \
viacooky/caddy-cloudflare:latest
```

## 反向代理
* 示例 [Caddyfile](./data/example/Caddyfile.ReverseProxy)
```
docker run --rm -it \
-p 80:80 \
-p 443:443 \
-v caddy_data:/data \
-v caddy_config:/config \
-v $(pwd)/data/example/Caddyfile.ReverseProxy:/etc/caddy/Caddyfile \
-v $(pwd)/data/example/site/:/usr/share/caddy/ \
viacooky/caddy-cloudflare:latest
```