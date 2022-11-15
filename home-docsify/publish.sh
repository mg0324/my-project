#!/usr/bin/env bash
sh ./autod.sh $1
scp -r * root@hw:/docs
echo '发布成功'