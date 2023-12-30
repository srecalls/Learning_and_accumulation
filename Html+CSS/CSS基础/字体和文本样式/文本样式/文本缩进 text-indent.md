# 文本缩进 text-indent
#### ➢ 属性名：
**text-indent**  记住是**段落的第一行**
#### ➢ 取值： 
**• 数字+px** 
**• 数字+em（推荐：1em = 当前标签的font-size的大小）**


在 CSS 中，`text-indent` 属性用于设置文本的缩进，即**段落第一行**相对于左侧边界的偏移量。

`text-indent` 属性可以接受以下类型的值：

- `<length>`：指定一个固定的长度值，以像素（px）、百分比（%）或其他长度单位表示。正值将使第一行向右缩进，负值将使第一行向左缩进。
- `inherit`：继承父元素的 `text-indent` 值。

以下是一个示例，展示了 `text-indent` 属性的使用：

```html
<style>
  .container {
    text-indent: 20px;
  }
</style>

<p class="container">
  This is a paragraph with an indented first line. The text of this paragraph will be indented by 20 pixels from the left side.
</p>
```

在上述示例中，`.container` 类选择器的段落元素应用了 `text-indent: 20px;` 属性。这使得段落的第一行缩进了 20 像素。

通过使用 `text-indent` 属性，您可以控制段落或文本块中第一行的缩进，以改善排版效果。常见的应用场景包括段落首行缩进、实现列表样式等。

![[Pasted image 20220905161933.png]]