# 外边框 margin

#### ➢ 作用：
**设置边框以外，盒子与盒子之间的距离** 
#### ➢ 属性名：
**margin** 
#### ➢ 常见取值：
取值|示例|含义
:-:|:-:|:-:
一个值|margin:10px;|<strong>上右下左</strong>都设置为10px
两个值|margin:10px 20px;|<strong>上下</strong>设置为10px，<strong>左右</strong>设置为20px
三个值|margin:10px 20px 30px;|<strong>上</strong>设置为10px，<strong>左右</strong>设置为20px，<strong>下</strong>设置为30px
四个值|margin:10px 20px 30px 40px;|<strong>上</strong>设置为10px，<strong>右</strong>边设置为20px，<strong>下</strong>设置为30px，<strong>左</strong>设置为40px
#### ➢ 记忆规则：
**从上开始赋值，然后顺时针赋值，如果设置赋值的，看对面的！！**


## 单方向设置
**➢ 场景：**
**只给盒子的某个方向单独设置外边距** 
**➢ 属性名：**
**margin - 方位名词** 
**➢ 属性值：**
**数字 + px**

![[Pasted image 20220906145359.png]]

**让盒子居中：margin:auto auto;**


在 CSS 中，`margin` 属性用于设置元素的外边距，即元素与其周围元素之间的空白区域。

`margin` 属性可以接受多个值，用于设置不同方向（上、右、下、左）的外边距。以下是 `margin` 属性的语法和常用值：

```css
margin: top right bottom left;
```

- `top`：设置元素的上外边距。
- `right`：设置元素的右外边距。
- `bottom`：设置元素的下外边距。
- `left`：设置元素的左外边距。

您还可以使用以下简写形式：

- `margin: vertical horizontal;`：通过指定垂直和水平外边距的值，分别设置上/下和左/右的外边距。
- `margin: value;`：使用单个值为所有四个方向设置相同的外边距。

外边距可以使用具体的长度单位（如像素、百分比、视窗单位等），也可以使用关键字（如 `auto`）来指定。例如：

```css
margin: 10px; /* 将为所有方向设置相同的 10 像素外边距 */
margin: 10px 20px; /* 上/下外边距为 10 像素，左/右外边距为 20 像素 */
margin: 10px 20px 30px 40px; /* 顺时针设置上、右、下、左的外边距值 */
margin: auto; /* 自动调整外边距（通常用于水平居中元素） */
```

以下是一个示例，展示了 `margin` 属性的使用：

```html
<style>
  .box {
    margin: 20px;
  }
</style>

<div class="box">
  <p>This is a box with margin.</p>
</div>
```

在上述示例中，`.box` 类选择器的 `<div>` 元素应用了 `margin: 20px;` 属性。这将在元素周围创建一个 20 像素的外边距。

通过使用 `margin` 属性，您可以控制元素与其周围元素之间的间距，调整页面布局和元素之间的空白区域。外边距可以用于创建元素之间的间隔、定位元素、调整元素的对齐方式等。