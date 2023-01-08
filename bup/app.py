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
    # sys.argv = ['app.py', 'read','-url=xxx','-count=1']
    # 运行
    run()

