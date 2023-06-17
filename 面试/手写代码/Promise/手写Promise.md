[[Promise基本概念]]
[[Promise的内部原理是什么？优缺点是什么]]
[[⭐发起http的api有哪些]]
[[Promise链式调用的实现]]
# Main
```js
const PENDING = 'pending'
const RESOLVED = 'resolved'
const REJECTED = 'rejected'

function MyPromise(fn) {
	// 保存初始化状态
	let self = this
	// 初始化状态
	this.state = PENDING
	// 用于保存 resolve 或者 reject 传入的值
	this.value = null
	// 用于保存 resolve 的回调函数
	this.resolvedCallbacks = []
	// 用于保存 reject 的回调函数
	this.rejectedCallbacks = []
	// 状态转变为resolved
	function resolve(value) {
		// 判断传入的元素是否为 Promise 值，如果是，则状态改变必须等待前一个状态
		if (value instanceof MyPromise) {
			return value.then(resolve, reject)
		}
		// 保证代码的执行顺序为本轮事件循环的末尾 
		setTimeout(() => {
			if (self.state === PENDING) {
				// 修改状态
				self.state = RESOLVED
				// 设置传入的值
				self.value = value
				// 执行回调函数
				self.resolvedCallbacks.forEach(callback => {
					callback(value)
				})
			}
		}, 0)
		// 状态转变为 rejected 方法
		function reject(value) {
			// 保证代码的执行顺序为本轮事件循环的末尾
			setTimeout(() => {
				// 只有状态为pendding 时才能转变
				if (self.state === PENDING) {
					// 修改状态
					self.state = REJECTED
					// 设置传入的值
					self.value = value
					// 执行回调函数
					self.rejectedCallbacks.forEach(callback => {
						callback(value)
					})
				}
			}, 0)
		}
	}
	// 将两个方法传入函数执行
	try {
		fn (resolve, reject)
	} catch {
		// 遇到错误时, 捕获错误, 执行 reject 函数
		reject(e)
	}
}

MyPromise.prototype.then
```

⭐记住： resolve和reject只改变状态，.then的时候才执行对应的函数


