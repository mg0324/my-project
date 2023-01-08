# coding=utf-8
import sys
# 被引用模块所在的路径
# sys.path.append("/Users/mango/git/my-project/bup")

from compontent.Robot import Robot


# 运行妙娃
def run():
    # 创建机器人
    app = Robot('bup')
    # 开始工作
    app.start_working()
    # 结束工作
    app.shut_down()

if __name__ == '__main__':
    # sys.argv = ['app.py','read','-short_url=BV1cP4y1v7o8@00:31']
    # sys.argv = ['app.py', 'urlGet','-url=https://space.bilibili.com/1174515315/video?tid=0&page=2&keyword=&order=pubdate']
    # 运行
    run()

