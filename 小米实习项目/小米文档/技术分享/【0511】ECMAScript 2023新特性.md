1. # 从后往前寻找数组元素
    

https://github.com/tc39/proposal-array-find-from-last

`Array` and `TypedArray` 原型

- findLast()
    
- findLastIndex()
    

基本作用和find()及findIndex()一样，只是查询开始的位置和顺序不同

```JavaScript
const isEven = (number) => number % 2 === 0;
const numbers = [1, 2, 3, 4];
// from first to the last lookup
console.log(numbers.find(isEven));// 2
console.log(numbers.findIndex(isEven));// 1
// from last to the first lookup
console.log(numbers.findLast(isEven));// 4
console.log(numbers.findLastIndex(isEven));// 3
```

意义：

1. 语义化
    
2. 节省操作，提高性能
    

  

2. # 通过复制改变数组
    

https://github.com/tc39/proposal-change-array-by-copy

调用`reverse()`,`sort()` 和`splice()`时会改变原数组，新提案提出三个API，其功能和以上三个方法一致，只是其会返回一个复制数组，且变化将在这个复制数组上进行。

- toReversed()
    
- toSorted()
    
- toSpliced()
    

```JavaScript
const original = [1, 4];
const spliced = original.toSpliced(1, 0, 2, 3);

console.log(original);// [ 1, 4 ]
console.log(spliced);// [ 1, 2, 3, 4 ]
```

同时新增一个方法，可以将指定索引位置的元素替换成指定元素。修改也是只在复制数组上进行

- with(index,elem)
    

```JavaScript
const original = [1, 2, 2, 4];
const withThree = original.with(2, 3);

console.log(original);// [ 1, 2, 2, 4 ]
console.log(withThree);// [ 1, 2, 3, 4 ]
```

意义：

1. 调用方法时可以保证修改原数组的一致性。
    

  

3. # hashbang语法
    

https://github.com/tc39/proposal-hashbang

哈希邦（Hashbang）注释，类似于unix的shebang，可以用来指定执行JS脚本的解释器路径

只在shell环境下有意义，其余情况同普通注释

它以 `#!` 开头，并且**只在脚本或模块的最开始处**有效

- `#!` 标志之前不能有任何空白字符
    
- 注释由 `#!` 之后的所有字符组成直到第一行的末尾
    
- 只允许有一条这样的注释
    

```JavaScript
// node-hello.js
console.log('hello world');

运行： node ./node-hello.js

// hello.js
#!/usr/bin/env node
console.log('hello world');

运行： ./hello.js
```

意义：

1. 将hashbang语法正式纳入JavaScript，使其与其他语言更加一致
    
2. Hashbang语法的使用使脚本的执行变得更加方便和可移植，不需要每次都手动指定解释器程序
    

  

  

4. # symbols可以作为weakMap的键值
    

https://github.com/tc39/proposal-symbols-as-weakmap-keys

在现有规定中，weakMap的键值只能是**object** 类型，现在支持了 Symbol 类型作为 key

```JavaScript
const weak = new WeakMap();
const key = Symbol("ref");
weak.set(key, "ECMAScript 2023");
console.log(weak.get(key));// ECMAScript 2023
```

  

  

1. stage-0：还是一个设想，只能由TC39成员或TC39贡献者提出
    
2. stage-1：提案阶段，比较正式的提议，只能由TC39成员发起，这个提案要解决的问题必须有正式的书面描述。
    
3. stage-2：草案，有了初始规范，必须对功能语法和语义进行正式描述，包括一些实验性的实现。
    
4. stage-3：候选，该提议基本已经实现，需要等待实验验证，用户反馈及验收测试通过。
    
5. stage-4：已完成，必须通过 Test262 验收测试，下一步就纳入ECMA标准。
    

  

以上特性目前都处于stage4，将在2023年7月获得批准，变成ES新版本正式特性