# coding=utf-8
import json
import time
import random
from compontent.cmd.CmdExecutor import CmdExecutor
from compontent.LogUtil import LogUtil

# read 执行
class ReadCmdExecutor(CmdExecutor):

    __base_path = "https://www.bilibili.com/video/"

    def execute(self, robot):
        urls = robot.argument.get_args().short_url
        url_list = urls.split(",")
        # 每次取5个
        url_list5 = random.sample(url_list,5)
        for url in url_list5:
            # 访问地址
            arr = url.split("@")
            true_url = self.__base_path + arr[0]
            LogUtil.debug("正在访问:"+true_url)
            LogUtil.error("> " + url)
            robot.browser.get(true_url)
            sleep_sec = 31
            if len(arr) > 0:
                LogUtil.info("视频总时长:" + str(arr[1]))
                v_time = arr[1].split(":")
                v_sec = int(v_time[0]) * 60 + int(v_time[1])
                sleep_sec = v_sec
                if v_sec > 30:
                    sleep_sec = 31
            LogUtil.debug("停顿:" + str(sleep_sec) + "秒")
            # 停顿秒
            time.sleep(sleep_sec)
        pass

