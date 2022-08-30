#!/usr/bin/env bash
# 停止并删除旧版本容器
#ssh root@master 'docker stop nginx && docker rm nginx'

scp conf/* root@master:/opt/nginx/conf
scp card.json root@master:/opt/nginx/html/config/card.json
# 重启nginx容器
ssh root@master 'docker restart nginx'