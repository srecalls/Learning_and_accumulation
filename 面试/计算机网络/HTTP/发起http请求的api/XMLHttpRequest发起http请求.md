# XMLHttpRequest发起http请求
好的，以下是使用XMLHttpRequest（XHR）对象发起HTTP请求的全部语法，包括创建、打开、发送和处理响应：

1. 创建 XMLHttpRequest 对象：

   ```javascript
   var xhr = new XMLHttpRequest();
   ```

2. 打开 HTTP 请求：

   ```javascript
   xhr.open(method, url, async, user, password);
   ```

   参数说明：

   - `method`：HTTP 请求方法，可以是 `"GET"`、`"POST"` 等
   - `url`：请求的 URL 地址
   - `async`：是否使用异步模式，默认为 `true`
   - `user`：可选，用户名
   - `password`：可选，密码

3. 设置请求头部（可选）：

   ```javascript
   xhr.setRequestHeader(header, value);
   ```

   参数说明：

   - `header`：请求头部字段名
   - `value`：请求头部字段值

4. 发送 HTTP 请求：

   ```javascript
   xhr.send(data);
   ```

   参数说明：

   - `data`：可选，要发送的数据，可以是字符串或者 FormData 对象等

5. 监听响应状态变化：

   ```javascript
   xhr.onreadystatechange = function() {
     if (xhr.readyState === XMLHttpRequest.DONE) {
       // 处理响应
       if (xhr.status === 200) {
         console.log(xhr.responseText);
       } else {
         console.log('Error: ' + xhr.status);
       }
     }
   };
   ```

   监听 `readystatechange` 事件，并在状态变化时进行处理。`readyState` 表示请求的当前状态，`XMLHttpRequest.DONE` 表示请求已完成。`status` 属性包含服务器响应的 HTTP 状态代码，如 `200` 表示成功，`404` 表示未找到请求的资源等。`responseText` 属性包含服务器响应的文本。

完整代码示例：

```javascript
var xhr = new XMLHttpRequest();
xhr.open('GET', 'https://example.com/api/data', true);
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.onreadystatechange = function() {
  if (xhr.readyState === XMLHttpRequest.DONE) {
    if (xhr.status === 200) {
      console.log(xhr.responseText);
      // 返回的是字符串
      // 需要JSON.parse对其进行转换
    } else {
      console.log('Error: ' + xhr.status);
    }
  }
};
xhr.send();
```

注意：在进行跨域请求时，需要注意浏览器的安全限制，可以使用 CORS（跨源资源共享）或 JSONP 等技术来解决跨域问题。此外，还需要注意请求的安全性，避免在请求中包含敏感信息。
![[Pasted image 20230615210631.png]]
这个是200里面的console.log
![[Pasted image 20230615210615.png]]

## XMLHttpRequest对象的常用属性和方法的介绍

![[Pasted image 20230615204332.png]]

![[Pasted image 20230615205134.png]]

以下是XMLHttpRequest对象的常用属性和方法的介绍：

属性：

1. `onabort`：当请求被取消时触发的事件处理程序。
2. `onerror`：当请求失败时触发的事件处理程序。
3. `onload`：当请求成功完成时触发的事件处理程序。
4. `onloadend`：当请求完成时，无论成功或失败，都会触发的事件处理程序。
5. `onloadstart`：当请求开始时触发的事件处理程序。
6. `onprogress`：当请求正在进行中时触发的事件处理程序。
7. `onreadystatechange`：状态变化时的回调函数。
8. `readyState`：当前请求的状态，取值为0到4，0表示未初始化，1表示已调用open方法，2表示已发送请求，3表示正在接收数据，4表示数据接收完成。
9. `response`：响应体的数据类型为ArrayBuffer、Blob、Document或JSON对象等。
10. `responseText`：响应体的文本内容。
11. `responseType`：响应体的数据类型，可取值为""、"arraybuffer"、"blob"、"document"、"json"、"text"。
12. `responseURL`：响应的URL。
13. `responseXML`：响应体的XML DOM对象。
14. `status`：HTTP响应状态码，如200表示成功，404表示未找到资源等。
15. `statusText`：HTTP响应状态码的文本描述。
16. `timeout`：请求超时时间，单位为毫秒。
17. `upload`：XMLHttpRequestUpload对象，用于上传数据时的事件处理。

方法：

1. `abort()`：取消当前请求。
2. `getAllResponseHeaders()`：返回所有响应头部。
3. `getResponseHeader(headerName)`：返回指定响应头部的值。
4. `open(method, url, async, user, password)`：初始化请求，指定HTTP请求方法、URL地址、是否异步以及用户名和密码。
5. `send(data)`：发送HTTP请求，可以携带数据。
6. `setRequestHeader(headerName, headerValue)`：设置HTTP请求头部。
[[HTTP协议规定的协议头和请求头有什么]]

以上就是XMLHttpRequest对象的常用属性和方法的介绍。


