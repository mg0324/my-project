# coding=utf-8
from compontent.cmd.ReadCmdExecutor import ReadCmdExecutor

# cmd管理器
class CmdManager:

    # 类型实现
    __impl = {
        "read": ReadCmdExecutor()
    }

    @staticmethod
    def get_instance(impl):
        return CmdManager.__impl.get(impl)
