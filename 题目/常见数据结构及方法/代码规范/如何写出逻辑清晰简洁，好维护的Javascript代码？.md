其实严格来讲，我还没有足够的资历去写这样一篇文章。有感于看大佬们的一些文章和代码，感觉到能写出逻辑清晰简洁，好维护的Javascript代码是一件类似于习惯养成的事，所以我想借写这篇文章的机会，将那些能使得代码逻辑清晰，提高代码可维护性的相关技巧总结一下～
# 一、代码简洁、逻辑清晰

---

# 使用ES6新特性

## - 字符串连接使用模板字符串 ` 和 ${} 代替 传统+
```js
let name = 'jasonlam'
let time = '8:00'  
  
// bad code  
let message = 'hello ' + name + ', it\'s ' + time +' now'  
console.log(message) // hello jasonlam, it's 8:00 now  
  
// good code  
let message = `hello ${name}, it's ${time} now`  
console.log(message) // hello jasonlam, it's 8:00 now
```


## - 使用解构赋值
###  一、简洁明了地获取对象、数组、函数return中的值 
```js
// 一、简洁明了地获取对象、数组、函数return中的值  
  
const data = { name: 'jasonlam', age: 22 };  
  
// bad code  
let name = data.name; // jasonlam  
let age = data.age; // 22  
  
// good code  
const { name, age } = data; // 简单明了  
console.log(name) // jasonlam  
console.log(age) // 22  
--------------------------------------------  
  
const fullName = ['jason', 'lam'];  
  
// bad code  
let firstName = fullName[0];  
let lastName = fullName[1];  
  
// good code  
const [firstName, lastName] = fullName;  
console.log(firstName) // jason  
console.log(lastName) // lam  
```

###  二、交换变量的值 
```js
// 二、交换变量的值  
  
let x = 1;  
let y = 2;  
[x, y] = [y, x];  
```

### 三、遍历Map结构 
```js
// 三、遍历Map结构  
  
const map = new Map();  
map.set('first', 'hello');  
map.set('second', 'world');  
  
for (let [key, value] of map) {  
    console.log(key + " is " + value);  
}  
// first is hello  
// second is world  
```

###  四、加载模块的指定方法
```js
// 四、加载模块的指定方法  
// 加载模块时，往往需要指定输入哪些方法。解构赋值使得输入语句非常清晰  
  
const { SourceMapConsumer, SourceNode } = require("source-map")
```


## - ES6 允许为函数的参数设置默认值，即直接写在参数定义的后面
好的，让我来详细解释一下。
在ES6中，我们可以为函数的参数设置默认值，例如：
```js
function greet(name = 'World') {
  console.log(`Hello, ${name}!`);
}

greet(); // 输出: Hello, World!
greet('Alice'); // 输出: Hello, Alice!
```
在上面的例子中，函数`greet`有一个名为`name`的参数，我们为其设置了默认值为`'World'`。当不传入参数或者传入`undefined`时，`name`将取默认值`'World'`，否则将取传入的值。
需要注意的是，如果一个参数没有设置默认值，它将被认为是必需的，如果调用函数时没有传入该必需参数，将抛出一个错误。
另外，参数默认值也可以是表达式，例如：
```js
function add(a, b = a + 1) {
  return a + b;
}

