# frps
usage: https://hub.docker.com/r/snowdreamtech/frps

## 在服务端上运行
```bash
scp frps.ini root@node:/etc/frp/frps.ini
docker run --restart=always --network host -d -v /etc/frp/frps.ini:/etc/frp/frps.ini --name frps snowdreamtech/frps
```



## 配置文件
见 frps.ini
