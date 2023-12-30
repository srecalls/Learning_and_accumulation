**8、animation-play-state：  （设置动画是否暂停）**
`animation-play-state` 是 CSS 中用于控制动画播放状态的属性。它允许您暂停或恢复动画的播放。

该属性接受以下两个关键字作为参数：

- `running`：默认值，动画正常播放。
- `paused`：动画暂停播放。

具体的语法如下：

```css
animation-play-state: running | paused;
```

例如，如果要暂停动画的播放，可以这样设置：

```css
.element {
  animation-name: myAnimation;
  animation-duration: 2s;
  animation-play-state: paused;
}
```

在上述示例中，`.element` 类的元素应用名为 "myAnimation" 的动画效果，并设置其持续时间为 2 秒。通过将 `animation-play-state` 设置为 `paused`，动画将暂停播放。

**通过 JavaScript 或通过添加交互事件**，您可以使用 `animation-play-state` 属性来动态控制动画的播放状态。例如，**可以通过点击按钮来暂停或恢复动画的播放。**

```css
.element {
  animation-name: myAnimation;
  animation-duration: 2s;
  animation-play-state: running;
}

.paused {
  animation-play-state: paused;
}


/* 动画关键帧 */
div:hover {
	/* 设置动画是否暂停*/
	animation-play-state: paused;
}
```




```html
<div class="element"></div>
<button onclick="pauseAnimation()">暂停动画</button>

<script>
  function pauseAnimation() {
    var element = document.querySelector('.element');
    element.classList.toggle('paused');
  }
</script>
```

在上述示例中，点击按钮会通过切换元素的类名来暂停或恢复动画的播放。

通过控制 `animation-play-state` 属性，您可以在需要时随时暂停或恢复动画的播放，以实现更灵活的动画控制和交互效果。