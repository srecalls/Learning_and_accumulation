# 边框 border 

## 单个属性
#### ➢ 作用：
**给设置边框粗细、边框样式、边框颜色效果** 
#### ➢ 单个属性：
![[Pasted image 20220906142801.png]]


## 连写形式
#### ➢ 属性名：
**border** 
#### ➢ 属性值：
**单个取值的连写，取值之间以空格隔开** 
**• 如：border : 10px solid red;** 
#### ➢ 快捷键：bd + tab

## 单方向设置
#### ➢ 场景：
**只给盒子的某个方向单独设置边框** 
#### ➢ 属性名：
**border - 方位名词** 
#### ➢ 属性值：连写的取值


在 CSS 中，`border` 属性用于设置元素的边框样式、宽度和颜色。

`border` 属性可以接受多个值，用于设置边框的样式、宽度和颜色。以下是 `border` 属性的语法和常用值：

```css
border: [border-width] [border-style] [border-color];
```

- `border-width`：设置边框的宽度，可以是具体的长度单位（如像素、百分比等），也可以是预定义的关键字（如 `thin`、`medium`、`thick`）。
- `border-style`：设置边框的样式，常用的值有 `none`（无边框）、`solid`（实线边框）、`dotted`（点状边框）、`dashed`（虚线边框）等。
- `border-color`：设置边框的颜色，可以是具体的颜色值（如十六进制、RGB、颜色关键字等）。

您还可以使用以下简写形式：

- `border: [border-width] [border-style] [border-color];`：通过指定宽度、样式和颜色的值，依次设置边框的宽度、样式和颜色。各个值之间用空格分隔。
- `border: [border-width] [border-style];`：省略颜色值，只设置宽度和样式。

以下是一个示例，展示了 `border` 属性的使用：

```html
<style>
  .box {
    border: 2px solid red;
  }
</style>

<div class="box">
  <p>This is a box with a red solid border.</p>
</div>
```

在上述示例中，`.box` 类选择器的 `<div>` 元素应用了 `border: 2px solid red;` 属性。这将为元素创建一个宽度为 2 像素、样式为实线、颜色为红色的边框。

通过使用 `border` 属性，您可以控制元素的边框样式、宽度和颜色，为元素添加视觉上的边界效果。边框可以用于美化元素、区分元素之间的分隔线、创建装饰效果等。