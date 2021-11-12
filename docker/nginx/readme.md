# mangomei/nginx
基于`nginx:alpine`打造适合自己的nginx容器。

## 运行命令
``` bash
docker run --name nginx -d --restart=always -p 80:80 -p 443:443 -v /opt/nginx/html:/usr/share/nginx/html mangomei/nginx:1.0
```