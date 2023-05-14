	moutations类似数据管家,操作state里的数据

在store/index.js定义mutations
语法:
```js
const store = new Vuex.Store({
	mutations: {
		函数名 (state, 可选值) {
			// 同步修改state值代码
		}
	}
})
```

具体代码:
```js
const store = new Vuex.Store({
	state: {
		count: 100 // 库存
	},
	mutations: {
		addCount (state, value) { // 负责增加库存的管家
			state.count += value
		},
		subCount (state, value) { // 负责减少库存的管家
			state.count -= value
		},
		setCount (state, value) { // 负责直接修改库存的管家
			state.count = value
		}
	}
})
```

###   注意

> 1.  mutations是**唯一**能修改state的地方, 确保**调试工具**可以追踪变化
> 2.  mutations函数内, 只能写同步代码, 调试工具可追踪变化过程
>     -   因为调试工具要**立刻**产生一次记录, 所以必须是同步的

### 小结
1.  mutations里函数作用?
	    -   负责修改state里的数据
2.  mutations只能写什么样的代码?
	    -   同步流程的代码


![[Pasted image 20230502094227.png]]