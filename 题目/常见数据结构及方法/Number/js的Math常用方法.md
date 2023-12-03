## 【一】`Math.abs()` 返回绝对值
	Math.abs()方法，接收一个参数，返回这个参数的绝对值，通俗的讲就是把任何一个有效数字返回一个正数： 
```js
console.log(Math.abs(10))   // 输出 10
console.log(Math.abs(-10))  // 输出 10
```


## 【二】`Math.ceil(),Math.floor()` 向上取整和向下取整
	Math.ceil(),Math.floor()方法是获取整数的方法，接收一个参数，把小数点后面的数向上或者向下取一个整数。Math.ceil()是向上，Math.floor()是向下： 
```js
console.log(Math.ceil(10.01))   // 输出 11
console.log(Math.floor(10.01))  // 输出 10
```

## 【三】`Math.max(),Math.min()` 最大值和最小值
	Math.max(),Math.min()方法接收多个参数，并返回参数里数值最大或者最小的那个数，Math.max()是获取最大，Math.min()是获取最小： 
```js
console.log(Math.max(5, 1, 9, 3, 7))   // 输出 9
console.log(Math.min(5, 1, 9, 3, 7))  // 输出 1
```

Math.max(),Math.min()也可以用来获取数组里的最大数值和最小数值
```js
var arr = [5, 1, 9, 3, 7];
// 先看用循环实现方法,采用循环方式的核心思想就是假设法。
var max = 0, min = 1;
for (var num of arr) {
    if (max < num) {
		max = num
	}
	if (min > num) {
		min = num;
	}
}   // 输出 9, 1;
// 下面是采用apply改变this指向的方式直接获取最大值和最小值
console.log(Math.max.apply(null, arr))   // 输出 9
console.log(Math.min.apply(null, arr))  // 输出 1
```

## 【四】`Math.round()` 四舍五入
	Math.round()方法接收一个数字参数，对数字小数点后一位的数进行四舍五入处理 
```js
console.log(Math.round(3.87))   // 输出 4
console.log(Math.round(3.39))  // 输出 3
```

## 【五】`Math.random()` 随机数
	Math.random()方法返回一个0到1之间的随机数；

```js
console.log(Math.random())   // 输出 0到1之间的随机数
```

Math.random()是一个应用非常广泛的方法，下面看一个限定范围内的随机数：
```js
function getRandom (min, max) {
	return	Math.round(Math.random()*(max - min))
}
console.log(getRandom(0, 100)); // 输出0到100的随机整数
```

基于这个思想，可以做很多事情，比如随机取字符串里的值，随机取数组里的某个当前项等等。
```js
var ary = ['red', 'orange', 'yellow', 'blue', 'green']
function getRandom (min, max) {
		 return	ary[Math.round(Math.random()*(max - min))]
	}
console.log(getRandom(0, ary.length-1)); // 输出数组里随机的一个当前项
```

### [返回值](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Math/random#%E8%BF%94%E5%9B%9E%E5%80%BC)

一个浮点型伪随机数字，在`0`（包括 0）和`1`（不包括）之间。

## [示例](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Math/random#%E7%A4%BA%E4%BE%8B)

请注意，由于 JavaScript 中的数字是 IEEE 754 浮点数字，具有最近舍入（round-to-nearest-even）的行为，因此以下函数的范围 (不包括`Math.random()` 本身) 并不准确。如果选择了非常大的边界 (2^53 或更高), 在极罕见的情况下会计算通常 - 排除（usually-excluded）的上界。（注：round-to-nearest-even 采用最近舍入的去偶数舍入的方式，对.5 的舍入上，采用取偶数的方式）

### [得到一个大于等于 0，小于 1 之间的随机数](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Math/random#%E5%BE%97%E5%88%B0%E4%B8%80%E4%B8%AA%E5%A4%A7%E4%BA%8E%E7%AD%89%E4%BA%8E_0%EF%BC%8C%E5%B0%8F%E4%BA%8E_1_%E4%B9%8B%E9%97%B4%E7%9A%84%E9%9A%8F%E6%9C%BA%E6%95%B0)

JSCopy to Clipboard

```js
function getRandom() {
  return Math.random();
}
```

### [得到一个两数之间的随机数](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Math/random#%E5%BE%97%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%A4%E6%95%B0%E4%B9%8B%E9%97%B4%E7%9A%84%E9%9A%8F%E6%9C%BA%E6%95%B0)

这个例子返回了一个在指定值之间的随机数。这个值不小于 `min`（有可能等于），并且小于（不等于）`max`。