add(1); // 输出: 3，b的默认值为2
add(1, 2); // 输出: 3，b的值为2被覆盖
```
在上面的例子中，参数`b`的默认值是`a + 1`，其中`a`是必需的参数。当我们调用`add(1)`时，`b`的默认值为`a + 1 = 2`，所以函数返回值为`1 + 2 = 3`。
希望这个例子可以更好地帮助你理解ES6中的参数默认值。

## - 尾调用优化 - 尾递归，递归函数改写 
首先是尾调用优化和尾递归。在 JavaScript 中，递归函数通常会导致栈溢出的问题，因为每次函数调用都会将一个新的帧（frame）压入调用栈中。但是，**如果函数的最后一个操作是一个函数调用**，并且**这个调用的结果是函数的返回值**，那么这个**函数调用就可以被优化成尾调用**（tail call），从而避免了栈溢出的问题。而如果**递归函数中的递归调用是一个尾调用**，就可以使用**尾递归（tail recursion）来解决栈溢出的问题**。

例如，下面是一个递归函数和一个尾递归函数的示例：
```js
// 递归函数
function factorial(n) {
  if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
// 尾递归函数
function factorial_tail(n, acc = 1) {
  if (n <= 1) {
    return acc;
  } else {
    return factorial_tail(n - 1, n * acc);
  }
}
```
`factorial`函数是一个递归函数，它计算一个数的阶乘。`factorial_tail`函数是一个**尾递归函数**，它使用一个累加器（`acc`）来避免使用调用栈，从而计算一个数的阶乘。在这个例子中，`factorial_tail`函数的调用是**尾调用，因为它是函数的最后一个操作，并且它的返回值是函数的返回值。**

## - 函数curry化
好的，这里再举一个函数柯里化的例子，并详细说明。
假设我们有一个函数`add`，它可以接受任意个数的参数，并将它们相加后返回结果：
```javascript
function add(...args) {
  return args.reduce((sum, num) => sum + num, 0);
}

add(1, 2, 3, 4); // 输出: 10
```
现在，我们想要使用柯里化的方式将这个函数转化为一个接受单个参数的函数序列。我们可以定义一个`curry`函数，该函数接受一个函数作为参数并返回一个新的函数，该新函数接受一个参数并返回一个新的函数，以此类推，直到所有参数都被收集完毕。
```javascript
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn.apply(this, args);
    } else {
      return function(...newArgs) {
        return curried.apply(this, args.concat(newArgs));
      };
    }
  };
}
```
在上面的`curry`函数中，我们首先定义一个名为`curried`的递归函数，该函数接受任意数量的参数。如果传入的参数个数大于或等于原始函数`fn`的参数个数，那么我们就直接调用`fn`函数并返回结果。否则，我们返回一个新的函数，该函数接受更多的参数，并将当前的参数与之前的参数合并后，递归调用`curried`函数。
现在我们可以使用`curry`函数将`add`函数柯里化：
```javascript
const curriedAdd = curry(add);

curriedAdd(1)(2)(3)(4); // 输出: 10
curriedAdd(1, 2)(3, 4); // 输出: 10
curriedAdd(1, 2, 3, 4); // 输出: 10
```
在上面的示例中，我们首先使用`curry`函数将`add`函数转化为一个柯里化函数`curriedAdd`。然后，我们可以使用多种方式调用`curriedAdd`函数，每次只传递一个参数，直到所有参数都被收集完毕，然后函数被调用并返回结果。
柯里化的好处是可以使代码更加模块化和可复用，因为我们可以将一个函数分解为多个单一的函数，这些函数可以更方便地组合到一起以构建更复杂的逻辑。

# 二、可维护性
## 变量相关
### - 数据只使用一次或不使用就无需装到变量中（没用的就删除掉，不然过久了自己都不敢删，怕是不是哪里会用到）

好的，这里举一个具体的例子来说明第一点：数据只使用一次或不使用就无需装到变量中。

假设我们有以下代码：

```javascript
function calculatePrice(quantity, price) {
  const taxRate = 0.1;
  const subTotal = quantity * price;
  const tax = subTotal * taxRate;
  const total = subTotal + tax;
  return total;
}

const price = calculatePrice(10, 100);
console.log(`Price: ${price}`);
```

在上面的代码中，我们定义了一个`calculatePrice`函数，该函数接受两个参数：`quantity`和`price`。在函数中，我们定义了一个名为`taxRate`的变量，它的值为`0.1`，表示税率。然后我们计算了商品的小计、税额和总价，并将总价返回。

在函数的最后，我们将总价存储在变量`price`中，并在控制台中打印出来。

但是我们发现，`taxRate`和`subTotal`这两个变量只在一个地方使用了，而且它们的值是通过计算得到的。因此，我们可以不需要将它们存储在变量中，而是直接将它们的计算结果用于后续的计算。

改进后的代码如下所示：

```javascript
function calculatePrice(quantity, price) {
  const taxRate = 0.1;
  return quantity * price * (1 + taxRate);
}

