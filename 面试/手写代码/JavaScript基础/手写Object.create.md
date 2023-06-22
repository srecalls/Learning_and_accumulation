[[JavaScript Object对象常用方法和属性]]
[[对原型、原型链的理解]]
## 思路：将传入的对象作为原型
```js
function create(obj) {
	function F() {}
	F.prototype = obj
	return new F()
}
```

当使用 `new` 关键字调用构造函数创建一个对象时，该对象的 `__proto__` 属性会指向构造函数的 `prototype` 属性。因此，在使用 `new` 关键字创建一个对象之后，该对象才会有 `__proto__` 属性，并且指向构造函数的 `prototype` 属性。

## 例子1
```js
var obj = {
    a: 1
}
var o = Object.create(obj)
console.log(o)
console.log(o.__proto__)
console.log(o.__proto__.constructor)

function create(obj) {
    function F() {}
    F.prototype = obj
    return new F()
}

let b = create(obj)
console.log(b)
console.log(b.__proto__)
console.log(b.__proto__.constructor)
```
![[Pasted image 20230621003417.png]]

在你的代码中，`create` 函数接受一个 `obj` 参数，然后创建一个新的函数 `F`，并将 `F.prototype` 属性设置为 `obj`，最后返回通过 `new F()` 创建的新对象。由于 `F.prototype` 属性被设置为 `obj`，因此新对象的原型链会指向 `obj`。

在这个过程中，确实会出现 `F.prototype` 的 `constructor` 属性被覆盖的情况。因为 `F.prototype` 被替换成了一个新的对象 `obj`，而这个新对象并没有 `constructor` 属性。因此，如果通过 `b.constructor` 来获取这个新对象的构造函数，会返回 undefined。


根据你提供的代码，假设你使用 `create` 函数创建了一个新对象 `b`，并将其原型链指向了 `obj` 对象，**那么 `b` 对象本身是一个空对象，没有自己的属性和方法。**

但是，由于 `b` 对象的原型链指向了 `obj` 对象，因此可以通过原型链来访问 `obj` 对象的属性和方法。例如，如果 `obj` 对象有一个属性 `prop`，那么可以通过 `b.prop` 来访问这个属性，也可以通过 `Object.getPrototypeOf(b).prop` 或 `b.__proto__.prop` 来访问原型对象 `obj` 上的属性。

以下是一个示例代码，展示了如何创建一个空对象，并通过原型链来访问原型对象的属性：

```
function create(obj) {
    function F() {}
    F.prototype = obj;
    return new F();
}

let obj = { prop: "value" };
let b = create(obj);
console.log(b); // 输出 {}
console.log(b.prop); // 输出 "value"
console.log(Object.getPrototypeOf(b).prop); // 输出 "value"
console.log(b.__proto__.prop); // 输出 "value"
```

在这个例子中，使用 `create` 函数创建了一个新对象 `b`，并将其原型链指向了 `obj` 对象。因为 `b` 对象本身没有属性，所以 `console.log(b)` 输出了一个空对象 `{}`。但是，通过 `console.log(b.prop)` 可以访问 `obj` 对象上的 `prop` 属性，输出了 `"value"`。同时，通过 `Object.getPrototypeOf(b).prop` 或 `b.__proto__.prop` 也可以访问原型对象 `obj` 上的属性。


## 例子2
```js
function create(obj) {
    function F() {}
    // F.prototype = obj   // 这里注释掉
    return new F()
}

let b = create(obj)

console.log(b)
console.log(b.__proto__)
console.log(b.__proto__.constructor)
```

![[Pasted image 20230621004507.png]]



## 说明：Object.create()
2. `Object.create()`方法创建一个新对象，使用现有对象来提供新创建对象的`__proto__`。


```js
var obj = {
	a: 1
}
var o = Object.create(obj)
console.log(o)
console.log(o.__proto__)
```
![[Pasted image 20230620235733.png]]

```js
var obj = {
	a: 1
}
var o = Object.create(obj)
console.log(o)
```
![[Pasted image 20230531172505.png]]

如上图所示，使用现有对象`obj`，来提供新对象`o`的`__proto__`。

`Object.create()`方法接收两个参数，  
第二个参数可省略,具体可参考我总结的这篇文章[《JavaScript ES6数据类型》](https://www.jianshu.com/p/2206959c0019)

留个代码图，注意看o.p的值是不可修改的。
  
![[Pasted image 20230531172518.png]]
create第二个参数