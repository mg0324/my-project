# 进入card-api目录
cd /Users/mango/git/card/card-api
# maven打包
mvn clean package
# docker build and push
docker build -t mangomei/card:latest .
docker push mangomei/card:latest
# 更新线上helm chart
# 进入helm-chart card-api目录下
cd /Users/mango/git/my-project/helm-charts/card-api
helm --kubeconfig ~/.kube/k8s.yaml upgrade card-api .
