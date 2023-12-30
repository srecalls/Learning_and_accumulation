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



在 CSS 中，`background-image` 属性用于设置元素的背景图片。

`background-image` 属性接受一个 URL 值，指定要用作背景图像的文件路径或 URL。可以使用相对路径或绝对路径指向图像文件，也可以使用外部资源的 URL。

以下是 `background-image` 属性的示例用法：

```css
div {
  background-image: url("image.jpg");
}
```

在上述示例中，`div` 元素的背景图片被设置为名为 "image.jpg" 的图像文件。请确保图像文件路径或 URL 正确，并位于可以被访问到的位置。

除了单个背景图片，您还可以通过使用多个 `background-image` 属性来设置多个背景层叠在一起：

```css
div {
  background-image: url("image1.jpg"), url("image2.jpg");
}
```

上述示例中，`div` 元素将同时显示 "image1.jpg" 和 "image2.jpg" 两个图像作为背景图片，层叠在一起。

请注意，背景图片默认会平铺（repeat）以填充整个元素的背景区域。您可以使用其他背景属性（如 `background-repeat`、`background-size`、`background-position`）来控制背景图片的平铺方式、尺寸和位置。

```css
div {
  background-image: url("image.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}
```

上述示例中，`background-repeat` 设置为 `no-repeat`，表示背景图片不会平铺；`background-size` 设置为 `cover`，表示背景图片将被缩放以填充元素的背景区域；`background-position` 设置为 `center`，表示背景图片在元素中居中显示。

通过使用 `background-image` 属性，您可以为元素设置背景图片，实现各种视觉效果和装饰效果。