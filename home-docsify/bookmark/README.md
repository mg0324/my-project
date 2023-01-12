<!-- 引入 layui.css -->
<link href="//unpkg.com/layui@2.7.6/dist/css/layui.css" rel="stylesheet">

<style type="text/css">
.layui-row{
    display: flex;
    flex-flow: row wrap;
    align-content: space-between;
}
.layui-row a:hover{
    text-decoration:underline;
}
.layui-row div{
    border:1px solid #ddd;
    height:40px;
    display: flex;
    flex-flow: row wrap;
    align-content: center;
    justify-content: center;
    margin-bottom: 5px;
    margin-right: 5px;
    border-radius: 2px;
    font-size: 12px;
}

.layui-row .no {
    background-color: white;
    color: black;
}
</style>

<div id="container" class="layui-container">
    <fieldset class="layui-elem-field" style="padding: 8px;" v-for="(item,index) in nodes">
        <legend>{{item.moduleName}}</legend>
        <div class="layui-row">
            <div class="layui-col-xs12 layui-col-sm12 layui-col-md2 no" v-for="(part,index) in item.parts">
                <a :href="theHref(part)" target="_blank">{{theName(part)}}</a>
            </div>
    </fieldset>
</div>

<script>
    (function(){
         new Vue({
            el:'#container',
            data() {
                return {
                    nodes: [
                        {
                            moduleName: '我的项目',
                            parts:[
                                    '项目资源分布@https://mg.meiflower.top/project/README',
                                    '我的项目@https://gitee.com/mgang/my-project',
                                    '猫大刚主页@https://mg.meiflower.top/',
                                    '我的计划@https://mg.meiflower.top/plan/',
                                    '我的B站空间@https://space.bilibili.com/1174515315',
                                    '我的博客@https://mg.meiflower.top/mb/',
                                    'marp分享@http://marp.meiflower.top/',
                                    '待办列表@http://todo.meiflower.top/',
                                    '芒果网盘@http://disk.meiflower.top/',
                                    '芒果卡片@https://mg.meiflower.top/card-admin/#/login',
                                    '芒果卡片构建@http://mg.meiflower.top/cp/bqr/',
                                    '点子队列@http://mg.meiflower.top/cp/keyqueue',
                                    'mango-kit@https://github.com/mg0324/mango-kit',
                                    '妙娃miaowa@https://mmtdd.gitee.io/miaowa/#/',
                                    'Java学习体系文档@https://mgang.gitee.io/s-java/#/',
                                    'CPU修行文档@http://mgang.gitee.io/s-cpu/#/',
                                    'B站工具bup@https://gitee.com/mgang/my-project/tree/master/bup',
                                    'jmedis@https://gitee.com/mangoorg/jmedis',
                                    'idea启动插件@https://gitee.com/mgang/idea-plugin-start-time',
                                    '我的分享@https://gitee.com/mgang/my-share',
                                    '我的模板@https://gitee.com/mgang/my-template',
                                    'leetcode刷题笔记@https://gitee.com/mgang/leet-code'
                            ]
                        },
                        {
                            moduleName: '常用工具',
                            parts:[
                                'chrome商店@https://chrome.google.com/webstore/category/extensions',
                                '定稿设计@https://gd74865930.qiye.gaoding.com/smartdesign',
                                '百度统计@https://tongji.baidu.com/main/homepage/22511391/homepage/index',
                                '图片转base64@https://kz16.top/png2base64.html',
                                '谷歌翻译@https://translate.google.com.hk/?hl=zh-CN&sourceid=cnhp',
                                'Free DNS@https://dns.he.net/index.cgi',
                                'processon@https://www.processon.com/login',
                                'drawio@https://app.diagrams.net/',
                                '华为云容器服务@https://console.huaweicloud.com/swr/?agencyId=9fb50aa2b84e4d9f820bb6d32ca2b5ab&region=cn-south-1&locale=zh-cn#/swr/warehouse/detail/hw_008618613073290_01/mangoorg/flask-api/guide',
                                'doocs md@https://doocs.gitee.io/md/'
                            ]
                        },
                        {
                            moduleName: '资源导航',
                            parts:[
                                '千库网@https://588ku.com/so/shuqianye/',
                                '胖虎的工具箱@https://www.955code.com/',
                                'JDK11下载@https://blog.lupf.cn/articles/2022/02/24/1645713619397.html#toc_h2_17',
                                'docker hub@https://hub.docker.com/',
                                '各操作系统包@https://pkgs.org/'
                            ]
                        },
                        {
                            moduleName: '前端UI库',
                            parts:[
                                'Layui@hhttps://layui.gitee.io/v2/',
                                'heyui@https://www.heyui.top/',
                                '热门前端@https://mg.meiflower.top/skill/front/all'
                            ]
                        },
                        {
                            moduleName: '跨境电商运营',
                            parts:[
                                '速卖通@https://gsp.aliexpress.com/',
                                '17Track@https://www.17track.net/zh-cn'
                            ]
                        },
                        {
                            moduleName: '代码托管',
                            parts:['Gitee@https://gitee.com/mgang','Github@https://github.com/mg0324']
                        },
                        {
                            moduleName: '开源项目',
                            parts:[
                                    '深度学习飞桨@https://www.paddlepaddle.org.cn/',
                                    '网络工具frp@https://github.com/fatedier/frp',
                                    'spring-boot-demo@https://github.com/xkcoding/spring-boot-demo',
                                    'spring-brick@https://gitee.com/starblues/springboot-plugin-framework-parent',
                                    'sofa-jarslink@https://github.com/sofastack/sofa-jarslink',
                                    'JavaGuide轻量级http框架@https://github.com/Snailclimb/jsoncat',
                                    '代码导航@https://github.com/liyupi/code-nav',
                                    '微信Markdown编辑器@https://github.com/doocs/md'
                            ]
                        },
                        {
                            moduleName: '算法学习',
                            parts:[
                                '左神算法@https://github.com/mg0324/zuoshen-algorithm',
                                '算法4可视化@https://algs4.cs.princeton.edu/home/'
                            ]
                        },
                        {
                            moduleName: 'IT大牛',
                            parts:[
                                'JavaGuide@https://github.com/Snailclimb',
                                'toBeBetterJavaer@https://github.com/itwanger/toBeBetterJavaer',
                                '龙进的博客@https://longjin666.cn/',
                                'liyupi@https://github.com/liyupi'
                            ]
                        },
                        {
                            moduleName: '树莓派',
                            parts:['树莓派操作系统@https://www.raspberrypi.com/software/operating-systems/']
                        },
                        {
                            moduleName: '文档相关',
                            parts:[
                                'python-selenium3@https://python-selenium-zh.readthedocs.io/zh_CN/latest/',
                                'python-argparse@https://docs.python.org/zh-cn/3/library/argparse.html#',
                                'python-random@http://study.yali.edu.cn/pythonhelp/library/random.html'
                            ]
                        },
                        {
                            moduleName: '我的资源',
                            parts:[
                                '我的蓝奏云@https://pc.woozooo.com/mydisk.php',
                                '七牛云oss@https://portal.qiniu.com/kodo/bucket/resource-v2?bucketName=mango',
                                '百度网盘@https://pan.baidu.com/',
                                '芒果网盘@http://disk.meiflower.top/'
                            ]
                        },
                        {
                            moduleName: '社会事宜',
                            parts:[
                                '广东交通局@https://gab.122.gov.cn/m/login',
                                '灵活就业事项@https://www.gdzwfw.gov.cn/portal/v2/search?region=440300&keyword=%E7%81%B5%E6%B4%BB%E5%B0%B1%E4%B8%9A&areaCode=440300&departmentCode=&onlyCorrespondingLevel=0&type='
                            ]
                        }

                    ]
                };
            },
            methods: {
                theName(v){
                    return v.split('@')[0];
                },
                theHref(v){
                    return v.split('@')[1];
                }
            }
        });
    })();
</script>