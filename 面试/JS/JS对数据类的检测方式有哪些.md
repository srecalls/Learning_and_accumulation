这里着重了解一下原型链
## 1.typeof
1.typeof(()) 对于基本数据类型没问题，遇到引用数据类型都不管用
```js
console.log(typeof 666 )//number
console.log(typeof [1,2,3]) //object
console.log(typeof 2); // number
console.log(typeof true); // boolean
console.log(typeof 'str'); // string
console.log(typeof []); // object
console.log(typeof function(){}); // function
console.log(typeof {}); // object
console.log(typeof undefined); // undefined
console.log(typeof null); // object
```


其中`数组、对象、null都会被判断为object`, 其他判断都正确。
[[9.typeof NaN的结果]]
[[5.typeof null的结果是什么,为什么]]
`typeof` 运算符只能用于检测基本数据类型，而不能用于检测对象类型，是因为 `typeof` 运算符是 JavaScript 语言的一种设计决策。

`typeof` 运算符将值的二进制表示与 JavaScript 中的类型标识进行比较，根据比较结果返回一个表示数据类型的字符串。

## 2. instanceof()
[[6.instanceof 操作符的实现原理及实现]]
2.instanceof() 只能判断引用数据类型，不能判断基本数据类型。
 instanceof可以正确判断对象的类型，其内部运行机制是**判断在其原型链中能否找到该类型的原型。**


```js
console. log(2 instanceof Number); // false
console. log(true instanceof Boolean); // false
console.log('str' instanceof String); // false
console.log([] instanceof Array); // true
console. log(function(){} instanceof Function); // true
console.log({} instanceof object); // true
```
可以看到,instanceof只能正确判断引用数据类型，而不能判断基本数据类型。instanceof 运算符可以用来测试一个对象在其原型链中是否存在一个构造函数的prototype 属性。

`instanceof` 运算符是 JavaScript 中的一种运算符，用于检测一个对象是否属于某个类或原型链中的某个类。它的原理是通过检查对象的原型链来判断它是否属于某个类。

在 JavaScript 中，每个对象都有一个原型属性（`[[Prototype]]` 或 `__proto__`），它指向该对象的原型。原型是一个普通的对象，用于存储共享的属性和方法。如果一个对象的某个属性或方法在自身上不存在，那么 JavaScript 引擎会沿着该对象的原型链向上查找，直到找到该属性或方法为止。

当使用 `instanceof` 运算符检测一个对象是否属于某个类时，它会沿着该对象的原型链向上查找，直到找到该类的原型为止。如果找到了该类的原型，则返回 `true`，否则返回 `false`。

`instanceof` 运算符只能用于检测复杂数据类型，而不能用于检测基本数据类型。这是因为基本数据类型在 JavaScript 中是不具有属性和方法的，因此它们不能被视为对象或类。


## constructor

3.constructor 几乎可以判断基本数据类型和引用数据类型;如果声明了一个构造函数，并把它的原型指向了Array
```js
console. log((2).constructor === Number); // true
console. log( (true). constructor === Boolean); // true
console.log(('str').constructor === String); // true
console. log(([ ]) . constructor === Array); // true
console. log((function() {}). constructor === Function); // true
console. log(({}) . constructor === Object); // true
```

虽然基本数据类型本身没有原型，但 JavaScript 会将它们自动封装成对应的包装对象，例如将字符串类型转换成 `String` 包装对象、将数字类型转换成 `Number` 包装对象等。这些包装对象是对象，因此它们具有原型。

对于包装对象来说，它们的构造函数是对应的基本数据类型的构造函数。例如，`Number` 包装对象的构造函数是 `Number`，`String` 包装对象的构造函数是 `String`，以此类推。因此，这些包装对象具有 `constructor` 属性，用于标识它们的构造函数。

例如，以下代码将一个数字类型的值转换成 `Number` 包装对象，并检测其 `constructor` 属性：

```js
let num = 123;
let numObj = new Number(num);
console.log(numObj.constructor === Number); // true
```

在这个例子中，`numObj` 是一个 `Number` 包装对象，它的构造函数是 `Number`，因此它的 `constructor` 属性指向 `Number` 构造函数。

需要注意的是，对于基本数据类型的值，`constructor` 属性只能用于检测其对应的包装对象的构造函数，而不能用于检测基本数据类型本身的类型。例如，以下代码将会返回 `false`：

```js
let num = 123;
console.log(num.constructor === Number); // true
console.log(num.constructor === Number.prototype.constructor); // false
```

