Date对象是 JavaScript 原生的时间库。它以1970年1月1日00:00:00作为时间的零点，可以表示的时间范围是前后各1亿天（单位为毫秒）。下面是本次分享的列表：

## - 【一】`Date()`普通函数用法和构造函数用法
1. Date()函数用法，Date对象可以作为普通函数直接调用，返回一个代表当前时间的字符串，直接调用Date，不论是否有参数，返回的都是当前时间的字符串。

```js
Date()  // 输出 Fri Oct 12 2018 16:41:20 GMT+0800
Date(2018, 10, 12)  // 输出 Fri Oct 12 2018 16:41:20 GMT+0800
```

2. Date()构造函数用法，使用new关键字实例化Date，返回一个Date对象的实例，如果不设置参数，返回的就是当前时间对象的实例
```js
var curDate = new Date();
console.log(curDate) // 当前时间字符串 Fri Oct 12 2018 16:57:10 GMT+0800
curDate.getFullYear() // 当前时间的年
curDate.getMonth()  // 当前时间的月
curDate.getDate() //  当前时间的天
```

实例化Date时接收参数，**而所谓接收参数，通俗的讲就是，给实例设置一个初始化的时间，不在取当前时间**。

实例化Date的参数可以接收多种格式。
### - 第一种 毫秒格式的整数参数
```js
var msDate = new Date(1539302400000)    // Date 2018-10-12T00:00:00.000Z
```

### - 第二种 日期字符串,**而日期字符串格式，只要可以被Date.parse()解析的，就可以作为参数应用**
```js
new Date('2018/10/12')    // Date 2018-10-12T00:00:00.000Z
new Date('2018-10-12')    // Date 2018-10-12T00:00:00.000Z
new Date('10/12/2018')    // Date 2018-10-12T00:00:00.000Z
```

### - 第三种 年,月,日,时,分,秒的整数参数
```js
var setMyDate = new Date(2018, 10, 12, 17, 17, 30);
setMyDate.getFullYear(); // 输出 2018
setMyDate.getMonth(); //输出 10
setMyDate.getDate(); // 输出 12
// ... 依次类推输出设置的时间
```
对于第三种年月日时分秒整数参数设置时，**必须设置年月两个参数,其他参数可选择性设置，因为如果只设置一个参数，就会被当作毫秒式格式**：
```js
new Date(2018)    //设置一个参数 Thu Jan 01 1970 08:00:02 GMT+0800 (CST)
new Date(2018, 10)  //设置两个参数 Date 2018-10-22T00:00:00.000Z
```

**第三种年月日时分秒整数参数设置，还可以设置为负数，负数表示从设置的时间日减去相应的时间**
```js
new Date(2018, -1)  // Sat Dec 01 2017 00:00:00 GMT+0800 (CST)
new Date(2018, 0, -1)   // Sun Dec 30 2017 00:00:00 GMT+0800 (CST)
```

Date实例各个参数的取值范围如下：

	- 年：使用四位数年份，比如2000。如果写成两位数或个位数，则加上1900，即10代表1910年。如果是负数，表示公元前。
	- 月：0表示一月，依次类推，11表示12月。注意，月份是从0开始
	- 日：1~31。
	- 小时：0~23。
	- 分钟：0~59。
	- 秒：0~59
	- 毫秒：0~999

## - 【二】Date日期运算
Date的日期运算主要应用+和-运算符，+运算符就是把两个Date实例的时间字符串拼接：

```js
var msDate = new Date(2018, 10);
var myDate = new Date(2015, 10, 12);
console.log(msDate + myDate)    // Thu Nov 01 2018 00:00:00 GMT+0800Thu Nov 12 2015 00:00:00 GMT+0800
```

**- 运算符会更具实用性，- 运算符会把两个实例对象转换为它们的毫秒数进行相减，得出两个实例间隔的毫秒数：**
```js
var msDate = new Date(2018, 10);
var myDate = new Date(2015, 10, 12);
console.log(msDate - myDate)    // 93744000000
```

## - 【三】Date静态方法`Date.now(),Date.parse(),Date.UTC()`

### Date.now()
- `Date.now()`方法返回当前时间距离（1970年1月1日 00:00:00 UTC）的毫秒数

```js
Date.now()  // 1539338654125
```

### Data.parse()
`Date.parse()`方法用来解析日期字符串,返回该时间距离（1970年1月1日 00:00:00 UTC）的毫秒数,如果Date.parse()失败，则返回NaN

