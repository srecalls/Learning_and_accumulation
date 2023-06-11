## 一、普通数组的排序
js中用方法sort()为数组排序。sort()方法有一个可选参数，是用来确定元素顺序的函数。如果这个参数被省略，那么数组中的元素将按照ASCII字符顺序进行排序。如：

 ```js
 let arr = ['A','C','B','D']
 arr.sort()
 console.log(arr) // ['A','B','C','D']
 ```

如果一个数组元素是数字，此时还是用sort()为数组排序，先看看效果如何：

 ```js
 let arr = [15,8,25,3]
 arr.sort()
 console.log(arr) // [15,25,3,8]
 ```

怎么没有起到效果（按大小排序），其实，sort方法会调用每个数组项的toString()方法，得到字符串，然后再对得到的字符串进行排序。虽然数值15比3大，但在进行字符串比较时"15"则排在"3"前面（ASCII字符顺序）。显然，这种结果不是我们想要的，这时，sort()方法的参数就起到了作用，我们把这个参数叫做比较函数。

 ```js
 let arr = [15,8,25,3]
 arr.sort((x,y)=> x - y) // 正序
 console.log(arr) // [3,8,15,25]
 arr.sort((x,y)=> y - x) // 倒序
 ```

比较函数接收两个参数，如果第一个参数应该位于第二个之前则返回一个负数，如果两个参数相等则返回0，如果第一个参数应该位于第二个之后则返回一个正数。

## 二、数组内对象排序
数组项是对象，需要根据数组项的某个属性对数组进行排序。

```js
let person = [
	{name:'zs',age:22},
	{name:'ls',age:20},
	{name:'ww',age:28},
]
// 如果我们需要按照对象中的age属性进行数组排序
person.sort((a,b)=>{
	return a.age - b.age
})
console.log(person) // [{name:'ls',age:20},{name:'zs',age:22},{name:'ww',age:28},]
```

## 三、指定位置开始进行排序
### 利用slice
要对数组中指定位置开始进行排序，可以使用 `Array.prototype.slice()` 方法将需要排序的部分切割出来，然后再对切割出来的部分使用 `Array.prototype.sort()` 方法进行排序。最后，再将排序后的部分与原数组的其余部分拼接起来，以得到最终的排序结果。

以下是一个示例，演示如何对数组中下标为 3 的位置开始进行排序：

```javascript
const arr = [2, 5, 7, 8, 9, 1];
const startIndex = 3;

const sortedPart = arr.slice(startIndex).sort((a, b) => a - b);
const result = arr.slice(0, startIndex).concat(sortedPart);

console.log(result);
// 输出：[2, 5, 7, 1, 8, 9]
```

在上面的示例中，我们首先使用 `Array.prototype.slice()` 方法将数组中下标为 3 的位置开始的部分切割出来，即 `[8, 9, 1]`。然后，我们对切割出来的部分使用 `Array.prototype.sort()` 方法进行排序。在这个例子中，我们使用了一个简单的比较函数 `(a, b) => a - b`，它将按升序排列数组元素。最后，我们使用 `Array.prototype.concat()` 方法将排序后的部分与原数组的其余部分拼接起来，以得到最终的排序结果。

请注意，如果您需要对其他位置进行排序，只需要相应地修改 `startIndex` 的值即可。


### 利用splice直接在原数组操作
可以直接在原数组上进行操作，不需要创建一个新数组来保存排序结果。您可以使用 `Array.prototype.splice()` 方法来在原数组中插入、删除和替换元素。这个方法的第一个参数是插入/删除/替换的起始位置，第二个参数是需要删除的元素个数（如果是插入或替换，则为 0），后面的参数是需要插入/替换的元素。

以下是一个示例，演示如何对数组中下标为 3 的位置开始进行排序：

```javascript
const arr = [2, 5, 7, 8, 9, 1];
const startIndex = 3;

arr.splice(startIndex, arr.length - startIndex, ...arr.slice(startIndex).sort((a, b) => a - b));

console.log(arr);
// 输出：[2, 5, 7, 1, 8, 9]
```

在上面的示例中，我们使用 `Array.prototype.splice()` 方法在原数组中插入排序后的部分，删除原始部分。我们使用 `Array.prototype.slice()` 方法获取需要排序部分的副本，并对其进行排序。然后，我们使用拓展运算符 `...` 将排序后的部分作为参数传递给 `Array.prototype.splice()` 方法，以将其插入到原数组的 `startIndex` 位置。由于我们已经删除了原始部分，我们需要将第二个参数设置为 `arr.length - startIndex`，以删除剩余的元素。最终，我们直接在原数组上进行了排序。

请注意，直接在原数组上进行操作可能会对您的代码造成副作用，并可能导致出现未预期的结果。因此，在进行操作之前，请确保您已经了解了可能的风险，并进行相应的检查和测试。