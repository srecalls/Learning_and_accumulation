[[JavaScript Object对象常用方法和属性]]
[[对原型、原型链的理解]]
[[1.new操作符的实现原理]]
## 思路：将传入的对象作为原型
```js




function create(obj) {
	function F() {}
	F.prototype = obj
	return new F()
}
```

当使用 `new` 关键字调用构造函数创建一个对象时，该对象的 `__proto__` 属性会指向构造函数的 `prototype` 属性。因此，在使用 `new` 关键字创建一个对象之后，该对象才会有 `__proto__` 属性，并且指向构造函数的 `prototype` 属性。



手动实现 `Object.create()` 的核心在于创建一个新对象，并将指定对象作为这个新对象的原型。




由于在ES5之前没有直接设置对象原型的方法（除了非标准的 `__proto__`），我们通常利用一个**空构造函数**来实现这一目标。

### 手写 `Object.create()`

我们将实现的函数命名为 `myObjectCreate`：

JavaScript

```js
/**
 * 模拟 Object.create() 的行为
 * @param {object | null} proto 要作为新对象原型的对象。
 * @param {object} [propertiesObject] 可选，包含属性描述符的对象。
 * @returns {object} 一个新对象，其原型为指定的 proto。
 */
function myObjectCreate(proto, propertiesObject) {
    // 1. 参数校验
    if (typeof proto !== 'object' && typeof proto !== 'function' && proto !== null) {
        // Object.create如果传入非null/非对象会抛出TypeError
        throw new TypeError('Object prototype may only be an Object or null.');
    }

    // 2. 创建一个临时构造函数
    // 这是一个关键步骤，因为函数的 prototype 属性天然就是所有实例的原型
    function F() {}

    // 3. 设置原型链
    // 将空函数的 prototype 设置为指定的 proto 对象
    F.prototype = proto;

    // 4. 创建新对象
    // 通过 new F() 创建的实例，它的 __proto__ 就会指向 F.prototype，
    // 也就是我们传入的 proto 对象。
    const newObject = new F();

    // 5. 处理纯净对象的情况
    // 如果传入的是 null，则 new F() 创建的对象会有一个默认的 Object.prototype，
    // 但根据 Object.create 的规范，传入 null 应该返回一个 __proto__ 为 null 的对象。
    // 在现代 JS 环境中，new F() 的 __proto__ 确实是 F.prototype，所以如果 proto 为 null，newObject 的 __proto__ 就是 null。
    // 但为了确保兼容性，如果 proto 为 null，我们确保 newObject 的原型是 null。
    if (proto === null) {
        // 由于 F.prototype = null 仍会创建一个继承自 Object.prototype 的对象
        // 这一步在某些老环境中可能需要特殊处理，但我们依赖 new F() 继承 F.prototype 的行为。
        // 在现代浏览器中，如果 F.prototype = null，new F() 仍可能继承 Object.prototype。
        // 最安全的做法是：
        // if (proto === null) {
        //     // 无法通过构造函数方式创建 __proto__ 为 null 的对象，需要依赖 Object.setPrototypeOf 或 __proto__
        //     // 为了手写实现，我们简化逻辑，忽略第二个参数，并假设浏览器支持 new F() 继承 F.prototype
        // }
    }


    // 6. 处理可选的 propertiesObject 参数
    if (propertiesObject !== undefined) {
        // 如果提供了属性描述符对象，则使用 Object.defineProperties() 将属性添加到新对象上
        Object.defineProperties(newObject, propertiesObject);
    }

    return newObject;
}
```

### 示例验证

JavaScript

```
const parent = {
    x: 1,
    sayX: function() {
        console.log(this.x);
    }
};

const child = myObjectCreate(parent, {
    y: {
        value: 2,
        writable: true,
        enumerable: true
    }
});

console.log(child.x);        // 输出: 1 (继承自原型)
child.sayX();                // 输出: 1 (继承自原型)
console.log(child.y);        // 输出: 2 (自有属性)
console.log(Object.getPrototypeOf(child) === parent); // 输出: true (原型设置成功)
```

#### 关键实现思路：借用构造函数

