## scoped原理
首先，明确什么是scoped
当一个style标签拥有scoped属性时，它的CSS样式就只能作用于当前的组件通过该属性，可以使得组件之间的样式不互相污染。
**那么scoped的原理是?**
- 1、为**组件实例** （组件的ID给他标上去，不是标签id，vnode里给他起个id）生成一个**唯一标识**，给**组件**中的**每个标签对应的dom元素添加**一个标签属性，data-V-xxxx
- 2、给`<style scoped>`中的每个选择器的最后一个选择器添加**一个属性选择器**，原选择器+`[data-V-xxxx]`，如: 原选择器为`.container #id div`，则更改后选择器为`.container #id div[data-V-xxxx]`


引出另外一个问题:
如果使用第三方组件，加了scoped之后就可能控制不到第三方组件中的样式（例如Element-ui）

## 样式穿透
所以这时候需要样式穿透
样式穿透的写法有两种:
```
1. /deep/
2. ::v-deep
```

![[Pasted image 20230717113100.png]]


```css
/deep/ .child {
	background-color: green;
}

::v-deep .child {
	background-color: green;
}
```
## 样式穿透原理
scoped后选择器最后默认会加上当前组件的一个标识，比如`[data-v-xxxx]`用了样式穿透后，同样可以通过这个标签属性来对其进行样式权重的控制。

(不会在选择器后面追加`[data-V-xxxx`])
