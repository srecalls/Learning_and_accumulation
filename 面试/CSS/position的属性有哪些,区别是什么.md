position有以下属性值:

- absolute
生成绝对定位的元素，相对于static定位以外的一个元素进行定位。元素的位置通过left、top、 right、bottom属性进行规定

- relative
生成相对定位的元素，相对于其原来的位置进行定位。元素的位置通过left、top、 right、 bottom属性进行规定

- fixed
生成绝对定位的元素,指定元素相对于屏幕视口(viewport) 的位来指定元素位置。元素的位置在滚动时不会改变，比如回到顶部的按钮一般都是用此定位方式

- static
默认值，没有定位,元素出现在正常的文档流中，会忽略top, bottom, left, right 或者z-index声明,块级元素从上往下纵向排布，行级元素从左向右排序。

- inherit
规定从父元素继承position属性的值
position: inherit inherit 值如同其他 css 属性的 inherit 值，即**继承父元素的 position 值**。
在 CSS 中，`position` 属性的值不会被子元素继承。`position` 属性用于控制元素的定位方式，包括 `static`、`relative`、`absolute`、`fixed` 和 `sticky` 五种值。当一个元素的 `position` 属性设置为非 `static` 值时，它会被视为一个定位元素，可以使用 `top`、`bottom`、`left` 和 `right` 属性来控制其在父级元素内的位置。

在这种情况下，子元素的 `position` 属性值不会继承父级元素的定位方式。子元素的 `position` 属性值将会默认为 `static`，即不做特殊定位处理，不会影响到父级元素的定位方式。

前三者定位方式如下
![[Pasted image 20230515042350.png]]

![[Pasted image 20230515042401.png]]

![[Pasted image 20230515042410.png]]





