# coding=utf-8
# 控制台日志工具
import time


class LogUtil:
    # 日志级别 error > info > debug > warning
    __level = "debug"
    # 分值
    __value = {
        "warning": 1,
        "debug": 2,
        "info": 3,
        "error": 4
    }

    @staticmethod
    def __level_value__():
        return LogUtil.__value.get(LogUtil.__level)

    @staticmethod
    def __log__(level,msg):
        if LogUtil.__value.get(level) >= LogUtil.__level_value__():
            print(msg)
        pass

    @staticmethod
    def set_level(level):
        LogUtil.__level = level
        pass

    @staticmethod
    def info(msg):
        LogUtil.__log__("info",msg)
        pass

    @staticmethod
    def debug(msg):
        LogUtil.__log__("debug",msg)
        pass

    @staticmethod
    def warning(msg):
        LogUtil.__log__("warning",msg)
        pass

    @staticmethod
    def error(msg):
        LogUtil.__log__("error",msg)
        pass

if __name__ == '__main__':
    LogUtil.set_level("warning")
    LogUtil.info("info")
    LogUtil.debug("debug")
    LogUtil.warning("warning")
    LogUtil.error("error")

