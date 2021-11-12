FROM nginx:alpine
MAINTAINER mangomei
COPY mg.txt /etc/nginx/conf.d/mg.conf
COPY www.txt /etc/nginx/conf.d/www.conf
COPY disk.txt /etc/nginx/conf.d/disk.conf
COPY cert /etc/nginx/cert/
COPY admin.passwd /etc/nginx/admin.passwd