# visibility 显示隐藏

#### visibility 可见性
**visibility属性用于指定一个元素应可见还是隐藏。
●visibility : visible;元素可视
●visibility : hidden;元素隐藏
●inherit : 继承上一个父对象的可见性**

**<font color=red>visibility隐藏元素后，继续占有原来的位置。</font>**

**如果隐藏元素想要原来位置，就用visibility : hidden
如果隐藏元素不想要原来位置，就用display : none (用处更多重点)**


在 CSS 中，`visibility` 属性用于控制元素的可见性，即元素在页面上的显示和隐藏。

`visibility` 属性可以接受以下两个值：

- `visible`：默认值，表示元素可见，将在页面中显示。
- `hidden`：表示元素隐藏，不在页面中显示，但仍占据其原有的空间。

以下是一个示例，展示了 `visibility` 属性的使用：

```html
<style>
  .container {
    visibility: hidden;
  }
</style>

<div class="container">
  <p>This is a hidden container.</p>
</div>
```

在上述示例中，`.container` 类选择器的 `<div>` 元素应用了 `visibility: hidden;` 属性。这将使容器元素隐藏，不在页面中显示，但仍会占据其原有的空间。

通过使用 `visibility` 属性，您可以根据需要控制元素的显示和隐藏。与 `display` 属性不同，`visibility` 属性隐藏的元素仍会占据其空间，而不会影响其他元素的布局。这在需要在页面中保留元素占位但不显示其内容时非常有用。

请注意，使用 `visibility: hidden;` 隐藏元素仍然存在于文档流中，可以通过 JavaScript 或其他方式修改其可见性。要完全移除元素，可以考虑使用 `display: none;`。


