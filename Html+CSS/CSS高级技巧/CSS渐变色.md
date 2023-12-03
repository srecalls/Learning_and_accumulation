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