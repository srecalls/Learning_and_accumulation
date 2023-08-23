生成器（Generator）是 JavaScript 中的一种特殊函数，它可以在函数执行过程中暂停和恢复。生成器提供了一种更灵活的迭代器模型，能够按需生成序列化的值，而不是一次性生成所有值。

生成器函数使用`function*`语法进行定义，并使用`yield`关键字来指示暂停点。当调用生成器函数时，它并不立即执行，而是返回一个称为生成器对象的迭代器。通过调用生成器对象的`next()`方法，可以依次获取生成器函数中`yield`语句返回的值，并在每次调用后暂停生成器的执行，直到下一次调用`next()`。

下面是一个简单的生成器函数的示例：

```javascript
function* numberGenerator() {
  console.log(0)
  yield 1;
  yield 2;
  yield 3;
  console.log(4)
}

const generator = numberGenerator();

console.log(generator.next()); // 1 { value: 1, done: false }
console.log(generator.next()); // { value: 2, done: false }
console.log(generator.next()); // { value: 3, done: false }
console.log(generator.next()); // 4 { value: undefined, done: true }
```

在上面的示例中，我们定义了一个名为`numberGenerator`的生成器函数，它通过`yield`语句依次返回数字1、2和3。通过调用`numberGenerator()`创建了一个生成器对象`generator`。然后，我们通过连续调用`generator.next()`来逐步获取生成器函数中的值。每次调用`next()`都会返回一个包含`value`和`done`属性的对象。`value`表示生成器函数中`yield`语句返回的值，而`done`表示生成器是否已经执行完毕。

除了`yield`语句，生成器函数还可以使用`return`语句来结束生成器的执行。

```javascript
function* numberGenerator() {
  yield 1;
  yield 2;
  return 3;
  yield 4; // 这个语句永远不会执行
}

const generator = numberGenerator();

console.log(generator.next()); // { value: 1, done: false }
console.log(generator.next()); // { value: 2, done: false }
console.log(generator.next()); // { value: 3, done: true }
console.log(generator.next()); // { value: undefined, done: true }
```

在上面的示例中，我们在生成器函数的最后使用了`return`语句来指定生成器的返回值。在调用`next()`时，`done`属性将变为`true`，并且`value`属性将是`return`语句指定的值。

生成器还支持通过`yield*`语句委托给其他生成器或可迭代对象。

```javascript
function* numberGenerator1() {
  yield 1;
  yield 2;
}

function* numberGenerator2() {
  yield* numberGenerator1();
  yield 3;
}

const generator = numberGenerator2();

console.log(generator.next()); // { value: 1, done: false }
console.log(generator.next()); // { value: 2, done: false }
console.log(generator.next()); // { value: 3, done: false }
console.log(generator.next()); // { value: undefined, done: true }
```

在上面的示例中，我们定义了两个生成器函数`numberGenerator1`和`numberGenerator2`。`numberGenerator2`通过使用`yield*`语句委托给了`numberGenerator1`生成器函数，从而实现了两个生成器函数的连续迭代。

生成器的主要优势在于它们可以生成一个序列化的值，而不需要将所有值一次性计算出来。这对于处理大量数据、按需加载或遍历无限序列等情况非常有用。

总结：

- 生成器是一种特殊函数，可以在执行过程中暂停和恢复。
- 使用`function*`语法定义生成器函数，使用`yield`关键字指示暂停点。
- 生成器函数返回一个生成器对象，通过调用`next()`方法逐步获取生成器函数中的值。
  -生成器函数可以使用`yield`语句返回一个值，并在每次调用`next()`时暂停函数执行，然后再次从暂停的位置继续执行。通过这种方式，我们可以按需生成序列化的值，而不是一次性生成所有值。

以下是一个更详细的示例，展示生成器函数的更多用法：

```javascript
function* fibonacciGenerator() {
  let prev = 0;
  let curr = 1;

  while (true) {
    // 使用yield语句返回当前斐波那契数，并暂停执行
    yield curr;

    // 计算下一个斐波那契数
    const next = prev + curr;
    prev = curr;
    curr = next;
  }
}

const generator = fibonacciGenerator();

console.log(generator.next().value); // 1
console.log(generator.next().value); // 1
console.log(generator.next().value); // 2
console.log(generator.next().value); // 3
console.log(generator.next().value); // 5
// ...

// 使用生成器函数可以方便地生成斐波那契数列
for (let i = 0; i < 10; i++) {
  console.log(generator.next().value);
}
```

在上面的示例中，我们定义了一个斐波那契数列的生成器函数`fibonacciGenerator`。它使用一个无限循环来计算下一个斐波那契数，并使用`yield`语句返回当前斐波那契数，然后暂停执行。通过调用`generator.next().value`，我们可以逐步获取斐波那契数列中的值。

生成器函数非常适合处理需要按需生成值的场景，尤其是在处理大量数据或需要延迟计算的情况下。生成器可以减少内存占用，并提供更灵活的控制流程。

需要注意的是，生成器函数返回的生成器对象符合可迭代协议，因此可以使用`for...of`循环或使用扩展运算符来遍历生成器生成的序列。

```javascript
function* numberGenerator() {
  yield 1;
  yield 2;
  yield 3;
}

const generator = numberGenerator();

for (const num of generator) {
  console.log(num);
}
// 输出：1 2 3

const numbers = [...numberGenerator()];
console.log(numbers); // [1, 2, 3]
```

在上面的示例中，我们使用`for...of`循环和扩展运算符来遍历生成器函数生成的序列。

生成器是 JavaScript 中强大而灵活的工具，它们提供了一种按需生成值的机制，可以简化代码并提高性能。


![[Pasted image 20230306212940.png]]
![[Pasted image 20230306213012.png]]
挂起：就是函数执行停留在那个位置
![[Pasted image 20230306213423.png]]

## 演示
![[Pasted image 20230306213613.png]]
![[Pasted image 20230306213629.png]]

![[Pasted image 20230306213812.png]]
![[Pasted image 20230306213840.png]]
![[Pasted image 20230306214502.png]]
![[Pasted image 20230306214620.png]]
![[Pasted image 20230306214701.png]]
![[Pasted image 20230306214817.png]]


# 使用场景
![[Pasted image 20230306215247.png]]

![[Pasted image 20230306215424.png]]
为obj的Symbol.iterator赋值迭代器
![[Pasted image 20230306215346.png]]
![[Pasted image 20230306215713.png]]