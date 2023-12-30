# 字体样式（是否倾斜） font-style
#### ➢ 属性名：
**font-style** 
#### ➢ 取值： 
**• 正常（默认值）：normal** 
**• 倾斜：italic**

![[Pasted image 20220905153919.png]]

在 CSS 中，`font-style` 属性用于设置文本的字体样式，例如斜体或正常（非斜体）。

`font-style` 属性可以接受以下类型的值：

- `normal`：默认值，表示使用正常（非斜体）字体样式。
- `italic`：表示使用斜体字体样式。
- `oblique`：表示使用倾斜的字体样式，类似于斜体，但是它是通过字体倾斜变换而不是专门设计的斜体字体来实现的。

以下是一个示例，展示了 `font-style` 属性的使用：

```html
<style>
  .container {
    font-style: italic;
  }
</style>

<div class="container">
  <p>This is a paragraph with italic font style.</p>
</div>
```

在上述示例中，`.container` 类选择器的 `<div>` 元素应用了 `font-style: italic;` 属性。这将使容器中的文本使用斜体字体样式。

通过使用 `font-style` 属性，您可以控制文本的字体样式，以实现不同的视觉效果。斜体字体样式可以用于强调特定文本，为其添加一种倾斜的外观。正常字体样式可用于普通文本或其他需要不带倾斜的字体的情况。选择合适的字体样式可以根据设计需求和风格来调整文本的外观。