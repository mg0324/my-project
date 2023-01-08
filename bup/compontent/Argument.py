# coding=utf-8
import argparse



# 命令行参数类
class Argument:
    # 参数
    __args = None
    # 主解析器
    __parser = None
    # cmd名称
    __name = None

    # 版本号
    def get_version(self):
        return self.__name + " 1.0.0"

    def __init__(self,name):
        self.__name = name
        description = "欢迎使用 " + self.get_version()
        usage = "python3 app.py [cmd]"
        parser = argparse.ArgumentParser(usage=usage,
                                         prog=self.__name,
                                         description=description,
                                         allow_abbrev=False)
        parser.add_argument('-v', '--version',
                            action="version",
                            version=self.get_version(),
                            help="查看版本号")

        parser.add_argument('-nl', '--need_login',
                            default=False,
                            type=bool,
                            metavar="",
                            required=False,
                            help="是否需要登录，True-需要；False-不需要；默认%(default)s")

        parser.add_argument('-sk', '--space_kind',
                            default="pcat",
                            type=str,
                            metavar="",
                            required=False,
                            help="空间类型，pcat-程序员猫大刚；默认%(default)s")

        parser.add_argument('-ll', '--log_level',
                            default="debug",
                            type=str,
                            metavar="",
                            required=False,
                            help="日志级别，error-错误；info-提醒；debug-调试；warning-警告；默认%(default)s")

        parser.add_argument('-bt', '--browser_type',
                            default="chrome",
                            type=str, metavar="",
                            required=False,
                            help="浏览器类型，如chrome-谷歌；firefox-火狐；默认%(default)s")

        parser.add_argument('-bh', '--browser_headless',
                            default="open",
                            type=str,
                            metavar="",
                            required=False,
                            help="无头浏览器运行，open-打开；close-关闭；默认%(default)s")

        subparsers = parser.add_subparsers(help='子命令说明')

        # 添加子命令 read
        parser_read = subparsers.add_parser('read', help='子命令read,刷加阅读量')
        parser_read.add_argument('-short_url', type=str, required=True, help='需要刷加阅读量的视频短地址,多个用逗号间隔,如BV1BG4y1L7kT,BV1A24y1e7La')
        parser_read.add_argument('-count', type=int, help='刷多少次')

        # 添加子命令 urlGet
        parser_url_get = subparsers.add_parser('urlGet', help='子命令urlGet,获取B站空间ID下的视频短地址')
        parser_url_get.add_argument('-url', type=str, required=True, help='需要获取短视频地址的页面url')
        
        self.__args = parser.parse_args()
        self.__parser = parser
        pass

    # 获取参数
    def get_args(self):
        return self.__args

    def get_parser(self):
        return self.__parser

    # 判断是否有工作任务
    def check_work_result(self):
        return self.__args.work_follow == 'open' or self.__args.work_review == 'open'

    def check_browser_headless(self):
        return self.__args.browser_headless == 'open'
