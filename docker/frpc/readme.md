# frps
usage: https://hub.docker.com/r/snowdreamtech/frpc

## 在客户端上运行
```bash
docker run --restart=always --network host -d -v /etc/frp/frpc.ini:/etc/frp/frpc.ini --name frpc snowdreamtech/frpc
```

## 配置文件
见 frps.ini
