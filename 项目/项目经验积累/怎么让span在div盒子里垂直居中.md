# 怎么让span在div盒子里垂直居中
您可以使用CSS的flexbox布局来使`span`元素在`div`盒子中垂直居中。具体方法如下：

HTML代码：
```html
<div class="container">
  <span>这是一段文本</span>
</div>

```
css
```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px; /* 设置容器的高度 */
  border: 1px solid black; /* 方便查看容器的边框 */
}

span {
  font-size: 24px;
}
```
上面的代码中，我们首先使用`display: flex`将`div`盒子设置为flex容器，然后使用`justify-content: center`将`span`元素在容器中水平居中，最后使用`align-items: center`将`span`元素在容器中垂直居中。请注意，我们还需要为容器设置高度，这是因为在没有指定高度的情况下，flex容器会根据其内容自动调整高度，这可能会导致垂直居中效果不生效。

在上面的示例中，我们还添加了一个边框，以方便查看容器的边界。您可以根据您的需要自定义样式，例如更改容器高度、`span`元素的字体大小等。

# 我div里有三个元素，怎么用display：flex的同时又能调整三个的间距

要使用 `display: flex` 并控制子元素之间的间距，可以使用 `justify-content` 属性和 `margin` 属性来实现。具体方法如下：

HTML 代码：
```html
<div class="container">
  <div class="item">元素1</div>
  <div class="item">元素2</div>
  <div class="item">元素3</div>
</div>

```

css
```css
.container {
  display: flex;
  justify-content: space-between;
}

.item {
  margin-right: 20px; /* 定义元素之间的间距 */
}

```
上面的代码中，我们使用 `display: flex` 将父元素 `.container` 设置为 flex 容器，然后使用 `justify-content: space-between` 将子元素之间的间距平均分布到容器中，从而实现元素之间的距离。

在子元素 `.item` 中，我们使用 `margin-right: 20px` 定义元素之间的间距，这将在每个元素的右侧添加 20 像素的外边距，以创建元素之间的间隔。如果您需要不同的间距，请相应地更改 `margin-right` 属性的值。

需要注意的是，`justify-content` 属性不会在子元素的左右两侧添加额外的间距，所以我们使用 `margin` 属性来实现元素之间的间隔。

希望这可以帮到您！