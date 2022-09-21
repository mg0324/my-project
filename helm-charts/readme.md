## helm

### 发布应用

``` bash
helm --kubeconfig ~/.kube/rancher-local.yaml install mysql-server .
```

### 删除应用

``` bash
helm --kubeconfig ~/.kube/rancher-local.yaml uninstall mysql-server .
```

### 更新应用

``` bash
helm --kubeconfig ~/.kube/rancher-local.yaml upgrade mysql-server .
```

### 脚本all
1. maven打包
2. docker打镜像并上传
3. helm更新

### helm-chart部署集群列表
* card-api - k8s的master节点 - 端口30901
* es-server - 未部署
* flask-api - docker服务器上的k3s - 端口30002
* home-docsify - k8s的node1节点 - 端口30300
* mysql-server - docker服务器上的k3s - 端口32306
* nginx-card-admin - k8s的node1节点 - 端口30180
* nginx-plan - 未部署
* redis-server - docker服务器上的k3s - 端口30379