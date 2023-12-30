# 背景颜色 background-color
#### ➢ 属性名：
**background-color（bgc）** 
#### ➢ 属性值： 
**• 颜色取值：关键字、rgb表示法、rgba表示法、十六进制……** 
#### ➢ 注意点： 
**• 背景颜色默认值是透明： rgba(0,0,0,0) 、transparent 
• 背景颜色不会影响盒子大小，并且还能看清盒子的大小和位置，一般在布局中会习惯先给盒子设置背景颜色**

![[Pasted image 20220906085827.png]]


在 CSS 中，`background-color` 属性用于设置元素的背景颜色。

`background-color` 属性接受各种颜色值，可以是具体的颜色表示形式，如十六进制、RGB 或颜色关键字，也可以是透明度值。

以下是一些常用的 `background-color` 属性值示例：

- 十六进制颜色值：`#RRGGBB`，例如 `#FF0000` 表示红色。
- RGB 颜色值：`rgb(R, G, B)`，其中 R、G、B 分别是红、绿、蓝通道的整数值（0-255），例如 `rgb(255, 0, 0)` 表示红色。
- RGBA 颜色值：`rgba(R, G, B, A)`，与 RGB 类似，但添加了透明度值 A（0-1），其中 0 表示完全透明，1 表示完全不透明，例如 `rgba(255, 0, 0, 0.5)` 表示半透明的红色。
- 颜色关键字：预定义的颜色名称，如 `red`、`green`、`blue` 等。
1. `transparent`：表示完全透明的颜色，常用于创建透明背景或边框效果。

以下是一个示例，展示了 `background-color` 属性的使用：

```html
<style>
  .box {
    background-color: #FF0000;
  }
</style>

<div class="box">
  <p>This is a box with a red background color.</p>
</div>
```

在上述示例中，`.box` 类选择器的 `<div>` 元素应用了 `background-color: #FF0000;` 属性。这将为元素设置一个红色的背景颜色。

通过使用 `background-color` 属性，您可以设置元素的背景颜色，改变元素的外观和视觉效果。背景颜色可以用于区分元素、突出显示内容等。