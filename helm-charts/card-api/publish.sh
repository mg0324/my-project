# 进入card-api目录
cd /Users/mango/git/card/card-api
# maven打包
mvn clean package
# docker build and push
docker build -t mangomei/card:latest .
docker push mangomei/card:latest
# 先缩容
ssh root@master 'kubectl scale deployment card-api --replicas 0'
sleep 5
# 删除掉master上的mangomei/card:latest镜像
ssh root@master 'docker image rm mangomei/card:latest'
# 扩容到1
ssh root@master 'kubectl scale deployment card-api --replicas 1'
# 更新线上helm chart
# 进入helm-chart card-api目录下
# cd /Users/mango/git/my-project/helm-charts/card-api
# helm --kubeconfig ~/.kube/k8s.yaml upgrade card-api .
