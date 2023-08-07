一面：

1. 自我介绍和项目介绍
2. 精灵图的原理？
   [[精灵图的原理]]
3. 精灵图有哪些优缺点？
   [[精灵图的优缺点]]
4. HTTP/2.0有哪些新特性？
[[7.HTTP 1.0和 HTTP 1.1 之间有哪些区别？]]
[[8.HTTP 1.1 和 HTTP 2.0的区别]]
6. 头部压缩用的什么算法？
```js
HPACK
```
7. HPACK算法的原理？
[[HPACK的原理]]
8. 多路复用解决了什么问题？
[[多路复用解决了什么问题？]]
9. 说一下强缓存和协商缓存
[[1.对浏览器缓存的理解 （强缓存、协商缓存）]]
10. 说说对打包工具的理解
    [[webpack的构建流程]]
11. loader和plugin的区别？
    [[Loader和Plugin的不同]]
12. 组件懒加载的原理？
    [[路由懒加载原理]]
13. ESM和CommonJS的区别？
    [[19.ES6 Module（ESM）与CommonJS模块有什么异同]]
14. Vue组件通信的方式有哪些？
14. 兄弟组件之间如何通信？
[[组件通信]]
15. Vue3和Vue2的区别？
    [[Vue2和Vue3有哪些区别]]
16. 哪些情况下Vue2的无法检测数据变化？如何解决？
17. 生命周期钩子有哪些？
18. 哪些钩子中可以获取到DOM节点？
[[对Vue生命周期的理解]]
19. nextTick有哪些使用场景？
20. 计算属性和侦听器的区别？
[[computed和watch的区别]]
[[5.Computed 和 Watch的区别]]
21. JS的数据类型有哪些？
[[JavaScript的数据类型]]
22. 判断数据类型的方法有哪些？
[[JS对数据类的检测方式有哪些]]
23. 浅拷贝和深拷贝的区别？
[[深浅拷贝的区别]]
24. 实现深拷贝
```js
let deepClone = function(object) {
	if (!object || typeof object !== 'object') return
	let newObject = Array.isArray(object) ? [] : {}
	for (let key in object) {
		if (object.hasOwnProperty(key)) {
			 newObject[key] = typeof object[key] === object ? deepClone(object[key]) : object[key]
		}
	}
	return newObject
}
```

```js
 let _ = require('lodash')
 或者
 import _ from 'lodash'
 let a = {
	 'name': sRecalls,
	 'age': 21
	 'detail': {
		 'region': 'guangzhou',
		 'hobby': 'computer'
	 }
 }
 let b = _.cloneDeep(a)
```

```js
 let a = {
	 'name': sRecalls,
	 'age': 21
	 'detail': {
		 'region': 'guangzhou',
		 'hobby': 'computer'
	 }
 }
 let b = JSON.parse(JSON.Stringify(a))
```

25. 说说对this的理解
[[1.对this对象的理解]]
[[this的四种绑定方式]]
26. 什么是原型链？
[[说一下原型链]]
27. 原型链的终点是什么？
[[原型链的终点]]
28. 什么是外边距塌陷？如何解决？
[[什么是外边距塌陷？如何解决？]]
    
29. BFC还有哪些功能？
30. 算法题：[有效的括号](https://hd.nowcoder.com/link.html?target=https://leetcode-cn.com/problems/valid-parentheses/)
```js
var isValid = function(s) {
	let stack = []
	let map = new Map([
		['}', '{'],
		[']', '['],
		[')', '(']
	])
	for (let item of s) {
		if (map.has(item)) {
			if (stack.length === 0 || stack[stack.length - 1] !== map.get(item)) {
				return false
			} else {
				stack.pop()
			}
		} else {
			stack.push(item)
		}
	}
	return !stack.length
}
```
[[20. 有效的括号]]

31. 算法题：[两数之和](https://hd.nowcoder.com/link.html?target=https://leetcode-cn.com/problems/two-sum/)
```js
var twoSum = function(nums, target) {
	let hash = {}
	for (let index in nums) {
		let curNum = nums[index]
		let targetNum = target - curNum
		let targetNumIndex = hash[targetNum]
		if (targetNumIndex !== undefined) {
			return [index, targetNumIndex]
		} else {
			hash[curNum] = i
		}
	}
}
```

32. 反问

二面：

1. 自我介绍和项目介绍
2. 为什么想做前端？
3. 说一下职业规划
4. 说一下Vue生命周期，每个步骤发生了什么，越详细越好
5. Vue组件通信的方式有哪些？
6. 在实际项目中，组件通信有哪些注意点？
[[vue组件通信--注意事项及经验总结]]
7. 计算属性和侦听器的区别？
[[5.Computed 和 Watch的区别]]
1. v-if和v-for的优先级？为什么不建议在同一元素上使用？
2. 说一下事件循环
3. Vue源码中有哪些用到了事件循环的地方？
4. 智力题：有一个7升的杯子和一个4升的杯子，如何盛出5升水？
    [[365. 水壶问题]]

1. 算法题：[二分查找](https://hd.nowcoder.com/link.html?target=https://leetcode-cn.com/problems/binary-search/)
2. 反问