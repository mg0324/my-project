#!/usr/bin/env bash
sh ../autod.sh $1
scp -r * root@node:/docs
echo '发布成功'