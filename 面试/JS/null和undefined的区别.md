>_Null 和 Undefined 区别_（面试问到过）

```js
console.log(null==undefined)//true
console.log(null===undefined)//false
```
null： object类型，代表“空值”，代表一个空对象指针，  
undefined： undefined类型，

null和 undefined都表示“值的空缺”，可以认为undefined是表示系统级的、出乎意料的或类似错误的值的空缺，  
  
null是表示程序级的、正常的或在意料之中的值的空缺。

undefined是访问一个未初始化的变量时返回的值，而null是访问一个尚未存在的对象时所返回的值。  
  
因此，可以把undefined看作是空的变量，而null看作是空的对象。

场景：  

	null  
	（1） 作为函数的参数，表示该函数的参数不是对象。  
	（2） 作为对象原型链的终点。  

	undefined  
	（1）变量被声明了，但没有赋值时，就等于undefined。  
	（2）调用函数时，应该提供的参数没有提供，该参数等于undefined。  
	（3）对象没有赋值的属性，该属性的值为undefined。  
	（4）函数没有返回值时或者return后面什么也没有，返回undefined。

  
  
作者：zhaoHui_Ti  
链接：https://www.jianshu.com/p/2206959c0019  
来源：简书  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
