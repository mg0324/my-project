# coding=utf-8
import json
import time
import random
from compontent.cmd.CmdExecutor import CmdExecutor
from compontent.LogUtil import LogUtil

# read 执行
class ReadCmdExecutor(CmdExecutor):

    __base_path = "https://www.bilibili.com/"

    def register(self,subparsers):
        parser_read = subparsers.add_parser('read', help='子命令read,刷加阅读量')
        parser_read.add_argument('-short_url', type=str, required=True, help='需要刷加阅读量的视频短地址,多个用逗号间隔,如BV1BG4y1L7kT,BV1A24y1e7La')
        parser_read.add_argument('-type', type=str, default='video', help='类型，video-视频，read-表示专栏')
        parser_read.add_argument('-count', type=int, default=5, help='数量，一次访问的个数，默认为5')
        pass

    def execute(self, robot):
        urls = robot.argument.get_args().short_url
        url_list = urls.split(",")
        type = robot.argument.get_args().type
        count = robot.argument.get_args().count
        url_list_new = url_list
        if len(url_list) > count:
            # 每次随机取count个
            url_list_new = random.sample(url_list,count)
        for url in url_list_new:
            # 访问地址
            arr = url.split("@")
            true_url = self.__base_path + type + "/" + arr[0]
            LogUtil.debug("正在访问:"+true_url)
            LogUtil.error("> " + type + "/" + url)
            robot.browser.get(true_url)
            if type == 'video':
                # 视频
                sleep_sec = 31
                if len(arr) > 0:
                    LogUtil.info("总时长:" + str(arr[1]))
                    v_time = arr[1].split(":")
                    v_sec = int(v_time[0]) * 60 + int(v_time[1])
                    sleep_sec = v_sec
                    if v_sec > 30:
                        sleep_sec = 31
                LogUtil.debug("停顿:" + str(sleep_sec) + "秒")
                # 停顿秒
                time.sleep(sleep_sec)
            elif type == 'read':
                # 专栏
                time.sleep(5)
                # 滑动到阅读推荐
                robot.browser.get_driver().execute_script("document.getElementById('readRecommendInfo').scrollIntoView(true);")
                time.sleep(5)

        pass

