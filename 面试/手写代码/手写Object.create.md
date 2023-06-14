[[JavaScript Object对象常用方法和属性]]
思路：将传入的对象作为原型
```js
function create(obj) {
	function F() {}
	F.prototype = obj
	return new F()
}
```