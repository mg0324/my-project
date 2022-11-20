scp docker-compose.yml root@hw:/opt
ssh root@hw 'cd /opt && docker-compose up -d'

docker run --rm -v /data/card:/data/card swr.cn-south-1.myhuaweicloud.com/mangoorg/card:latest