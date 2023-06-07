在 js 中是不能直接用 == 或者 === 来比较两个数组是否相等，那就需要对数组的值进行比较。

下面各种方法，要根据具体情况来使用。

## 一、 toString()

当两个数组元素类型相同，顺序相同时，直接判断是否相等，结果不相等；转化为字符串后，结果相等

```js
[1,2,3].toString() === [1, 2, 3].toString(); // true
[1,2,3].toString() === ['1', 2, 3].toString(); // true
```

## 二、join()

```js
[1,2,3,'4'].join() === [1,2,3,4].join(); // true
```

## 三、 JSON.stringify()

```js
JSON.stringify([{name:'许善祥'},{sex:'男'}]) == JSON.stringify([{name:'许善祥'},{sex:'男'}]); // true
```

## 四、sort()

当两个数组元素排序不相同时，先排序，再比较。如果是对象数组，可以结合 JSON.stringify 来使用。

```js
var a = ['1', '3', '2'];
var b = ['3', '1', '2'];

var c = a.length === b.length && a.sort().toString() === b.sort().toString();

console.log(c); // true
```

## 五、filter()

```js
var a = ['1', '3', '2'];
var b = ['3', '1', '2'];

var c = a.length === b.length && a.filter(t => !b.includes(t));

console.log(c); // true
```

	 filter() 创建一个新的数组，新数组中的元素是通过检查指定数组中符合条件的所有元素。  
 语法：  
```js
array.filter(function(currentValue,index,arr), thisValue);
```

**附：JS要比较两个数组是否有相同的元素，即两个数组所有元素都相同，但元素的顺序不一定一致。**

只就需要先将数组进行排序，再比较两个数组是否相等。

试比较以下两行代码：

```js
<script type="text/javascript">
        alert([1,2,3].toString()== [3,2,1].toString());
        alert([1,2,3].<strong>sort</strong>().toString()== [3,2,1].<strong>sort</strong>().toString());
</script>
```