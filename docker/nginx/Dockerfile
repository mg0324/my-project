# 基础镜像
FROM nginx:alpine
# 作者
MAINTAINER mangomei
# http://mg.meiflower.top conf
COPY mg.txt /etc/nginx/conf.d/mg.conf
# https://mg.meiflower.top conf
COPY mg_https.txt /etc/nginx/conf.d/mg_https.conf
# http://www.meiflower.top conf
COPY www.txt /etc/nginx/conf.d/www.conf
# http://disk.meiflower.top conf
COPY disk.txt /etc/nginx/conf.d/disk.conf
# https://mg.meiflower.top cert
COPY cert /etc/nginx/cert/
# auth passwd
COPY admin.passwd /etc/nginx/admin.passwd