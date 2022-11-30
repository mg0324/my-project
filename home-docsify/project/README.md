## 项目
``` plantuml
@startmindmap
* 项目
-- 程序猫大刚主页
--- 部署地址
----_ http://mg.meiflower.top
--- 项目地址
----_ https://gitee.com/mgang/my-project/home-docsify
--- 部署方式
----_ docsify + docker + docker-compose
--- 服务器
----_ hw服务器

-- 芒果网盘
--- 部署地址
----_ http://disk.meiflower.top
--- 部署方式
----_ java + kiftd + docker + docker-compose
--- 服务器
----_ hw服务器

-- 芒果卡片
--- 后端
---- card-api
-----_ http://mg.meiflower.top/card
-----_ springboot + sqlite3 + docker + docker-compose
-----_ hw服务器
---- flask-api 
-----_ http://mg.meiflower.top/api
-----_ python + flask + docker + docker-compose
-----_ hw服务器
--- 微信小程序
---- 芒果卡片
-----_ mpxapp + 小程序体验版
--- 前端
---- 点子队列
-----_ http://mg.meiflower.top/cp/keyqueue
-----_ vue + element
-----_ node服务器
---- 二维码卡片
-----_ http://mg.meiflower.top/cp/bqr
-----_ vue + element
-----_ node服务器
---- 卡片管理系统
-----_ http://mg.meiflower.top/card-admin/
-----_ heyui + heyui-admin
-----_ hw服务器
---- 项目地址
-----_ https://gitee.com/mangororg/card

-- 芒果网盘
--- 部署地址
----_ http://disk.meiflower.top
--- 部署方式
----_ java + kiftd + docker + docker-compose
--- 服务器
----_ hw服务器

-- JMedis
--- 项目地址
----_ https://gitee.com/mangoorg/jmedis
----_ Java自实现的redis服务

** 猫大刚博客
*** 部署地址
****_ http://mg.meiflower.top/mb/
*** 项目地址
****_ https://gitee.com/mgang/mb
*** 部署方式
****_ hugo + docker + docker-compose
*** 服务器
****_ hw服务器

** 我的计划
*** 部署地址
****_ http://mg.meiflower.top/plan/
*** 项目地址
****_ https://gitee.com/mgang/plan
*** 部署方式
****_ vuepress + docker + docker-compose
*** 服务器
****_ node服务器

** 我的简历
*** 部署地址
****_ http://mg.meiflower.top/mr/
*** 项目地址
****_ https://gitee.com/mgang/mr
*** 部署方式
****_ gitee pages

** 我的工具集
*** 部署地址
****_ http://mg.meiflower.top/mango-kit/
*** 项目地址
****_ https://gitee.com/mgang/mango-kit
*** 部署方式
****_ gitee pages

** 看云笔记
*** 工作总结
****_ http://worksum.meiflower.top
*** 深入学习
****_ http://doc.meiflower.top

@endmindmap
```

## 服务器
``` plantuml
@startmindmap
* 服务器

** node服务器
***_ 腾讯云
***_ 2C2G 5M 至2024年6月
*** 服务列表
****_ nginx 
*****_ mg支持https，至2023年2月
*****_ cp
*****_ plan
****_ frps

** hw服务器
***_ 华为云
***_ 2C4G 2M 至2023年11月
*** 服务列表
****_ card-api
****_ flask-api
****_ card-admin
****_ mb
****_ kiftd
****_ home-docsify
****_ redis-stack

** gitee pages服务器
***_ mango-kit
***_ mr

@endmindmap
```