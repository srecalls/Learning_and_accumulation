`WeakMap`、`WeakSet` 和 `WeakRef` 都是 JavaScript 的内置对象，它们提供了一些特殊的功能，主要是用于处理对象的引用和垃圾回收。

1. `WeakMap`

`WeakMap` 是一种弱引用的数据结构，它可以存储键值对。与 `Map` 不同的是，`WeakMap` 中的键是弱引用的，这意味着如果键没有被其他对象引用，那么它将被垃圾回收。因此，`WeakMap` 中的键必须是对象，而值可以是任意类型。

使用 `WeakMap` 的主要场景是在需要存储一些与对象相关联的元数据时，可以将对象作为键存储元数据，这样当对象被垃圾回收时，元数据也会被自动清除，避免出现内存泄漏问题。

2. `WeakSet`

`WeakSet` 是一种弱引用的集合数据结构，它可以存储一组唯一的对象。与 `Set` 不同的是，`WeakSet` 中的元素是弱引用的，当元素没有被其他对象引用时，它将被垃圾回收。因此，`WeakSet` 中的元素必须是对象。

使用 `WeakSet` 的主要场景是在需要存储一组相关联的对象时，可以将对象存储到 `WeakSet` 中，这样当对象不再被其他对象引用时，它将被自动清除，避免出现内存泄漏问题。

3. `WeakRef`

`WeakRef` 是一种弱引用的对象，它可以引用任何 JavaScript 对象，但不会阻止垃圾回收器回收对象。它提供了一种轻量级的垃圾回收机制，可以通过 `deref()` 方法获取被引用对象的强引用，如果对象已经被回收，则返回 `undefined`。

使用 `WeakRef` 的主要场景是在需要通过引用来跟踪一些对象的生命周期时，可以使用 `WeakRef` 来创建一个弱引用，这样当对象被垃圾回收时，弱引用也会被自动清除，避免出现内存泄漏问题。

需要注意的是，`WeakMap`、`WeakSet` 和 `WeakRef` 都是弱引用的数据结构，因此在使用它们时需要注意引用关系，避免对象被提前清除导致程序出现错误。此外，`WeakMap`、`WeakSet` 和 `WeakRef` 都是相对较新的 JavaScript 特性，需要在支持这些特性的浏览器或者 Node.js 版本中使用。

## 例子
下面是一些使用 `WeakMap`、`WeakSet` 和 `WeakRef` 的示例：

1. `WeakMap` 示例：

```js
// 创建一个 WeakMap 对象
const wm = new WeakMap();

// 创建一个对象作为键
const key = {};

// 向 WeakMap 中添加键值对
wm.set(key, 'value');

// 从 WeakMap 中获取值
console.log(wm.get(key)); // "value"

// 销毁对象
key = null;

// 再次获取值
console.log(wm.get(key)); // undefined
```

在上面的例子中，我们使用 `WeakMap` 存储了一个对象和一个字符串的键值对。当对象被销毁后，`WeakMap` 中的键也会被自动清除，从而避免出现内存泄漏问题。

2. `WeakSet` 示例：

```js
// 创建一个 WeakSet 对象
const ws = new WeakSet();

// 创建一个对象
const obj = {};

// 向 WeakSet 中添加对象
ws.add(obj);

// 检查 WeakSet 中是否包含对象
console.log(ws.has(obj)); // true

// 销毁对象
obj = null;

// 再次检查 WeakSet 中是否包含对象
console.log(ws.has(obj)); // false
```

在上面的例子中，我们使用 `WeakSet` 存储了一个对象。当对象被销毁后，`WeakSet` 中的元素也会被自动清除，从而避免出现内存泄漏问题。

3. `WeakRef` 示例：

```js
// 创建一个对象
const obj = {};

// 创建一个 WeakRef 对象
const ref = new WeakRef(obj);

// 获取被引用对象的强引用
const strongRef = ref.deref();

// 检查被引用对象是否存在
console.log(strongRef === obj); // true

// 销毁对象
obj = null;

// 再次获取被引用对象的强引用
const newStrongRef = ref.deref();

// 检查被引用对象是否存在
console.log(newStrongRef === obj); // false
```

在上面的例子中，我们使用 `WeakRef` 创建了一个弱引用对象，然后使用 `deref()` 方法获取被引用对象的强引用。当对象被销毁后，`deref()` 方法返回 `undefined`，从而避免出现内存泄漏问题。