Map转换为的数组对象]中索引值为0的为key，为1的为value。
所以如果需要根据其中内容进行排序的话如下操作即可。
```js
//按key值进行排序
//升序
const sortMap = new Map([...myMap].sort((a, b) => a[0] - b[0]));
//降序
const sortMap = new Map([...myMap].sort((a, b) => b[0] - a[0]));
 
//按value值进行排序
//升序
const sortMap = new Map([...myMap].sort((a, b) => a[1] - b[1]));
//降序
const sortMap = new Map([...myMap].sort((a, b) => b[1] - a[1]));
```

 完整测试代码
 ```js
var myMap = new Map();
myMap.set(2,4);
myMap.set(5,3);
myMap.set(7,6);
myMap.set(3,8);
myMap.set(9,4);
myMap.set(1,6);
const sortMap = new Map([...myMap].sort((a, b) => a[1] - b[1]));
for (const [key, value] of sortMap) 
{
	console.log(key + ' ' + value)
}
 ```


使用 sort() 方法对 Map 中的键进行排序，例如
``` js
const sorted = new Map([...map1].sort())
```

`(...)` 是用于获取 Map 元素的数组，我们可以使用 sort 方法对其进行排序。看下面的例子

```js
const map1 = new Map([ ['z', 'three'], ['a', 'one'], ['b', 'two'], ]);
``` 

```js
console.log(map1);
//  {'z' => 'three', 'a' => 'one', 'b' => 'two'}
```
      
```js
console.log(...map1);
//Array(2)                  Array(2)            Array(2)
//0:"z" , 1:"three"         //0:"a", 1:"one"       0:"b",  1:"two"
```
      

```js
console.log([...map1]);
// Array(3); [Array(2),Array(2),Array(2)]
// 0: (2) ['z', 'three']
// 1: (2) ['a', 'one']
// 2: (2) ['b', 'two']
```


```js
console.log([...map1].sort());
// Array(3); [Array(2),Array(2),Array(2)]
// 0: (2) ['a', 'one']
// 1: (2) ['b', 'two']
// 2: (2) ['z', 'three']
```

new Map就是给数组一个键对值的对应关系
```js
// 升序
const sortedAsc = new Map([...map1].sort());
// {'a' => 'one', 'b' => 'two', 'z' => 'three'}
console.log(sortedAsc);
```


**使用 sort() 方法对 Map 中的键进行排序，例如
``` js
const sorted = new Map([...map1].sort())
```

`(...)` 是用于获取 Map 元素的数组，我们可以使用 sort 方法对其进行排序。看下面的例子

```js
const map1 = new Map([ ['z', 'three'], ['a', 'one'], ['b', 'two'], ]); 
// {'z' => 'three', 'a' => 'one', 'b' => 'two'} 
console.log(map1); 
// 升序 
const sortedAsc = new Map([...map1].sort()); 
// {'a' => 'one', 'b' => 'two', 'z' => 'three'} 
console.log(sortedAsc);
``` 

上面代码运行结果如下

```js
Map(3) { 'z' => 'three', 'a' => 'one', 'b' => 'two' }
Map(3) { 'a' => 'one', 'b' => 'two', 'z' => 'three' }
Map(3) { 'z' => 'three', 'b' => 'two', 'a' => 'one' }
Map(3) { 1 => 'one', 2 => 'two', 3 => 'three' }
Map(3) { 3 => 'three', 2 => 'two', 1 => 'one' }
```

Map 对象会记住键的插入顺序。
这就是我们使用 Map() 构造函数以正确顺序创建新 Map 的原因。
扩展语法 `(...)` 允许我们获取包含 Map 元素的数组。

```js
const map1 = new Map([ ['z', 'three'], ['a', 'one'], ['b', 'two'], ]); 
// [['z', 'three'], ['a', 'one'], ['b', 'two']] 
console.log([...map1]);
```

当使用字符串键对 Map 进行排序时，我们只需要调用 sort() 方法。
```js
const map1 = new Map([ ['z', 'three'], ['a', 'one'], ['b', 'two'], ]); 
// [['a', 'one'], ['b', 'two'], ['z', 'three']] 
console.log([...map1].sort());
```
这为我们提供了一个包含键值对数组的数组，我们可以直接将其传递给 Map 构造函数以\从而创建一个带有排序键的新 Map。
这是完整的代码片段：
```js
const map1 = new Map([
  ['z', 'three'],
  ['a', 'one'],
  ['b', 'two'],
]);

// {'z' => 'three', 'a' => 'one', 'b' => 'two'}
console.log(map1);

// 升序
const sortedAsc = new Map([...map1].sort());
```
在键值对数组上调用 sort() 方法时，我们只是对键值对的字符串转换进行排序，例如 `{z,three}` 对 `{a,one}`。

我们使用相同的方法按降序对 Map 的键进行排序。 我们所要做的就是在排序后添加对 reverse() 方法的调用。
```js
const map1 = new Map([ ['z', 'three'], ['a', 'one'], ['b', 'two'], ]); 
// 降序 
const sortedDesc = new Map([...map1].sort().reverse()); 
console.log(sortedDesc);
```

如果 Map 的键是数字，则sort()方法的参数必须是一个函数。该方法的参数是一个定义排序顺序的函数。该函数使用 2 个参数。
```js
const map2 = new Map([ [3, 'three'], [1, 'one'], [2, 'two'], ]); 
// 升序 
const sortNumAsc = new Map([...map2].sort((a, b) => a[0] - b[0])); 
// {1 => 'one', 2 => 'two', 3 => 'three'} 
console.log(sortNumAsc);
```

sort() 方法对元素进行排序的逻辑如下：

-   如果比较函数的返回值大于0，则将b排在a之前。
-   如果比较函数的返回值小于0，则将a排在b之前。
-   如果 compare 函数的返回值等于 0，则保持 a 和 b 的原始顺序。

在上面的代码片段中：

-   如果a数组的第一个元素（键）减去b数组的第一个元素返回的值大于0，我们将b排在a之前
-   如果减法返回负数，我们将 a 排序在 b 之前。
-   如果减法返回 0，我们保持 a 和 b 的原始顺序。**
