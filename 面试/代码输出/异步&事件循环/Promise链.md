## Promise链
以下是一个简单的例子，用于说明 Promise 链是如何工作的：

```javascript
// 定义一个 Promise 对象，它会在 1 秒后返回一个字符串 "Hello"
const promise1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('Hello')
  }, 1000)
})

// 在 promise1 的基础上定义一个新的 Promise 对象，它会在 promise1 执行完成后将字符串转为大写
const promise2 = promise1.then((result) => {
  return result.toUpperCase()
})

// 在 promise2 的基础上定义一个新的 Promise 对象，它会在 promise2 执行完成后将字符串添加后缀 "World"
const promise3 = promise2.then((result) => {
  return result + ' World'
})

// 在 promise3 的基础上定义一个新的 Promise 对象，它会在 promise3 执行完成后将字符串打印到控制台中
promise3.then((result) => {
  console.log(result)
})
```

在这个例子中，我们定义了一个 Promise 对象 `promise1`，它会在 1 秒后返回一个字符串 "Hello"。然后，在 `promise1` 的基础上定义了一个新的 Promise 对象 `promise2`，它会在 `promise1` 执行完成后将字符串转为大写。接着，在 `promise2` 的基础上定义了一个新的 Promise 对象 `promise3`，它会在 `promise2` 执行完成后将字符串添加后缀 "World"。最后，在 `promise3` 的基础上定义了一个新的 Promise 对象，它会在 `promise3` 执行完成后将字符串打印到控制台中。

这个例子中的 Promise 链是基于前一个 Promise 对象返回一个新的 Promise 对象而构建的。当 Promise 对象的 `then` 方法返回一个新的 Promise 对象时，这个新的 Promise 对象会被添加到 Promise 链中，成为前一个 Promise 对象的后继，形成一个链式调用的结构。在这个例子中，`promise2` 和 `promise3` 都是在前一个 Promise 对象执行完成后返回的新的 Promise 对象，它们被添加到 Promise 链的末尾。

当 Promise 链中的每个 Promise 对象执行完成后，它会将执行结果传递给下一个 Promise 对象，直到 Promise 链的最后一个 Promise 对象执行完成，并且执行结果被处理完成。在这个例子中，`promise3` 是 Promise 链中的最后一个 Promise 对象，它会将处理结果打印到控制台中。


```js
// 定义一个 Promise 对象，它会在 1 秒后返回一个字符串 "Hello"  
const promise1 = new Promise((resolve, reject) => {  
	setTimeout(() => {  
		resolve('Hello')  
	}, 1000)  
})

// 在 promise1 的基础上定义一个新的 Promise 对象，它会在 promise1 执行完成后将字符串转为大写  
const promise2 = promise1.then((result) => {  
	console.log(1)  
	return result.toUpperCase()  
})

// 在 promise2 的基础上定义一个新的 Promise 对象，它会在 promise2 执行完成后将字符串添加后缀 "World"  
const promise3 = promise2.then((result) => {  
	return result + ' World'  
})
```
在这段代码中，确实是定义了一些函数，而没有显式地调用它们。但是，在 Promise 的执行过程中，这些函数是会被自动调用的。

当 Promise 对象的状态从挂起（pending）变为已完成（fulfilled）时，它会自动调用 `then` 方法中传入的回调函数。在这个例子中，当 `promise1` 对象执行完成后，它会调用 `promise2` 的 `then` 方法中传入的回调函数，将执行结果传递给这个回调函数，并将回调函数的返回值作为新的 Promise 对象的执行结果。

当新的 Promise 对象的状态从挂起（pending）变为已完成（fulfilled）时，它又会自动调用下一个 `then` 方法中传入的回调函数，以此类推。在这个例子中，当 `promise2` 对象执行完成后，它会调用 `promise3` 的 `then` 方法中传入的回调函数，将执行结果传递给这个回调函数，并将回调函数的返回值作为新的 Promise 对象的执行结果。

因此，在 Promise 链中定义的函数都是会被自动调用的，而不需要显式地调用它们。这也是 Promise 链的一个重要特性，可以将异步操作串联起来，以便更好地组织和管理异步代码。