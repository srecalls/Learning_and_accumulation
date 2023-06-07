Array.from()方法就是将一个类数组对象或者可遍历对象转换成一个真正的数组，也是ES6的新增方法。

## [语法](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/from#%E8%AF%AD%E6%B3%95)

```
Array.from(arrayLike)
Array.from(arrayLike, mapFn)
Array.from(arrayLike, mapFn, thisArg)
```


# 参数

`arrayLike`

想要转换成数组的类数组或可迭代对象。

`mapFn` 可选

调用数组每个元素的函数。如果提供，每个将要添加到数组中的值首先会传递给该函数，然后将 `mapFn` 的返回值增加到数组中。使用以下参数调用该函数：

`element`

数组当前正在处理的元素。

`index`

数组当前正在处理的元素的索引。

`thisArg` 可选

执行 `mapFn` 时用作 `this` 的值。

### [返回值](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/from#%E8%BF%94%E5%9B%9E%E5%80%BC)

一个新的[数组](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array)实例。

那么什么是类数组对象呢？所谓类数组对象，最基本的要求就是具有length属性的对象。

1、将类数组对象转换为真正数组：

```js
let arrayLike = {
	0: 'tom', 
	1: '65',
	2: '男',
	3: ['jane','john','Mary'],
	'length': 4
}
let arr = Array.from(arrayLike)
console.log(arr) // ['tom','65','男',['jane','john','Mary']]
```

那么，如果将上面代码中length属性去掉呢？实践证明，答案会是一个长度为0的空数组。

这里将代码再改一下，就是具有length属性，但是对象的属性名不再是数字类型的，而是其他字符串型的，代码如下：

```js
let arrayLike = {
    'name': 'tom', 
    'age': '65',
    'sex': '男',
    'friends': ['jane','john','Mary'],
    length: 4
}
let arr = Array.from(arrayLike)
console.log(arr)  // [ undefined, undefined, undefined, undefined ]
```

会发现结果是长度为4，元素均为undefined的数组

由此可见，要将一个类数组对象转换为一个真正的数组，必须具备以下条件：

	　　1、该类数组对象必须具有length属性，用于指定数组的长度。如果没有length属性，那么转换后的数组是一个空数组。
	　　2、该类数组对象的属性名必须为数值型或字符串型的数字
	　　ps: 该类数组对象的属性名可以加引号，也可以不加引号

2、将Set结构的数据转换为真正的数组：

```js
let arr = [12,45,97,9797,564,134,45642]
let set = new Set(arr)
console.log(Array.from(set))  // [ 12, 45, 97, 9797, 564, 134, 45642 ]
```

Array.from还可以接受第二个参数，作用类似于数组的map方法，用来对每个元素进行处理，将处理后的值放入返回的数组。如下：

```js
let arr = [12,45,97,9797,564,134,45642]
let set = new Set(arr)
console.log(Array.from(set, item => item + 1)) // [ 13, 46, 98, 9798, 565, 135, 45643 ]
```

3、将字符串转换为数组：

```js
let  str = 'hello world!';
console.log(Array.from(str)) // ["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d", "!"]
```

4、Array.from参数是一个真正的数组：

```js
console.log(Array.from([12,45,47,56,213,4654,154]))
```

像这种情况，Array.from会返回一个一模一样的新数组。

原文链接：https://blog.csdn.net/qq_27674439/article/details/108793223