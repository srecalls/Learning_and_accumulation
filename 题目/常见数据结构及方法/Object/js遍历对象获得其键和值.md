## 实例代码
在 JavaScript 中，可以使用 for...in 循环来遍历一个对象，并获取对象的键和对应的值。示例如下：

```js
const myObject = { a: 1, b: 2, c: 3 };

for (const key in myObject) {
  if (myObject.hasOwnProperty(key)) {
    const value = myObject[key];
    console.log(key, value);
  }
}
```


## 加判断条件的原因
在 JavaScript 中，对象有两种类型的属性：自有属性和继承属性。自有属性是直接在对象上定义的属性，而继承属性是从对象的原型链上继承而来的属性。

当使用 `for...in` 循环遍历一个对象时，除了遍历对象自身定义的属性外，还会遍历对象原型链上继承而来的属性。如果不加判断，可能会将原型链上的属性也一并遍历，从而导致意外的结果。

因此，在遍历对象属性时，建议使用 `hasOwnProperty` 方法来判断属性是否为对象自身的属性，以避免遍历到原型链上的属性。

在循环内部，key 变量将存储当前键的值，value 变量将存储当前值的值。需要注意的是，由于 for...in 循环会遍历对象的原型链，因此需要使用 hasOwnProperty 方法来判断对象是否具有该属性。

## 例子
可以通过以下示例来说明：

```javascript
// 定义一个对象和一个构造函数
const protoObj = { a: 1 };
function CustomObj() {
  this.b = 2;
}

// 将 CustomObj 的原型设置为 protoObj
CustomObj.prototype = protoObj;

// 创建一个 CustomObj 的实例
const myObj = new CustomObj();

// 使用 for...in 循环遍历 myObj 的属性
for (const key in myObj) {
  console.log(key);
}

// b
// a
```

以上代码创建了一个 `CustomObj` 的实例 `myObj`，并将 `CustomObj.prototype` 设置为 `{ a: 1 }`。在 `for...in` 循环中遍历 `myObj` 的属性时，会遍历到 `b` 属性和从原型链上继承而来的 `a` 属性。因此，如果不加判断，会输出两个属性名：`a` 和 `b`。如果加上判断，只会输出一个属性名：`b`。

```javascript
// 使用 for...in 循环和 hasOwnProperty 方法遍历 myObj 的属性
for (const key in myObj) {
  if (myObj.hasOwnProperty(key)) {
    console.log(key);
  }
}

// b
```

在这个例子中，`hasOwnProperty` 方法可以用来判断属性是否为 `myObj` 自身的属性，从而避免遍历到原型链上的属性。

## 错误用法
对于 `for...in` 循环，可以遍历对象的键，但不能直接访问对象的值。因此，不能在 `for...in` 循环中使用解构语法来同时获取键和值，如下所示：

```javascript
// 错误的示例：使用解构语法获取键和值
for (const [key, value] in myObj) {
  console.log(key, value);
}
```

如果想要访问对象的值，可以在循环体内使用键来获取值。示例如下：

```javascript
// 正确的示例：使用键来获取值
for (const key in myObj) {
  const value = myObj[key];
  console.log(key, value);
}
```

在循环内部，通过 `myObj[key]` 的方式可以获取对象的值。这里的 `key` 是一个变量，表示对象的键。因此，可以根据键来获取相应的值，并将键和值一起打印出来。

## 无法直接解构赋值的原因
在 JavaScript 中，解构赋值语法本质上是在对数组或对象进行解构操作，而 `for...in` 循环遍历的是对象的键。因此，如果想要使用解构赋值来同时获取对象的键和值，需要先将对象转换为一个包含 `[key, value]` 对的数组。

可以使用 `Object.entries()` 方法将对象转换为一个包含 `[key, value]` 对的数组，然后使用解构赋值语法来获取键和值。示例如下：

```javascript
const myObj = { a: 1, b: 2, c: 3 };

for (const [key, value] of Object.entries(myObj)) {
  console.log(key, value);
}
```

在这个例子中，`Object.entries()` 方法将 `myObj` 转换为一个数组，其中每个元素都是一个包含 `[key, value]` 对的数组。然后使用 `for...of` 循环遍历这个数组，并使用解构赋值语法将数组元素解构为 `key` 和 `value` 两个变量。这样就可以方便地获取对象的键和值了。

## 简便方法
在 JavaScript 中，可以使用 `Object.entries()` 方法将对象转换为一个包含 `[key, value]` 对的数组。然后可以使用 `for...of` 循环来遍历这个数组。在循环体内，第一个元素是键，第二个元素是值。示例如下：

```javascript
const myObj = { a: 1, b: 2, c: 3 };

for (const [key, value] of Object.entries(myObj)) {
  console.log(key, value);
}
[['a', 1], ['b', 2], ['c', 3]]
```
![[js遍历对象获得其键和值-1.png]]

在这个例子中，`Object.entries()` 方法将 `myObj` 转换为一个数组，其中每个元素都是一个包含 `[key, value]` 对的数组。然后使用 `for...of` 循环遍历这个数组，同时使用解构语法将数组元素解构为 `key` 和 `value` 两个变量。这样就可以方便地获取对象的键和值了。

需要注意的是，`Object.entries()` 方法是在 ES2017（ECMAScript 8）中引入的，因此在一些较老的浏览器中可能不支持。如果需要兼容旧版本浏览器，可以使用其他方式来遍历对象的键和值。

## for of + 解构
在 for...of 循环中，使用的是迭代器协议（Iterator Protocol），而不是解构赋值语法。迭代器协议是一种约定，用于指定一个对象应该如何进行迭代访问。具体来说，一个实现了迭代器协议的对象必须包含一个 next() 方法，该方法返回一个包含 value 和 done 两个属性的对象。在 for...of 循环中，会重复调用这个 next() 方法，直到 done 属性为 true 为止。

虽然 for...of 循环**本身并不使用解构赋值语法**，但是**可以结合解构赋值语法**来获取迭代器返回的值。示例如下：

```javascript
const myArray = [1, 2, 3];

for (const [index, value] of myArray.entries()) {
  console.log(index, value);
}
```
在这个例子中，使用 myArray.entries() 方法获取一个包含 `[index, value]` 对的迭代器。然后在 for...of 循环中使用解构赋值语法将迭代器返回的元素解构为 index 和 value 两个变量。这样就可以方便地获取数组的下标和元素值了。需要注意的是，entries() 方法是在 ES2015（ECMAScript 6）中引入的，因此在一些较老的浏览器中可能不支持。