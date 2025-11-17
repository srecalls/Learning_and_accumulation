position有以下属性值:

- absolute
生成绝对定位的元素，相对于static定位以外的一个元素进行定位。元素的位置通过left、top、 right、bottom属性进行规定
[[绝对定位 absolute]]

- relative
生成相对定位的元素，相对于其原来的位置进行定位。元素的位置通过left、top、 right、 bottom属性进行规定
[[相对定位 relative]]
- fixed
生成绝对定位的元素,指定元素相对于屏幕视口(viewport) 的位来指定元素位置。元素的位置在滚动时不会改变，比如回到顶部的按钮一般都是用此定位方式
[[固定定位 fixed]]
- static
默认值，没有定位,元素出现在正常的文档流中，会忽略top, bottom, left, right 或者z-index声明,块级元素从上往下纵向排布，行级元素从左向右排序。

在 CSS 中，如果没有明确指定一个元素的定位方式（position 属性），则该元素的默认定位方式是“静态定位”（static position）。静态定位表示元素按照正常的文档流排列，不受 top、bottom、left、right 等属性的影响。同时，静态定位的元素也不会受到 z-index 属性的影响，无法与其他元素重叠或遮挡。

- inherit
规定从父元素继承position属性的值
position: inherit inherit 值如同其他 css 属性的 inherit 值，即**继承父元素的 position 值**。
在 CSS 中，`position` 属性的值不会被子元素继承。`position` 属性用于控制元素的定位方式，包括 `static`、`relative`、`absolute`、`fixed` 和 `sticky` 五种值。当一个元素的 `position` 属性设置为非 `static` 值时，它会被视为一个定位元素，可以使用 `top`、`bottom`、`left` 和 `right` 属性来控制其在父级元素内的位置。

在这种情况下，子元素的 `position` 属性值不会继承父级元素的定位方式。子元素的 `position` 属性值将会默认为 `static`，即不做特殊定位处理，不会影响到父级元素的定位方式。


- sticky
`position` 是 CSS 属性之一，用于设置元素的定位方式。其取值包括 `static`、`relative`、`absolute`、`fixed` 和 `sticky`。其中 `sticky` 是相对较新的定位方式，它的作用是在元素滚动到特定位置时将元素固定在屏幕上。会占据位置
[[粘性定位 sticky]]
`sticky` 定位方式类似于 `fixed` 定位，但是它不会一直固定在屏幕的某个位置，而是在满足特定条件时生效.比如top：30，只有距离顶部三十以内才才触发

使用 `sticky` 定位方式需要设置 `position: sticky`，并指定 `top`、`bottom`、`left` 或 `right` 等值。例如，下面的代码将元素固定在容器的顶部，当滚动到容器底部时解除固定状态：

```css
.container {
  height: 400px;
  overflow-y: scroll;
}

.element {
  position: sticky;
  top: 0;
}
```

在上述代码中，`.container` 是容器元素，`.element` 是要进行 `sticky` 定位的元素。当 `.element` 元素滚动到 `.container` 的顶部时，它会固定在顶部，直到滚动到 `.container` 的底部时，才会解除固定状态。

需要注意的是，`sticky` 定位方式在一些老的浏览器中可能不被支持。此外，使用 `sticky` 定位时还需要注意元素所处的上下文环境和滚动容器的大小等因素，以确保效果正确。
前三者定位方式如下
![[Pasted image 20230515042350.png]]

![[Pasted image 20230515042401.png]]

![[Pasted image 20230515042410.png]]





