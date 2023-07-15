![[Pasted image 20230713112348.png]]


### 1. window.onerror

> 可以监听当前页面所有的 JS 报错，`jQuery`时代经常用。 **注意，全局只绑定一次即可。不要放在多次渲染的组件中，这样容易绑定多次。** 一般在`App.vue`的`mounted`生命周期中使用。

```js
window.onerror = function(msg, source, line, column, error) {
    console.log('window.onerror---------', msg, source, line, column, error)
}
// 注意，如果用 window.addEventListener('error', event => {}) 参数不一样！

```

### 2. errorCaptured 生命周期

> 会监听所有**下级组件**的错误。可以返回 `false` 阻止向上传播，因为可能会有多个上级节点都监听错误。 如果设置了`false`，那么在 window.onerror 中就不会再报错。 一般在`App.vue`中使用。

```js
errorCaptured(error, instance, info) {
    console.log('errorCaptured--------', error, instance, info)
}
```

### 3. errorHandler

> 全局的错误监听，所有组件的报错都会汇总到这里来。 如果 `errorCaptured` 返回 `false` 则**不会**到这里。`errorHandler` 会阻止错误走向 `window.onerror`。 一般在`main.js`中使用。

```js
const app = createApp(App)
app.config.errorHandler = (error, instance, info) => {
    console.log('errorHandler--------', error, instance, info)
}

```

#### 4. 异步错误

> 组件内的异步错误 `errorHandler` 监听不到，还是需要 `window.onerror`。 Promise 监听报错要使用 `window.onunhandledrejection`

```js
mounted() {
    setTimeout(() => {
        throw new Error('setTimeout 报错')
    }, 1000)
},

```

## 总结

- `errorCaptured` 监听下级组件的错误，可返回 `false` 阻止向上传播。
- `errorHandler` 监听 Vue 全局错误。
- `window.onerror` 监听其他的 JS 错误，如异步。 **建议：结合使用**
- 一些重要的、复杂的、有运行风险的组件，可使用 `errorCaptured` 重点监听。
- 然后用 `errorHandler` `window.onerror` 候补全局监听，避免意外情况。

  https://juejin.cn/post/7114292356672651272

作者：不准吃零食  
链接：https://juejin.cn/post/7223278436893933629  
来源：稀土掘金  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。