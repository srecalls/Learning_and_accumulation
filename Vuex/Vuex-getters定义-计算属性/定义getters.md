###  定义getters

在store/index.js定义getters

语法:

```js
const store = new Vuex.Store({
	getters: {
		计算属性名 (state) {
			return 值给计算属性
		}
	}
})
```

具体代码

```js
const store = new Vuex.Store({
    // ...省略其他
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
})
```