<!-- 引入 layui.css -->
<link href="//unpkg.com/layui@2.7.6/dist/css/layui.css" rel="stylesheet">

## 猫大刚 * Mango Mei
<i class="layui-icon layui-icon-email" style="color:green;"></i> 邮箱：1092017732@qq.com <br/>
<i class="layui-icon layui-icon-login-wechat" style="color:green;"></i> 微信：meigangww<br/>
<i class="layui-icon layui-icon-read" style="color:green;"></i> 博客：http://mg.meiflower.top/mb/ <br/>
<i class="layui-icon layui-icon-star" style="color:green;"></i> csdn：https://blog.csdn.net/mg0324 

## 经历
<div id="container">
    <ul class="layui-timeline">
        <li class="layui-timeline-item" v-for="(node,index) in nodes" :key="index">
            <i class="layui-icon layui-timeline-axis">&#xe63f;</i>
            <div class="layui-timeline-content layui-text">
            <div class="layui-timeline-title">{{node.year}}</div>
            <p v-for="remark in node.remarks">
                {{remark}}
            </p>
            </div>
        </li>
    </ul>
</div>

<script>
    (function(){
         new Vue({
            el:'#container',
            data() {
                return {
                    nodes: [
                        {
                            year: '2021年4月',
                            remarks: [
                                "4月17号离开浪潮，结束了5年多的电子政务行业经历，进入平安做hr平台相关业务。",
                                "开始实践spring cloud微服务和docker容器自动化部署，以及k8s容器编排相关技术。"
                            ]
                        },
                        {
                            year: '2017年',
                            remarks: [
                                "2017年，来到深圳，加入浪潮。从事电子政务行业，为人民群众提供更好的办事体验，可跳转深圳网上办事大厅。参与政务大厅，网上预约，公安系统等平台的建设；快速积累行业经验，沉淀开发技术。",
                                "从jquery到react到vue，从传统系统到 前后台分离体系，从单系统到分布式，从普通组员到小组长，从后端到关注全栈，各方面都得以提升。"
                            ]
                        },
                        {
                            year: '2015年-2016年',
                            remarks: [
                                "在广州工作，接触电子政务，交易服务，房地产系统和医院门户网站的领域，慢慢的积累工作经验。"
                            ]
                        },
                        {
                            year: '2015年7月',
                            remarks: [
                                "毕业于普通本科（二本）院校，湖北文理学院。在校期间， 完成了朋友社区、 襄阳内容管理系统和 毕业设计权限控制 等3个系统。"
                            ]
                        },
                        {
                            year: '2015年1月',
                            remarks: [
                                "到佛山实习，接触到社区矫正和智慧公路领域。"
                            ]
                        }
                    ]
                };
            }
        });
    })();
</script>