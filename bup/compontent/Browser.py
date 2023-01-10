# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from compontent.GetTime import getTime

# 创建谷歌浏览器
def new_chrome(argument):
    # 浏览器参数优化
    chrome_options = Options()
    # 无头运行
    if argument.check_browser_headless():
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    # 大量渲染时候写入/tmp而非/dev/shm
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--mute-audio')
    # chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-running-insecure-content')
    # 禁止加载图片
    chrome_options.add_argument("blink-settings=imagesEnabled=false")
    chrome_options.add_argument('--disable-images')
    chrome_options.add_argument("--disable-blink-features")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument('--incognito')  # 无痕模式
    # browser = webdriver.PhantomJS()
    # browser = webdriver.Chrome(executable_path="/usr/local/lib/python3.6/site-packages/chromedriver_binary/chromedriver",options=chrome_options)
    browser = webdriver.Chrome(options=chrome_options)
    # 需要设置浏览器的window.navigator.webdriver=undefined，不然无法通过滑块检查（速卖通加了webdriver禁止）
    # https://blog.csdn.net/weixin_43881394/article/details/108467118?spm=1005.2026.3001.5635&utm_medium=distribute.pc_relevant_ask_down.none-task-blog-2~default~OPENSEARCH~Rate-5.pc_feed_download_top3ask&depth_1-utm_source=distribute.pc_relevant_ask_down.none-task-blog-2~default~OPENSEARCH~Rate-5.pc_feed_download_top3ask
    # browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    #    "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
    # })
    # 最大化
    browser.maximize_window()
    # 最小化
    # browser.minimize_window()
    return browser

# 浏览器
class Browser:
    __instance = None

    def __init__(self):
        pass

    @staticmethod
    @getTime("创建浏览器")
    def new_browser(argument):
        b = Browser()
        if argument.get_args().browser_type == "chrome":
            b.__instance = new_chrome(argument)
        return b

    # 获取browser driver
    def get_driver(self):
        return self.__instance

    # 关闭当前窗口
    def close(self):
        self.__instance.close()
        pass

    # 请求地址
    def get(self,url):
        self.__instance.get(url)
        pass

    # 添加cookie
    def add_cookie(self,cookie):
        self.__instance.add_cookie(cookie)
        pass

    # 切换浏览器窗口
    def switch_window(self,index):
        # 切回到订单详情页，点击评价，进入评价页
        handles = self.__instance.window_handles
        # 切换到im tab页
        self.__instance.switch_to_window(handles[index])

