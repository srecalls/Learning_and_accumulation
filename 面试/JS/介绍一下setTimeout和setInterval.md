## setTimeout

`setTimeout()` 是 JavaScript 中的一个内置函数，用于在一定的延迟时间后执行指定的函数或一段代码。

语法：

```javascript
setTimeout(function, delay, arg1, arg2, ...)
```

参数：

- `function`: 要执行的函数或要执行的代码块。
- `delay`: 延迟的毫秒数，表示多久后执行函数或代码块。
- `arg1, arg2, ...`: 可选参数，传递给函数的参数。

返回值：

- `timeoutID`，一个用于取消定时执行的标识符。

示例：

```javascript
function greet(name) {
  console.log(`Hello, ${name}!`);
}

setTimeout(greet, 2000, 'Alice');
// 2秒后输出: Hello, Alice!
```

在上面的示例中，我们使用 `setTimeout()` 来安排在 2000 毫秒（2 秒）后执行 `greet()` 函数。函数 `greet()` 接受一个参数 `name`，我们在 `setTimeout()` 的参数中传递了 `'Alice'` 作为参数。

`setTimeout()` 可以用于执行任意的函数或代码块，而不仅限于定义的函数。下面是一个使用匿名函数的示例：

```javascript
setTimeout(function() {
  console.log('This is a delayed message.');
}, 3000);
// 3秒后输出: This is a delayed message.
```

在上面的示例中，我们传递了一个匿名函数作为 `setTimeout()` 的第一个参数，函数体中的代码将在 3000 毫秒（3 秒）后执行。

需要注意的是，`setTimeout()` 只会执行一次。如果需要重复执行一个函数，可以使用 `setInterval()` 函数。

取消定时器：

`setTimeout()` 返回一个标识符 `timeoutID`，可以使用该标识符来取消定时器，即在指定时间之前阻止函数的执行。

示例：

```javascript
function sayHello() {
  console.log('Hello!');
}

const timerId = setTimeout(sayHello, 5000);
// 5秒后输出: Hello!

// 取消定时器
clearTimeout(timerId);
```

在上面的示例中，我们首先使用 `setTimeout()` 安排在 5000 毫秒（5 秒）后执行 `sayHello()` 函数，并将返回的 `timeoutID` 存储在变量 `timerId` 中。然后，我们使用 `clearTimeout()` 函数取消了定时器，阻止了函数的执行。

总结：

- `setTimeout()` 用于在指定的延迟时间后执行函数或代码块。
- 可以传递函数或匿名函数作为要执行的内容。
- 可以传递参数给函数。
- 返回一个标识符 `timeoutID`，可以使用 `clearTimeout()` 函数取消定时器。
- `setTimeout()` 只会执行一次。如果需要重复执行，可以使用 `setInterval()` 函数。


## setInterval
`setInterval()` 是 JavaScript 中的一个内置函数，用于按照指定的时间间隔重复执行指定的函数或一段代码。

语法：

```javascript
setInterval(function, delay, arg1, arg2, ...)
```

参数：

- `function`: 要重复执行的函数或要执行的代码块。
- `delay`: 重复执行的时间间隔，以毫秒为单位。
- `arg1, arg2, ...`: 可选参数，传递给函数的参数。

返回值：

- `intervalID`，一个用于取消重复执行的标识符。

示例：

```javascript
function greet() {
  console.log('Hello!');
}

setInterval(greet, 1000);
// 每隔1秒输出: Hello!
```

在上面的示例中，我们使用 `setInterval()` 来安排每隔 1000 毫秒（1 秒）执行一次 `greet()` 函数。

`setInterval()` 可以用于执行任意的函数或代码块，而不仅限于定义的函数。下面是一个使用匿名函数的示例：

```javascript
setInterval(function() {
  console.log('This is a repeated message.');
}, 2000);
// 每隔2秒输出: This is a repeated message.
```

在上面的示例中，我们传递了一个匿名函数作为 `setInterval()` 的第一个参数，函数体中的代码将每隔 2000 毫秒（2 秒）执行一次。

取消定时器：

`setInterval()` 返回一个标识符 `intervalID`，可以使用该标识符来取消重复执行，即停止函数的执行。

示例：

```javascript
function sayHello() {
  console.log('Hello!');
}

const intervalId = setInterval(sayHello, 3000);
// 每隔3秒输出: Hello!

// 取消定时器
clearInterval(intervalId);
```

在上面的示例中，我们首先使用 `setInterval()` 安排每隔 3000 毫秒（3 秒）执行一次 `sayHello()` 函数，并将返回的 `intervalID` 存储在变量 `intervalId` 中。然后，我们使用 `clearInterval()` 函数取消了重复执行，停止了函数的执行。

总结：

- `setInterval()` 用于按照指定的时间间隔重复执行函数或代码块。
- 可以传递函数或匿名函数作为要执行的内容。
- 可以传递参数给函数。
- 返回一个标识符 `intervalID`，可以使用 `clearInterval()` 函数取消重复执行。
- `setInterval()` 会持续重复执行，直到被取消。
- 若要执行一次性的延迟操作，可以使用 `setTimeout()` 函数。