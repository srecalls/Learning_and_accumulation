# Map的属性
## size
Map 的属性，有一个属性`size`，用来存储它的成员个数
```js
const m = new Map([
    ['val', 'map'],
    ['cat', 'animal'],
    ['orange', 'fruit']
]);
console.log(m.size);
```

# Map的方法
## set
给 Map 中添加成员
```js
const m = new Map();
// 它的参数为两个，第一个为键，第二个为值
m.set('val', 'map');
console.log(m);
// 可以连缀 Set
m.set('orange', 'fruit').set('cat', 'animal');
console.log(m);
// 添加的新成员如果键已经存在了，那么将会覆盖它
// 键的顺序不会发生改变，因为 Map 能够记住键的原始插入顺序
m.set('orange', 'sweet');
console.log(m);
```
![[Pasted image 20230414132423.png]]

## get
通过键获取 Map 的成员
```js
const m = new Map([
    ['val', 'map'],
    ['orange', 'fruit'],
    ['cat', 'animal'],
    [true, 'false']
]);
console.log(m.get('val'));
console.log(m.get(true));
// 获取不存在的键时，会返回 undefined
console.log(m.get('tigger'));
```
![[Pasted image 20230414132452.png]]

## has
用来判断 Map 是否含有某个键
```js
const m = new Map([
    ['val', 'map'],
    ['orange', 'fruit'],
    ['cat', 'animal'],
    [true, 'false']
]);
console.log(m.has(true));
console.log(m.has('true'));
```
![[Pasted image 20230414132521.png]]

## delete
通过键，来删除 Map 中的成员
```js
const m = new Map([
    ['val', 'map'],
    ['orange', 'fruit'],
    ['cat', 'animal'],
    [true, 'false']
]);
m.delete('cat');
// 删除不存在的成员，将什么也不会发生，也不会报错
m.delete('true');
console.log(m);
```
![[Pasted image 20230414132612.png]]

## clear
删除 Map 的所有成员
```js
const m = new Map([
    ['val', 'map'],
    ['orange', 'fruit'],
    ['cat', 'animal'],
    [true, 'false']
]);
m.clear();
console.log(m);
```
![[Pasted image 20230414132650.png]]

## forEach
用来遍历 Map 的成员

它有两个参数，第一个参数为回调函数，第二个参数设定回调函数中this指向什么，即
**先来看第一个参数**
```js
m.forEach(function(value, key, map){
	value 就是 Map 的值
	key 就是 Map 的键
	map 就是前面Map的本身，即这里 map === m
});
```

**通过一个例子理解一下：**
```js
const m = new Map([    ['val', 'map'],    ['orange', 'fruit'],    ['cat', 'animal'],    [true, 'false']]);m.forEach(function(value, key, map) {    console.log(value, key, map == m);});const m = new Map([
    ['val', 'map'],
    ['orange', 'fruit'],
    ['cat', 'animal'],
    [true, 'false']
]);

m.forEach(function(value, key, map) {
    console.log(value, key, map == m);
});
```
![[Pasted image 20230414132749.png]]

**再来看第二个参数**
```js
const m = new Map([
    ['val', 'map'],
    ['orange', 'fruit'],
    ['cat', 'animal'],
    [true, 'false']
]);

m.forEach(function(value, key, map) {
    console.log(this);
}, document);
const m = new Map([
    ['val', 'map'],
    ['orange', 'fruit'],
    ['cat', 'animal'],
    [true, 'false']
]);

m.forEach(function(value, key, map) {
    console.log(this);
}, document);
```
![[Pasted image 20230414132816.png]]

# Map的注意事项
Map 对键名是否相同的判断基本遵循严格相等`===`的判断

不过对于`NaN`，在 `Set` 中，`NaN` 等于 `NaN`

# Map的使用场景
-   只需要键值对的结构时，即 key => value 的结构
-   需要字符串以外的键或者值


举个例子来看看 Map 的应用：
对`DOM`元素进行操作
先写一个 HTML 代码

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Map</title>
</head>
<body>
    <p>one</p>
    <p>two</p>
    <p>three</p>
</body>
</html>
```

**此时效果是这样的：**
![[Pasted image 20230414133002.png]]

然后对`p`元素进行修改：
```js
<script>
    // 利用数组解构赋值将 p 元素获取的同时解构出来
    const [p1, p2, p3] = document.querySelectorAll('p');
    const m = new Map([
        [p1, new Map([
            ['color', 'blue'],
            ['fontSize', '40px']
        ])], 
        [p2,  new Map([
            ['color', 'orange'],
            ['fontSize', '40px']
        ])], 
        [p3,  new Map([
            ['color', 'green'],
            ['fontSize', '40px']
        ])]
    ]);

    m.forEach((propMap, elem) => {
        propMap.forEach((value, prop) => {
            elem.style[prop] = value;
        });
    });
</script>
```
![[Pasted image 20230414133032.png]]