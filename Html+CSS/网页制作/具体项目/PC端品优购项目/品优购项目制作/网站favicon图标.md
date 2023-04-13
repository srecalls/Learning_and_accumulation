# 网站favicon图标
**favicon.ico**一般用于作为缩略的网站标志，它显示在浏览器的地址栏或者标签上。
目前主要的浏览器都支持**favicon.ico**图标。
一、制作favicon图标
1．把品优购图标切成png图片。
2.把png图片转换为ico图标，这需要借助于第三方转换网站，例如比特虫 : http://www.bitbug.net/

二、favicon图标放到网站根目录下
![[Pasted image 20220920151113.png]]

三、HTML页面引入favicon图标
1．在html页面里面的\<head> \</head>元素之间引入代码.

```CSS
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon"/>
```
`

