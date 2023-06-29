1.新增块级作用域(let, const)  
[[var、let、const的使用及区别，什么是暂时性死区？]]

	不存在变量提升
	存在暂时性死区的问题
	块级作用域的内容
	不能在同一个作用域内重复声明

2.新增了定义类的语法糖(class)
[[class类的用法]]

3.新增了一种基本数据类型(symbol)
[[Symbol的基本使用]]
[[面试/Vue/Symbol的特性|Symbol的特性]]

	ES6引入了一种新的原始数据类型 Symbol，表示独一无二的值。它是
	Javascript 语言的第七种数据类型，是一种类似于字符串的数据类型。
	Symbol特点
	1) Symbol 的值是唯一的，用来解决命名冲突的问题
	2) Symbol值不能与其他数据进行运算
	3） symbol定义的对象属性不能使用for..in 循环遍历，但是可以使用
	Reflect.ownkeysT来获取对象的所有键名

	不能进行四则运算

4.新增了解构赋值

	从数组或者对象中取值，然后给变量赋值

[[变量解构赋值]]


5.新增了函数参数的默认值
6.给数组新增了API
[[JavaScript常用数组操作方法，包含ES6方法]]
7.对象和数组新增了扩展运算符
[[扩展运算符实例]]
8.Promise

	解决回调地狱的问题。
	自身有al1, reject , resolve,race方法
	原型.上有then,catch
	把异步操作队列化
	三种状态: pending 初始状态, fulfilled操作成功, rejected操作失败
	状态: pending -> fulfilled;pending -> rejected 一旦发生，状态就会凝固，不会再变
	async await
	同步代码做异步的操作，两者必须搭配使用
	async表明函数内有异步操作，调用函数会返回promise
	await是组成async的表达式，结果是取决于它等待的内容，如果是promi se那就是promise的结果，如果是普通函数就进行链式调用
	await后的promi se如果是reject状态，那么整个async函数都会中断，后面的代码不执行

[[⭐Promise基本概念]]

9.新增了模块化( import , export)
10.新增了set和map数据结构

	set就是不重复
	map的key的类型不受限制

11.新增了generator
[[Generator的应用]]
[[生成器Generator的用法]]
12.新增了箭头函数

	不能作为构造函数使用，不能用new
	箭头函数没有原型
	箭头函数没有arguments
	箭头函数不能用ca1l, apply, bind去改变this的执行
	this指向外层第一个函数的this|

[[箭头函数和普通函数的区别]]
[[箭头函数及其生命特点]]
