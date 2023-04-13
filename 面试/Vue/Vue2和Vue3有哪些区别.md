Vue2 和 Vue3 都采用了响应式原理来实现双向数据绑定。

在 Vue2 中，双向数据绑定是通过 `Object.defineProperty` 方法来实现的。当一个组件实例创建时，Vue2 会遍历其所有的属性，并使用 `Object.defineProperty` 方法将其转换为 getter 和 setter，这样当数据发生变化时，Vue2 就可以自动更新视图。具体来说，当一个组件实例中的数据被修改时，Vue2 会触发 setter 方法，然后通知相关的组件进行重新渲染。

而在 Vue3 中，双向数据绑定是通过 `Proxy` 对象来实现的。当一个组件实例创建时，Vue3 会将其所有的属性包装成 `Proxy` 对象，并在 `Proxy` 对象上设置 getter 和 setter，这样当数据发生变化时，Vue3 就可以自动更新视图。具体来说，当一个组件实例中的数据被修改时，Vue3 会触发 setter 方法，然后通知相关组件进行重新渲染。

相比于 Vue2，Vue3 中的双向数据绑定使用 `Proxy` 对象实现，具有更高的性能和更好的兼容性，同时还可以监听数组和对象的变化，提高了开发效率和代码可读性。


Vue2 `Object.defineProperty` 进行数据劫持，然后配合发布订阅者模式实现
Vue3利用Proxy对数据进行代理，监听所有的对象
![[Pasted image 20230410105254.png]]

1.双向数据绑定的原理不同
2.是否支持碎片 （fragment)
3.API不同
4.定义数据变量方法不同(vue2在methods里，vue3在setup)
5.生命周期的不同
6.传值不同 setup的第二个参数
7.指令和插槽不同