## 运算符新增

### 数字分隔符(Numeric Separators)

数字分隔符，可以在数字之间创建可视化分隔符，通过_下划线来分割数字，使数字更具可读性。

```
const oneMillion = 1000000;

// 数据分隔符
const oneMillion = 1_000_000;
```

该新特性支持在**二进制、八进制和十六进制**中使用

```
const max8bits = 0b1111_1111;
const message = 0xA0_B0_C0;
```

该特性使用十分简单，却可以有效的提高代码的阅读性。

### 逻辑赋值运算符(Logical Assignment Operators)

目前已有的复合赋值运算符：

- 操作运算符：+= -= _= /= %=_ *=
- 位操作运算符：&= ^= |=
- 按位运算符：<<= >>= >>>=

ES12新增了三种复合赋值运算符：

- 逻辑空赋值`(??=) -> (x ??= y)` （仅在 x 为null或undefined时赋值）
- 逻辑与赋值`(&&=) -> (x &&=y)`（仅在 x 为真时赋值）
- 逻辑或赋值`(||=) -> (x ||=y )`（仅在 x 为假时赋值）

```
a ||= b; 
// 等同于 
a || (a = b); a = a || b;

a &&= b; 
// 等同于 
a && (a = b); 

a ??= b; 
// 等同于 
a ?? (a = b); a = a ?? b;
```

## API新增

### replaceAll

String 原型中添加了一个新函数。replaceAll返回一个全新的字符串，所有符合匹配规则的字符都将被替换掉，替换规则可以是字符串或者正则表达式。

```
let string = 'I love 前端,I love coding';

//使用replace
let replaceStr = string.replace('love','hate');
console.log(replaceStr)  // 'I hate 前端,I love coding'

//replace使用正则匹配所有
console.log(string.replace(/love/g,'hate')) // 'I hate 前端,I hate coding'

//使用replaceAll
let replaceAllStr = string.replaceAll('love','hate')
console.log(replaceAllStr) // 'I hate 前端,I hate coding'
```

### Promise.any

当Promise列表中的任意一个promise成功resolve则返回第一个resolve的结果状态 如果所有的promise均reject，则会抛出一种新类型的异常`AggregateError`。

```
Promise.any([
    Promise.reject('Error 1'),
    Promise.reject('Error 2'),
    Promise.resolve('success'),
]).then((result) => {
    console.log('result:', result);
});
// 输出result: success


Promise.any([
  Promise.reject('Error 1'),
  Promise.reject('Error 2'),
  Promise.reject('Error 3')
])
.then(value => console.log(`请求结果: ${value}`))
.catch (err => console.log(err))
//输出AggregateError: All promises were rejected
```

这是对Promise原型的第四次添加，回顾一下之前的API：

- **[ES2020] Promise.allSettled**: This method returns a promise that resolves when all the given promises have either been fulfilled or rejected. The returned object describes each individual promise result.

```
const delay = n => new Promise(resolve => setTimeout(resolve, n)); 
const promises = [
  delay(100).then(() => 1),
  delay(200).then(() => 2),
  Promise.reject(3)
  ]

Promise.allSettled(promises).then(values=>console.log(values))
// 最终输出： 
//    [
//      {status: "fulfilled", value: 1},
//      {status: "fulfilled", value: 2},
//      {status: "rejected", value: 3},
//    ]
```

- **[ES2015] Promise.all**: This method returns a promise that is fulfilled only if all the target promises were fulfilled.

```

const promises = [
  delay(100).then(() => 1),
  delay(200).then(() => 2),
  ]
Promise.all(promises).then(values=>console.log(values))// 最终输出： [1, 2]

// 如果有返回reject
const promises = [
  delay(100).then(() => 1),
  delay(200).then(() => 2),
  Promise.reject(3)
  ]
Promise.all(promises)
.then(values=>console.log(values))
.catch(err=>console.log(err))// 加入catch语句后，最终输出：3
```

- **[ES2015] Promise.race**: This method will return a promise that will be fulfilled as soon as one of the promises is either rejected or fulfilled.

```
const promises = [
  delay(100).then(() => 1),
  Promise.reject(2)
  ]
  Promise.race(promises)
  .then(values => console.log('success: ', values))
  .catch(err => console.log('err: ', err))
```

### 弱引用(WeakRefs)

[WeakRef-MDN Web Docs](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/WeakRef)

WeakRef 对象允许您保留对另一个对象的弱引用，而不会阻止被弱引用对象被 GC 回收。

对于 WeakRef 对象的使用要慎重考虑，**能不使用就尽量不要使用**

```
function Foo() {}

// strong reference to a Foo instance 
const x = new Foo(); 

// weak reference to the Foo's instance 
const xWeak = new WeakRef(x); 

// strong reference to the Foo's instance 
const xFromWeak = xWeak.deref();
```

### FinalizationRegistry

FinalizationRegistry 注册 Callback，某个对象被 GC 回收后调用。此功能的作用是让您知道对象何时被垃圾收集。但是，需要牢记几点：

- 不保证回调会执行。
- 目标对象已经被清理，将无法访问。
- 回调将执行多长时间是不确定的。它可以是一分钟或一小时。

```
let x = new Array(1000).fill(true);

// constructing the finalizer method
const cleanup = new FinalizationRegistry(key => {
  console.log('key: ', key);
});

// hooking the x variable to the finalizer
cleanup.register(x, 'fsdfs');

// object 'x' is now unreachable, finalizer callback might happen after
// object has been garbage collected
x = null;

// 输出：key: fsddfs
```

此功能使您有机会进行进一步的清理以帮助优化您的应用程序。

关联文档：

[ECMAScript® 2020(ES11) 新特性介绍](https://xiaomi.f.mioffice.cn/docs/dock4uipI0teVUhuFo9J0a9n7zc)

[垃圾回收](https://xiaomi.f.mioffice.cn/docs/dock4bTdvESTo1XSd15g1kqzyob)