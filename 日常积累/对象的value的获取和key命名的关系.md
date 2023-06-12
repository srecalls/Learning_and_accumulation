- 如果对象里面的key是number的话或者string类型的数字的话，可以通过下标的方式直接获取，而不用加字符串
- 如果是对象里面key是字符串，则只能通过\[字符串]的形式获取
- 当然直接用` . `也可以

在 JavaScript 中，对象的属性名可以是字符串或者符号。当你使用点操作符（`.`）或者中括号（`[]`）来访问对象的属性时，如果属性名是一个字符串，那么就可以直接使用点操作符或者中括号来访问属性值。但是，如果属性名是一个数字，那么只能使用中括号来访问属性值。

如果属性名是一个数字，那么它会自动被转换成一个字符串，例如 `obj2[1]` 等同于 `obj2['1']`。
```js
let obj = [1, 2, 3]
function a(obj) {
    console.log(obj) 
    console.log(arguments[0])  // [1, 2, 3]
    return 0
}

console.log(a(obj,1,2,3,4,5))

let obj2 = {
    'name': 111,
    '1': 222,
    '2': [
        0,
        1,
        2
    ]
}
console.log(obj2[0]) // undefined
console.log(obj2[name]) // undefined
console.log(obj2['name']) // 111
console.log(obj2[2]) // [0, 1, 2]
```