使用 Promise 封装 AJAX 请求的好处有很多，包括：

1. 更好的可读性和可维护性：使用 Promise 可以将异步操作的状态转换为同步风格的代码，使代码更加直观和易于理解。Promise 还提供了丰富的方法，如 `.then()`、`.catch()`、`.finally()` 等，可以方便地处理异步操作的结果和错误。

2. 更好的可复用性：将 AJAX 请求封装为 Promise，可以将其作为一个独立的模块，方便在多个地方进行调用和复用。

3. 更好的错误处理：使用 Promise 可以方便地处理 AJAX 请求中的错误，例如网络错误、服务器错误等。通过 `.catch()` 方法可以捕获错误并进行处理，避免了回调函数中的错误处理逻辑过于复杂的问题。

4. 更好的可测试性：使用 Promise 可以方便地进行单元测试，因为它提供了可靠的异步操作管理和错误处理机制，可以更加容易地编写测试用例。


## 实例代码 1
例如，以下是使用 Promise 封装 AJAX 请求的示例代码：

```javascript
function ajax(url, options) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();

    xhr.open(options.method || 'GET', url);

    xhr.onload = function() {
      if (this.status >= 200 && this.status < 300) {
        resolve(xhr.response);
      } else {
        reject(new Error(this.statusText));
      }
    };

    xhr.onerror = function() {
      reject(new Error('Network Error'));
    };

    xhr.send(options.body);
  });
}

// 使用示例
ajax('/api/users', {
  method: 'POST',
  body: JSON.stringify({
    name: 'John Doe',
    email: 'john.doe@example.com'
  }),
  headers: {
    'Content-Type': 'application/json'
  }
})
.then(response => {
  console.log(response);
})
.catch(error => {
  console.error(error);
});
```

## 示例代码 2
```js
// promise 封装实现
function ajax(url) {
    // 创建一个 promise 对象
    let promise = new Promise(function(resolve, reject) {
        let xhr = new XMLHttpRequest()
        // 新建一个 http 请求
        xhr.open('GET', url, true)
        // 设置状态的监听函数
        xhr.onreadystatechange = function () {
            if (xhr.readyState !== 4) return
            // 当请求成功或失败时，改变promise的状态
            if (this.status == 200) {
                // console.log(this.responseText)
                resolve(this.response)
            } else {
                reject(new Error(this.statusText))
            }
        }
        // 设置错误监听函数
        xhr.onerror = function() {
            reject(new Error(this.statusText))
        }
        // 设置响应的数据结构
        xhr.responseType = "json"
        // 设置请求头信息
        xhr.setRequestHeader("Accept", "Application/json")
        // 发送http请求
        xhr.send(null)
    })
    return promise
}

ajax('https://mock.mengxuegu.com/mock/645ba6c87ba95d67784d689b/aJaxTest/test')
.then(response => {
    console.log(response)
})
.catch(error => {
    console.log(error)
})
```

在这个例子中，我们使用 `new Promise()` 创建了一个 Promise 对象，并在其中编写了 AJAX 请求的代码。在请求完成时，我们使用 `resolve()` 方法将响应数据传递给 `.then()` 方法，如果请求失败，我们使用 `reject()` 方法将错误信息传递给 `.catch()` 方法。这样，我们就可以方便地处理 AJAX 请求中的错误和响应数据，使代码更加清晰和易于维护。


## reject里面是一个对象直接返回this.statusText是不是也可以
您可以在 `reject` 方法中直接返回 `this.statusText`，但这样会丢失一些错误信息，因为 `this.statusText` 只包含 HTTP 状态文本，而不包含详细的错误信息。因此，建议将错误信息封装在一个 Error 对象中，以便更好地管理和处理错误。

`Error` 对象可以包含错误的名称、消息和堆栈跟踪信息，这些信息可以帮助您更好地理解和解决错误。例如，以下是一个包含错误信息的 Error 对象的示例：

