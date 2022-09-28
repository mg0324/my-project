# 基础镜像
FROM nginx:alpine
# 作者
MAINTAINER mangomei

COPY conf/node.conf /etc/nginx/conf.d/node.conf
# auth passwd
COPY admin.passwd /etc/nginx/admin.passwd
# 复制nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf