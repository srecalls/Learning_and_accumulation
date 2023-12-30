# 背景位置 background-position

#### ➢ 属性名：
**background-position（bgp）** 
#### ➢ 属性值：

![[Pasted image 20220906090306.png]]
![[Pasted image 20220906090328.png]]
#### ➢ 注意点： 
**• 方位名词取值和坐标取值可以混使用，第一个取值表示水平，第二个取值表示垂直**

![[Pasted image 20220906090404.png]]

在 CSS 中，`background-position` 属性用于设置元素背景图片的位置。

`background-position` 属性接受一对值，用于指定背景图片在元素背景区域中的位置。可以使用关键字或长度单位来表示位置。

以下是 `background-position` 属性的语法和常用值：

```css
background-position: X-axis Y-axis;
```

- `X-axis`：用于指定水平方向上的背景位置。可以使用关键字（如 `left`、`center`、`right`）或长度单位（如像素、百分比）。
- `Y-axis`：用于指定垂直方向上的背景位置。同样可以使用关键字或长度单位。

如果只提供一个值，则该值将应用于水平方向，并且垂直方向默认为 `center`。

以下是一些示例，展示了 `background-position` 属性的使用：

```css
div {
  background-image: url("image.jpg");
  background-position: center top;
}
```

在上述示例中，`div` 元素的背景图片被设置为 "image.jpg"，并且背景位置被设置为水平居中（`center`）和垂直顶部（`top`）。

您还可以使用长度单位来指定精确的背景位置，例如像素或百分比：

```css
div {
  background-image: url("image.jpg");
  background-position: 20px 50%;
}
```

上述示例中，背景位置被设置为水平偏移 20 像素和垂直偏移 50% 的位置。

通过调整 `background-position` 属性，您可以控制背景图片在元素背景区域中的位置，以实现所需的布局和视觉效果。