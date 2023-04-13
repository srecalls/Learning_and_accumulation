
## 一，`transform`（变形）

1.`transform`字面的意思就是变形的意思，在`CSS3`中，`transform`支持的几个操作有

（1）**旋转`rotate`、**  
（2）**扭曲`skew`、**  
（3）**缩放`scale`**  
（4）**移动`translate`**  
（5）**矩阵变形`matrix`。**

2.`transform`不会触发回流，和重绘。


## 二，`transform`各操作使用介绍

1.rotate(xx deg)(2D), rotateX()(3D), rotateY()(3D)：以中心为基点，deg表示旋转的角度，为负数时表示逆时针旋转。

2.translate(x,y) ，translateX(x) ，translateY(y)：以中心为基点按照设定的x,y参数值,对元素进行进行平移。

3.scale(x,y)，scaleX(x,1)， scaleY(1,Y)：缩放基数为1，如果其值大于1元素就放大，反之其值小于1为缩小。

4.skew(x,y)， skewX(x)， skewY(y)：以中心为基点，第一个参数是水平方向扭曲角度，第二个参数是垂直方向扭曲角度。


![[Pasted image 20230406043834.png]]


三，基点
1.所有操作的默认的基点都在中心位置，我们可以使用transform-origin：(x,y)来改变元素基点。

x可以取left，center ，right，是水平方向取值，也可以取对应的百分值为left=0%;center=50%;right=100%

y可以取top ，center， bottom，是垂直方向的取值，其中top=0%;center=50%;bottom=100%;


```css
#tran{ 
	transform-orgin:(left,top);
	transform:rotate(30deg);
	}

```

![[Pasted image 20230406043910.png]]


## 四，浏览器兼容
1.目前`transform`只支持`IE10+`，对`IE9`不支持，要兼容浏览器需要添加前缀
```css
{
	transform:translate(10,10) // W3c标准
	-webkit-transform:translate(10,10) // Safari Chrome
	-moz-transform:translate(10,10) // firefox
	-ms-transform:translate(10,10) // IE9
	-o-transform:translate(10,10) // opera
	
}
```