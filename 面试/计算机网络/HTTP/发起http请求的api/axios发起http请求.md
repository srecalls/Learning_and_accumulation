Axios 是一个基于 Promise 的 HTTP 客户端，可以用于浏览器和 Node.js。它提供了许多可选参数，使您可以定制您的 HTTP 请求。下面是使用 Axios 发起 HTTP 请求的基本语法和一些常用的配置选项：

```javascript
axios({
  method: 'get', // 请求方法，默认为 get
  url: 'https://jsonplaceholder.typicode.com/posts/1', // 请求地址
  params: { // 请求参数，会被自动转换为查询字符串 (比如 ?id=1&name=test)
    id: 1,
    name: 'test'
  },
  headers: { // 请求头
    'Content-Type': 'application/json'
  },
  data: { // 请求体
    username: 'test',
    password: '123456'
  },
  responseType: 'json', // 响应数据类型，可以是 'arraybuffer'、'blob'、'document'、'json'、'text' 等，默认为 'json'
})
.then(response => {
  console.log(response.data); // 响应数据
})
.catch(error => {
  console.error(error); // 错误信息
});
```

在这个示例中，我们使用 Axios 发起一个 HTTP GET 请求，获取 `https://jsonplaceholder.typicode.com/posts/1` 的响应数据。我们指定了请求方法为 GET，请求地址为 `https://jsonplaceholder.typicode.com/posts/1`，请求参数为 `{id: 1, name: 'test'}`，请求头为 `{ 'Content-Type': 'application/json' }`，请求体为 `{ username: 'test', password: '123456' }`。我们还指定了响应数据类型为 JSON。

在请求成功时，我们使用 `then()` 回调函数访问响应对象，打印响应数据到控制台。在请求失败时，我们使用 `catch()` 回调函数捕获错误对象，打印错误信息到控制台。

这只是 Axios 请求的一个简单示例，您可以根据实际需要使用其他配置选项来完全定制您的请求。

[[params和query的区别]]
## params和data的区别
`params` 和 `data` 是 Axios 中用于传递请求参数的两个不同的选项。

`params` 选项用于传递 URL 查询参数，即将参数编码为查询字符串并附加到 URL 的末尾，例如 `http://example.com/?param1=value1&param2=value2`。这些参数通常在 GET 请求中使用，例如：

```javascript
axios({
  method: 'get',
  url: 'https://jsonplaceholder.typicode.com/posts',
  params: {
    userId: 1
  }
})
.then(response => {
  console.log(response.data);
})
.catch(error => {
  console.error(error);
});
```

在这个示例中，我们使用 `params` 选项将 `userId` 参数设置为 1，它将自动编码为查询字符串并附加到 URL 的末尾，即 `https://jsonplaceholder.typicode.com/posts?userId=1`。

`data` 选项用于传递请求体数据，即将数据封装在请求体中发送给服务器。这些参数通常在 POST、PUT、PATCH 等请求中使用，例如：

```javascript
axios({
  method: 'post',
  url: 'https://jsonplaceholder.typicode.com/posts',
  data: {
    title: 'foo',
    body: 'bar',
    userId: 1
  }
})
.then(response => {
  console.log(response.data);
})
.catch(error => {
  console.error(error);
});
```

在这个示例中，我们使用 `data` 选项将请求体数据设置为 `{ title: 'foo', body: 'bar', userId: 1 }`，它将被封装在请求体中发送给服务器。

因此，`params` 和 `data` 的区别在于它们所处的位置和用途。`params` 用于传递 URL 查询参数，而 `data` 用于传递请求体数据。


## params、query、data的关系
`params`、`query` 和 `data` 这三个概念都与 HTTP 请求中的参数相关，但它们在不同的上下文中使用，具有不同的含义。

在 RESTful API 中，通常使用 `params` 和 `query` 来表示不同的参数类型：

- `params`：表示请求路径中的参数，通常是用来标识资源的唯一标识符。例如，在以下 URL 中，`:id` 就是一个 `params` 参数：

  ```
  https://example.com/api/users/:id
  ```

- `query`：表示请求路径中的查询参数，通常用来过滤、排序或分页资源。例如，在以下 URL 中，`?page=2` 就是一个 `query` 参数：

  ```
  https://example.com/api/users?page=2
  ```

在 Axios 中，`params` 和 `data` 选项用于传递请求参数，而不是 `query`。`params` 选项表示将参数编码为 URL 查询参数，并将其附加到请求 URL 的末尾。例如：

```javascript
axios({
  method: 'get',
  url: 'https://example.com/api/users',
  params: {
    page: 2
  }
})
.then(response => {
  console.log(response.data);
})
.catch(error => {
  console.error(error);
});
```

在这个示例中，我们使用 `params` 选项将 `page` 参数设置为 2，它将自动编码为查询字符串并附加到 URL 的末尾，即 `https://example.com/api/users?page=2`。

`data` 选项表示请求体中的数据，通常在 POST、PUT、PATCH 等请求中使用。例如：

```javascript
axios({
  method: 'post',
  url: 'https://example.com/api/users',
  data: {
    name: 'John Doe',
    email: 'john.doe@example.com'
  }
})
.then(response => {
  console.log(response.data);
})
.catch(error => {
  console.error(error);
});
```

在这个示例中，我们使用 `data` 选项将请求体数据设置为 `{ name: 'John Doe', email: 'john.doe@example.com' }`，它将被封装在请求体中发送给服务器。

因此，`params`、`query` 和 `data` 都是用于在 HTTP 请求中传递参数的选项，但它们的含义和用法略有不同。



是的，您可以这样理解：在 RESTful API 中，`params` 和 `query` 是用来传递 API 请求的参数，而在 HTTP 请求中，`params` 和 `data` 是用来传递 HTTP 请求的参数。

在 RESTful API 中，`params` 和 `query` 通常用来标识和过滤资源，例如：

```javascript
// 获取用户信息的 API
GET /api/users/:id

// 获取用户列表的 API，支持分页和排序
GET /api/users?page=2&sort=name
```

在这里，`:id` 是一个 `params` 参数，它用来标识一个用户的唯一标识符；`page` 和 `sort` 是 `query` 参数，它们用来过滤和排序用户列表。

在 HTTP 请求中，`params` 和 `data` 用于传递请求的参数和数据，例如：

```javascript
// 使用 GET 方法获取用户信息
axios.get('/api/users', {
  params: {
    id: 123
  }
})
.then(response => {
  console.log(response.data);
})
.catch(error => {
  console.error(error);
});

// 使用 POST 方法创建用户
axios.post('/api/users', {
  name: 'John Doe',
  email: 'john.doe@example.com'
})
.then(response => {
  console.log(response.data);
})
.catch(error => {
  console.error(error);
});
```

在这里，`params` 用于传递 GET 请求的参数，`data` 用于传递 POST 请求的数据。注意，这里的 `params` 和 `data` 是 Axios 中的选项，不同的 HTTP 客户端库可能会使用不同的术语来表示类似的概念。