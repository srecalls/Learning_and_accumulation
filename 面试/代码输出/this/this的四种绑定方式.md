`this` 是 JavaScript 中一个重要的关键字，它指向当前函数的执行上下文对象。`this` 的值在函数调用时动态确定，可以通过四种绑定规则来确定其值：默认绑定、隐式绑定、显示绑定和 `new` 绑定。

## 1. 默认绑定

当函数的调用方式没有明确指定 `this` 的值时，`this` 默认绑定到全局对象（在浏览器中通常是 `window` 对象）。例如：

```js
function foo() {
  console.log(this.a);
}

var a = 2;
foo();
// 输出 2
```

在这个例子中，函数 `foo()` 被默认调用，`this` 指向了全局对象，因此打印了全局变量 `a` 的值 `2`。

## 2. 隐式绑定

当函数作为对象的方法被调用时，`this` 绑定到该对象。例如：

```js
var obj = {
  a: 2,
  foo: function() {
    console.log(this.a);
  }
};

obj.foo();
// 输出 2
```

在这个例子中，函数 `foo()` 被作为对象 `obj` 的方法调用，`this` 指向了 `obj`，因此打印了 `obj.a` 的值 `2`。

但是需要注意的是，如果函数嵌套在另一个函数中，那么 `this` 的绑定会丢失。例如：

```js
var obj1 = {
  a: 2,
  foo: function() {
    console.log(this.a);
  }
};

var obj2 = {
  a: 3,
  bar: function() {
    setTimeout(obj1.foo, 100);
  }
};

obj2.bar(); // 输出 2
```

在这个例子中，函数 `foo()` 被作为 `setTimeout()` 的回调函数调用，此时 `this` 指向了全局对象，因此打印了全局变量 `a` 的值 `2`。

## 3. 显示绑定

可以使用 `call()` 或 `apply()` 方法来显式地绑定 `this` 的值。例如：

```js
function foo() {
  console.log(this.a);
}

var obj = {
  a: 2
};

foo.call(obj); // 输出 2
```

在这个例子中，函数 `foo()` 被显式地调用，并将 `this` 绑定到了对象 `obj` 上，因此打印了 `obj.a` 的值 `2`。

## 4. `new` 绑定
### 无返回值
当使用 `new` 关键字调用构造函数时，`this` 绑定到新创建的对象上。例如：

```js
function Foo(a) {
  this.a = a;
}

var obj = new Foo(2);
console.log(obj.a); // 输出 2
```

在这个例子中，函数 `Foo()` 被用作构造函数，并使用 `new` 关键字调用，`this` 绑定到了新创建的对象 `obj` 上，因此在 `Foo()` 函数中设置的属性 `a` 被赋值给了 `obj.a`，最终打印了 `obj.a` 的值 `2`。

###  有返回值
需要注意的是，在使用 `new` 关键字调用构造函数时，如果构造函数返回了一个对象，那么这个对象将会被返回，而不是新创建的对象。例如：

```js
function Foo(a) {
  this.a = a;
  return {b: 3};
}

var obj = new Foo(2);
console.log(obj.a); // undefined
console.log(obj.b); // 输出 3
```

在这个例子中，函数 `Foo()` 返回了一个新的对象 `{b: 3}`，因此 `obj` 实际上被赋值为这个新的对象，而不是通过 `new` 关键字创建的对象。因此，`obj.a` 的值为 `undefined`，而 `obj.b` 的值为 `3`。