const price = calculatePrice(10, 100);
console.log(`Price: ${price}`);
```

在上面的代码中，我们直接将`subTotal`和`tax`的计算结果用于后续的计算，而不是将它们存储在变量中。这样做的好处是可以减少内存的使用，同时也可以使代码更加简洁和易读。

当然，这并不是说我们应该完全避免使用变量，而是需要根据具体情况来判断何时使用变量，何时不使用变量。如果一个变量的值只会使用一次或不使用就可以删除掉，那么就可以不使用变量。但是如果一个变量的值会被多次使用，那么就需要将它存储在变量中，以避免重复计算。

### - 变量命名最好字面上就要看得懂并且尽可能简洁不啰嗦，别搞那些花里胡哨的
```js
// JS Bad Code：  
  
if(value.length < 8){  
// 为什么要小于8，8表示的是什么？长度，还是位移，还是高度？Oh,my God!!  
}  
  
// JS Good Code  
  
const MAX_INPUT_LENGTH = 8;  
if (value.length < MAX_INPUT_LENGTH) {   
// 一目了然，判断中表示的是不能超过最大输入长度      
}
```

### - 特定的数值（参数）最好放在变量里并且要命名好，在JS与CSS预处理器（如Less or Sass）都有用武之地
```js
// 这部分的代码并不具有很强的代表性，但就是希望告诉你可以这么做  
  
// Less Bad Code  
.text-line {  
    line-height: 20px;  
}  
.banner {  
    line-height: 60px;  
}  
  
// Less Good Code  
@Banner_LINE_HEIGHT: 20px;  
.text-line {  
    line-height: @Banner_LINE_HEIGHT; // 1行的高度  
}  
.banner {  
    line-height: @Banner_LINE_HEIGHT * 3; // 3行的高度  
}
```

## 函数相关

### 1. 从函数名就可以知道返回值的类型，对于返回`true or false`的函数，最好以`should/is/can/has`开头

例如，我们有一个函数，它用于检查一个数组是否为空：

```javascript
function isEmptyArray(arr) {
  return arr.length === 0;
}
```

这个函数的名字`isEmptyArray`很好地表明了它的作用，但是它的返回值是一个布尔值，可以进一步改进函数名，以`should/is/can/has`开头，如`is`：

```javascript
function isArrayEmpty(arr) {
  return arr.length === 0;
}
```

这样函数名`isArrayEmpty`就更加直白地表达了函数的返回值类型，使得函数更加易懂。

### 2. 功能函数最好为纯函数，一个函数完成一个独立的功能，不要一个函数混杂多个功能

例如，我们有一个函数，它接受一个数组和一个数字，然后将数组中所有小于该数字的元素删除并返回新的数组：

```javascript
function removeLessThan(arr, num) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < num) {
      arr.splice(i, 1);
      i--;
    }
  }
  return arr;
}
```

这个函数虽然实现了删除小于特定数字的元素的功能，但是它同时也改变了原始的数组，这违反了“一个函数完成一个独立的功能”的原则。因此，我们可以分解这个函数，将其拆分为两个单独的函数：一个用于过滤数组中的元素，另一个用于返回新的数组。

```javascript
function filterLessThan(arr, num) {
  return arr.filter((item) => item >= num);
}

