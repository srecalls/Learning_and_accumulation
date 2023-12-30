# 行高 line-height
#### ➢ 作用：
**控制一行的上下行间距** 
#### ➢ 属性名：
**line-height** 
#### ➢ 取值： 
**• 数字+px** 
**• 倍数（当前标签font-size的倍数）** 


在 CSS 中，`line-height` 属性用于设置行高，即行框的高度。

`line-height` 属性可以接受以下类型的值：

- `<number>`：指定一个数字值，表示行高为当前字体大小的倍数。例如，`1.5` 表示行高为字体大小的 1.5 倍。
- `<length>`：指定一个固定的长度值，以像素（px）、百分比（%）或其他长度单位表示。例如，`20px` 表示行高为 20 像素。
- `normal`：默认值。表示使用浏览器默认的行高。

以下是一个示例，展示了 `line-height` 属性的使用：

```html
<style>
  .container {
    line-height: 1.5;
  }
</style>

<div class="container">
  <p>
    This is a paragraph with increased line height. The line height is set to 1.5 times the font size, providing more spacing between lines.
  </p>
</div>
```

在上述示例中，`.container` 类选择器的 `<div>` 元素应用了 `line-height: 1.5;` 属性。这将使容器中的文本行高为字体大小的 1.5 倍。

通过使用 `line-height` 属性，您可以控制文本行之间的垂直间距，从而影响文本的可读性和排版效果。增加行高可以提高文本的可读性和舒适度，减少行高可以使文本更加紧凑。选择合适的行高可以根据具体的设计需求和排版风格来调整文本的外观。

#### ➢ 应用： 
**1. 让单行文本垂直居中可以设置 line-height : 文字父元素高度** 
**2. 网页精准布局时，会设置 line-height : 1 可以取消上下间距** 
#### ➢ 行高与font连写的注意点： 
**• 如果同时设置了行高和font连写，注意覆盖问题** 
**• [[字体font相关属性的连写|font]] :  style  weight  size/line-height  family ;**
