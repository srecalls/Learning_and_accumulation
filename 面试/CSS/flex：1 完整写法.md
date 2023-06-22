### flex: 1 完整写法

`flex`属性是`flex-grow`, `flex-shrink` 和 `flex-basis`, 默认值为`0 1 auto`。后两个属性可选。

`flex-grow`属性定义项目的放大比例，默认为0，即如果存在剩余空间，也不放大。

`flex-shrink`属性定义了项目的缩小比例，默认为1，即如果空间不足，该项目将缩小。

`flex-basis`属性定义了在分配多余空间之前，项目占据的主轴空间（main size）。浏览器根据这个属性，计算主轴是否有多余空间。它的默认值为auto，即项目的本来大小。

记住
flex：1 默认是 flex： 1 1 0%
而不是flex: 1 1 auto
如果是auto的话，默认就是项目本身大小

![[Pasted image 20230621144702.png]]

[flex：1到底是什么](https://zhuanlan.zhihu.com/p/136223806)



