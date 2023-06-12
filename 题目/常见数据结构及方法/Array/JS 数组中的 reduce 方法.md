## 1、定义

 reduce() 可以作为一个高阶函数，用于函数的 compose。

## 2、语法

```javascript
array.reduce(function(total, currentValue, currentIndex, arr), initialValue)
```

## 3、参数说明
![[Pasted image 20230420155351.png]]
![[Pasted image 20230420155411.png]]
total默认0

## 4、用法
reduce() 方法接收一个函数作为累加器，数组中的每个值（从左到右）开始缩减，最终计算为一个值。

## 5、注意事项
注意: reduce() 对于空数组是不会执行回调函数的。

## 6、初级应用使用实例讲解，对数组 array 进行求和。
*1、没有设置函数的初始迭代值*
 
```js
const array = [1, 2, 3, 4]
const newArr = array.reduce((total, currentValue, index, arr) => {
  console.log(total, currentValue, index, arr);
// 总共迭代三次，打印:
// 1 2 1 Array(4) [1, 2, 3, 4]
// 3 3 2 Array(4) [1, 2, 3, 4]
// 6 4 3 Array(4) [1, 2, 3, 4]
  return total + currentValue
})
console.log(newArr);// 最终求和，打印 10
```
分析：
在这里reduce的作用就是对这个数组进行求和，迭代了3次，函数迭代的初始值是1，也就是默
认值（数组的第一项），total的值是每次计算后的值。
 
*2、设置函数的初始迭代值*
```js
const array = [1, 2, 3, 4]
const newArr = array.reduce((total, currentValue, index, arr) =>{
  console.log(total, currentValue, index, arr);
// 因为设置可初始值，所以总共迭代四次，打印:
// 5 1 0 Array(4) [1, 2, 3, 4]
// 6 2 1 Arra(4) [1, 2, 3, 4]
// 8 3 2 Arra(4) [1, 2, 3, 4]
// 11 4 3 Arra(4) [1, 2, 3, 4]
  return total + currentValue
}, 5)
console.log(newArr);// 最终求和，打印 15
```
分析：
这里添加了一个初始的迭代值，也就是让total从5开始计算，可以看到这里迭代了4次，结果也加上了初始值。

## 7、常用实例 
1、求和，求乘积等等

```js
const arr = [1, 2, 3, 4, 5]
console.log(arr.reduce((a, b) => a + b))//15
console.log(arr.reduce((a, b) => a * b))//120
console.log(arr.reduce((a, b) => a - b))//-13
console.log(arr.reduce((a, b) => a / b))//0.008333333333333333
```

2、计算出数组中每个元素出现的次数

```js
const array = ['name', 'age', 'long', 'short', 'long', 'name', 'name']
const arrResult = array.reduce((total, cur) => {
console.log(total, cur)
   if (cur in total) {
    total[cur]++
  } else {
    total[cur] = 1
  }
  return total
}, {})
console.log(arrResult)
```
结果：
```js
{name: 3, age: 1, long: 2, short: 1}
```
name出现三次，age出现1次，long出现两次，short出现一次
 
分析：
1、由于设置了迭代初始值，total的第一个值是一个空对象，此时cur为name，然后进行判断，发现在pre没
有name属性，所以就将name对应的属性值赋为1；
2、后面没有重复的是一样的道理，如果碰到重复值，就会将该属性值加1，这样就能计算元素重复的次了。


3、去除数组中重复的元素

```js
const array = ['name', 'age', 'long', 'short', 'long', 'name', 'name']
const arrResult = array .reduce((pre,cur) =>{
    if(!pre.includes(cur)){
        pre.push(cur)
    }
    return pre;
},[])
 
console.log(arrResult)//结果：["name", "age", "long", "short"]
```
 
分析：
这里主要是借助迭代功能实现数组的扩展，判断当前元素是否已经添加到数组中，如果不存在就从尾部加，
这个方法在去重方法中应该算比较简单高效的。

4、对对象的属性求和。

```js
const array= [
    {
        name: 'xiaoming',
        age: 18
    },{
        name: 'xiaohong',
        age: 17
    },{
        name: 'xiaogang',
        age: 19
    }
]
 
const result = array.reduce((a,b) =>{
    a += b.age;
    return a;
},0)
console.log(result)//结果：54
```

分析：
这里主要就是利用reduce第一个参数是迭代，可以通过初始化这个参数的数据类型，达到想实现的效果。


## reduceRight()
`reduceRight()` 是 JavaScript 中数组的一个方法，它可以从数组的末尾开始，对数组中的每个元素执行一个提供的回调函数，将回调函数的返回值累计到一个最终的返回值中，并返回该最终值。

该方法接受两个参数，第一个参数是一个回调函数，它用来处理数组中的每个元素，该函数接受四个参数：

- `accumulator`：累加器，它存储了上一次调用回调函数时的返回值，或者是在第一次调用时提供的初始值。
- `currentValue`：当前元素，即当前被处理的数组元素。
- `currentIndex`：当前元素的索引。
- `array`：原始数组。

回调函数可以返回任何值，它返回的值将成为下一次调用回调函数时的 `accumulator` 的值。

第二个参数是可选的，它是一个初始值，如果提供了初始值，则它将被用作第一次调用回调函数时的 `accumulator` 的值。如果没有提供初始值，则将使用数组的最后一个元素作为初始值，并从数组的倒数第二个元素开始执行回调函数。

以下是一个示例：

```
const arr = [1, 2, 3, 4, 5];
const sum = arr.reduceRight((accumulator, currentValue) => accumulator + currentValue);

console.log(sum); // 15
```

在这个示例中，`reduceRight()` 方法被用来计算数组中所有元素的和。回调函数将每个元素与累加器相加，并返回新的累加器值。由于没有提供初始值，`reduceRight()` 方法从数组的最后一个元素开始执行回调函数，依次计算出所有元素的和，最终返回 15。