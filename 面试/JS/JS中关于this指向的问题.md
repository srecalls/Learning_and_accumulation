1.全局中的this指向

	指向的是window
2.全局作用域或则普通函数中的this

	指向全局window
3.this永远指向最后调用它的那个对象

	在不是箭头函数的情况下
4.new 关键词改变了this的指向
5.apply，call，bind

	可以改变this的指向，不是箭头函数
6.箭头函数中的this

	它的指向在定义的时候就已经确定了
	箭头函数它本身没有this，看外层是否有函数，有就是外层函数的this，没有就是window
7.匿名函数中的this

	永远指向window，匿名函数的执行环境具有全局性，因此this指向window