![[Pasted image 20230306104957.png]]
![[Pasted image 20230306105359.png]]

![[Pasted image 20230306142348.png]]
![[Pasted image 20230306142816.png]]
![[Pasted image 20230306143025.png]]


在 JavaScript 中，`Symbol()` 和 `Symbol.for()` 都可以用来创建符号（Symbol）类型的值，但它们之间有一些区别。

`Symbol()` 创建的符号是本地符号，它们在每个调用 `Symbol()` 的地方都是唯一的，即使它们的描述符相同。

```javascript
const s1 = Symbol('foo');
const s2 = Symbol('foo');

console.log(s1 === s2); // false
```

在上面的例子中，虽然 `s1` 和 `s2` 的描述符都是 "foo"，但它们是两个不同的符号，因此它们不相等。

另一方面，`Symbol.for()` 创建的符号是全局符号，它们被注册在一个全局符号注册表中，并且可以在不同的上下文中共享。

```javascript
const s1 = Symbol.for('foo');
const s2 = Symbol.for('foo');

console.log(s1 === s2); // true
```

在上面的例子中，尽管 `s1` 和 `s2` 是在不同的位置创建的，它们的描述符相同并且都是 "foo"，但是它们指向了同一个全局符号，因此它们是相等的。

使用 `Symbol.for()` 创建的符号，可以通过 `Symbol.keyFor()` 方法获取它们的描述符。如果一个符号是通过 `Symbol()` 创建的，则无法通过 `Symbol.keyFor()` 方法获取它的描述符。

```javascript
const s1 = Symbol.for('foo');
console.log(Symbol.keyFor(s1)); // "foo"

const s2 = Symbol('bar');
console.log(Symbol.keyFor(s2)); // undefined
```

需要注意的是，全局符号注册表是全局共享的，因此在不同的上下文中创建相同描述符的全局符号将指向同一个符号。这可能会导致意外的行为和错误，因此在使用 `Symbol.for()` 时需要小心。