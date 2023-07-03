## 一、concat() 生成 不改变

concat() 方法用于连接两个或多个数组。该方法不会改变现有的数组，仅会返回被连接数组的一个副本。

```js
var arr1 = [1,2,3];
var arr2 = [4,5];
var arr3 = arr1.concat(arr2);
console.log(arr1); //[1, 2, 3]
console.log(arr3); //[1, 2, 3, 4, 5]
```

## 二、join() 生成 不改变

join() 方法用于把数组中的所有元素放入一个字符串。元素是通过指定的分隔符进行分隔的，默认使用','号分割，不改变原数组。

```js
var arr = [2,3,4];
console.log(arr.join());  //2,3,4
console.log(arr);  //[2, 3, 4]
```

## 三、push() 返回长度 改变

push() 方法可向数组的末尾添加一个或多个元素，并返回新的长度。末尾添加，返回的是长度，会改变原数组。

```js
var a = [2,3,4];
var b = a.push(5);
console.log(a);  //[2,3,4,5]
console.log(b);  //4
//push方法可以一次添加多个元素push(data1,data2....)
```

## 四、pop() 返回最后 改变

pop() 方法用于删除并返回数组的最后一个元素。返回最后一个元素，会改变原数组。

```js
var arr = [2,3,4];
console.log(arr.pop()); //4
console.log(arr);  //[2,3]
```

## 五、shift() 返回第一个 改变

shift() 方法用于把数组的第一个元素从其中删除，并返回第一个元素的值。返回第一个元素，改变原数组。

```js
var arr = [2,3,4];
console.log(arr.shift()); //2
console.log(arr);  //[3,4]
```

## 六、unshift() 返回长度 改变

unshift() 方法可向数组的开头添加一个或更多元素，并返回新的长度。返回新长度，改变原数组。

```js
var arr = [2,3,4,5];
console.log(arr.unshift(3,6)); //6
console.log(arr); //[3, 6, 2, 3, 4, 5]
//tip:该方法可以不传参数,不传参数就是不增加元素。
```

## 七、slice() 生成 不改变

返回一个新的数组，包含从 start 到 end （不包括该元素）的 arrayObject 中的元素。返回选定的元素，该方法不会修改原数组。

```js
var arr = [2,3,4,5];
console.log(arr.slice(1,3));  //[3,4]
console.log(arr);  //[2,3,4,5]
```

## 八、splice() 生成 改变

splice() 方法可删除从 index 处开始的零个或多个元素，并且用参数列表中声明的一个或多个值来替换那些被删除的元素。如果从 arrayObject 中删除了元素，则返回的是含有被删除的元素的数组。splice() 方法会直接对数组进行修改。

`splice()` 方法接受三个或更多参数，它们的含义如下：

1. `start`（必需）**是包含start的（关键）**：指定要修改的起始位置的索引，可以是负数，表示从数组末尾向前计算的位置。如果 `start` 大于或等于数组的长度，则不会删除任何元素，但可以插入新元素。
2. `deleteCount`（可选）：指定要删除的元素的数量。如果省略此参数或其值大于或等于数组中从 `start` 位置开始的元素数量，则删除从 `start` 位置开始的所有元素。如果 `deleteCount` 的值为 0，则不会删除任何元素。
3. `item1, item2, ...`（可选）：要添加到数组的新元素，从 `start` 位置开始插入。如果省略所有 `item` 参数，则 `splice()` 方法将仅删除元素并不添加新元素。

```js
var a = [5,6,7,8];
console.log(a.splice(1,0,9)); //[]
console.log(a);  // [5, 9, 6, 7, 8]
var b = [5,6,7,8];
console.log(b.splice(1,2,3));  //[6, 7]
console.log(b); //[5, 3, 8]
var c = [1,2,3,4];
console.log(c.splice(0,1));  // [1]
console.log(c) // [2,3,4]
```

## 九、写错了（已删除）

