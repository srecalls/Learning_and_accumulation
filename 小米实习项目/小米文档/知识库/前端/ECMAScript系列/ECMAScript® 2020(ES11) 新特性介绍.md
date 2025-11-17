

## 1、运算符类新增

### 1.1 Optional Chaining 可选链式调用(?.)

我们在开发过程中经常会遇到这样一个报错：_TypeError: Cannot read property 'lily' of undefined，_

这个错误表示我们正在访问一个不属于对象的属性。

```
const user = {
    info: {
        age: 20,
        name: 'Lily'
    }
};

var age = user.info.age;      // 正常运行
var name = user.address.adName；// 抛出错误：TypeError: Cannot read property 'name' of undefined
```

在这种情况下，JavaScript 引擎会像这样抛出错误，并会终止代码继续向下执行。

为了保证程序的正确运行，我们不得不做一些很繁琐但又必须做的前置校验操作：

```
var name = user && user.address && user.address.adName;
var age = user && user.info && user.info.getAge && user.info.getAge();
```

有了可选链式调用方式，我们就可以这样来处理上面的问题：

```
var name = user?.info?.name;
var age = user?.info?.getAge?.();
```

该语法会在进行取出的时候判定前面的值是否为 undefined 或者 null ，如果是，那么则返回undefine ,不会报错。用可选链式调用方式取值既可以大量简化类似繁琐的前置校验操作，又使程序执行更安全，不会被异常终止。

除了访问对象，当访问数组或调用函数时均可使用。

```
// 访问对象
console.log(user?.info?.name) // 输出 undefined

// 访问数组
let users =  ['lily', 'daisy', 'rose'];

console.log(users[1]);  // 输出：daisy
users = null;
console.log(users[1]);  // 抛出错误：TypeError: Cannot read property '1' of null
console.log(users?.[1]);// 输出：undefined

// 调用函数
const user ={
  info: {
    age: 5
  },
  getAge() {
    return this.info?.age;
  }
};

console.log(user.getAge()); // 输出：5
user = null;
console.log(user.getAge()); // 抛出错误
console.log(user?.getAge?.());// 输出：undefined
```

### 1.2 Nullish Coalescing 空值合并(??)

通常我们处理默认参数时都会使用逻辑运算符 ||，利用其短路的性质，当第一个值经过转换为false时就取第二个默认值。

但是一些特殊场景下，这种方式不能按照我们的预期执行。

```
function foo(opt) {
    opt = opt || 'default';
    console.log(opt);
}
foo(0);        // 'default'
foo(false);    // 'default'
foo('');       // 'default'
```

这三种场景下，因为传入参数经过转换都为false，所以就会触发短路取值'default'，但这并不是我们所期望的。

ES11提出了一种由两个问号??组成的合并操作符。操作符右边的值仅在左边的值等于 **null** 或 **undefined** 时有效。

```
function foo(opt) {
    opt = opt ?? 'default';
    console.log(opt);
}
foo(0);        // 0
foo(false);    // false
foo('');       // ''
```

### 1.3 可选链式调用与空值合并运算符结合

我们在做排行榜相关需求时可能会遇到一下场景：

```
const user = {
    info: {
        name: 'Lily'
    },
    data: {
        level: 0
    }
};

let level = user && user.data && user.data.level;

level = (level || level === 0) ? `${level}等级` : '暂无等级';  // 0等级
```

若采用以上两种运算符结合的方式来处理这个问题，就会发现代码既简洁又保证逻辑的正确性。

```
var level = `${user?.data?.level ?? '暂无'}等级`； //  0等级
```

## 2、class类新增

### 2.1 Private Fields 私有字段

许多具有 **classes** 的编程语言允许定义类作为公共的，受保护的或私有的属性：

**Public：** 属性可以从类的外部或者子类访问，

**protected：** 属性只能被子类访问，

**private：** 属性只能被类内部访问。

JavaScript 从 **ES6** 开始支持类语法，但直到现在才引入了私有字段。要定义私有属性，必须在其前面加上散列符号：**#**。

