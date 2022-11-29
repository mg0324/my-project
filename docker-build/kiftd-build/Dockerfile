# 基础镜像
FROM openjdk:8-jdk-alpine3.9
# 作者
MAINTAINER mangomei <1092017732@qq.com>
# 设置镜像为国内，并安装curl
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
    && apk update \
    && apk add curl
# 设置环境变量
# ENV JAVA_HOME /usr/java/jdk
# ENV PATH ${PATH}:${JAVA_HOME}/bin
# 时区设置
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone
# 复制文件
ADD kiftd /opt/kiftd
# 设置工作目录 
WORKDIR /opt/kiftd
# 启动脚本
ENTRYPOINT ["/bin/sh","-c","exec java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar kiftd-1.0.35-RELEASE.jar -start"]
# 暴露端口
EXPOSE 8080
