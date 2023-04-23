要让输入框 `<input>` 和按钮 `<button>` 在同一行，可以使用 CSS 中的 `display` 和 `float` 属性。

一种简单的方法是将输入框和按钮放在同一个父元素中，然后将父元素的 `display` 属性设置为 `flex`，并将输入框和按钮的 `flex` 属性设置为 `1`，以使它们平均分配父元素的宽度。例如，以下代码将输入框和按钮放在一个 `<div>` 元素中，并将该元素的 `display` 属性设置为 `flex`：

```html
<div style="display: flex;">
  <input type="text" style="flex: 1;">
  <button style="flex: 1;">按钮</button>
</div>
```

在这个示例中，我们将父元素的 `display` 属性设置为 `flex`，这样输入框和按钮就会在同一行上。然后，我们将输入框和按钮的 `flex` 属性都设置为 `1`，以使它们平均分配父元素的宽度。请注意，这只是一个基本的示例，您需要将内联样式替换为类或 ID 选择器，并根据您的实际需求进行调整。

另一种方法是使用 `float` 属性。例如，以下代码将输入框和按钮的 `float` 属性都设置为 `left`，以使它们在同一行上：

```html
<input type="text" style="float: left;">
<button style="float: left;">按钮</button>
```

在这个示例中，我们将输入框和按钮的 `float` 属性都设置为 `left`，这样它们就会在同一行上，并排显示。请注意，当使用 `float` 属性时，需要注意清除浮动，以避免影响后面的元素布局。