function removeLessThan(arr, num) {
  return arr.filter((item) => item >= num);
}
```

这样，我们就可以将两个不同的功能分别实现在两个不同的函数中，并且这两个函数都是纯函数，不会改变原始的数组。

### 3. 动作函数要以动词开头，如`send/add/delete`

例如，我们有一个函数，它用于向服务器发送请求并获取响应：

```javascript
function serverRequest(url, data) {
  // ...
}
```

这个函数的名字`serverRequest`描述了函数的作用，但是它并没有以动词开头，使得函数的命名不够直观。因此，我们可以将函数名更改为`sendServerRequest`，这样函数名就更加清晰地表达了函数的作用。

```javascript
function sendServerRequest(url, data) {
  // ...
}
```

### 4. 优先使用函数式编程

函数式编程是一种编程范式，它强调函数的纯洁性和无状态性，避免使用可变状态和副作用，从而提高代码的可读性、可维护性和可测试性。在函数式编程中，函数被视为一等公民，可以作为参数传递和返回值使用，从而实现高度的抽象和复用。

例如，我们有一个函数，它用于计算一个数组中所有偶数的平均值：

```javascript
function averageEvenNumbers(arr) {
  let sum = 0;
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0) {
      sum += arr[i];
      count++;
    }
  }
  return sum / count;
}
```

这个函数使用了可变状态，即`sum`和`count`变量，而且它还使用了循环语句，使得代码不够简洁和优雅。我们可以使用函数式编程的方法，将这个函数重构为一个更简洁、更纯洁的形式：

```javascript
function averageEvenNumbers(arr) {
  const evenNumbers = arr.filter((item) => item % 2=== 0);
  const sum = evenNumbers.reduce((acc, item) => acc + item, 0);
  return sum / evenNumbers.length;
}
```

在上面的代码中，我们使用了`filter`和`reduce`两个数组方法，它们都是纯函数，不会修改原始的数组，并且它们的返回值也是纯粹的，因此使得代码更加简洁、清晰和易读。

#### 可变状态和副作用
可变状态和副作用是函数式编程中的概念。

可变状态是指在程序执行过程中可以改变的状态。在函数式编程中，我们尽可能避免使用可变状态，因为它会导致程序的不确定性和不可预测性。如果一个函数依赖于可变状态，那么它就不是一个纯函数，因为相同的输入可能得到不同的输出。而且，可变状态也会使得代码的调试和测试变得更加困难。

副作用是指函数执行过程中对其它部分产生的影响。在函数式编程中，我们也尽可能避免使用副作用。如果一个函数具有副作用，那么它就不是一个纯函数，因为相同的输入可能会对其它部分产生不同的影响。常见的副作用包括修改全局变量、修改输入参数、读写文件等。

函数式编程强调函数的纯洁性和无状态性，即函数不依赖于可变状态和副作用。通过避免使用可变状态和副作用，可以使得程序更加可读、可维护、可测试和可扩展。同时，函数式编程也提供了一系列的技术和工具来处理可变状态和副作用，例如函数柯里化、纯函数组合、惰性求值等。

##### 例子
好的，我来举几个例子来说明可变状态和副作用的概念。

1. 可变状态的例子

考虑以下的 JavaScript 代码：

```javascript
let count = 0;

function increment() {
  count++;
}

increment();
console.log(count); // 1
increment();
console.log(count); // 2
```

在上面的代码中，我们定义了一个全局变量`count`，然后定义了一个名为`increment`的函数，它用于将`count`的值加1。在函数的每次调用中，`count`的值都会被改变，因此`count`是一个可变状态。这会导致函数的输出值依赖于函数调用的顺序，使得程序的行为变得不确定和不可预测。

2. 副作用的例子

考虑以下的 JavaScript 代码：

```javascript
function logMessage(message) {
  console.log(`Message: ${message}`);
}

function getUser(id) {
  const user = fetch(`/api/users/${id}`).then((response) => response.json());
  logMessage(`Retrieved user: ${user.name}`);
  return user;
}

const user = getUser(123);
```

在上面的代码中，我们定义了一个名为`logMessage`的函数，它用于将一条消息打印到控制台中。然后，我们定义了一个名为`getUser`的函数，它用于从服务器上获取用户信息，并在获取成功后调用`logMessage`函数将用户信息打印到控制台中。

这个函数具有副作用，因为它会修改程序的输出，即打印一条消息到控制台中。这意味着相同的输入可能会有不同的输出，因此这个函数不是一个纯函数。

3. 函数式编程的例子

考虑以下的 JavaScript 代码：

```javascript
const numbers = [1, 2, 3, 4, 5];

function sumArray(arr) {
  return arr.reduce((acc, item) => acc + item, 0);
}

function doubleArray(arr) {
  return arr.map((item) => item * 2);
}

const sum = sumArray(numbers);
console.log(`Sum: ${sum}`); // 15

const doubled = doubleArray(numbers);
console.log(`Doubled: ${doubled}`); // [2, 4, 6, 8, 10]
```

在上面的代码中，我们定义了两个纯函数`sumArray`和`doubleArray`，它们分别用于计算数组中所有元素的和和将数组中的每个元素都乘以2。这两个函数都不依赖于可变状态和副作用，因此它们是纯函数，可以保证相同的输入得到相同的输出。同时，这两个函数的实现也很简洁和优雅，使用了函数式编程的技巧和方法。