这个手写实现的关键在于使用一个空函数 `F`：

1. 将 `F.prototype` 设为 `proto`。
    
2. 通过 `new F()` 创建实例 `newObject`。
    
3. 根据原型链原理，`newObject.__proto__` 自动等于 `F.prototype`，也就是我们指定的 `proto`。
    

这个方法是ES5之前模拟 `Object.create` 最标准的方式。

您是否希望我展示如何处理传入 `null` 的特殊情况（即创建一个真正的纯净对象）？


## 例子1
```js
var obj = {
	a: 1
}

function create(obj) {
	function F() {}
	F.prototype = obj
	return new F()
}
console.log('obj', obj)
console.log('obj.__proto__', obj.__proto__)
console.log('obj.__proto__.constructor', obj.__proto__.constructor)
let b = create(obj)

console.log('b', b)
console.log('b.__proto__', b.__proto__)
console.log('b.__proto__.constructor', b.__proto__.constructor)
```
![[Pasted image 20230628213736.png]]

在你的代码中，`create` 函数接受一个 `obj` 参数，然后创建一个新的函数 `F`，并将 `F.prototype` 属性设置为 `obj`，最后返回通过 `new F()` 创建的新对象。由于 `F.prototype` 属性被设置为 `obj`，因此新对象的原型链会指向 `obj`。

在这个过程中，确实会出现 `F.prototype` 的 `constructor` 属性被覆盖的情况。因为 `F.prototype` 被替换成了一个新的对象 `obj`，而这个新对象并没有 `constructor` 属性。因此，如果通过 `b.constructor` 来获取这个新对象的构造函数，会返回 undefined。


根据你提供的代码，假设你使用 `create` 函数创建了一个新对象 `b`，并将其原型链指向了 `obj` 对象，**那么 `b` 对象本身是一个空对象，没有自己的属性和方法。**

但是，由于 `b` 对象的原型链指向了 `obj` 对象，因此可以通过原型链来访问 `obj` 对象的属性和方法。例如，如果 `obj` 对象有一个属性 `prop`，那么可以通过 `b.prop` 来访问这个属性，也可以通过 `Object.getPrototypeOf(b).prop` 或 `b.__proto__.prop` 来访问原型对象 `obj` 上的属性。

以下是一个示例代码，展示了如何创建一个空对象，并通过原型链来访问原型对象的属性：

```
function create(obj) {
    function F() {}
    F.prototype = obj;
    return new F();
}

let obj = { prop: "value" };
let b = create(obj);
console.log(b); // 输出 {}
console.log(b.prop); // 输出 "value"
console.log(Object.getPrototypeOf(b).prop); // 输出 "value"
console.log(b.__proto__.prop); // 输出 "value"
```

在这个例子中，使用 `create` 函数创建了一个新对象 `b`，并将其原型链指向了 `obj` 对象。因为 `b` 对象本身没有属性，所以 `console.log(b)` 输出了一个空对象 `{}`。但是，通过 `console.log(b.prop)` 可以访问 `obj` 对象上的 `prop` 属性，输出了 `"value"`。同时，通过 `Object.getPrototypeOf(b).prop` 或 `b.__proto__.prop` 也可以访问原型对象 `obj` 上的属性。


## 例子2
```js
function create(obj) {
    function F() {}
    // F.prototype = obj   // 这里注释掉
    return new F()
}

let b = create(obj)

console.log(b)
console.log(b.__proto__)
console.log(b.__proto__.constructor)
```

![[Pasted image 20230621004507.png]]



## 说明：Object.create()
2. `Object.create()`方法创建一个新对象，使用现有对象来提供新创建对象的原型`__proto__`。
（即新对象的 `[[Prototype]]` 或 `__proto__`）。

```js
var obj = {
	a: 1
}
var o = Object.create(obj)
console.log(o)
console.log(o.__proto__)
```
![[Pasted image 20230620235733.png]]

```js
var obj = {
	a: 1
}
var o = Object.create(obj)
console.log(o)
```
![[Pasted image 20230531172505.png]]

如上图所示，使用现有对象`obj`，来提供新对象`o`的`__proto__`。

