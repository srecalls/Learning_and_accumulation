	1.都是处理异步请求的方式
	2. promise是ES6，async await 是ES7的语法
	3.async await是 基于promise实现的，他和promise都是非阻塞性的
优缺点:

	1. promise是返回对象我们要用then，catch方法去 处理和捕获异常，并且书写方式是链式，容易造成代码重叠，不好维护，async await 是通过try catch进 行捕获异常
	2. async await最大的优点就是能让代码看起来像同步一样， 只要遇到await就会立刻返回结果，然后再执行后面的操作
	promise. then()的方式返回，会出现请求还没返回，就执行了后面的操作