## 十、sort 排序 生成 不改变
[[JS数组的排序（sort方法）]]
按照 Unicode code 位置排序，默认升序

```js
var fruit = ['cherries', 'apples', 'bananas'];
fruit.sort(); // ['apples', 'bananas', 'cherries']

var scores = [1, 10, 21, 2];
scores.sort(); // [1, 10, 2, 21]
```


```js
	// sort排序
    const sortArr = [5,2,1,3,6,8,4,5,7,0,15];
    const sortAns = sortArr.sort();
    console.log(sortAns);
    // [0, 1, 15, 2, 3, 4, 5, 5, 6, 7, 8] 

    const sortArr1 = [5,2,1,3,6,8,4,5,7,0,15];
    const sortAns1 = sortArr1.sort((a,b)=>{return a-b});
    console.log(sortAns1);
    // [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 15] 
    
    const sortArr2 = ["Banana", "Orange", "Apple", "Mango"];
    const sortAns2 = sortArr2.sort();
    // ['Apple', 'Banana', 'Mango', 'Orange']
```
sort() 方法用于对数组的元素进行排序。

排序顺序可以是字母或数字，并按升序或降序。默认排序顺序为按字母升序。

注意： 当数字是按字母顺序排列时"40"将排在"5"前面。因为“40”中的"4"小于“5”。

使用数字排序，你必须通过一个函数作为参数来调用。函数指定数字是按照升序还是降序排列。

注意： 这种方法会改变原始数组！。


## 十一、reverse() 生成 改变

reverse() 方法用于颠倒数组中元素的顺序。返回的是颠倒后的数组，会改变原数组。

```js
var arr = [2,3,4];
console.log(arr.reverse()); //[4, 3, 2]
console.log(arr);  //[4, 3, 2]
```

## 十二、indexOf 和 lastIndexOf 查找值

都接受两个参数：查找的值、查找起始位置  
不存在，返回 -1 ；存在，返回位置。indexOf 是从前往后查找， lastIndexOf 是从后往前查找。  
**indexOf**

```js
var a = [2, 9, 9];
a.indexOf(2); // 0
a.indexOf(7); // -1
if (a.indexOf(7) === -1) {
  // element doesn't exist in array
}
```

**lastIndexOf**

```js
var numbers = [2, 5, 9, 2];
numbers.lastIndexOf(2);     // 3
numbers.lastIndexOf(7);     // -1
numbers.lastIndexOf(2, 3);  // 3
numbers.lastIndexOf(2, 2);  // 0
numbers.lastIndexOf(2, -2); // 0
numbers.lastIndexOf(2, -1); // 3
```

## 十三、every

对数组的每一项都运行给定的函数，每一项都返回 ture,则返回 true

```js
function isBigEnough(element, index, array) {
  return element < 10;
}    
[2, 5, 8, 3, 4].every(isBigEnough);   // true
```

```js
arr= [2, 5, 8, 3, 4]  
console.log(arr.every((item,index) => {  
	item++  
	return item < 10  
})) // true  
console.log(arr); // [2, 5, 8, 3, 4]
```
在这个例子中，`arr.every()` 方法传递给回调函数的参数 `item` 是数组中每个元素的值的副本，它的值被复制到新的变量中，并在回调函数中被修改。这些修改不会影响原始数组中元素的值，因此 `arr` 数组的值不会受到影响。

回调函数接受三个参数：

- `currentValue`：当前元素的值。
- `index`：当前元素的索引。
- `array`：原始数组。

`every()` 方法会遍历数组中的每个元素，并依次调用回调函数进行测试。如果回调函数返回 `false`，则 `every()` 方法立即返回 `false`，不再继续测试数组中的其他元素；否则继续测试下一个元素，直到遍历完整个数组或发现不满足条件的元素为止。

**原理: 每一项都调用回调函数，如果全部return true则为true，有一个为false则为false**
## 十四、some

对数组的每一项都运行给定的函数，任意一项都返回 ture,则返回 true

