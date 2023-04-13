# vue如何实现在路由切换时出现过渡效果
Vue提供了 `<transition>` 组件，可以用于在组件进入或离开页面时添加过渡效果。要在路由切换时添加过渡效果，可以将 `<transition>` 组件嵌套在 `<router-view>` 组件中。

下面是一个例子：
```html
<template>
  <div>
    <transition name="fade" mode="out-in">
      <router-view></router-view>
    </transition>
  </div>
</template>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
```

在上面的代码中，我们定义了一个名为 `fade` 的过渡动画，并将其应用于 `<transition>` 组件中。`mode` 属性设置为 `out-in`，这意味着先进行离开动画，然后再进行进入动画。

在样式中，我们定义了 `fade-enter` 和 `fade-leave-to` 类，它们控制了元素的透明度。`fade-enter-active` 和 `fade-leave-active` 类则定义了过渡动画的持续时间和动画类型。

在这种设置下，当路由切换时，离开页面的组件会先执行离开动画，然后进入页面的组件会执行进入动画，从而实现了过渡效果。