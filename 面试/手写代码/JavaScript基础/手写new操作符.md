## 过程
[[手写Object.create]]
在调用` new `的过程中会发生以上四件事情:
(1) 首先创建了一个新的空对象
(2) 设置原型，将对象的原型设置为函数的 prototype 对象
(3) 让函数的 this 指向这个对象，执行构造函数的代码 (为这个新对象添加属性)
(4) 判断函数的返回值类型，如果是值类型，返回创建的对象。如果是引用类型，就返回这个引用类型的对象。

[[对原型、原型链的理解]]
[[1.对原型、原型链的理解]]
[[原型链]]
[[https]]
```js
function objectFactory() {
	let newObject = null
	let constructor = Array.prototype.shift.call(arguments)
	// console.log(constructor) // fn(name) { this.name = name }
	let result = null
	// 判断参数是否是一个函数
	 if (typeof constructor !== 'function') {
		 console.error("type error")
		 return
	 }
	 //  新建一个空对象，对象的原型为构造函数的prototype对象
	 newObject = Object.create(constructor.prototype)
	 // console.log(constructor.prototype)
	 // Object   { constructor: fn(name)}
	 // console.log(newObject)
	 // fn { }
	 // 将 this 指向新建对象,并执行函数 (为这个新对象添加属性)
	 result = constructor.apply(newObject, arguments)
	 // console.log(result)  // undefined
	 // console.log(newObject)
	 // fn {name: '111'}
	 // 判断返回对象
	 let flag = result && (typeof result === 'object' || typeof result === 'function')
	 // 判断返回结果
	 return flag ? result : newObject
}
// 使用方法
objectFactory(构造函数, 初始化参数)
```

```js
function fn(name) {
    this.name = name
}
let obj = objectFactory(fn, '111')
console.log(obj) // {"name": "111"}
```


### 进行返回类型判断的原因
```js
function fn(name) {
    this.name = name
    return  { '111':'111'}
}
let obj = objectFactory(fn, '111')
console.log(obj) // {'111': '111'}
```

## Array.prototype.shift.call(arguments)什么意思

```Js
let a = [1,2,3]
let b = Array.prototype.shift.call(a)
console.log(b)  // 1
```

在你提供的 `objectFactory` 函数中，`Array.prototype.shift.call(arguments)` 的作用是将函数参数列表中的第一个参数（即构造函数）移除并返回该参数。

首先，`arguments` 是一个特殊的对象，它代表了函数调用时传入的所有参数。虽然 `arguments` 看起来像一个数组，但是它实际上是一个类数组对象，没有数组的方法和属性。

`Array.prototype.shift` 是 JavaScript 数组对象的方法之一，它用于移除数组的第一个元素，并返回该元素。由于 `arguments` 不是一个真正的数组，因此不能直接使用 `shift` 方法。但是，由于 `shift` 方法是通过 `this` 来访问数组对象的，因此可以通过 `call` 方法来改变它的 `this` 上下文，使其指向 `arguments` 对象。

因此，`Array.prototype.shift.call(arguments)` 的作用是将函数参数列表中的第一个参数（即构造函数）从 `arguments` 对象中移除，并返回该参数。移除后，`arguments` 对象只剩下实际的函数参数。这样就可以将剩余的参数传递给构造函数，并执行相应的操作。