```javascript
const error = new Error('请求失败：404 Not Found');
error.name = 'RequestError';
error.code = 404;
throw error;
```

![[Pasted image 20230615223810.png]]

在这个例子中，我们创建了一个包含错误信息的 Error 对象，并设置了它的名称和代码。这样，我们就可以在错误处理程序中更好地识别和处理不同类型的错误。

在您的代码中，`reject` 方法接受一个 Error 对象作为参数，因此建议使用 `new Error()` 创建一个新的 Error 对象，并将错误信息作为参数传递给它。这样，您就可以在错误处理程序中获取到更详细的错误信息，帮助您更好地解决问题。


## Error对象的属性
`Error` 对象是 JavaScript 中用于表示错误的内置对象，它可以包含错误的名称、消息和堆栈跟踪信息等属性。以下是一些常见的 `Error` 对象的属性：

1. `name`：表示错误的名称，通常是一个字符串。例如，`SyntaxError`、`TypeError`、`ReferenceError` 等都是 `Error` 对象的子类，它们的 `name` 属性分别为 `"SyntaxError"`、`"TypeError"`、`"ReferenceError"` 等。

2. `message`：表示错误的详细消息，通常是一个字符串。可以通过在 `Error` 对象的构造函数中传递一个字符串参数来设置错误消息。

3. `stack`：表示错误的堆栈跟踪信息，通常是一个字符串。堆栈跟踪信息包含了错误发生时函数的调用栈，可以帮助开发者定位错误的原因和位置。

4. `fileName`：表示引发错误的文件名。在浏览器中，通常是包含错误的脚本文件名；在 Node.js 等环境中，通常是包含错误的模块文件名。

5. `lineNumber`：表示引发错误的代码行号，通常是一个整数。

6. `columnNumber`：表示引发错误的代码列号，通常是一个整数。

7. `stackTraceLimit`：表示堆栈跟踪信息的最大深度。默认情况下，堆栈跟踪信息的深度是 10 层，可以通过设置该属性来改变最大深度。

例如，以下是一个自定义的 `Error` 对象的示例：

```javascript
class MyError extends Error {
  constructor(message) {
    super(message);
    this.name = 'MyError';
    this.code = 500;
  }
}

const error = new MyError('请求失败：服务器内部错误');
console.log(error.name); // "MyError"
console.log(error.message); // "请求失败：服务器内部错误"
console.log(error.stack); // 堆栈跟踪信息
console.log(error.code); // 500
```

在这个例子中，我们创建了一个自定义的 `Error` 对象，并设置了它的名称、消息和代码等属性。这些属性可以帮助我们更好地管理和处理错误。

`code` 属性是 `Error` 对象的一个自定义属性，它可以用于存储错误代码或状态码等信息。 `code` 属性通常是一个数字，用于标识不同类型的错误或状态。

在 JavaScript 中，`Error` 对象的构造函数接受一个消息字符串作为参数，该字符串通常用于描述错误的详细信息。但是，如果需要在错误中存储更多的信息，例如错误代码、状态码等，可以将它们存储在 `Error` 对象的自定义属性中，例如 `code` 属性。

例如，以下是一个自定义的 `Error` 对象的示例，其中包含了一个 `code` 属性：

```javascript
class APIError extends Error {
  constructor(message, code) {
    super(message);
    this.name = 'APIError';
    this.code = code;
  }
}

const error = new APIError('请求失败：服务器内部错误', 500);
console.log(error.code); // 500
```

在这个例子中，我们创建了一个名为 `APIError` 的自定义 `Error` 对象，并在构造函数中设置了 `code` 属性。这样，我们就可以在错误处理程序中获取到错误的代码，并根据不同的错误代码进行处理。

需要注意的是，`code` 属性是一个自定义属性，它并不是 `Error` 对象的标准属性，因此在不同的环境中，`Error` 对象可能没有 `code` 属性或者将其定义为其他名称。