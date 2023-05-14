# HTML_DTD
HTML并非图灵完备，他只是一门标记语言

图灵完备（Turing complete）是指一种计算机系统或编程语言具有与图灵机等价的计算能力。也就是说，如果一种计算机系统或编程语言是图灵完备的，那么它可以执行任何图灵机可以执行的计算任务。
![[Pasted image 20230506182552.png]]

标签（元素） ： 由<>包裹

文本： 不带有<> ，如果有需要进行转义，而在放在CDATA中则不需要转义

注释：HTML只有一种标准注释方式 
```html
<!-- comments -->
```

DTD (Document Type Defination)
用来声明文档中可以有哪些标签，每个标签语法特性有哪些，类似语言的语法定义文档

处理信息：目前没有什么大用，可以忽略


# HTML全部标签分类
![[Pasted image 20230506183653.png]]


文档型：必须具备的标签
闭合型：标签是否闭合
- 闭合：向\</p>这种  就是有反斜杠的


# HTML head标签
![[Pasted image 20230506202259.png]]
# HTML head标签
head
- title

        标签，全局唯一
- base

        向页面所有相对URL提供前缀
        全局唯一，不建议使用
- meta

        通常是约定好的键值对
        例外：charset、http-equiv
- link

        rel决定类型，href决定引入地址
- script

        type指定MIME类型
        可内嵌代码，可外链文件

title 显示网站标题
base 如今不再留下
meta是约定好的
link ref
script

## MIME类型
 MIME类型是一种在互联网上标识文件类型的标准化方式。MIME类型是通过在HTTP头部中添加Content-Type字段来表示的。MIME类型由两个部分组成：类型(type)和子类型(subtype)，中间用斜杠分隔。例如，HTML文件的MIME类型为"text/html"，JPEG图片的MIME类型为"image/jpeg"。




# HTML body功能性标签
![[Pasted image 20230506202453.png]]

# 功能标签 body
HTML中的body功能性标签是用来标识页面内容的主体部分的标签，其中包含了网页的主要内容。以下是一些常见的HTML body功能性标签：

-   `<header>`：表示页面或页面部分的页眉。
-   `<nav>`：表示导航链接的部分。
-   `<main>`：表示页面的主要内容，通常只出现一次。
-   `<article>`：表示独立的文章或者内容块。
-   `<section>`：表示文档中的节或者区块。
-   `<aside>`：表示页面的侧边栏内容。
-   `<footer>`：表示页面或页面部分的页脚。

这些标签有助于将页面内容分组和组织，使页面结构更加清晰和易于理解。此外，这些标签还可以帮助搜索引擎和其他工具更好地理解网页的结构和内容，提高网页的可访问性和SEO效果。


# HTML ARIA
![[Pasted image 20230506202555.png]]
HTML中可以使用ARIA属性来为组件和元素提供附加的语义信息。例如，可以使用ARIA属性来表示一个按钮、一个下拉列表或者一个对话框的角色和状态。以下是一些常见的ARIA属性：

-   `role`：表示元素的角色或者类型。
-   `aria-label`：提供元素的文本标签，用于辅助技术读取。
-   `aria-describedby`：指向一个元素的ID，该元素包含了对当前元素的描述信息。
-   `aria-haspopup`：表示元素是否有一个弹出菜单或对话框。
-   `aria-expanded`：表示元素是否展开或折叠。

使用ARIA属性可以帮助开发人员使得Web应用程序更加可访问，从而提高用户体验和可用性。同时，使用ARIA属性还可以使得Web应用程序更容易被搜索引擎爬取和理解，提高SEO效果。


# HTML5
![[Pasted image 20230506202745.png]]


# HTML5 语义化标签
![[Pasted image 20230506202919.png]]
可以帮助开发者更好的维护网站结构
也便于seo来进行网站的整理


# HTML5 表单增强
![[Pasted image 20230506203112.png]]
HTML5为表单提供了许多增强功能，使得Web开发人员可以更容易地创建交互式表单，并提供更好的用户体验。以下是HTML5表单增强的一些主要特性：

新的表单元素：HTML5引入了一些新的表单元素，如`<datalist>`、`<keygen>`、`<output>`等，可以帮助开发人员更好地处理表单数据。

表单验证：HTML5新增了一些表单验证属性和API，如`required`、`pattern`、`checkValidity()`等，可以帮助开发人员在客户端验证表单数据的有效性。

自动填充：HTML5的自动填充功能可以自动填充表单字段，从而提高用户填写表单的效率。

日期和时间选择器：HTML5新增了`<input type="date">`、`<input type="time">`等表单元素，可以帮助用户更方便地选择日期和时间。

拖放上传：HTML5的拖放上传功能可以允许用户将文件拖拽到表单中进行上传，提高了上传文件的便捷性和用户体验。

表单进度条：HTML5的表单进度条可以显示表单提交的进度，从而提高用户对表单提交的可见性和可控性。


# HTML5 存储
![[Pasted image 20230506203214.png]]
Cookie
Local Storage
Session Storage


# HTML indexedDB
![[Pasted image 20230506203358.png]]


# HTML5 PWA&AMP
基于存储的应用
AMP主要对搜索引擎来用


# HTML5 Audio
![[Pasted image 20230506203845.png]]


# HTML5 Video
![[Pasted image 20230506204056.png]]

# HTML5 二进制
![[Pasted image 20230506204531.png]]

# HMTL API
![[Pasted image 20230506204659.png]]


# HTML Web Worker
![[Pasted image 20230506204724.png]]


# HTML5 Web Socket

![[Pasted image 20230506205052.png]]
支持全双工通信的http方式
本质是一个TCP的连接请求


# HTML5 Shadow DOM
特殊的节点
可以挂载很多节点
![[Pasted image 20230506205327.png]]
避免内部元素被外部元素访问到


# HTML5 Web Component
![[Pasted image 20230506205503.png]]
赋予可以自定义标签的能力



# HTML5 SVG&Canvas
![[Pasted image 20230506205828.png]]
SVG是一个基于xml的，一个向量化的图片，可以用来交互 （矢量的）（可扩展）（不会失真）
svg对事件处理的更好，本身是dom元素，不能绘制很复杂图像
Canvas是html元素   （点阵的）（会失真） 游戏



# WebGL & WebGPU
![[Pasted image 20230506205854.png]]
![[Pasted image 20230506205905.png]]

# HTML5 WebAssembly

![[Pasted image 20230506210011.png]]
紧凑的二进制格式文件


