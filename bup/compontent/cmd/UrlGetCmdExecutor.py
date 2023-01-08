# coding=utf-8
import json
import time
from compontent.cmd.CmdExecutor import CmdExecutor
from compontent.LogUtil import LogUtil

# urlGet 执行
class UrlGetCmdExecutor(CmdExecutor):

    __base_path = "https://space.bilibili.com/1174515315/video?tid=0&page=1&keyword=&order=pubdate"

    def execute(self, robot):
        url = robot.argument.get_args().url
        # 访问地址
        LogUtil.info("正在访问:"+url)
        robot.browser.get(url)
        lis = robot.browser.get_driver().find_elements_by_css_selector("#submit-video-list > ul.clearfix.cube-list > li")
        array = []
        for li in lis:
            aid = li.get_attribute("data-aid")
            array.append(aid)
        LogUtil.info("已获取完成:" + ",".join(s for s in array))
        pass