在这个例子中，虽然 `num` 对应的包装对象是 `Number` 类型的，但它的原型是 `Number.prototype`，因此 `num.constructor` 指向 `Number.prototype.constructor`，而不是 `Number` 构造函数。

因此，虽然基本数据类型本身没有原型，但它们的包装对象具有原型，并且具有 `constructor` 属性，用于标识它们的构造函数


constructor有两个作用，一是判断数据的类型,二是对象实例通过constrcutor 对象访问它的构造函数。需要注意，如果创建一个对象来改变它的原型，constructor 就不能用来判断数据类型了。

```js
function Fn(){};
Fn.prototype = new Array();
var f = new Fn();
console. log(f.constructor===Fn); // false
console. log(f.constructor===Array); // true
```

## Object.prototype.tostring.call
4.Object.protoype.tostring.call() 完美的方法
使用Object对象的原型方法toString来判断数据类型。


```js
var opt = Object.prototype.tostring
console.log( opt.call(2) ) //"[object Number]"
console.log( opt.call(true) ) //"[object Boolean]"
console.log( opt.call(' aaa ' ) ) //"[object String]"
console.log( opt.call([]) )   //"[object Array]"
console.log( opt.call({}) )    //"[object Function]"

Object.prototype.toString.call(arr); // "[object Array]"
Object.prototype.toString.call(2); // "[object Number]"
Object.prototype.toString.call(""); // "[object String]"
Object.prototype.toString.call(true); // "[object Boolean]"
Object.prototype.toString.call(undefined); // "[object Undefined]"
Object.prototype.toString.call(null); // "[object Null]"
Object.prototype.toString.call(Math); // "[object Math]"
Object.prototype.toString.call({}); // "[object Object]"
Object.prototype.toString.call([]); // "[object Array]"
Object.prototype.toString.call(function () {}); // "[object Function]"
```

同样是检测对象obj调用toString方法, obj.toString)的结果和Object.prototype toString.call(obj)的结果不一样,这是为什么?

这是因为toString是Object的原型方法,而Array、 function等类型作为Object的实例， 都重写了toString方法。不同的对象类型调用toString方法时，根据原型链的知识,调用的是对应的重写之后的toString方法(function类型返回内容为函数体的字符串，Array类型返回元素组成的字符串)，而不会去调用Object上原型toString方法(返回对象的具体类型)，所以采用obj.toString()不能得到其对象类型，只能将obj转换为字符串类型;因此，在想要得到对象的具体类型时，应该调用Object原型上的toString方法。

# 面试题：

- typeof "foo"   

		string

- typeof Object 、String、Array、Boolean、Date、RegExp
![[Pasted image 20230411210319.png]]
		
		Function
	
这是因为在 JavaScript 中，`Object` 和 `String` 都是构造函数（也就是函数类型），用于创建对象和字符串类型的值。因此，它们的 `typeof` 运算符结果分别为 `'function'`。

	
- typeof undefined

		undefined
执行 `typeof undefined` 的结果是 `'undefined'`。

这是因为 `undefined` 是一个特殊的值，表示一个未定义的变量或对象属性。在 JavaScript 中，如果使用 `typeof` 运算符检测一个未定义的变量或对象属性，其结果将会是 `'undefined'`。



- typeof 数组\[\]和Array出来的数组


		const a = new Array();

      console.log(typeof a); // object

      console.log(typeof [1, 2, 3]);  //object

typeof(typeof Object)  
  
	typeof Object的返回值为“function”，是个字符串，那么再获取它的类型时，肯定就是String咯！



#  知识点
1. 在[JavaScript](https://so.csdn.net/so/search?q=JavaScript&spm=1001.2101.3001.7020)中，数组是一种特殊的对象类型。 因此 typeof [1,2,3,4] 返回 object。 

2. 在 JavaScript 中 null 表示 "什么都没有"。null是一个只有一个值的特殊类型。表示一个空对象引用。

    用 typeof 检测 null 返回是object。

3.  在JavaScript 中, **undefined** 是一个没有设置值的变量。**typeof** 一个没有值的变量会返回 **undefined**。

     任何变量都可以通过设置值为 **undefined** 来清空。 类型为 **undefined**.

4. undefined 和 null 的区别

		null 和 undefined 的值相等，但类型不等：		
		typeof undefined             // undefined  
		typeof null                  // object  
		null === undefined           // false  
		null == undefined            // true