# 内边距 padding

## 取值
#### ➢ 作用：
**设置 边框 与 内容区域 之间的距离** 
#### ➢ 属性名：
**padding** 
#### ➢ 常见取值：
取值|示例|含义
:-:|:-:|:-:
一个值|padding:10px;|<strong>上右下左</strong>都设置为10px
两个值|padding:10px 20px;|<strong>上下</strong>设置为10px，<strong>左右</strong>设置为20px
三个值|padding:10px 20px 30px;|<strong>上</strong>设置为10px，<strong>左右</strong>设置为20px，<strong>下</strong>设置为30px
四个值|padding:10px 20px 30px 40px;|<strong>上</strong>设置为10px，<strong>右</strong>边设置为20px，<strong>下</strong>设置为30px，<strong>左</strong>设置为40px

#### ➢ 记忆规则：
**从上开始赋值，然后顺时针赋值，如果设置赋值的，看对面的！！**


## 单方向设置
#### ➢ 场景：
**只给盒子的某个方向单独设置内边距** 
#### ➢ 属性名：
**padding - 方位名词** 
#### ➢ 属性值：
**数字 + px**


在 CSS 中，`padding` 属性用于设置元素的内边距，即元素内容与元素边界之间的空白区域。

`padding` 属性可以接受多个值，用于设置不同方向（上、右、下、左）的内边距。以下是 `padding` 属性的语法和常用值：

```css
padding: top right bottom left;
```

- `top`：设置元素的上内边距。
- `right`：设置元素的右内边距。
- `bottom`：设置元素的下内边距。
- `left`：设置元素的左内边距。

您还可以使用以下简写形式：

- `padding: vertical horizontal;`：通过指定垂直和水平内边距的值，分别设置上/下和左/右的内边距。
- `padding: value;`：使用单个值为所有四个方向设置相同的内边距。

内边距可以使用具体的长度单位（如像素、百分比、视窗单位等）。例如：

```css
padding: 10px; /* 将为所有方向设置相同的 10 像素内边距 */
padding: 10px 20px; /* 上/下内边距为 10 像素，左/右内边距为 20 像素 */
padding: 10px 20px 30px 40px; /* 顺时针设置上、右、下、左的内边距值 */
```

以下是一个示例，展示了 `padding` 属性的使用：

```html
<style>
  .box {
    padding: 20px;
  }
</style>

<div class="box">
  <p>This is a box with padding.</p>
</div>
```

在上述示例中，`.box` 类选择器的 `<div>` 元素应用了 `padding: 20px;` 属性。这将在元素内容和元素边界之间创建一个 20 像素的内边距。

通过使用 `padding` 属性，您可以控制元素内容与元素边界之间的间距，调整元素的内部空白区域。内边距可以用于增加元素的可读性、调整元素的尺寸、创建元素的背景区域等。