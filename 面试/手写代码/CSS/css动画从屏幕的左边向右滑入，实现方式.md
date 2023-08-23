可以使用CSS中的`@keyframes`关键字来创建动画，并通过`animation`属性将其应用于元素。下面是一个从屏幕左侧向右滑入的简单示例动画：

HTML:

```html
<div class="slide-in"></div>
```

CSS:
[[7.transition和animation的区别]]
```css
.slide-in {
  width: 100px;
  height: 100px;
  background-color: red;
  animation: slide 1s ease-in forwards;
}

@keyframes slide {
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(0);
  }
}
```

在上面的代码中，我们首先创建一个`<div>`元素，并将其类设置为`slide-in`。然后，我们定义了一个名为`slide`的`@keyframes`动画，在该动画中，元素从屏幕左侧向右移动。最后，我们通过在元素的CSS样式中设置`animation`属性来应用动画，其中`animation`属性包括动画名称`slide`，持续时间1秒，缓动函数`ease-in`，以及最终状态`forwards`。