call 函数的实现步骤:
1. 判断调用对象是否为函数，即使我们是定义在函数的原型上的，但是可能出现使用 call 等方式调用的情况
2. 判断传入上下文对象是否存在，如果不存在，则设置为 window 
3. 处理传入的参数，截取第一个参数后的所有参数
4. 将函数作为上下文对象的一个属性
5. 使用上下文对象来调用这个方法，并保存返回结果
6. 删除刚才新增的属性。
7. 返回结果。

```js
Function.prototype.myCall = function(context) {
	// 如果调用的对象不为函数
	if (typeof this !== 'function') {
		throw new typeError('Error')
	}
	// 返回的结果
	let result = null
	// 将类数组转化为数组去除第一个上下文参数，获取后续传入参数
	let args = Array.from(arguments).slice(1)
	// 看是否存在上下文
	context = context || windows
	// 在context创建多一个fn属性用以改变this的指向
	// console.log(this)
	// getDate(month, day) { return this.year + '-' + month + '-' + day }
	context.fn = this
	result = context.fn(args)
	delete context.fn
	return result
}
```



如果不加第一条的if判断
```js
function greet() {
  console.log(`Hello, ${this.name}!`);
}

const person = [10, 20, 30];

// 使用 call 方法调用 myApply
console.log(greet.myApply.call(person)); // Error
```

运行例子
```js
var year = 2021
function getDate(month, day) {
  return this.year + '-' + month + '-' + day
}

let obj = {year: 2022}
getDate.myCall(obj, 8, 7)
```

注意，如果这里obj里有fn选项，则会被删除
```js
var year = 2021
function getDate(month, day) {
  return this.year + '-' + month + '-' + day
}

let obj = {
    year: 2022,
    fn: function() {
        console.log(111)
    }
}

console.log(getDate.myCall(obj, 8, 7))
obj.fn()
```
![[Pasted image 20230621015814.png]]
![[Pasted image 20230621015744.png]]

如果是getDate则没事
```js
let obj = {
    year: 2022,
    getDate: function() {
        console.log(111)
    }
}
console.log(getDate.myCall(obj, 8, 7))
obj.getDate()
```
![[Pasted image 20230621015911.png]]
因为前面mycall把fn删了

 其他例子，用以认识this
```js
Function.prototype.myMethod = function() {
  console.log(this)
  /*
  ƒ obj() {
	  let a = 0
  }
  */
  console.log(typeof this) // function
}
 function obj()  {
  let a = 0
}
obj.myMethod()
```