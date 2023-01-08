# coding=utf-8
import time
from functools import wraps
from compontent.LogUtil import LogUtil

# 装饰器注解getTime
# @getTime
def getTime(stage):
    def doit(func):
        @wraps(func)
        def inner(*args, **kwarg):
            s1 = time.time()
            res = func(*args,**kwarg)
            e1 = time.time()
            prefix = ""
            if len(stage) > 0:
                prefix = "["+stage+"]"
            LogUtil.info(prefix + "用时" + str(int(e1) - int(s1)) + "秒")
            return res
        return inner
    return doit

