###   定义actions

在store/index.js定义actions

语法:

```js
const store = new Vuex.Store({
	actions: {
		函数名 (store, 可选值) {
			// 异步代码, 把结果commit给mutations给state赋值
		}
	}
})
```

具体代码:

```js
const store  = new Vuex.Store({
    // ...省略state和mutations此处
    actions: {
        asyncAddCount(store, num){
            setTimeout(() => { // 1秒后, 异步提交给add的mutations
                store.commit('addCount', value)
            }, 1000)
        },
        asyncSubCount(store, num) {
            setTimeout(() => { // 1秒后, 异步提交给sub的mutations
                store.commit('subCount', value)
                //就是说这里传入一个对象,然后用什么取什么
            }, 1000)
        }
    }
    // 注意!mutations和actions只能接收一个参数值(一个value),(如果传递多个,请传递一个完整的对象)
})
```

### [](https://gitee.com/lidongxuwork/bilibili-matching-code/blob/master/Web%E5%89%8D%E7%AB%AF/5-%E6%A1%86%E6%9E%B6/V2.x/%E6%A6%82%E5%BF%B5/1-vuex%E4%BD%BF%E7%94%A8/0_%E7%AC%94%E8%AE%B0/vuex%E4%BD%BF%E7%94%A8.md#%E5%B0%8F%E7%BB%93-7)小结

1.  actions和mutations区别?

	    mutations里同步修改state
	    actions里放入异步操作

2.  actions是否能操作state?

	    不建议, 要commit给mutations(为调试工具可追踪)

3.  actions和mutations里函数, 第一个形参分别是什么?

	    mutations的是state
	    actions的是store