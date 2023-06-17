下面是使用不同的 HTTP 方法和配置选项发起 HTTP 请求的完整语法，以及如何处理响应和错误：


```js
// 创建一个模拟的 Response 对象
const response = {
    status: 200,
    data: "Hello, World!",
};

// 创建一个已经 resolved 的 Promise 对象
const myPromise = new Promise((resolve) => {
    // 在这里 resolve 一个 Response 对象
    resolve(response);
});

// 使用 .then() 处理 resolved 的 Promise 对象
myPromise
    .then((resolvedResponse) => {
        console.log("Promise resolved with: ", resolvedResponse);
    })
    .catch((error) => {
        console.error("Promise rejected with: ", error);
    });
```

### 发起 GET 请求

```javascript
fetch(url, {
  method: 'GET',
  headers: {
    // 请求头
  }
})
.then(response => {
  if (response.ok) {
    // 处理成功响应
    return response.json(); // 将响应数据解析为 JSON 格式
  } else {
    // 处理错误响应
    throw new Error('Network response was not ok');
  }
})
.then(data => {
  // 处理响应数据
})
.catch(error => {
  // 处理错误
});
```

在这个例子中，我们使用 `fetch()` 函数发起一个 HTTP GET 请求，可以在 `headers` 选项中添加请求头，例如设置 `Content-Type` 或 `Authorization`。在 `then()` 回调函数中，我们检查响应对象的状态码是否为 200，如果是，则使用 `response.json()` 方法将响应数据解析为 JSON 格式，并将解析后的数据传递给下一个 `then()` 回调函数进行处理。如果响应状态码不是 200，则抛出一个错误对象，进入 `catch()` 回调函数进行处理。

![[Pasted image 20230615212641.png]]
![[Pasted image 20230615212754.png]]


### 具体例子
当然，下面是一个使用 `fetch()` 函数发起 HTTP GET 请求的具体代码示例：

```javascript
fetch('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Network response was not ok');
    }
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Error:', error);
  });
```

在这个示例中，我们使用 `fetch()` 函数发起一个 HTTP GET 请求，获取 `https://jsonplaceholder.typicode.com/posts/1` 的响应数据。在 `then()` 回调函数中，我们检查响应对象的状态码是否为 200，如果是，则使用 `response.json()` 方法将响应数据解析为 JSON 格式，并将解析后的数据传递给下一个 `then()` 回调函数进行处理。如果响应状态码不是 200，则抛出一个错误对象，进入 `catch()` 回调函数进行处理。在 `catch()` 回调函数中，我们打印错误信息到控制台。

您可以将上述代码复制到任何支持 JavaScript 的环境中（例如浏览器控制台或 Node.js），然后运行它来查看它的输出。请注意，在运行此代码之前，您需要确保您的环境已经连接到互联网。

### 发起 POST 请求

```javascript
fetch(url, {
  method: 'POST',
  headers: {
    // 请求头
  },
  body: JSON.stringify({
    // 请求体
  })
})
.then(response => {
  if (response.ok) {
    // 处理成功响应
    return response.json(); // 将响应数据解析为 JSON 格式
  } else {
    // 处理错误响应
    throw new Error('Network response was not ok');
  }
})
.then(data => {
  // 处理响应数据
})
.catch(error => {
  // 处理错误
});
```

在这个例子中，我们使用 `fetch()` 函数发起一个 HTTP POST 请求，可以在 `headers` 选项中添加请求头，例如设置 `Content-Type` 或 `Authorization`。在 `body` 选项中添加请求体，可以是一个字符串或一个 JavaScript 对象。在 `then()` 回调函数中，我们检查响应对象的状态码是否为 200，如果是，则使用 `response.json()` 方法将响应数据解析为 JSON 格式，并将解析后的数据传递给下一个 `then()` 回调函数进行处理。如果响应状态码不是 200，则抛出一个错误对象，进入 `catch()` 回调函数进行处理。

### 处理响应数据

在 `then()` 回调函数中，我们可以使用 `response` 对象的方法和属性来处理响应数据，例如：

- `response.json()`：将响应数据解析为 JSON 格式，返回一个 Promise 对象。
- `response.text()`：将响应数据解析为文本格式，返回一个 Promise 对象。
- `response.blob()`：将响应数据解析为二进制数据，返回一个 Promise 对象。
- `response.arrayBuffer()`：将响应数据解析为 ArrayBuffer 格式，返回一个 Promise 对象。
- `response.headers`：响应头对象，可以使用 `get()` 方法获取特定的响应头。
- `response.status`：响应状态码，例如 200、404、500 等。
- `response.statusText`：响应状态描述，例如 OK、Not Found、Internal Server Error 等。

### 处理错误

在 `catch()` 回调函数中，我们可以处理网络错误、请求超时、服务器错误、JSON 解析错误等错误，例如：

```javascript
.catch(error => {
  if (error instanceof TypeError) {
    // 处理网络错误或请求超时
  } else {
    // 处理服务器响应错误或 JSON 解析错误
  }
});
```

在这个例子中，我们检查错误对象的类型，如果是 `TypeError`，则处理网络错误或请求超时；否则，处理服务器响应错误或 JSON 解析错误。在实际开发中，您可以根据具体的错误信息来处理错误。