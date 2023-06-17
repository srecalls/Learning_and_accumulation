##   AJAX 怎么发起请求
在使用AJAX发起请求时，需要通过JavaScript代码调用XMLHttpRequest对象来实现。以下是一个基本的AJAX请求示例：

```javascript
// 创建XMLHttpRequest对象
var xhr = new XMLHttpRequest();

// 配置请求参数
xhr.open('GET', 'http://example.com/api/data', true);

// 设置响应类型
xhr.responseType = 'json';

// 发送请求
xhr.send();

// 监听请求状态变化
xhr.onreadystatechange = function() {
  if (xhr.readyState === XMLHttpRequest.DONE) {
    if (xhr.status === 200) {
      // 请求成功
      console.log(xhr.response);
    } else {
      // 请求失败
      console.error(xhr.statusText);
    }
  }
};
```

在上面的代码中，首先通过`XMLHttpRequest`对象创建了一个AJAX请求实例，然后使用`open`方法配置了请求参数，包括请求的URL、请求方式（GET或POST）、是否异步等。接着设置了响应类型为JSON，然后调用`send`方法发送了请求。

在发送请求之后，需要监听`XMLHttpRequest`对象的`onreadystatechange`事件，该事件会在请求状态发生变化时触发。在监听函数中，可以检查`readyState`和`status`属性，以判断请求是否成功。当`readyState`为`XMLHttpRequest.DONE`时，表示请求已完成，此时可以根据`status`属性的值来判断请求的结果，如果是200，则请求成功，可以通过`response`属性来获取响应数据。

需要注意的是，AJAX请求是异步的，即在发送请求之后，JavaScript代码会继续执行，不会等待响应返回。因此，在处理响应数据时需要在`onreadystatechange`事件监听函数中处理。