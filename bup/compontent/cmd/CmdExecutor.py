# coding=utf-8
# 命令策略
class CmdExecutor:
    # 参数
    __args = None

    # 执行命令接口
    def execute(self, robot):

        pass

    # 注册子命令
    def register(self,subparsers):

        pass