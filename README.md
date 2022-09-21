# my-project

## 介绍
![](./res/struct.jpg)

## 服务器资源
![](./res/server.jpg)

## helm发布命令
### 更新card-api
``` bash
helm --kubeconfig ~/.kube/k8s.yaml upgrade card-api .
```

## 资源说明
* docker - 采用docker方式部署的资源，包括如下：
    * nginx
    * frps
* docker-compose - 采用docker-compose方式部署的资源，目前在本地机器部署，主要是搭建一些演示测试环境
* helm-charts - 采用helm部署到k8s的资源，包括如下：
    * card接口
    * python卡片的二维码生成接口
    * 猫大刚主页
    * 卡片admin前端
    * plan我的计划
* home - 是低版本的主页代码
* home-docsify - 是猫大刚主页代码
* oss - 是阿里云上的mangomei的文件存储备份
* resume - 是drawio版本的简历文档