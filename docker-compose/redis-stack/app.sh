docker run -d --name redis-stack -e REDIS_ARGS="--requirepass Mg19930324@" -p 30379:6379 -p 30378:8001 swr.cn-south-1.myhuaweicloud.com/mangoorg/redis-stack:latest


docker run -d --name redis-stack -e REDIS_ARGS="--requirepass Mg19930324@" -p 30379:6379 -p 30378:8001 redis-stack:latest
