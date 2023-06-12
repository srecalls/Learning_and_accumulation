该函数库也有提供 .cloneDeep用来做 Deep Copy
```js
var= require('lodash');
var obj1 = {
	a: 1,
	b: { f: { g: 1 } },
	c: [1, 2, 3]
}
var obj2 = _.cloneDeep(obj1);
console.log(obj1.b.f === obj2.b.f);// false
```