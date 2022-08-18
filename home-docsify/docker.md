## 打包
```shell script
docker build -t mangomei/home-docsify:1.0 .
```
## 运行
```shell script
docker run -d -p 3000:3000 --name=home-docsify -v $(pwd):/docs mangomei/home-docsify:1.0
```
## 上传
```shell script
docker push mangomei/home-docsify:1.0
```