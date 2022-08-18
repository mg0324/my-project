git add .
git commit -m $1
git push

sh publish.sh
echo "发布成功"