如果我们从外部访问类的私有属性，势必会报错。

### 

```
class Counter {
  #number = 10
  increment() {
    this.#number++;
  }
  getNum() {
    return this.#number;
  }
}

const counter = new Counter();
counter.increment();
console.log(counter.getNum());    //11
console.log(counter.#number);    //SyntaxErro: Private field '#number' must be declared in an enclosing class
```

2.2 Static Fields 静态字段

ES6增加了class的关键字后，并没有提供static这种方法，导致我们在开发时如果想使用类的方法，首先必须实例化一个类，如下所示：

```
const counter = new Counter();

counter.getNum();   // 
Counter.getNum();   // TypeError: Counter.getNum is not a function
```

ES2020提供了static关键字，允许通过类直接访问静态方法。

#### 2.2.1 静态变量和非静态变量

**区别：**静态变量被所有的实例所共享，在内存中只有一个副本，它当且仅当在类初次加载时会被初始化。而非静态变量是实例所拥有的，在创建实例的时候被初始化，存在多个副本，各个实例拥有的副本互不影响。

**定义：**类（class）通过 **static** 关键字定义静态方法。不能在类的实例上调用静态方法，而应该通过类本身调用。这些通常是实用程序方法，例如创建或克隆对象的功能。

> The static keyword defines a static method for a class. Static methods aren't called on instances of the class. Instead, they're called on the class itself. These are often utility functions, such as functions to create or clone objects.

**作用：**优化程序性能，只会在类加载的时候执行一次，存在一个副本。

#### 2.2.2 调用方法

静态方法调用直接在类上进行，不能在类的实例上调用。

a、基本用法

```
class ClassWithStaticMethod {

  static staticProperty = 'someValue';
  static staticMethod() {
    return 'static method has been called.';
  }

}

console.log(ClassWithStaticMethod.staticProperty);
// output: "someValue"
console.log(ClassWithStaticMethod.staticMethod());
// output: "static method has been called."
```

b、从另一个静态方法中调用

静态方法调用同一个类中的其他静态方法，可使用this关键字。

```
class StaticMethodCall {
    static staticMethod() {
        return 'Static method has been called';
    }
    static anotherStaticMethod() {
        return this.staticMethod() + ' from another static method';
    }
}
StaticMethodCall.staticMethod();
// 'Static method has been called'

StaticMethodCall.anotherStaticMethod();
// 'Static method has been called from another static method'
```

c、从类的构造函数和其它一般方法中调用

非静态方法中，不能直接使用 `[this](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/this)` 关键字来访问静态方法。而是要用类名来调用：`CLASSNAME.STATIC_METHOD_NAME()` ，或者用构造函数的属性来调用该方法： `this.constructor.STATIC_METHOD_NAME()`.

```
class StaticMethodCall {
    constructor() {
        console.log(StaticMethodCall.staticMethod());
        // 'static method has been called.'
        console.log(this.constructor.staticMethod());
        // 'static method has been called.'
    }
    static staticMethod() {
        return 'static method has been called.';
    }
}
```

举个例子🌰，下面的例子说明了这几点：

1. 静态方法如何在类上实现。
2. 具有静态成员的类，可以被子类化 。
3. 什么情况下静态方法可以调用，什么情况下不能调用。

```
class Tripple {
  static tripple(n = 1) {
    return n * 3;
  }
}
class BiggerTripple extends Tripple {
  static tripple(n) {
    return super.tripple(n) * super.tripple(n);
  }
}
console.log(Tripple.tripple());// 3
console.log(Tripple.tripple(6));// 18

let tp = new Tripple();
console.log(BiggerTripple.tripple(3));// 81（不会受父类实例化的影响）
console.log(tp.tripple());// 'tp.tripple 不是一个函数'.
```

## 3、语法规则类新增

### 3.1 Dynamic Import 动态引入

