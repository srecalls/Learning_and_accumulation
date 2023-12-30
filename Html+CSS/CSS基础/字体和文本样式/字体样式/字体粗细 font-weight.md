# 字体粗细 font-weight
#### ➢ 属性名：
**font-weight** 
#### ➢ 取值： 
 **• 关键字：**
 
![[Pasted image 20220905153434.png]]

- normal
- bold
- lighter
- bolder

 **• 纯数字：100~900的整百数：**

![[Pasted image 20220905153448.png]]
#### ➢ 注意点： 
 **• 不是所有字体都提供了九种粗细，因此部分取值页面中无变化** 
 **• 实际开发中以：正常、加粗两种取值使用最多。**

在 CSS 中，`font-weight` 属性用于设置文本的字体粗细。

`font-weight` 属性可以接受以下类型的值：

- 数字值：指定字体的粗细程度。常用的值包括 `normal`（默认值，相当于 `400`）、`bold`（相当于 `700`）、`lighter`（相对较轻的字体，取决于父元素的字体粗细）和 `bolder`（相对较粗的字体，取决于父元素的字体粗细）。
- 关键字：除了上述的关键字外，还可以使用 `100`、`200`、`300`、`500`、`600`、`800` 和 `900` 等数字值来表示不同的字体粗细。

以下是一个示例，展示了 `font-weight` 属性的使用：

```html
<style>
  .container {
    font-weight: bold;
  }
</style>

<div class="container">
  <p>This is a paragraph with bold font weight.</p>
</div>
```

在上述示例中，`.container` 类选择器的 `<div>` 元素应用了 `font-weight: bold;` 属性。这将使容器中的文本使用粗体字体。

通过使用 `font-weight` 属性，您可以控制文本的字体粗细，以实现不同的视觉效果。较粗的字体可以用于强调重要内容，而较轻的字体可以用于辅助文本或提供更加柔和的外观。选择合适的字体粗细可以根据设计需求和风格来调整文本的外观。