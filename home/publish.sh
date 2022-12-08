#!/usr/bin/env bash
# 编译打包
yarn build
# 删除原来部署的文件
ssh root@node 'rm -rf /opt/nginx/html/home/*'
# 上传新的部署文件
scp dist/* root@node:/opt/nginx/html/home
# 发布成功
echo 'publish success to server node!'

