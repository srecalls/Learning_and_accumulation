`animation-fill-mode` 是 CSS 中用于指定动画在**播放之前**和**播放之后**如何**应用样式的属性**。它定义了**动画播放前和播放后元素的样式状态。**

该属性接受以下几个关键字作为参数：

- `none`：默认值，动画不会影响元素的样式状态。
- `forwards`：动画播放完毕后，元素将保持动画结束时的样式状态。
- `backwards`：动画播放前，元素将应用动画起始时的样式状态。
- `both`：同时应用 `forwards` 和 `backwards` 的效果，即动画播放前和播放后都应用对应的样式状态。

具体的语法如下：

```css
animation-fill-mode: none | forwards | backwards | both;
```

例如，如果要在动画播放完毕后保持动画结束时的样式状态，可以这样设置：

```css
.element {
  animation-name: myAnimation;
  animation-duration: 2s;
  animation-fill-mode: forwards;
}
```

在上述示例中，`.element` 类的元素将应用名为 "myAnimation" 的动画效果，并设置其持续时间为 2 秒，动画播放完毕后将保持动画结束时的样式状态。

通过调整 `animation-fill-mode` 的值，您可以控制动画播放前和播放后元素的样式状态。这使您能够在动画播放期间创建平滑的过渡效果，或者在动画播放完毕后保持特定的样式状态。

请注意，`animation-fill-mode` 属性并不会改变元素的实际位置，它只是应用动画的样式状态。如果需要让元素在动画播放期间改变位置，请使用 CSS 属性（如 `transform`、`position` 等）来实现位置变化。