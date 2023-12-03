# 介绍
ECMAScript6 新增的 Set 是一种新集合类型，为这门语言带来集合数据结构。Set 在很多方面都像是加强的 Map，这是因为它们的大多数 API 和行为都是共有的。

# 基本API
## 1.创建Set实例
使用 new 关键字和 Set 构造函数可以创建一个空集合：
```js
const s = new Set();
```
如果想在创建的同时初始化实例，则可以给 Set 构造函数传入一个可迭代对象，其中需要包含插入到新集合实例中的元素**Set 可以包含任何 JavaScript 数据类型作为值：**
```js
const s = new Set(["val1", 1, true, {}, undefined, function fun() {}]);
```
**注意**Set结构不会添加重复的值
```js
const s = new Set([1, 1, 2, 3, 4, 4, 5, 6, 7, 4, 2, 1]);
Array.from(s); //  [1, 2, 3, 4, 5, 6, 7]


Set(3) { [ -1, 0, 1 ], [ -1, -1, 2 ], [ -1, 0, 1 ] }
```

## 2.Set实例转数组
```js
const s = new Set([1, 2, 3]);
Array.from(s); // [1, 2, 3]
```

## 3.size属性
size: 获取Set实例的元素个数：
```js
const s = new Set([1, 2, 3]);
s.size; // 3
```

## 4.add()
add(): 添加元素：
```js
const s = new Set();
s.add(1).add(2).add(3);
Array.from(s); // [1, 2, 3]
```

## 5.has()
has(): 查询Set实例是否存在某元素(返回布尔值)：
```js
const s = new Set();
s.add(1).add(2).add(3);
s.has(1); // true
```

## 6.delete()
delete(): 删除Set实例中某个元素(返回布尔值)：
```js
const s = new Set();
s.add(1).add(2);
s.delete(1);
Array.from(s); // [2]
```

## 7.clear()
clear(): 清空Set实例：
```js
const s = new Set();
s.add(1).add(2).add(3);
Array.from(s); // [1, 2, 3]
s.clear();
Array.from(s); // []
```

## 8.迭代
keys():返回键名;  
values(): 返回键值；  
entries(): 返回键值对;
**键名=键值**
```js
const s = new Set();
s.add(1).add(2).add(3);
Array.from(s.keys()); // [1, 2, 3]
Array.from(s.values()); // [1, 2, 3]
Array.from(s.entries()); // [[1, 1], [2, 2], [3, 3]]
```

## for-of：
```js
const s = new Set();
s.add(1).add(2).add(3);
for (const i of s) {
	console.log(i);
}
// 1
// 2
// 3
```

## forEach
```js
const s = new Set();
s.add(1).add(2).add(3);
s.forEach((value, key) => console.log(key + ' : ' + value));
// 1 : 1
// 2 : 2
// 3 : 3
```