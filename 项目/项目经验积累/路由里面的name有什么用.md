```js
const routes = [ { path: "/", name: "home", component: Login }
```
name有什么用
在Vue Router中，`name`属性用于给路由命名，从而使代码更加易读和易于维护。可以通过路由名称来引用该路由，而不是硬编码路径字符串。这对于在项目中重用路由或在程序中进行路由导航时非常有用。例如，可以通过路由名称来实现以下操作：

1.  在组件内部使用`$router.push({ name: 'routeName' })`实现路由的编程式导航。
2.  在`<router-link>`组件中使用`:to="{ name: 'routeName' }"`来渲染链接。
3.  在导航守卫（`beforeEach`、`beforeResolve`、`afterEach`等）中使用路由名称来判断导航的来源和目标。

在代码中使用命名路由而不是硬编码路径字符串，可以使代码更加清晰易读，同时还可以方便地更改路径，而不必在代码中进行全局查找和替换。