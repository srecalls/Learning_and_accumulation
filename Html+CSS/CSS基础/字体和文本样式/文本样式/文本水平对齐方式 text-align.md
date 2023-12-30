# 文本水平对齐方式 text-align

#### ➢ 属性名：
**text-align** 
#### ➢ 取值：


在 CSS 中，`text-align` 属性用于控制文本的水平对齐方式。

`text-align` 属性可以接受以下取值：

- `left`：将文本左对齐。
- `right`：将文本右对齐。
- `center`：将文本居中对齐。
- `justify`：将文本两端对齐，除非最后一行。
- `start`：根据文本的书写方向，左对齐或右对齐（取决于文本的书写方向，例如，对于从右向左的文本，将右对齐）。
- `end`：根据文本的书写方向，右对齐或左对齐。

`justify` 是 CSS 中 `text-align` 属性的一个取值选项，用于将文本两端对齐，除非最后一行。

当使用 `text-align: justify;` 时，浏览器会**自动调整文本行的间距和字间距**，以使**每一行的文本沿着容器的左右边界对齐**，并且除了最后一行，每行的文本都会被拉伸或压缩，以填充整个行宽。

以下是一个示例，展示了 `text-align: justify;` 的使用：

```html
<style>
  .container {
    text-align: justify;
  }
</style>

<div class="container">
  <p>
    This is a paragraph with justified text alignment. Justified text creates a clean and organized appearance by aligning the text along the left and right edges of the container, with even spacing between words and slightly adjusted letter spacing.
  </p>
</div>
```

在上述示例中，`.container` 类选择器的 `<div>` 元素应用了 `text-align: justify;` 属性。这将使容器中的文本以两端对齐的方式显示。

通过使用 `text-align: justify;`，您可以在文本布局中实现两端对齐的效果，使得文本在容器中呈现出整齐的排列，提供更好的可读性和视觉效果。这种对齐方式常用于段落、新闻文章、杂志排版等场景。
以下是一个示例，展示了 `text-align` 属性的使用：

```html
<style>
  .container {
    text-align: center;
  }
</style>

<div class="container">
  <p>This is a paragraph with centered text alignment.</p>
  <p>Another paragraph with centered text alignment.</p>
</div>
```

在上述示例中，`.container` 类选择器的 `<div>` 元素应用了 `text-align: center;` 属性。这将使该容器中的文本居中对齐。

通过使用 `text-align` 属性，您可以控制文本内容在其容器中的水平对齐方式，以满足不同的布局需求和设计风格。
![[Pasted image 20220905162107.png]]

#### ➢ 注意点： 
**• 如果需要让文本水平居中，text-align属性给文本所在标签（文本的父元素）设置**
