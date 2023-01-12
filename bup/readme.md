# bup
## 简介
作为一个up主，为了运营好空间，用程序为其助力！

## 依赖
* [selenium==3.141.0](https://python-selenium-zh.readthedocs.io/zh_CN/latest/)

## 命令
* read - 阅读视频或者专栏
* urlGet - 获取合集视频列表短地址字符串

可使用子命令`-h`查看命令帮助：
``` shell
(venv) (base) mango@mangodeMacBook-Pro bup % python app.py read -h
usage: python3 app.py [cmd] read [-h] -short_url SHORT_URL [-type TYPE]
                                 [-count COUNT]

optional arguments:
  -h, --help            show this help message and exit
  -short_url SHORT_URL  需要刷加阅读量的视频短地址,多个用逗号间隔,如BV1BG4y1L7kT,BV1A24y1e7La
  -type TYPE            类型，video-视频，read-表示专栏
  -count COUNT          数量，一次访问的个数，默认为5
```


## 安装
1. 基于[conda](https://docs.conda.io/en/latest/miniconda.html)创建虚拟环境
``` shell
conda create -n bup python=3.6
```
2. 切换并激活`bup`虚拟环境
``` shell
conda activate bup
```
3. 安装依赖
``` shell
pip3 install -r requirements.txt
```
4. 运行测试显示usage
``` shell
python3 app.py --help
```

## 示例
```shell
# read
python app.py read -short_url=BV1C3411S7q6@00:40,BV1cP4y1v7o8@00:38
```
docker运行read视频：
```shell
docker run --rm -e EXECUTE_CMD='python app.py -ll=error -rt=docker read -short_url=BV1cP4y1v7o8' mangomei/bup:1.0.2 
```
manjaro服务器运行5分钟2篇文章
``` shell
docker run -d --name bup-read -e EXECUTE_TIMEOUT=10 -e EXECUTE_CMD='python app.py -ll=error -rt=docker read -short_url=cv21131381,cv21130726,cv21126649,cv21124166,cv21143777,cv21143782,cv21143774 -type=read -count=4' mangomei/bup:1.0.2 
```
hw服务器运行5分钟2篇文章
``` shell
docker run -d --name bup-read -e EXECUTE_TIMEOUT=10 -e EXECUTE_CMD='python app.py -ll=error -rt=docker read -short_url=cv21131381,cv21130726,cv21126649,cv21124166,cv21143777,cv21143782,cv21143774 -type=read -count=4' swr.cn-south-1.myhuaweicloud.com/mangoorg/bup:1.0.2 
```
manjaro服务器运行3分钟5视频
``` shell
docker run -d --name bup-read-video -e EXECUTE_TIMEOUT=3 -e EXECUTE_CMD='python app.py -ll=error -rt=docker read -short_url=BV1fd4y1j7Aw@00:39,BV1BG4y1L7kT@02:40,BV1JP411F7pG@00:13,BV1L84y1e7fy@02:20,BV1DP4y1r7YF@01:02,BV16d4y1E7T4@16:47,BV1hM41187QH@11:29,BV18R4y1m7VN@00:11,BV1Y841157YF@18:04,BV1Lv4y1o7Ps@09:08,BV1f44y1S7AW@17:47,BV1S8411G7VS@20:24' mangomei/bup:1.0.2
```
hw服务器运行3分钟5视频
``` shell
docker run -d --name bup-read-video -e EXECUTE_TIMEOUT=3 -e EXECUTE_CMD='python app.py -ll=error -rt=docker read -short_url=BV1fd4y1j7Aw@00:39,BV1BG4y1L7kT@02:40,BV1JP411F7pG@00:13,BV1L84y1e7fy@02:20,BV1DP4y1r7YF@01:02,BV16d4y1E7T4@16:47,BV1hM41187QH@11:29,BV18R4y1m7VN@00:11,BV1Y841157YF@18:04,BV1Lv4y1o7Ps@09:08,BV1f44y1S7AW@17:47,BV1S8411G7VS@20:24' swr.cn-south-1.myhuaweicloud.com/mangoorg/bup:1.0.2 
```
