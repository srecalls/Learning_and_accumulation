**5、animatiom-iteration-count：1   （动画播放次数为1次）**
`animation-iteration-count` 是 CSS 中用于指定动画循环次数的属性。它定义了动画效果在播放完一次后是否重复播放，并可以设置重复播放的次数。

该属性接受一个数值或关键字作为参数，表示动画的循环次数。
常用的数值包括**整数值（如 1、2、3）和特殊值 `infinite`（表示无限循环）**。具体的语法如下：

```css
animation-iteration-count: <count>;
```

例如，如果要将动画效果设置为重复播放 3 次，可以这样设置：

```css
.element {
  animation-name: myAnimation;
  animation-duration: 2s;
  animation-iteration-count: 3;
}
```

在上述示例中，`.element` 类的元素将应用名为 "myAnimation" 的动画效果，并设置其持续时间为 2 秒，循环播放 3 次。

如果希望动画无限循环播放，可以使用关键字 `infinite`：

```css
.element {
  animation-name: myAnimation;
  animation-duration: 2s;
  animation-iteration-count: infinite;
}
```

上述示例中的动画效果将无限循环播放，直到被停止或移除。

通过调整 `animation-iteration-count` 的值，您可以控制动画效果的重复播放次数。默认情况下，动画只会播放一次，可以通过设置循环次数为大于 1 的值或使用 `infinite` 来实现重复播放。

此外，您还可以使用其他动画属性（如 `animation-direction`、`animation-fill-mode` 等）来控制动画的播放方向和填充模式等。通过组合使用这些动画属性，您可以创建更复杂的动画效果和过渡效果。