```js
let arr = [1,2,3,5,6]
// 传递的参数是参数列表而不是数组
console.log(Math.max(...arr)) // 6
console.log(Math.max(arr)) // NaN
console.log(Math.max(2,5,6,8,7,9)) // 9
```