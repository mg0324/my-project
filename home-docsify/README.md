<!-- 引入 layui.css -->
<link href="//unpkg.com/layui@2.7.6/dist/css/layui.css" rel="stylesheet">

<style type="text/css">
.layui-row{
    display: flex;
    flex-flow: row wrap;
    align-content: space-between;
}
.layui-row a{
    color: white;
}
.layui-row a:hover{
    text-decoration:underline;
}
.layui-row div{
    border: 1px solid gray;
    height:50px;
    display: flex;
    flex-flow: row wrap;
    align-content: center;
    justify-content: center;
    border-radius: 5px;
    margin-bottom: 5px;
    margin-right: 5px;
}
.layui-row .has {
    background-color: green;
    color: white;
}

.layui-row .doing {
    background-color: blue;
    color: white;
}

.layui-row .no {
    background-color: white;
    color: black;
}
</style>

<div id="container" class="layui-container">
    <div style="position:fixed;right:10px;bottom:50px;">
        <img style="width:40px;border:1px solid green;" src="https://mg.meiflower.top/res/drawio/okr/10.drawio.png"/>
    </div>
    <fieldset class="layui-elem-field" style="padding: 10px;" v-for="(item,index) in nodes">
        <legend>{{item.moduleName}}</legend>
        <div class="layui-row">
            <div v-if="status(part) == '1'" class="layui-col-xs12 layui-col-sm12 layui-col-md2 has" v-for="(part,index) in item.parts">
                <a :href="theHref(part)">{{theName(part)}}</a>
            </div>
            <div v-else-if="status(part) == '2'" class="layui-col-xs12 layui-col-sm12 layui-col-md2 doing">
                <a :href="theHref(part)" target="_blank">{{theName(part)}}</a>
            </div>
            <div v-else class="layui-col-xs12 layui-col-sm12 layui-col-md2 no">
                    {{theName(part)}}
                </div>
            </div>
    </fieldset>
    <div style="text-align:right;color:gray;">
        蓝色 - 进行中<br/>
        绿色 - 完　成<br/>
        白色 - 待修行<br/>
    </div>
</div>

<script>
    (function(){
         new Vue({
            el:'#container',
            data() {
                return {
                    nodes: [
                        {
                            moduleName: 'DevOps',
                            parts:['GitLab','Maven','Jekins','Docker','Kuberneters']
                        },
                        {
                            moduleName: '高可用',
                            parts:['HAProxy','KeepAlived']
                        },
                        {
                            moduleName: '高性能Web',
                            parts:['Nginx','Openresty']
                        },
                        {
                            moduleName: '分库分表',
                            parts:['Sharding JDBC','MyCat']
                        },
                        {
                            moduleName: '分布式存储',
                            parts:['FastDFS','HDFS']
                        },
                        {
                            moduleName: '分布式消息队列',
                            parts:['Kafka','RocketMQ','RabbitMQ']
                        },
                        {
                            moduleName: '分布式缓存',
                            parts:['Redis','Memcache']
                        },
                        {
                            moduleName: '分布式理论',
                            parts:['CAP','Raft','一致性Hash算法']
                        },
                        {
                            moduleName: '工具集',
                            parts:['IDEA','Git','Maven','Grade','UML']
                        },
                        {
                            moduleName: '计算机语言学习',
                            parts:['Java体系学习@2@https://mgang.gitee.io/s-java/','Python体系学习']
                        },
                        {
                            moduleName: '编程基石',
                            parts:['数据结构','算法','设计模式']
                        },
                        {
                            moduleName: '计算机基础',
                            parts:['计算机组成原理@2@https://mgang.gitee.io/sn-cpu/','计算机网络','操作系统']
                        }
                    ]
                };
            },
            methods: {
                theName(v){
                    return v.split('@')[0];
                },
                theHref(v){
                    return v.split('@')[2];
                },
                status(v){
                    return v.split('@')[1];
                }
            }
        });
    })();
</script>