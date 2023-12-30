# 轮廓线 outline

#### 介绍：
**给表单添加outline:O;或者 outline: none;样式之后，就可以去掉默认的蓝色边框。**


#### 代码：
input { outline: none; }


`outline` 是 CSS 的简写属性，用于同时设置元素的轮廓样式、宽度和颜色。

`outline` 属性可以接受以下值：

- `<outline-color>`：指定轮廓的颜色，可以是具体的颜色值或 `invert` 关键字。
- `<outline-style>`：指定轮廓的样式，可以是 `none`、`solid`、`dashed`、`dotted`、`double`、`groove`、`ridge`、`inset` 或 `outset`。
- `<outline-width>`：指定轮廓的宽度，可以是具体的长度值（如像素）或 `thin`、`medium`、`thick`。

示例：
```css
div {
  outline: 2px dashed red;
}
```
上述示例将 `<div>` 元素的轮廓设置为红色的虚线轮廓，宽度为 2 像素。

注意事项：
- `outline` 属性的顺序不重要，可以按任意顺序指定颜色、样式和宽度。
- 如果未指定其中的任何一个值，那么未指定的部分将使用浏览器的默认值。
- 使用 `outline` 属性设置的轮廓不会占据空间，不会影响元素的布局。
- 轮廓通常在用户聚焦元素时显示，例如在点击一个链接或使用 Tab 键导航时。


**- outline-style**
`outline-style` 是 CSS 属性，用于指定一个元素的轮廓样式。轮廓（outline）是围绕元素边界的一种可见样式，类似于边框，但与边框不同，轮廓不占据空间，不影响布局。

`outline-style` 属性可以接受以下值：

- `none`：无轮廓样式，即不显示轮廓。
- `solid`：实线轮廓样式，使用实线显示轮廓。
- `dashed`：虚线轮廓样式，使用虚线显示轮廓。
- `dotted`：点线轮廓样式，使用点线显示轮廓。
- `double`：双线轮廓样式，使用两条线显示轮廓。
- `groove`：凹槽轮廓样式，显示为凹槽效果。
- `ridge`：脊状轮廓样式，显示为脊状效果。
- `inset`：内嵌轮廓样式，显示为内嵌效果。
- `outset`：外嵌轮廓样式，显示为外嵌效果。

示例：
```css
div {
  outline-style: dashed;
}
```
上述示例将 `<div>` 元素的轮廓样式设置为虚线。

注意事项：
- 轮廓样式默认为 `none`，如果要显示轮廓，需要设置合适的值。
- `outline-style` 属性通常与 `outline-color` 和 `outline-width` 属性一起使用，以完整地定义轮廓效果。
- 轮廓样式不会影响元素的布局，因此不会改变元素的尺寸或位置。
- 轮廓通常在用户聚焦元素时显示，例如在点击一个链接或使用 Tab 键导航时。

**- outline-style**
`outline-width` 是 CSS 属性，用于指定元素轮廓的宽度。

`outline-width` 属性可以接受以下值：

- `thin`：指定轮廓宽度为细线。
- `medium`：指定轮廓宽度为中等线。
- `thick`：指定轮廓宽度为粗线。
- `<length>`：使用具体长度值来指定轮廓的宽度，例如 `2px`。

示例：
```css
div {
  outline-width: 3px;
}
```
上述示例将 `<div>` 元素的轮廓宽度设置为 3 像素。

注意事项：
- 轮廓的默认宽度取决于用户代理（浏览器）和操作系统的设置，通常为中等宽度。
- `outline-width` 属性通常与 `outline-style` 和 `outline-color` 属性一起使用，以完整地定义轮廓效果。
- 轮廓宽度不会影响元素的尺寸或位置，它只是在元素周围绘制可见的轮廓线。
- 轮廓通常在用户聚焦元素时显示，例如在点击一个链接或使用 Tab 键导航时。

**outline-color**
`outline-color` 是 CSS 属性，用于指定元素轮廓的颜色。

`outline-color` 属性可以接受以下值：

- `<color>`：使用具体颜色值来指定轮廓的颜色，例如 `red`、`#00ff00`、`rgba(255, 0, 0, 0.5)`。
**- `invert`：将轮廓颜色设为与背景颜色相反的颜色。**

示例：
```css
div {
  outline-color: blue;
}
```
上述示例将 `<div>` 元素的轮廓颜色设置为蓝色。

注意事项：
- 轮廓的默认颜色取决于用户代理（浏览器）和操作系统的设置，通常为与文本颜色相同或与元素边框颜色相同。
- `outline-color` 属性通常与 `outline-style` 和 `outline-width` 属性一起使用，以完整地定义轮廓效果。
- 轮廓颜色不会影响元素的尺寸或位置，它只是在元素周围绘制可见的轮廓线。
- 轮廓通常在用户聚焦元素时显示，例如在点击一个链接或使用 Tab 键导航时。
- 当使用 `outline` 缩写属性时，`outline-color` 可以作为其值之一，用于同时设置轮廓的样式、宽度和颜色。例如：`outline: 2px dashed red;`
