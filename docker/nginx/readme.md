# mangomei/nginx
基于`nginx:alpine`打造适合自己的nginx容器。

## 运行命令
``` bash
docker run --name nginx -d --restart=always \
-p 80:80 -p 443:443 \
-v /opt/nginx/html:/usr/share/nginx/html \
-v /opt/nginx/conf:/etc/nginx/conf.d \
-v /opt/nginx/cert:/etc/nginx/cert \
mangomei/nginx:3.0
```