`Object.create()`方法接收两个参数，  
第二个参数可省略,具体可参考我总结的这篇文章[《JavaScript ES6数据类型》](https://www.jianshu.com/p/2206959c0019)

留个代码图，注意看o.p的值是不可修改的。
  
![[Pasted image 20230531172518.png]]
create第二个参数



好的，`Object.create()` 是一个非常重要的方法，用于创建新对象并设置其原型。

### `Object.create()` 的作用

`Object.create()` 方法用于创建一个新对象，使用现有对象作为新创建对象的**原型**（即新对象的 `[[Prototype]]` 或 `__proto__`）。

它的主要目的是提供一种简洁、标准化的方式来实现**原型式继承**（Prototypal Inheritance）。

---

### 语法和参数

JavaScript

```
Object.create(proto, propertiesObject)
```

#### 1. `proto` (必需参数)

- **定义：** 新创建对象的原型对象。
    
- **作用：** 这个参数会成为新创建对象的 `[[Prototype]]`。
    
    - **如果传入一个对象：** 新对象将继承该对象的所有属性和方法。
        
    - **如果传入 `null`：** 新对象将是一个“纯净”的对象，它不会继承 `Object.prototype` 上的任何属性（例如 `toString`、`hasOwnProperty` 等），它的原型链终点就是 `null`。
        

#### 2. `propertiesObject` (可选参数)

- **定义：** 一个包含一个或多个属性描述符（Property Descriptors）的对象。
    
- **作用：** 这些属性将添加到新创建的对象上，就像使用 `Object.defineProperties()` 一样。
    

---

### 示例解析

#### 1. 实现原型式继承（最常见用法）

使用一个对象作为新对象的原型：

JavaScript

```
const personPrototype = {
  sayGreeting: function() {
    console.log(`Hello, my name is ${this.name}.`);
  }
};

// 使用 personPrototype 作为 student 的原型
const student = Object.create(personPrototype);

student.name = 'Alice'; // 添加新对象的自有属性

student.sayGreeting(); // 输出: Hello, my name is Alice. (方法来自原型)

// 检查原型链关系
console.log(Object.getPrototypeOf(student) === personPrototype); // true
console.log(student.hasOwnProperty('sayGreeting')); // false (sayGreeting 在原型上)
```

在这个例子中，`student` 对象通过原型链继承了 `personPrototype` 上的 `sayGreeting` 方法。

#### 2. 创建“纯净”对象

传入 `null` 创建一个没有继承自 `Object.prototype` 的对象：

JavaScript

```
// 创建一个原型为 null 的对象
const pureObject = Object.create(null);

pureObject.x = 10;

console.log(pureObject.toString); // undefined
// 尝试调用继承自 Object.prototype 的方法会报错：
// pureObject.toString(); // ❌ TypeError: pureObject.toString is not a function

console.log(Object.getPrototypeOf(pureObject)); // null
```

这种对象在用作映射表（Map）时非常有用，可以避免键名（key）与 `Object.prototype` 上的默认属性（如 `constructor` 或 `toString`）发生冲突。

#### 3. 添加自有属性（使用第二个参数）

JavaScript

```
const basePrototype = { type: 'animal' };

const dog = Object.create(basePrototype, {
  // 定义自有属性 name
  name: {
    value: 'Buddy',
    writable: true,
    enumerable: true,
    configurable: true
  },
  // 定义一个 getter 属性
  species: {
    get: function() {
      return 'dog';
    },
    enumerable: true
  }
});

console.log(dog.name);    // 输出: Buddy
console.log(dog.type);    // 输出: animal (继承自原型)
console.log(dog.species); // 输出: dog
```

---

### 总结

Object.create 创建一个对象，并让 props成为 对象的原型

`Object.create()` 是一个强大的工具，它提供了对对象原型创建的**精细控制**：

- **继承**：它是实现原型链继承最直接的方式。
    
- **纯净对象**：能够创建不带任何继承属性的纯净对象，避免原型污染。
    

您对原型、原型链和 `Object.create()` 还有其他疑问吗？或者需要我介绍其他常用的前端概念？