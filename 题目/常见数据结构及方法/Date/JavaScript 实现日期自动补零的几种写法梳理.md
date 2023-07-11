### 0.入门版
```js
var month = new Date().getMonth() + 1
if(month < 10) {
    month = '0' + month
} else {
    month = month + ''
}
```

### 1.三元运算符版
```js
var month = new Date().getMonth() + 1;
month = (month < 10 ? '0' : '') + month
```

### 2.ES6 版
```js
let month = new Date().getMonth() + 1
month = `${month < 0 ? '0' : ''}${month}`
```

### 3.string.padStart 版 (ES2017)
```js
let month = new Date().getMonth() + 1
month = String(month).padStart(2, '0')
```

### 4.repeat 版
```js
let month = new Date().getMonth() + 1
month = ('0'.repeat(2) + month).slice(-2)
```

### 5.Array.from(obj) 版
```js
let month = new Date().getMonth() + 1
month = (Array.from({length: 2}, e => 0).join('') + month).slice(-2)
```

### 6.Array(num) 版
与其用 `Array.from`，不如直接用 `Array()`：
```js
let month = new Date().getMonth() + 1
month = (Array(2).join('0') + month).slice(-2)
```


**注意**  
`Array(2).join('0')` 仅生成 `(n - 1)` 个占位符，因为月份或日期数 **至少占一位**。

由此可以抽取一个通用方法：
```js
const leadingDigit = (num, len=2, sep='0') => `${Array(len + 1).join(sep)}${num}`.slice(-len)
const month = new Date().getMonth() + 1
leadingDigit(month)          // '06'
leadingDigit(month, 3)       // '006'
leadingDigit(month, 3, '*')  // '**6'
```