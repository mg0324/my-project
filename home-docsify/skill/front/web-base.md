> web编程基础三剑客：html、css和javascript。

## html
> 超文本标记语言（英语：HyperText Markup Language，简称：HTML）是一种用于创建网页的标准标记语言。
您可以使用 HTML 来建立自己的 WEB 站点，HTML 运行在浏览器上，由浏览器来解析。

入门学习请参考菜鸟教程：https://www.runoob.com/html/html-tutorial.html

``` html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
    <h1>我的第一个标题</h1>
    <p>我的第一个段落。</p>
</body>
</html>
```

## css
> CSS (Cascading Style Sheets，层叠样式表），是一种用来为结构化文档（如 HTML 文档或 XML 应用）添加样式（字体、间距和颜色等）的计算机语言，CSS 文件扩展名为 .css。

入门学习请参考菜鸟教程：https://www.runoob.com/css/css-tutorial.html

``` css
body {
    background-color:#d0e4fe;
}
h1 {
    color:orange;
    text-align:center;
}
p {
    font-family:"Times New Roman";
    font-size:20px;
}
```
## javascript
> JavaScript 是 Web 的编程语言。
所有现代的 HTML 页面都可以使用 JavaScript。

入门学习请参考菜鸟教程：https://www.runoob.com/css/css-tutorial.html

``` html
<!DOCTYPE html>
<html>
	<head>
	<meta charset="utf-8">
	<title>菜鸟教程(runoob.com)</title>
	<style>
		#demo{
			font-size:14px;
			color: white;
			background-color: blue;
		}
	</style>
	<script>
		function displayDate(){
			document.getElementById("demo").innerHTML=Date();
		}
	</script>
	</head>
	<body>

	<h1>我的第一个 JavaScript 程序</h1>
	<p id="demo">这是一个段落</p>
	<button type="button" onclick="displayDate()">显示日期</button>
	</body>
</html>
```

### 总结
如下图，通过一个简单的示例将3者的关系清晰的表示出来：

![](../../static/skill/front/web/web-base.drawio.svg)

html是网页内容和布局的载体，通过css美化样式，js脚本来和用户交互，最后通过浏览器解析渲染显示出来。

> [!tip]
> 1. `html`利用标签组织各个部分，包括`header`、`body`，和一些布局标记`div`,`table`等，最后通过浏览器解析得到dom树并渲染显示网页。
> 2. `css`定义样式，并绑定到`html`的各个节点上，美化网页。
> 3. `javascript`作为浏览器脚本，可以给`html`的各个节点绑定好时间处理，让网页按钮得到响应，使得网页能和用户交互。
