# coding=utf-8
from compontent.Config import Config

# 店
class Space:
    # 主页
    home_url = "https://space.bilibili.com/1174515315"
    
    # 类型
    __kind = None
    # 是否登录
    __is_login = False

    def __init__(self,kind):
        self.__kind = kind
        pass

    # 是否登录
    def is_login(self):
        return self.__is_login

    # 获取cookies配置
    def get_cookies_path(self):
        return Config.get_config_path(self.__kind,"cookies")

    # 获取orders配置
    def get_orders_path(self):
        return Config.get_config_path(self.__kind,"orders")

    # 获取名
    def get_name(self):
        return self.__kind

    # 设置登录状态
    def set_login(self, v):
        self.__is_login = v
        pass



