# coding=utf-8
from compontent.cmd.ReadCmdExecutor import ReadCmdExecutor
from compontent.cmd.UrlGetCmdExecutor import UrlGetCmdExecutor

# cmd管理器
class CmdManager:

    # 类型实现
    __impl = {
        "read": ReadCmdExecutor(),
        "urlGet": UrlGetCmdExecutor()
    }

    @staticmethod
    def get_instance(impl):
        return CmdManager.__impl.get(impl)

    # 注册命令
    @staticmethod
    def register(parser):
        subparsers = parser.add_subparsers(help='子命令说明')
        for executor in CmdManager.__impl.values():
            executor.register(subparsers)

    
if __name__ == '__main__':
    CmdManager.register()

