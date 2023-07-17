BFC 是块级格式化上下文（Block Formatting Context）的缩写，是 Web 页面中常见的一种 CSS 布局模式，用于控制块级元素的布局和对齐方式。

BFC 是指一个独立的渲染区域，其中的元素布局是相互独立的，不受外部元素的影响。在 BFC 中，每个元素的左边和右边都会贴着它的包含块（container box）的左边和右边，即使它们之间有空隙。BFC 还具有防止浮动元素重叠的特性，可以避免父元素高度塌陷的问题。因此，BFC 是 Web 页面中常用的布局技术之一。

以下是一些可能会生成 BFC 的场景：

1. 根元素：HTML 页面中的根元素（即 `<html>` 元素）会生成一个 BFC。
2. 浮动元素：浮动元素会生成一个 BFC，可以避免浮动元素重叠的问题。
3. 绝对定位元素：绝对定位元素会生成一个 BFC，可以避免与其他元素的重叠问题。
4. display 属性为 inline-block、table-cell、table-caption、flex、inline-flex、grid、inline-grid 的元素会生成一个 BFC。
5. overflow 属性不为 visible 的元素会生成一个 BFC，可以避免父元素高度塌陷的问题。

在实际开发中，可以根据需要使用 BFC 来解决一些布局问题，例如实现清除浮动、避免元素重叠、避免父元素高度塌陷等。