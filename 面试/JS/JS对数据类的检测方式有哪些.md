1.typeof(()) 对于基本数据类型没问题，遇到引用数据类型都不管用

	console.log(typeof 666 )//number
	console.log(typeof [1,2,3]) //object
2.instanceof() 只能判断引用数据类型，不能判断基本数据类型
 
	console.log( [] instanceof Array) //true
	console.log( 'abc' instanceof String) //false


3.constructor 几乎可以判断基本数据类型和引用数据类型;如果声明了一个构造函数，并把它的原型指向了Array


	console.1og( ('abc'). constructor === String ) //true


4.Object.protoype.tostring.call() 完美的方法

	var opt = 0bject. prototype.tostring
	console.1log( opt.ca11(2) ) //Number
	console.1og( opt. call(true) ) //Boolean
	console.log( opt.call(' aaa ' ) ) //String
	console.1og( opt.call([]) )   //Array
	console.1og( opt. call({}) )    //Object
	
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

5.判断数组是不是数组
在 JavaScript 中，可以使用 `Array.isArray(a)` 方法来判断变量 `a` 是否为数组。这个方法会返回一个布尔值，如果 `a` 是数组，则返回 `true`，否则返回 `false`。例如：

```javascript
const a = [];
const b = Array(3);

console.log(Array.isArray(a)); // true
console.log(Array.isArray(b)); // true
console.log(Array.isArray({})); // false
console.log(Array.isArray('hello')); // false
```

在上面的例子中，变量 `a` 和 `b` 都是数组，所以调用 `Array.isArray()` 方法返回的都是 `true`。而变量 `{}` 和 `'hello'` 都不是数组，所以返回的是 `false`。


# 面试题：

typeof "foo"   

	string
	
typeof Object 、String、Array、Boolean、Date、RegExp
![[Pasted image 20230411210319.png]]

	Function
	
	
typeof undefined

	undefined


typeof 数组\[\]和Array出来的数组

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