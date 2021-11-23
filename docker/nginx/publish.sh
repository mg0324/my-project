#!/usr/bin/env bash
# 停止并删除旧版本容器
ssh root@master 'docker stop nginx && docker rm nginx'
# 运行新版本容器
ssh root@master 'docker run --name nginx -d --restart=always -p 80:80 -p 443:443 -v /opt/nginx/html:/usr/share/nginx/html mangomei/nginx:2.2'