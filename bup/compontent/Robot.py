# coding=utf-8
import json
import time
import sys
from compontent.Argument import Argument
from compontent.Browser import Browser
from compontent.Config import Config
from compontent.GetTime import getTime
from compontent.LogUtil import LogUtil
from compontent.Space import Space
from compontent.cmd.CmdManager import CmdManager

# 机器人
class Robot:
    # 名字
    name = ""
    # 浏览器
    browser = Browser()
    # 空间
    space = None
    # 配置
    config = None
    # 命令行参数
    argument = None

    # 初始化机器人
    def __init__(self,name):
        self.name = name
        self.config = Config()
        self.argument = Argument(self.name)
        # 设置日志级别
        LogUtil.set_level(self.argument.get_args().log_level)
        LogUtil.debug("[bup]参数集：" + str(self.argument.get_args()))
        # 创建浏览器
        self.browser = Browser.new_browser(self.argument)
        # 创建空间
        self.space = Space(self.argument.get_args().space_kind)
        pass

    # 判断是否有任务需要执行
    def __check__(self):
        result = self.argument.check_work_result()
        if not result:
            LogUtil.info("["+self.name+"]无任务执行")
        return result

    # 开始工作
    @getTime(stage="主工作")
    def start_working(self):
        if len(sys.argv) > 0:
            # 根据子命令分流执行 找到子命令
            cmdName = self.find_sub_cmd()
            cmdExecutor = CmdManager.get_instance(cmdName)
            if cmdExecutor:
                LogUtil.debug("执行命令:" + cmdName)
                self.login_to_home()
                cmdExecutor.execute(self)
        pass
    
    # 找到子命令
    def find_sub_cmd(self):
        index = 1
        while True:
            cmd = sys.argv[index]
            if not cmd.startswith("-"):
                return cmd
            index = index + 1

    # 关机
    def shut_down(self):
        self.browser.switch_window(0)
        self.browser.close()
        pass

    # 登录
    @getTime("尝试登录")
    def do_login(self):
        # 需要登录 并且 没有加载cookie则加载
        if self.argument.get_args().need_login and not self.space.is_login():
            cookies_path = self.space.get_cookies_path()
            # 找到最小需要的cookies，加快登录cookie的操作
            needs = ["sid"]
            # 设置cookies跳过登录
            with open(cookies_path) as f:
                list_cookies = json.loads(f.read())
            for cookie in list_cookies:
                if cookie["name"] in needs:
                    del cookie['sameSite']
                    self.browser.add_cookie(cookie)
            # 设置登录状态为True
            self.space.set_login(True)
            LogUtil.debug("[space=" + self.space.get_name() + "]加载登录信息成功")
        pass

    # 登录到后端首页
    @getTime("去往空间首页")
    def login_to_home(self):
        # 尝试到首页
        self.browser.get(self.space.home_url)
        # 登录
        self.do_login()
        pass

    # 处理follow
    @getTime("处理follow")
    def do_follow(self, order_number):
        prefix = "[store=" + self.store.get_name() + "][" + order_number + "]"
        LogUtil.debug(prefix + "开始处理follow")
        while 1:
            start = time.time()
            try:
                self.browser.get_driver().find_element_by_link_text('联系买家').click()
                LogUtil.debug(prefix + '已点击联系买家链接')
                end = time.time()
                break
            except:
                time.sleep(1)
                LogUtil.debug(prefix + "还未定位到元素!")
        LogUtil.debug(prefix + "定位耗费时间：" + str(end - start))

        self.browser.switch_window(1)
        self.browser.get_driver().execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
        })
        while 1:
            start = time.time()
            try:
                self.browser.get_driver().find_element_by_class_name("message-fields__autosize")
                LogUtil.debug(prefix + '已定位到元素')
                end = time.time()
                break
            except:
                time.sleep(1)
                LogUtil.debug(prefix + "还未定位到元素!")

        LogUtil.debug(prefix + '定位耗费时间：' + str(end - start))
        # 找到评价框
        textarea = self.browser.get_driver().find_element_by_class_name("message-fields__autosize")
        next_show = False
        try_count = 1
        while 1:
            start = time.time()
            try:
                for i in range(0, 10):
                    self.browser.get_driver().find_element_by_class_name("button-primiary").click()
                    LogUtil.debug(prefix + '已点击下一步')
                    next_show = True
                end = time.time()
                break
            except:
                if next_show:
                    end = time.time()
                    break
                else:
                    if try_count > self.config.try_count:
                        break
                    time.sleep(1)
                    LogUtil.debug(prefix + "还未定位到元素!")
                    try_count = try_count + 1
        LogUtil.debug(prefix + '点击下一步耗费时间：' + str(end - start))
        textarea.send_keys(self.config.follow_msg)
        time.sleep(1)
        js = "var q=document.getElementsByClassName('im-icon-paper-plane')[0].click()"
        self.browser.get_driver().execute_script(js)
        # document.getElementsByClassName('im-icon-paper-plane').children[0].click()
        # browser.find_element_by_class_name("im-icon-paper-plane").click()
        time.sleep(2)
        self.browser.close()
        pass

