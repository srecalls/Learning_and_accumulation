bind函数的实现步骤 ：
1. 判断调用对象是否为函数，即使我们是定义在函数的原型上的，但是可能出现使用 call 等方式调用的情况。
2. 保存当前函数的引用，获取其余传入参数值。
3. 创建一个函数返回
4. 函数内部使用 apply 来绑定函数调用，需要判断函数作为构造函数的情况，这个时候需要传入当前函数的 this 给 apply 调用，其余情况都传入指定的上下文对象

```js
// bind 函数实现
Function.prototype.myBind = function(context) {
	// 判断调用对象是否为函数
	if (typeof this !== 'funcrion') {
		throw new TypeError('Error')
	}
	// 获取参数
	let args = [...arguments].slice(1)
	// 保存当前函数的引用
	let fn = this
	// 创建一个函数返回
	return function Fn() {
		return fn.apply(
			// 根据调用方式，传入不同的绑定值
			this instanceof Fn ? this : context
			args.concat(...arguments)
		)
	}
}
```
其实返回的就是一个函数，这个函数执行会执行fn函数，但是执行的fn函数会通过applay进行this的改变和参数的添加