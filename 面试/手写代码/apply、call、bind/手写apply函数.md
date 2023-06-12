[[call，apply，bind三者有什么区别]]
[[改变this(apply、call、bind)]]

## apply 函数的实现步骤
1. 判断调用对象是否为函数，即使我们是定义在函数的原型上的，但是可能出现使用 call 等方式调用的情况。
2. 判断传入上下文对象是否存在，如果不存在，则设置为 window 。
3. 将函数作为上下文对象的一个属性
4. 判断参数值是否传入
5. 使用上下文对象来调用这个方法，并保存返回结果
6. 删除刚才新增的属性
7. 返回结果
```js
// apply 函数实现
Function.prototype.myApply = function (context) {
	// 判断调用对象是否为函数
	if (typeof this !== 'function') {
		throw new TypeError('Error')
	}
	let result = null
	// 判断 context 是否存在, 如果未传入则为windows
	context = context || window
	// 将函数设为对象的方法
	context.fn = this
	console.log(this)
	/* 以下面的举例
	getDate(month, day) {
	  return this.year + '-' + month + '-' + day
	}
	*/ 
	// 调用方法
	if (arguments[1]) {
		// 以下面的举例
		/*
			obj = {
				year: 2022
				fn: getDate(month, day) {
					  return this.year + '-' + month + '-' + day
				}
			}
		*/
		// 通过这一步改变this的指向
		result = context.fn(...arguments[1])
	} else {
		result = context.fn()
	}
	// 将属性删除
	delete context.fn
	return result
}
```

运行例子
```js
var year = 2021
function getDate(month, day) {
  return this.year + '-' + month + '-' + day
}

let obj = {year: 2022}
getDate.myApply(obj,[8, 7])
```


第一步的情况
```js
let o = {
}

let obj = {year: 2022}
// 利用call修改了myCall的this
console.log(getDate.myCall.call(o, 8, 7))
```