```js
function compare(element, index, array) {
  return element > 10;
}    
[2, 5, 8, 1, 4].some(compare);  // false
[12, 5, 8, 1, 4].some(compare); // true
```
**原理：每一项都调用回调函数，有一项返回true则返回true，否则就返回false**
## 十五、filter

对数组的每一项都运行给定的函数，返回 结果为 ture 的项组成的数组

```js
var words = ["spray", "limit", "elite", "exuberant", "destruction", "present", "happy"];

var longWords = words.filter(function(word){
  return word.length > 6;
});
// Filtered array longWords is ["exuberant", "destruction", "present"]
```

## 十六、map

对数组的每一项都运行给定的函数，返回每次函数调用的结果组成一个新数组

```js
var numbers = [1, 5, 10, 15];
var doubles = numbers.map(function(x) {
   return x * 2;
});
// doubles is now [2, 10, 20, 30]
// numbers is still [1, 5, 10, 15]
```

```js
var numbers = [1, 5, 10, 15];
var doubles = numbers.map(function(x) {
    x = x
});
console.log(doubles) 
// [undefinded, undefinded, undefinded, undefinded]
```
**原理：每一项都调用回调函数，每一项执行的回调函数返回的数存入数组中，如果不返回则为undefinded**
## 十七、forEach 数组遍历

```js
const items = ['item1', 'item2', 'item3'];
const copy = [];    
items.forEach(function(item){
  copy.push(item)
});
```
**原理：每一项都调用回调函数**
## ES6新增新操作数组的方法

## 1、find()：
传入一个回调函数，找到数组中符合当前搜索规则的第一个元素，返回它，并且终止搜索。

```js
const arr = [1, "2", 3, 3, "2"]
console.log(arr.find(n => typeof n === "number")) // 1
console.log(arr.find(n => n === "4")) // undefined
```
**原理： 每一项都调用回调函数，如果有一项返回true，则返回传入的那项，否则则为undefined。当为true时返回的是那一项的拷贝，所以不是对原数进行操作**
## 2、findIndex()：

传入一个回调函数，找到数组中符合当前搜索规则的第一个元素，返回它的下标，终止搜索。

```js
const arr = [1, "2", 3, 3, "2"]
console.log(arr.findIndex(n => typeof n === "number")) // 0
console.log(arr.findIndex(n =>  n === 4)) // -1
```
**原理： 每一项都调用回调函数，如果有一项返回对应下标，否则返回-1**
## 3、fill()：

用新元素替换掉数组内的元素，可以指定替换下标范围。

```js
arr.fill(value, start, end)
```

## 4、copyWithin()：

选择数组的某个下标，从该位置开始复制数组元素，默认从0开始复制。也可以指定要复制的元素范围。
**start和end 左闭右开**
```js
arr.copyWithin(target, start, end)
const arr = [1, 2, 3, 4, 5]
console.log(arr.copyWithin(3))
 // [1,2,3,1,2] 从下标为3的元素开始(包括下标为3)，复制数组，所以4, 5被替换成1, 2
const arr1 = [1, 2, 3, 4, 5]
console.log(arr1.copyWithin(3, 1)) 
// [1,2,3,2,3] 从下标为3的元素开始(包括下标为3)，复制数组，指定复制的第一个元素下标为1，所以4, 5被替换成2, 3
const arr2 = [1, 2, 3, 4, 5]
console.log(arr2.copyWithin(3, 1, 2)) 
// [1,2,3,2,5] 从下标为3的元素开始(包括下标为3)，复制数组，指定复制的第一个元素下标为1，结束位置为2，所以4被替换成2
```

`copyWithin()` 是一个 JavaScript 数组方法，用于从数组的指定位置开始复制元素，并将其粘贴到数组的另一位置。该方法会修改原始数组，并返回修改后的数组。

`copyWithin()` 方法接受三个参数：

1. `target`（必需）：表示从哪个位置开始替换元素。如果是负数，则表示从数组末尾开始计算的位置。如果不指定该参数，则默认为 0。