```js
Date.parse('2012-01-01')    // 1325376000000
Date.parse('2015/01/01')    // 1420041600000
Date.parse('***')   // NaN
```

### Date.UTC
`Date.UTC`方法接受年、月、日等变量作为参数，返回该时间距离时间零点（1970年1月1日 00:00:00 UTC）的毫秒数。
```js
Date.UTC(2018, 10, 12, 18, 15, 30)  // 1542046530000
```

该方法的参数用法与Date构造函数完全一致，比如月从0开始计算，日期从1开始计算。区别在于Date.UTC方法的参数，会被解释为 UTC 时间（世界标准时间），Date构造函数的参数会被解释为当前时区的时间。

## - 【四】Date实例方法get系列，set系列，to系列，`valueOf()`

Date的实例对象，有几十个自己的方法，除了valueOf和toString，可以分为以下三类。

- `to`类：从Date对象返回一个字符串，表示指定的时间。
- `get`类：获取Date对象的日期和时间。
- `set`类：设置Date对象的日期和时间。


`Date.prototype.valueOf()`,`valueOf`方法返回实例对象距离时间零点（1970年1月1日00:00:00 UTC）对应的毫秒数，该方法等同于`getTime`方法。

```js
var myDate = new Date()
    myDate.valueOf();   // 1541001600000
    myDate.getTime();   // 1541001600000
```

### **(1)to系列方法**

	- Date.prototype.toString() 
	方法返回一个完整的日期字符串,和实例对象输出一样;

	- Date.prototype.toUTCString()
	方法返回对应的 UTC 时间，也就是比北京时间晚8个小时;

	- Date.prototype.toISOString()
	方法返回对应时间的 ISO8601 写法

	- Date.prototype.toJSON() 
	方法返回一个符合 JSON 格式的 ISO 日期字符串，与toISOString方法的返回结果完全相同

	- Date.prototype.toDateString()
	方法返回日期字符串（不含小时、分和秒）

	- Date.prototype.toTimeString()
	toTimeString方法返回时间字符串（不含年月日)

	- Date.prototype.toLocaleString()
	方法返回完整的本地时间

	- Date.prototype.toLocaleDateString()
	方法返回本地日期（不含小时、分和秒）

	- Date.prototype.toLocaleTimeString()
	方法返回本地时间（不含年月日）

### **(2)get系列方法**

get系列，是获取Date实例上的时间，new Date()已经初始化了一个时间。

	- getTime()：返回实例距离1970年1月1日00:00:00的毫秒数，等同于valueOf方法。
	- getDate()：返回实例对象对应每个月的几号（从1开始）。
	- getDay()：返回星期几，星期日为0，星期一为1，以此类推。
	- getYear()：返回距离1900的年数。
	- getFullYear()：返回四位的年份。
	- getMonth()：返回月份（0表示1月，11表示12月）。
	- getHours()：返回小时（0-23）。
	- getMilliseconds()：返回毫秒（0-999）。
	- getMinutes()：返回分钟（0-59）。
	- getSeconds()：返回秒（0-59）。
	- getTimezoneOffset()：返回当前时间与 UTC 的时区差异，以分钟表示，返回结果考虑到了夏令时因素

  ### **(3)set系列方法**

set系列，是对实例对象上的时间重新设置，也可以理解成修改，因为Date构造函数创建时，就已经初始化了一个时间，给new Date()传入参数就是设置时间：

	- setDate()：设置实例对象对应的每个月的几号（1-31），返回改变后毫秒时间戳。
	- setYear(): 设置距离1900年的年数。
	- setFullYear()：设置四位年份。
	- setHours()：设置小时（0-23）。
	- setMilliseconds()：设置毫秒（0-999）。
	- setMinutes()：设置分钟（0-59）。
	- setMonth()：设置月份（0-11）。
	- setSeconds()：设置秒（0-59）。
	- setTime()：设置毫秒时间戳。

get系列和set系列还有对应的UTC世界标准时间的get方法，这里将不在一一列举了，大家也可以去[w3c官网](https://link.juejin.cn?target=http%3A%2F%2Fwww.w3school.com.cn%2Fjsref%2Fjsref_obj_date.asp "http://www.w3school.com.cn/jsref/jsref_obj_date.asp")查看；

链接：https://juejin.cn/post/6844903692697600014  
来源：稀土掘金  