## responseType 和 responseText
  
	test5.html:23 Uncaught DOMException: Failed to read the 'responseText' property from 'XMLHttpRequest': The value is only accessible if the object's 'responseType' is '' or 'text' (was 'json').

这个错误意味着您正在尝试从一个响应类型为 JSON 的 XMLHttpRequest 对象中读取 `responseText` 属性，但是 `responseType` 属性被设置为 `json`，这使得 `responseText` 属性不可读。

默认情况下，XMLHttpRequest 对象的 `responseType` 属性是空字符串，这表示响应类型是文本。在这种情况下，可以使用 `responseText` 属性来获取响应内容。例如：

```javascript
const xhr = new XMLHttpRequest();
xhr.open('GET', '/api/users');
xhr.send();
xhr.onload = function() {
  console.log(xhr.responseText);
};
```

在这个例子中，我们发送了一个 GET 请求，然后在 `onload` 事件处理程序中使用 `responseText` 属性来获取响应文本。

但是，如果您将 `responseType` 属性设置为 `json`，则必须使用 `response` 属性来获取 JSON 格式的响应。例如：

```javascript
const xhr = new XMLHttpRequest();
xhr.open('GET', '/api/users');
xhr.responseType = 'json';
xhr.send();
xhr.onload = function() {
  console.log(xhr.response);
};
```

在这个例子中，我们将 `responseType` 属性设置为 `json`，然后在 `onload` 事件处理程序中使用 `response` 属性来获取响应数据。注意，这里不能使用 `responseText` 属性，因为它只能读取响应类型为文本的响应。

如果您需要将响应类型设置为 JSON，您可以使用 `JSON.parse()` 方法将 `responseText` 属性转换为 JSON 对象。例如：

```javascript
const xhr = new XMLHttpRequest();
xhr.open('GET', '/api/users');
xhr.responseType = 'text';
xhr.send();
xhr.onload = function() {
  const data = JSON.parse(xhr.responseText);
  console.log(data);
};
```

在这个例子中，我们将 `responseType` 属性设置为 `text`，然后在 `onload` 事件处理程序中使用 `JSON.parse()` 方法将响应文本解析为 JSON 对象。

## post请求通过send发送参数

`xhr.send()` 方法用于发送 HTTP 请求。它可以接受一个可选的参数，用于设置请求体中的数据。如果请求是 GET 或 HEAD 方法，或者没有请求体数据，那么该参数应该设置为 `null`。

如果请求是 POST、PUT、DELETE 等方法，或者需要发送请求体数据，那么可以将请求体数据作为 `send()` 方法的参数传递。具体来说，这个参数可以是以下类型之一：

- 字符串：表示请求体数据的字符串，例如 `"username=johndoe&password=123456"`。
- FormData 对象：表示包含表单字段和值的数据，可以使用 `new FormData()` 创建。
- Blob 对象：表示二进制数据，例如图片或视频。
- ArrayBuffer 或 ArrayBufferView 对象：表示原始二进制数据。

例如，以下代码示例使用 POST 方法发送 JSON 格式的数据：

```javascript
const xhr = new XMLHttpRequest();
xhr.open('POST', '/api/users');
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.send(JSON.stringify({
  name: 'John Doe',
  email: 'john.doe@example.com'
}));
```

在这个例子中，我们将 JSON 格式的数据作为字符串传递给 `send()` 方法。在发送请求之前，我们使用 `setRequestHeader()` 方法设置了 "Content-Type" 字段为 "application/json"，表示请求体中的数据是 JSON 格式的。

##   XMLHttpRequest有DONE这个属性吗
是的，XMLHttpRequest对象有一个名为 `readyState` 的属性，它表示请求的当前状态。`readyState` 属性的值是一个整数，它可以取以下五个值中的一个：

- `0` (UNSENT)：XMLHttpRequest对象已被创建，但尚未调用 `open()` 方法。
- `1` (OPENED)：`open()` 方法已经被调用，但请求尚未被发送。在这个状态下，您可以通过 `setRequestHeader()` 方法设置请求头，但不能访问响应头和响应数据。
- `2` (HEADERS_RECEIVED)：请求头已经被接收，响应头也已经可用。在这个状态下，您可以通过 `getResponseHeader()` 方法访问响应头，但不能访问响应数据。
- `3` (LOADING)：响应数据正在接收中。在这个状态下，您可以通过 `responseText` 或 `responseXML` 属性访问部分响应数据。
- `4` (DONE)：响应数据已经被完全接收。在这个状态下，您可以通过 `responseText` 或 `responseXML` 属性访问完整的响应数据。

因此，`readyState` 属性可以用来判断 XMLHttpRequest 对象的状态，以便在不同的状态下采取不同的操作。例如，在 `readyState` 的值变为 `4` (DONE) 时，可以在 `onreadystatechange` 回调函数中获取响应数据。