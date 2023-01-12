# coding=utf-8
import json
import time
from compontent.cmd.CmdExecutor import CmdExecutor
from compontent.LogUtil import LogUtil

# urlGet 执行
class UrlGetCmdExecutor(CmdExecutor):

    __base_path = "https://space.bilibili.com/1174515315/video?tid=0&page=1&keyword=&order=pubdate"

    def register(self,subparsers):
        # 添加子命令 urlGet
        parser_url_get = subparsers.add_parser('urlGet', help='子命令urlGet,获取B站空间ID下的视频短地址')
        parser_url_get.add_argument('-url', type=str, required=True, help='需要获取短视频地址的页面url')
        pass

    def execute(self, robot):
        url = robot.argument.get_args().url
        # 访问地址
        LogUtil.info("正在访问:"+url)
        robot.browser.get(url)
        lis = robot.browser.get_driver().find_elements_by_css_selector("#submit-video-list > ul.clearfix.cube-list > li")
        array = []
        for li in lis:
            aid = li.get_attribute("data-aid")
            length = li.find_element_by_css_selector(".length").text
            array.append(aid + "@" + length)
        LogUtil.info("已获取完成:" + ",".join(s for s in array))
        pass

