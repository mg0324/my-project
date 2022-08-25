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