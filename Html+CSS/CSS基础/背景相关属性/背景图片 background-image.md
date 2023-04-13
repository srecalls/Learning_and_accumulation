# 背景图片 background-image
#### ➢ 属性名：
**background-image（bgi）** 
#### ➢ 属性值： 
![[Pasted image 20220906090004.png]]
#### ➢ 注意点： 
**• 背景图片中url中可以省略引号 
• 背景图片默认是在水平和垂直方向平铺的 
• 背景图片仅仅是指给盒子起到装饰效果，类似于背景颜色，是不能撑开盒子的**

![[Pasted image 20220906090029.png]]
怎么能调整background-image里的图片大小
-   `auto`: 图片大小不会被调整。
-   `cover`: 图片会被缩放以完全覆盖元素，可能会剪切部分图片。
-   `contain`: 图片会被缩放以适合元素的大小，保持纵横比，可能会有空白区域。
- 您可以设置`background-size`属性的值为一个百分比值、像素值、关键字值（如`cover`或`contain`）或者一个由多个值组成的字符串（如`50% 50%`表示图片在水平和垂直方向上都居中）。

以下是一个使用`background-size`属性调整背景图片大小的示例：
```html
<div style="background-image: url('your-image-url'); background-size: cover; width: 400px; height: 400px;"></div>

```
在上面的示例中，我们使用`background-size: cover`将背景图片缩放以完全覆盖元素，并设置元素的宽度和高度为400像素，以使其具有指定的尺寸。

您可以根据需要调整`background-size`属性的值，以适合您的设计要求。