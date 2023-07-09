https://developer.mozilla.org/zh-CN/docs/Web/API/console

`console` 是 Web API 中常用的调试工具，提供了一系列用于输出信息和调试代码的方法。下面是 `console` 的一些基本接口：
##### 1.console.log()
1. `console.log()`：输出信息到控制台，可以输出字符串、数字、对象等类型的数据。
```js
const name = 'Alice';
const age = 30;
console.log('Name:', name, 'Age:', age); // 输出：Name: Alice Age: 30
```
![[Pasted image 20230709173121.png]]

##### 2.console.error()
2. `console.error()`：输出错误信息到控制台，会在控制台中以红色字体显示。
```js
const result = 10 / 'abc';
if (isNaN(result)) {
  console.error('Error: Invalid calculation result'); // 输出：Error: Invalid calculation result
}
```
![[Pasted image 20230709173142.png]]

##### 3.console.warn()
3. `console.warn()`：输出警告信息到控制台，会在控制台中以黄色字体显示。
```js
const count = 11;
if (count > 10) {
  console.warn('Warning: Count is greater than 10'); // 输出：Warning: Count is greater than 10
}
```
![[Pasted image 20230709173215.png]]

##### 4.console.info()
4. `console.info()`：输出信息到控制台，会在控制台中以蓝色字体显示。打印资讯类说明信息.
```js
const user = {
  name: 'Bob',
  age: 25,
  email: 'bob@example.com'
};
console.info('User information:', user); // 输出：User information: {name: "Bob", age: 25, email: "bob@example.com"}   
```
![[Pasted image 20230709173434.png]]

##### 5.console.debug()
5. `console.debug()`：输出调试信息到控制台，通常用于调试代码。
`console.debug()` 是 `console` 对象的一个方法，用于在调试代码时输出调试信息。`console.debug()` 与 `console.log()` 的作用相似，都可以用于输出调试信息，只是在一些浏览器中，`console.debug()` 输出的信息有一些不同于 `console.log()` 的特殊处理，例如在 Chrome 浏览器中，使用 `console.debug()` 输出的信息会在控制台中以灰色字体显示。
```js
function calculate(a, b) {
  console.debug('Start calculating...');
  const result = a + b;
  console.debug('Calculation complete. Result:', result);
  return result;
}

const a = 10;
const b = 20;
calculate(a, b);
```
##### 6.console.table()
6. `console.table()`：以表格形式输出数组或对象的数据。
```js
const fruits = ['apple', 'banana', 'orange'];
console.table(fruits); // 输出以表格形式的数组数据

const user = {
  name: 'Bob',
  age: 25,
  email: 'bob@example.com'
};
console.table(user); // 输出以表格形式的对象数据
```
![[Pasted image 20230709173802.png]]

##### 7.console.group()和console.groupEnd()
7. `console.group()` 和 `console.groupEnd()`：用于将输出信息分组，方便查看和分析。`console.group()` 用于开始一个新的分组，`console.groupEnd()` 用于结束当前分组。
```js
console.group('Group 1');
console.log('Message 1');
console.log('Message 2');
console.groupEnd();

console.group('Group 2');
console.log('Message 3');
console.log('Message 4');
console.groupEnd();
```
![[Pasted image 20230709173819.png]]

##### 8.console.time()和console.timeEnd()
8. `console.time()` 和 `console.timeEnd()`：用于计算代码执行时间。`console.time()` 用于开始计时，`console.timeEnd()` 用于结束计时，并输出执行时间。
```js
console.time('Test');
const result = calculate();
console.timeEnd('Test');
console.log('Result:', result);

function calculate() {
  let sum = 0;
  for (let i = 0; i < 100000000; i++) {
    sum += i;
  }
  return sum;
}
```
![[Pasted image 20230709173836.png]]

##### 9.console.assert()
9. `console.assert()`：用于断言某个条件是否成立，如果条件不成立，则输出错误信息到控制台。常用于调试代码中的逻辑错误。语法如下：

```js
console.assert(condition, message);
```

其中，`condition` 是要断言的条件，如果为 `false`，则输出 `message` 到控制台。例如：

```js
function divide(a, b) {
  console.assert(b !== 0, 'Divide by zero');
  return a / b;
}

const result = divide(10, 0); // 输出错误信息：Assertion failed: Divide by zero
```

在这个例子中，`divide()` 函数用于计算两个数的商，使用 `console.assert()` 断言除数不为零，如果除数为零，则输出错误信息到控制台。

![[Pasted image 20230709173907.png]]
##### 10.console.dir()
10. `console.dir()`：用于以对象形式输出数据到控制台。常用于查看对象的属性和方法。语法如下：
```js
console.dir(obj);
```
其中，`obj` 是要输出的对象。例如
```js
const user = {
  name: 'Bob',
  age: 25,
  email: 'bob@example.com'
};
console.dir(user);
```
在控制台中，会以对象形式输出 `user` 对象的属性和方法。
![[Pasted image 20230709173922.png]]

##### 11.console.clear()
11. `console.clear()`：用于清空控制台中的所有输出信息。常用于清理控制台中的多余信息，以便更清晰地查看新的输出信息。语法如下：
```js
console.clear();
```
例如，在控制台中执行以下代码：
```js
console.log('Message 1');
console.log('Message 2');
console.log('Message 3');
console.clear();
console.log('Message 4');
```

在执行 `console.clear()` 后，控制台中的所有输出信息都被清除，只有 `Message 4` 被输出到控制台中。

![[Pasted image 20230709173943.png]]