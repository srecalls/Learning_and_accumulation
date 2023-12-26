
## 一，`transform`（变形）

1.`transform`字面的意思就是变形的意思，在`CSS3`中，`transform`支持的几个操作有

（1）**旋转`rotate`、**  
（2）**扭曲`skew`、**  
（3）**缩放`scale`**  
（4）**移动`translate`**  
（5）**矩阵变形`matrix`。**

**2.`transform`不会触发回流，和重绘。**


## 二，`transform`各操作使用介绍

1.`rotate(xx deg)(2D)`, `rotateX()(3D)`, `rotateY()(3D)`：以中心为基点，deg表示旋转的角度，为负数时表示逆时针旋转。

2.`translate(x,y)` ，`translateX(x)` ，`translateY(y)`：以中心为基点按照设定的x,y参数值,对元素进行进行平移。

3.`scale(x,y)`，`scaleX(x,1)`， `scaleY(1,Y)`：缩放基数为1，如果其值大于1元素就放大，反之其值小于1为缩小。

4.`skew(x,y)`， `skewX(x)`， `skewY(y)`：以中心为基点，第一个参数是水平方向扭曲角度，第二个参数是垂直方向扭曲角度。


非常抱歉，下面是拆分开的`translate()`、`translateX()`、`translateY()`、`scale()`、`scaleX()`、`scaleY()`、`skew()`、`skewX()`、`skewY()`的说明和示例：

2. `translate(x, y)`：以元素中心为基点，按照指定的水平和垂直距离进行平移。

   ```css
   .element {
     transform: translate(50px, 100px);
   }
   ```

   上述示例将元素在水平方向上平移50像素，在垂直方向上平移100像素。

1. `scale(x, y)`、`scaleX(x)`、`scaleY(y)`：以元素中心为基点，按照指定的水平和垂直比例进行缩放。

   ```css
   .element {
     transform: scale(1.5, 0.8);
   }
   ```

   上述示例将元素在水平方向上放大1.5倍，在垂直方向上缩小0.8倍。

1. `skew(x, y)`、`skewX(x)`、`skewY(y)`：以元素中心为基点，按照指定的水平和垂直角度进行扭曲。

   ```css
   .element {
     transform: skew(30deg, -10deg);
   }
   ```

   上述示例将元素在水平方向上扭曲30度，在垂直方向上扭曲-10度。

这些`translate()`、`translateX()`、`translateY()`、`scale()`、`scaleX()`、`scaleY()`、`skew()`、`skewX()`、`skewY()`函数可用于对元素进行平移、缩放和扭曲变换。您可以根据需要调整参数值来实现所需的效果。

![[Pasted image 20230406043834.png]]


## 三，基点
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

# transform

`transform`属性是CSS中用于对元素进行变换的属性，可以实现平移、旋转、缩放、倾斜等效果。下面是对`transform`属性的详细介绍以及带有示例的说明：

## 1.  平移（Translate）：通过`translate()`函数实现元素在平面上的移动。

   ```css
   .element {
     transform: translate(50px, 100px);
   }
   ```

   上述示例将元素沿X轴正向移动50像素，沿Y轴正向移动100像素。

## 2.  旋转（Rotate）：通过`rotate()`函数实现元素的旋转效果。

   ```css
   .element {
     transform: rotate(45deg);
   }
   ```

   上述示例将元素顺时针旋转45度。

## 3. 缩放（Scale）：通过`scale()`函数实现元素的缩放效果。

   ```css
   .element {
     transform: scale(1.5);
   }
   ```

   上述示例将元素在水平和垂直方向上放大1.5倍。

## 4. 倾斜（Skew）：通过`skew()`函数实现元素的倾斜效果。

   ```css
   .element {
     transform: skew(30deg, 10deg);
   }
   ```

   上述示例将元素在X轴方向上倾斜30度，在Y轴方向上倾斜10度。

## 5. 综合变换：可以通过组合使用多个变换函数来实现多个效果的叠加。

   ```css
   .element {
     transform: translate(50px, 50px) rotate(45deg) scale(1.2);
   }
   ```

   上述示例将元素先在平面上平移50像素，然后顺时针旋转45度，最后在水平和垂直方向上放大1.2倍。

## 6. 变换原点（Transform Origin）：通过`transform-origin`属性可以指定变换的原点，默认为元素的中心点。

   ```css
   .element {
     transform-origin: top left;
   }
   ```

   上述示例将变换的原点设置为元素的左上角。

以上是对`transform`属性及其常见函数的介绍。需要注意的是，`transform`属性可以与其他CSS属性一起使用，如`transition`属性实现平滑过渡效果，以及`animation`属性实现动画效果。通过灵活使用`transform`属性，可以为元素带来丰富的动态效果。


## transform-origin有哪些值
`transform-origin` 属性可以接受多种不同的值，用于定义变换的基点或原点。以下是一些常见的 `transform-origin` 值：

1. 百分比值：可以使用百分比相对于元素自身的宽度和高度来定义原点的位置。例如，`transform-origin: 50% 50%;` 表示变换的基点在元素的中心。
2. 长度值：可以使用具体的像素值来定义原点的位置。例如，`transform-origin: 100px 50px;` 表示基点位于距离元素左边缘100像素、距离上边缘50像素的位置。
3. 关键字值：有一些预定义的关键字可以用于直接指定基点的位置：
   - `top`：基点位于元素顶部中心。
   - `bottom`：基点位于元素底部中心。
   - `left`：基点位于元素左侧中心。
   - `right`：基点位于元素右侧中心。
   - `center`：基点位于元素水平和垂直中心。
   - `top left`：基点位于元素左上角。
   - `top right`：基点位于元素右上角。
   - `bottom left`：基点位于元素左下角。
   - `bottom right`：基点位于元素右下角。

你可以根据需要选择合适的 `transform-origin` 值来控制变换的基点和变换效果。

