# regex-vis

# 简介
基于 [Bowen7/regex-vis](https://github.com/Bowen7/regex-vis) 的Docker 镜像

[regex-vis](https://github.com/Bowen7/regex-vis) 是一个辅助学习、编写和验证正则的工具。它不仅能对正则进行可视化展示，而且提供可视编辑正则的能力

# 使用

## docker Run

```bash
docker run -d --name=regex-vis --restart=always -p 80:80 viacooky/regex-vis:latest
```


## docker Compose


``` bash
cd regex-vis/
docker-compose up -d
```