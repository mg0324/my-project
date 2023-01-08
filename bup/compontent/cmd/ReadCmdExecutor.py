# coding=utf-8
import json
import time
from compontent.cmd.CmdExecutor import CmdExecutor
from compontent.LogUtil import LogUtil

# read 执行
class ReadCmdExecutor(CmdExecutor):

    __base_path = "https://www.bilibili.com/video/"

    def execute(self, robot):
        urls = robot.argument.get_args().short_url
        for url in urls.split(","):
            # 访问地址
            true_url = self.__base_path + url
            LogUtil.info("正在访问:"+true_url)
            robot.browser.get(true_url)
            # 停顿3秒
            time.sleep(3)
        pass