2. `start`（可选）：表示从哪个位置开始读取要复制的元素。如果是负数，则表示从数组末尾开始计算的位置。如果不指定该参数，则默认为 0。

3. `end`（可选）：表示在哪个位置停止读取要复制的元素。如果是负数，则表示从数组末尾开始计算的位置。如果不指定该参数，则默认为数组的长度（end = arr.length）。

例如，可以使用以下语句将数组的前两个元素复制到数组的第三个位置：

```js
var arr = [1, 2, 3, 4, 5];
arr.copyWithin(2, 0, 2); // 1 2 1 2 5
```

在这个例子中，`target` 参数为 2，表示从数组的第三个位置开始替换元素。`start` 参数为 0，表示从数组的第一个位置开始读取要复制的元素，`end` 参数为 2，表示在第三个位置之前停止读取要复制的元素。因此，`copyWithin()` 方法将数组的前两个元素（1 和 2）复制到了数组的第三个位置（即 [1, 2, 1, 2, 5]）。

## 5、from

将类似数组的对象（array-like object）**类数组**和可遍历（iterable）**迭代器**的对象转为真正的数组
[[Array.from ()方法详解]]
```js
const bar = ["a", "b", "c"];
Array.from(bar);
// ["a", "b", "c"]

Array.from('foo');
// ["f", "o", "o"]
```

## 6、of

用于将一组值，转换为数组。这个方法的主要目的，是弥补数组构造函数 Array() 的不足。因为参数个数的不同，会导致 Array() 的行为有差异。

```js
Array() // []

Array(3) // [, , ,]    // [空属性 × 3]
Array(3, 11, 8) // [3, 11, 8]

Array.of(7);       // [7]
Array(7);          // [ , , , , , , ]

Array.of(1, 2, 3); // [1, 2, 3]
Array(1, 2, 3);    // [1, 2, 3]
```

## 7、entries() 返回迭代器：返回键值对

```js
//数组
const arr = ['a', 'b', 'c'];
for(let v of arr.entries()) {
  console.log(v)
}
// [0, 'a'] [1, 'b'] [2, 'c']

//Set
const arr = new Set(['a', 'b', 'c']);
for(let v of arr.entries()) {
  console.log(v)
}
// ['a', 'a'] ['b', 'b'] ['c', 'c']

//Map
const arr = new Map();
arr.set('a', 'a');
arr.set('b', 'b');
for(let v of arr.entries()) {
  console.log(v)
}
// ['a', 'a'] ['b', 'b']
```

## 8、values() 返回迭代器：返回键值对的value

```js
//数组
const arr = ['a', 'b', 'c'];
for(let v of arr.values()) {
  console.log(v)
}
//'a' 'b' 'c'

//Set
const arr = new Set(['a', 'b', 'c']);
for(let v of arr.values()) {
  console.log(v)
}
// 'a' 'b' 'c'

//Map
const arr = new Map();
arr.set('a', 'a');
arr.set('b', 'b');
for(let v of arr.values()) {
  console.log(v)
}
// 'a' 'b'
```

## 9、keys() 返回迭代器：返回键值对的key

```js
//数组
const arr = ['a', 'b', 'c'];
for(let v of arr.keys()) {
  console.log(v)
}
// 0 1 2

//Set
const arr = new Set(['a', 'b', 'c']);
for(let v of arr.keys()) {
  console.log(v)
}
// 'a' 'b' 'c'

//Map
const arr = new Map();
arr.set('a', 'a');
arr.set('b', 'b');
for(let v of arr.keys()) {
  console.log(v)
}
// 'a' 'b'
```

## 10、includes

判断数组中是否存在该元素，参数：查找的值、起始位置，可以替换 ES5 时代的 indexOf 判断方式。indexOf 判断元素是否为 NaN，会判断错误。

```js
var a = [1, 2, 3];
a.includes(2); // true
a.includes(4); // false
```