标准用法的import导入的模块是静态的，会使所有被导入的模块，在加载时就被编译（无法做到按需编译，降低首页加载速度）。有些场景中，你可能希望根据条件导入模块或者按需导入模块，这时你可以使用动态导入代替静态导入。下面的是你可能会需要动态导入的场景：

- 当静态导入的模块很明显的降低了代码的加载速度且被使用的可能性很低，或者并不需要马上使用它。
- 当静态导入的模块很明显的占用了大量系统内存且被使用的可能性很低。
- 当被导入的模块，在加载时并不存在，需要异步获取
- 当导入模块的说明符，需要动态构建。（静态导入只能使用静态说明符）
- 当被导入的模块有副作用（这里说的副作用，可以理解为模块中会直接运行的代码），这些副作用只有在触发了某些条件才被需要时。（原则上来说，模块不能有副作用，但是很多时候，你无法控制你所依赖的模块的内容）

请不要滥用动态导入（只有在必要情况下采用）。静态框架能更好的初始化依赖，而且更有利于静态分析工具和[tree shaking](https://wiki.developer.mozilla.org/en-US/docs/Glossary/Tree_shaking)发挥作用

关键字import可以像调用函数一样来动态的导入模块。以这种方式调用，将返回一个promise.

```
import('/modules/my-module.js')
  .then((module) => {
    // Do something with the module.
  });
```

这种使用方式也支持 `await` 关键字。

```
let module = await import('/modules/my-module.js');
```

**示例：**

标准导入：

```
// file.js
function getJSON(url, callback) {
  let xhr = new XMLHttpRequest();
  xhr.onload = function () {
    callback(this.responseText)
  };
  xhr.open('GET', url, true);
  xhr.send();
}

export function getUsefulContents(url, callback) {
  getJSON(url, data => callback(JSON.parse(data)));
}

// main.js
import { getUsefulContents } from '/modules/file.js';

getUsefulContents('http://www.example.com',
    data => { doSomethingUseful(data); });
```

动态导入：

此示例展示了如何基于用户操作去加载功能模块到页面上，在例子中通过点击按钮，然后会调用模块内的函数。当然这不是能实现这个功能的唯一方式，import()函数也可以支持await。

```
const main = document.querySelector("main");
for (const link of document.querySelectorAll("nav > a")) {
  link.addEventListener("click", e => {
    e.preventDefault();

    import('/modules/my-module.js')
      .then(module => {
        module.loadPageInto(main);
      })
      .catch(err => {
        main.textContent = err.message;
      });
  });
}
```

### 3.2 Top Level Await 顶级 Await

目前，如果用 **await** 获取 promise 函数的结果，那使用 **await** 的函数必须用 **async** 关键字定义，这意味着，你不能在其他自然函数中使用await。。

```
const func = async () => {
    const response = await fetch(url)
}
```

头疼的是，在全局作用域中去等待某些结果基本上是不可能的。除非使用 立即调用的函数表达式（IIFE）。

```
(async () => {
    const response = await fetch(url)
})()
```

但引入了 顶级 Await 后，不需要再把代码包裹在一个 async 函数中了，如下即可：

```
const response = await fetch(url)
```

使用场景：

a、加载兜底

这个特性对于解决模块依赖或当初始源无法使用而需要备用源的时候是非常有用的。

```
let Vue
try {
    Vue = await import('url_1_to_vue')
} catch {
    Vue = await import('url_2_to_vue)
}
```

b、使用加载速度最快的资源

```
const resPromises = [    
    donwloadFromResource1Site,
    donwloadFromResource2Site
 ];
const res = await Promise.any(resPromises);
```

c、资源初始化

顶级await允许您在模块中wait一个promise，就像它们被封装在异步函数中一样。这对于执行应用程序初始化非常有用。

```
import { dbConnector} from './dbUtils.js'
//connect() return a promise.
const connection = await dbConnector.connect();
export default function(){connection.list()}
```

d、动态加载模块

这允许模块使用运行时值来确定依赖项。

```

const params = new URLSearchParams(window.location.search);
const lang = params.get('lang');
const messages = await import(`./messages-${lang}.mjs`);
```

## 4、API新增

### 4.1 Promise.allSettled 方法

等待多个 promise 返回结果时，我们可以用 Promise.all([promise_1, promise_2])。但问题是，如果其中一个请求失败了，就会抛出错误。然而，有时候我们希望某个请求失败后，其他请求的结果能够正常返回。针对这种情况 ES11 引入了 Promise.allSettled 。

```
const promise1 = Promise.resolve(3);
const promise2 = new Promise((resolve, reject) => setTimeout(reject, 100, 'foo'));
const promises = [promise1, promise2];

Promise.allSettled(promises).
  then((results) => results.forEach((result) => console.log(result.status)));

// expected output:
// "fulfilled"
// "rejected"
```

对于每个结果对象，都有一个 `status` 字符串。如果它的值为 `fulfilled`，则结果对象上存在一个 `value` 。如果值为 `rejected`，则存在一个 `reason` 。value（或 reason ）反映了每个 promise 决议（或拒绝）的值。

### 4.2 正则 MatchAll 匹配所有项

如果你想要查找字符串中所有正则表达式的匹配项和它们的位置，MatchAll 非常有用。

```
var re = /[0-9]+/g;
var str = '2016-01-02';
var result = re[Symbol.matchAll](str);

Array.from(result, x => {
    console.log(x, x[0]);
});

//
0: "2016"
groups: undefined
index: 0
input: "2016-01-02"

console.log(Array.from(result));
// ["2016", "01", "02"]
```

### 4.3 globalThis 全局对象

**描述：**

在以前，从不同的 JavaScript 环境中获取全局对象需要不同的语句。在 浏览器环境中，可以通过 window、self 或者 frames 取到全局对象，但是在 Node.js 中，它们都无法获取，必须使用 global。

在非严格模式下，可以在函数中返回 this 来获取全局对象，但是在严格模式和模块环境下，this 会返回 undefined。

> You can also use Function('return this')(), but environments that disable [eval()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/eval), like [CSP](https://wiki.developer.mozilla.org/en-US/docs/Glossary/CSP) in browsers, prevent use of [Function](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Function) in this way.

globalThis 提供了一个标准的方式来获取不同环境下的全局 this 对象（也就是全局对象自身）。不像 window 或者 self 这些属性，它确保可以在有无窗口的各种环境下正常工作。所以，你可以安心的使用 globalThis，不必担心它的运行环境。

**示例：**

在 `globalThis` 之前，获取某个全局对象的唯一方式就是 `Function('return this')()`，但是这在某些情况下会违反 [CSP](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CSP) 规则，所以，[es6-shim](https://github.com/paulmillr/es6-shim) 使用了类似如下的方式：

```
var getGlobal = function () {
  if (typeof self !== 'undefined') { return self; }
  if (typeof window !== 'undefined') { return window; }
  if (typeof global !== 'undefined') { return global; }
  throw new Error('unable to locate global object');
};

var globals = getGlobal();

if (typeof globals.setTimeout !== 'function') {
  // 此环境中没有 setTimeout 方法！
}

```

但是有了 globalThis 之后，只需要：

### 

```
if (typeof globalThis.setTimeout !== 'function') {
  //  此环境中没有 setTimeout 方法！
}
```

4.4 BigInt

JavaScript中 Number类型只能安全的表示-(2^53-1)至 2^53-1 范的值，即Number.MINSAFEINTEGER 至Number.MAXSAFEINTEGER，超出这个范围的整数计算或者表示会丢失精度。

```
var num = Number.MAX_SAFE_INTEGER;  // -> 9007199254740991
num = num + 1; // -> 9007199254740992
// 再次加 +1 后无法正常运算
num = num + 1; 
// -> 9007199254740992

// 两个不同的值，却返回了true
9007199254740992 === 9007199254740993 // -> true
```

BigInt是一种内置对象，它提供了一种方法来表示大于2^53 - 1 的整数。BigInt可以表示任意大的整数。

**语法：**在一个整数字面量后面加`n`的方式定义一个 `BigInt` ，如：`10n`，或者调用函数`BigInt()`。

```
const theBiggestInt = 9007199254740991n;
const alsoHuge = BigInt(9007199254740991);
// ↪ 9007199254740991n

通过 BigInt， 我们可以安全的进行大数整型计算。
var bigNumRet = 9007199254740993n+ 9007199254740993n; // -> -> 18014398509481986n
bigNumRet.toString(); // -> '18014398509481986'
```

Note:

它在某些方面类似于`Number`，但是也有几个关键的不同点：

- 不能用于 `[Math](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Math)` 对象中的方法；
- 不能和任何 `[Number](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Number)` 实例混合运算，两者必须转换成同一种类型。

在两种类型来回转换时要小心，因为 `BigInt` 变量在转换成 `[Number](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Number)` 变量时可能会丢失精度。

**类型信息：**

使用 `typeof` 测试时， `BigInt` 对象返回 "bigint" ：

```
typeof 1n === 'bigint'; // true
typeof BigInt('1') === 'bigint'; // true
```

使用 Object 包装后， BigInt 被认为是一个普通 "object" ：

```
typeof Object(1n) === 'object'; // true
```

**运算**：

以下操作符可以和 `BigInt` 一起使用： `+`、``*``、``-``、``**``、``%`` 。除 `>>>` （无符号右移）之外的 [位操作](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_Operators) 也可以支持。因为 `BigInt` 都是有符号的， `>>>` （无符号右移）不能用于 `BigInt`。

```
const previousMaxSafe = BigInt(Number.MAX_SAFE_INTEGER);
// ↪ 9007199254740991n
const maxPlusOne = previousMaxSafe + 1n;
// ↪ 9007199254740992n
const theFuture = previousMaxSafe + 2n;
// ↪ 9007199254740993n, this works now!
const multi = previousMaxSafe * 2n;
// ↪ 18014398509481982n
const subtr = multi – 10n;
// ↪ 18014398509481972n
const mod = multi % 10n;
// ↪ 2
const bigN = 2n ** 54n;
// ↪ 18014398509481984n
bigN * -1n
// ↪ –18014398509481984n
```

`/` 操作符对于整数的运算也没问题。可是因为这些变量是 `BigInt` 而不是 `BigDecimal` ，该操作符结果会向零取整，也就是说不会返回小数部分。

Note：当使用 `BigInt` 时，带小数的运算会被取整。

```
const expected = 4n / 2n;
// ↪ 2n

const rounded = 5n / 2n;
// ↪ 2n, not 2.5n
```

**比较：**

```
// BigInt 和 Number 不是严格相等的，但是宽松相等的。
0n === 0
// ↪ false
0n == 0
// ↪ true

// Number 和 BigInt 可以进行比较。
1n < 2
// ↪ true
2n > 1
// ↪ true
2 > 2
// ↪ false
2n > 2
// ↪ fals
2n >= 2
// ↪ true

//两者也可以混在一个数组内并排序。
const mixed = [4n, 6, -12n, 10, 4, 0, 0n];
// ↪  [4n, 6, -12n, 10, 4, 0, 0n]
mixed.sort();
// ↪ [-12n, 0, 0n, 10, 4n, 4, 6]

```

注意被 Object 包装的 BigInt 使用 object 的比较规则进行比较，只用同一个对象在比较时才会相等。

```
0n === Object(0n); // false
Object(0n) === Object(0n); // false

const o = Object(0n);
o === o // true
```

## 其它

[ECMAScript2019（Chapter 16-18）](https://xiaomi.f.mioffice.cn/docs/dock40zWIZviMXBr6aFnkTFC1uh)

[ECMAScript® 2019（19到21章）](https://xiaomi.f.mioffice.cn/docs/dock4oaFne7xnVXSBhiHIrZ16Pd)

官方文档： https://tc39.es/ecma262/2020/

BigInt: https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/BigInt