**4、animation-delay:5s  (动画等待5后开始)**
`animation-delay` 是 CSS 中用于指定动画延迟开始的属性。它定义了动画效果开始之前的等待时间。

该属性接受一个时间值作为参数，表示延迟的时间长度。时间值可以使用秒（s）或毫秒（ms）表示。具体的语法如下：

```css
animation-delay: <time>;
```

例如，如果要将一个动画效果的延迟时间设置为 1 秒，可以这样设置：

```css
.element {
  animation-name: myAnimation;
  animation-duration: 2s;
  animation-delay: 1s;
}
```

在上述示例中，`.element` 类的元素将应用名为 "myAnimation" 的动画效果，并将其持续时间设置为 2 秒，延迟时间设置为 1 秒。

通过调整 `animation-delay` 的值，您可以控制动画效果在触发后的延迟开始时间。较长的延迟时间将导致动画效果在触发后更晚开始，而较短的延迟时间将导致动画效果更快开始。

使用 `animation-delay` 属性，您可以创建更复杂的动画序列，通过在不同元素上设置不同的延迟时间，使它们在不同的时间点开始执行动画效果。

请注意，`animation-delay` 属性仅影响动画的开始时间，而不会影响动画的持续时间。如果需要设置动画的持续时间，请使用 `animation-duration` 属性。