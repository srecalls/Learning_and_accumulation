-   新建store/modules/user.js
-   新建store/modules/cart.js
语法: 对象里包含5个核心概念, 只有state变成函数形式

user.js - 用户模块对象

```js
// 用户模块对象
const userModule = {
    state(){
        return {
            name: "",
            age: 0,
            sex: ''
        }
    },
    mutations: {},
    actions: {},
    getters: {}
}
export default userModule
```


cart.js - 购物车模块对象
```js
// 购物车模块对象
import axios from 'axios'
const cartModule = {
    state() {
        return {
            goodsList: []
        }
    },
    mutations: {
        setGoodsList(state, newList) {
            state.goodsList = newList
        }
    },
    actions: {
        async asyncGetGoodsList(store) {
            const url = `https://www.escook.cn/api/cart`
            // 发送异步请求
            const res = await axios({ url: url });
            store.commit('setGoodsList', res.data.list) // 提交mutation修改state中的数据
        }
    },
    getters: {
        allCount(state) {
            return state.goodsList.reduce((sum, obj) => {
                if (obj.goods_state === true) { // 选中商品才累加数量
                    sum += obj.goods_count;
                }
                return sum;
            }, 0)
        },
        allPrice(state) {
            return state.goodsList.reduce((sum, obj) => {
                if (obj.goods_state) {
                    sum += obj.goods_count * obj.goods_price
                }
                return sum;
            }, 0)
        }
    }
}
export default cartModule
```