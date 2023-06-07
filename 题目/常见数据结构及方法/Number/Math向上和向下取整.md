## Math方法向上向下取整
在Javascript的数值运算中，很多时侯需要对最后计算结果向下取整，Math.floor是javascrip中对计算结果向下取整的函数，它总是将数值向下舍入为最接近的整数。此外Math.ceil()函数则是javascript中向上取整函数，Math.round0方法可对计算结果进行四舍五入操作。

## Math.floor
例如一个数值变量 var num=25.4。对num变量向下取整可使用
```js
var floorNum=Math.floor(num)://计算结果为floorNum=25
```

## Math.ceil
如果需要对num变量进行向上取整，则使用Math.ceil()函数来实现

```js
var ceilNum=Math.ceil(num);//计算结果为ceilNum=26。
```

## Math.round
对num变量进行四舍五入取整，则使用Math.round()函数来实现

```js
var roundNum=Math.roundNumnum)://计算结果为roundNum=25。
```