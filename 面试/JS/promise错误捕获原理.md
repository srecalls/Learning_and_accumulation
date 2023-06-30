在JavaScript中，Promise对象是一种异步编程模式，用于处理异步操作并返回异步操作的结果。在使用Promise时，我们可以通过`then()`方法来处理异步操作成功的情况，或者通过`catch()`方法来处理异步操作失败的情况。当异步操作失败时，Promise会将错误信息封装成一个Error对象，并将其传递给`catch()`方法。

具体来说，当Promise对象在执行异步操作时出现错误时，它会将该错误封装成一个Error对象，并将其作为参数传递给`reject()`方法。然后，`reject()`方法会将Error对象传递给`catch()`方法。因此，在`catch()`方法中，我们可以通过捕获Error对象来处理异步操作失败的情况。

以下是一个示例，演示如何使用Promise的`then()`和`catch()`方法来处理异步操作成功和失败的情况：

```javascript
function asyncFunction() {
  return new Promise(function(resolve, reject) {
    // 异步操作
    setTimeout(function() {
      // 模拟异步操作出现错误的情况
      reject(new Error("Async operation failed"));
    }, 1000);
  });
}

asyncFunction()
  .then(function(result) {
    console.log("Async operation succeeded:", result);
  })
  .catch(function(error) {
    console.error("Async operation failed:", error);
  });
```

在上述代码中，我们定义了一个异步函数`asyncFunction()`，它返回一个Promise对象，并在异步操作完成后将其结果传递给`resolve()`方法，或者在异步操作出现错误时将错误信息封装成一个Error对象，并将其传递给`reject()`方法。然后，我们使用Promise的`then()`方法和`catch()`方法来处理异步操作成功和失败的情况。在`catch()`方法中，我们捕获了Error对象，并将其输出到控制台上。

需要注意的是，当Promise对象中的异步操作出现错误时，如果没有使用`catch()`方法来处理错误，错误信息将被忽略，无法得到任何反馈。因此，使用`catch()`方法来处理异步操作失败的情况非常重要。


## 捕获过程
```js
Promise.reject(new Error('aaaa'))
	.then(res => {
		console.log(2)
	}, err=> {
		throw err
	})
	.catch(err => {
		console.log(1)
	})
```