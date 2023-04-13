# CSS属性书写顺序
建议遵循以下顺序:

![[Pasted image 20220908191623.png]]
#### 1.布局定位属性: 
display / position/ float / clear / visibility/ overflow (建议display第一个写,毕竟关系到模式)
#### 2.自身属性: 
width/ height / margin/ padding / border/ background
#### 3.文本属性: 
color/ font / text-decoration/ text-align/ vertical-align/ white- space / break-word
#### 4.其他属性( CSS3) :
content / cursor / border-radius / box-shadow/ text-shadow/ background:linear-gradient...

```css
，idc{
	display: block;
	position: relative;
	float: left;
	width: 1 00px;
	height: 100px;
	margin: 0 10px;
	padding: 20px 0;
	font-family: Arial, 'Helvetica Neue' ，Helvetica, sans-serif;
	color: #333;
	background: rgba(0,0,0, .5) ;
	border-radius: 10px;
}

```
