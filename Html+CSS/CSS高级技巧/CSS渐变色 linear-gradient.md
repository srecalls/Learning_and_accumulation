![[CSS渐变色-1.png]]

https://www.runoob.com/css3/css3-gradients.html
CSS3 渐变（gradients）可以让你在两个或多个指定的颜色之间显示平稳的过渡。

以前，你必须使用图像来实现这些效果。但是，通过使用 CSS3 渐变（gradients），你可以减少下载的时间和宽带的使用。此外，渐变效果的元素在放大时看起来效果更好，因为渐变（gradient）是由浏览器生成的。

CSS3 定义了两种类型的渐变（gradients）：

- **线性渐变（Linear Gradients）- 向下/向上/向左/向右/对角方向**
- **径向渐变（Radial Gradients）- 由它们的中心定义**

线性渐变相关属性：[background-image](https://www.runoob.com/cssref/pr-background-image.html)。

线性渐变在线工具：[渐变在线工具](https://c.runoob.com/more/gradients/#LemonLime)。


## CSS3 线性渐变

为了创建一个线性渐变，你必须至少定义两种颜色节点。颜色节点即你想要呈现平稳过渡的颜色。同时，你也可以设置一个起点和一个方向（或一个角度）。

**线性渐变的实例：**
![[CSS渐变色.png]]

### 语法

```css
background-image: linear-gradient(direction, color-stop1, color-stop2, ...);
```

**线性渐变 - 从上到下（默认情况下）**

下面的实例演示了从顶部开始的线性渐变。起点是红色，慢慢过渡到蓝色：

```js
#grad {
    background-image: linear-gradient(#e66465, #9198e5);
}
```

**线性渐变 - 从左到右**

下面的实例演示了从左边开始的线性渐变。起点是红色，慢慢过渡到黄色：
```js
#grad {
  height: 200px;
  background-image: linear-gradient(to right, red , yellow);
}
```


**线性渐变 - 对角**

你可以通过指定水平和垂直的起始位置来制作一个对角渐变。

下面的实例演示了从左上角开始（到右下角）的线性渐变。起点是红色，慢慢过渡到黄色：
从左上角到右下角的线性渐变：
```js
#grad {
  height: 200px;
  background-image: linear-gradient(to bottom right, red, yellow);
}
```


## 使用角度

如果你想要在渐变的方向上做更多的控制，你可以定义一个角度，而不用预定义方向（to bottom、to top、to right、to left、to bottom right，等等）。

### 语法

```css
background-image: linear-gradient(angle, color-stop1, color-stop2);
```

角度是指水平线和渐变线之间的角度，逆时针方向计算。换句话说，0deg 将创建一个从下到上的渐变，90deg 将创建一个从左到右的渐变。
![[CSS渐变色-2.png]]

但是，请注意很多浏览器（Chrome、Safari、firefox等）的使用了旧的标准，即 0deg 将创建一个从左到右的渐变，90deg 将创建一个从下到上的渐变。换算公式 **90 - x = y** 其中 x 为标准角度，y为非标准角度。

下面的实例演示了如何在线性渐变上使用角度：

```css
#grad {
  background-image: linear-gradient(-90deg, red, yellow);
}
```


`linear-gradient` 是 CSS 中用于创建线性渐变色的函数。它允许您在元素的背景、边框或文本等属性中应用从一个颜色到另一个颜色的平滑过渡效果。以下是 `linear-gradient` 函数的详细说明和示例：

语法：
```css
linear-gradient([direction], [color-stop1], [color-stop2], ...);
```

- `[direction]`：表示渐变的方向。可以使用角度值（例如 `45deg` 表示 45 度角）或关键字（例如 `to right` 表示从左到右）来指定渐变的方向。默认值为 `to bottom`，表示从上到下的垂直渐变。
- `[color-stop1]`, `[color-stop2]`, ...：表示渐变的颜色和位置。您可以指定任意多个颜色和位置（称为颜色停止点），以控制渐变的过渡效果。颜色停止点由颜色值和可选的位置值组成。

示例：
```css
div {
  background: linear-gradient(to right, #ff0000, #00ff00);
}
```
上述示例将 `<div>` 元素的背景应用了一个从红色到绿色的水平渐变。渐变的方向是从左到右（`to right`），颜色停止点为红色 (`#ff0000`) 和绿色 (`#00ff00`)。

您还可以添加更多的颜色停止点来创建更复杂的渐变效果：
```css
div {
  background: linear-gradient(45deg, #ff0000, #00ff00, #0000ff);
}
```
在这个示例中，渐变的方向是 45 度角，颜色停止点为红色 (`#ff0000`)、绿色 (`#00ff00`) 和蓝色 (`#0000ff`)，从左上角开始平滑过渡。

`linear-gradient` 还支持指定颜色停止点的位置，以控制颜色的分布和过渡的速度。例如：
```css
div {
  background: linear-gradient(to bottom, #ff0000 0%, #00ff00 50%, #0000ff 100%);
}
```
在这个示例中，渐变的方向是从上到下，红色 (`#ff0000`) 从顶部开始，绿色 (`#00ff00`) 在距离顶部 50% 的位置开始，蓝色 (`#0000ff`) 在底部结束。

通过调整 `linear-gradient` 函数中的参数，您可以创建各种不同的线性渐变色效果，以实现所需的视觉效果。