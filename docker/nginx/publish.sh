#!/usr/bin/env bash
# 停止并删除旧版本容器
#ssh root@node 'docker stop nginx && docker rm nginx'

scp conf/* root@node:/opt/nginx/conf
scp card.json root@node:/opt/nginx/html/config/card.json
# 重启nginx容器
ssh root@node 'docker restart nginx'