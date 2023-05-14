语法:

```js
modules: {
    模块名: 模块对象
}
```

-   把2个模块对象, 引回到store里注册

```js
import Vue from 'vue'
import Vuex from 'vuex'
import cartModule from './modules/cart'
import userModule from './modules/user'
Vue.use(Vuex)
const store = new Vuex.Store({
    modules: {
        user: userModule,
        cart: cartModule
    }
})
export default store
```
