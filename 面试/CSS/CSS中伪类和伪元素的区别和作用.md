[[伪元素选择器]]
[[Html+CSS/HTML5和CSS3提高/CSS3的新特性/结构伪类选择器|结构伪类选择器]]

	伪元素: 在内容元素的前后插入额外的元素或样式，但是这些元素实际上并不在文档中生成。它们只在外部显示可见，但不会在文档的源代码中找到它们，因此，称为“伪”元素。
例如:

```js
p::before {
	content: "第一章"
}
P::after {
	content: "hot"
}
p::first-line {
	background: red
}
P::first-letter {
	font-size: 30px
}
```


	伪类:将特殊的效果添加到特定选择器上。它是已有元素上添加类别的，不会产生新的元素。
例如:
```js
a:hover {
	color: #FF00FF
}
p:first-child {
	color: red
}
```
	
	总结:伪类是通过在元素选择器上加入伪类改变元素状态，而伪元素通过对元素的操作进行对元素的改变


