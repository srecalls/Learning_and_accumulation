![[Pasted image 20230326000537.png]]
![[Pasted image 20230326000737.png]]

使用vuex
![[Pasted image 20230326041200.png]]


## vuex中store对象的准备
store.js
```js
import Vue from 'vue'
// 使用vuex
// 1. 下载vuex模块
npm install vuex --save
// 2. 引入vuex暴露函数对象
import Vuex from 'vuex'
// 3. 注册 - Vue实例原型添加$store属性
Vue.use(Vuex)
// 4. 定义规则和生产store对象
const store = new Vuex.Store({})
// 5. 导出到main.js中注册到new Vue里
export default store
```

main.js
```js
import Vue from 'vue'
import App from './App.vue'
import store(叫什么都可以) from '@/store.js' //导入store对象

new Vue({
	// new Vue也提前留好一个属性叫store,可以放入你创建的store对象
	// 让Vue项目有用vuex功能
	
	// 6. 注入到Vue实例中(确保组件this.$store使用) //this.$store = store
	// Vue实例原型上$store属性赋值
	store,
	render: h => h(App),
}).$mount('#app')
```

小结:
1. vuex的核心是什么?
-  store对象(包含5个核心属性)

2.. 如何创建store对象?
- 工程下载vuex模块
- store/index.js
	引入注册
	生成store对象导出
	main.js-导入注入
	