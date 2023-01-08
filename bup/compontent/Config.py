# coding=utf-8
# 配置类
class Config:
    # 系统版本
    __version = "1.0.0"
    # follow消息
    follow_msg = "Dear friend, \n Please follow my shop, I will thank you very much！\n [Admire]"
    # 评价内容
    review_msg = "You are a very good buyer, looking forward to your next purchase and hope you follow my shop"
    # 尝试刷新下一步的次数
    try_count = 5

    def __init__(self):
        pass

    @staticmethod
    def get_config_path(store_kind, config_type):
        return "config/" + store_kind + "/" + config_type + ".json"