```js
// 10 - 100
function getRandomArbitrary(min, max) {
  return Math.random() * (max - min) + min;
  10 + 0 - 90
}
```

### [得到一个两数之间的随机整数](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Math/random#%E5%BE%97%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%A4%E6%95%B0%E4%B9%8B%E9%97%B4%E7%9A%84%E9%9A%8F%E6%9C%BA%E6%95%B4%E6%95%B0)

这个例子返回了一个在指定值之间的随机整数。这个值不小于 `min` （如果 `min` 不是整数，则不小于 `min` 的向上取整数），且小于（不等于）`max`。

JSCopy to Clipboard

```js
function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  // 10 - 100
  return Math.floor(Math.random() * (max - min)) + min; //不含最大值，含最小值
}
```

**备注：** 也许很容易想到用 `Math.round()` 来实现，但是这会导致你的随机数处于一个不均匀的分布，这可能不符合你的需求。

### [得到一个两数之间的随机整数，包括两个数在内](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Math/random#%E5%BE%97%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%A4%E6%95%B0%E4%B9%8B%E9%97%B4%E7%9A%84%E9%9A%8F%E6%9C%BA%E6%95%B4%E6%95%B0%EF%BC%8C%E5%8C%85%E6%8B%AC%E4%B8%A4%E4%B8%AA%E6%95%B0%E5%9C%A8%E5%86%85)

上一个例子提到的函数 `getRandomInt()` 结果范围包含了最小值，但不含最大值。如果你的随机结果需要同时包含最小值和最大值，怎么办呢？`getRandomIntInclusive()` 函数可以实现。

JSCopy to Clipboard

```js
function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  // 10 - 100
  return Math.floor(Math.random() * (max - min + 1)) + min; //含最大值，含最小值
}
```

## 【六】`Math.pow()` 指数运算
	Math.pow()方法返回以第一个参数为底数、第二个参数为幂的指数值。

```js
console.log(Math.pow(2, 2)); // 输出4
// 等同于 2 ** 2
console.log(Math.pow(2, 3)); // 输出8
// 等同于 2 ** 3
```

## 【七】`Math.sqrt()` 平方根
	Math.sqrt()方法返回参数值的平方根。如果参数是一个负值，则返回NaN。

```js
console.log(Math.sqrt(9)); // 输出3
console.log(Math.sqrt(-9)); // 输出NaN
```
## 【八】`Math.log()` 自然对数
	Math.log方法返回以e为底的自然对数值。

```js
console.log(Math.log(10)); // 输出 2.302585092994046
```


## 【九】`Math.exp()` e的指数
Math.exp()方法返回常数e的参数次方。

```js
console.log(Math.exp(1)); // 输出 2.7182818284590455
console.log(Math.exp(2)); // 输出 7.38905609893065
```

## 【十】Math属性

	- Math.E：常数e。
	- Math.LN2：2 的自然对数。
	- Math.LN10：10 的自然对数。
	- Math.LOG2E：以 2 为底的e的对数。
	- Math.LOG10E：以 10 为底的e的对数。
	- Math.PI：常数π。
	- Math.SQRT1_2：0.5 的平方根。
	- Math.SQRT2：2 的平方根

```js
Math.E // 2.718281828459045
Math.LN2 // 0.6931471805599453
Math.LN10 // 2.302585092994046
Math.LOG2E // 1.4426950408889634
Math.LOG10E // 0.4342944819032518
Math.PI // 3.141592653589793
Math.SQRT1_2 // 0.7071067811865476
Math.SQRT2 // 1.4142135623730951
```
注意Math的这些属性都是只读，不可以修改的。

##  【十一】Math三角函数

	- Math.sin()：返回参数的正弦（参数为弧度值）
	- Math.cos()：返回参数的余弦（参数为弧度值）
	- Math.tan()：返回参数的正切（参数为弧度值）
	- Math.asin()：返回参数的反正弦（返回值为弧度值）
	- Math.acos()：返回参数的反余弦（返回值为弧度值）
	- Math.atan()：返回参数的反正切（返回值为弧度值）

```js
Math.sin(0) // 0
Math.cos(0) // 1
Math.tan(0) // 0
Math.sin(Math.PI / 2) // 1
Math.asin(1) // 1.5707963267948966
Math.acos(1) // 0
Math.atan(1) // 0.7853981633974483
```



链接：https://juejin.cn/post/6844903687932870670  
来源：稀土掘金  
