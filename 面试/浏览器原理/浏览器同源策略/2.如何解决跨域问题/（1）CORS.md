## （1）CORS
下面是MDN对于CORS的定义:

	跨域资源共享(CORS)是一种机制，它使用额外的 HTTP头 来告诉浏览器让运行在一个origin (domain)上的Web应用被准许访问来自不同源服务器上的指定的资源。当一个资源从与该资源本身所在的服务器不同的域、协议或端口请求一个资源时，资源会发起一个跨域HTTP请求。


CORS需要浏览器和服务器同时支持，整个CORS过程都是浏览器完成的，无需用户参与。因此实现**CORS的关键就是服务器，只要服务器实现了CORS请求**，就可以跨源通信了。
浏览器将CORS分为**简单请求**和**非简单请求**:

简单请求不会触发CORS预检请求。若该请求满足以下两个条件，就可以看作是简单请求:
**1)请求方法是以下三种方法之一:**
- HEAD
- GET
- POST
**2)HTTP的头信息不超出以下几种字段:**
- Accept
- Accept-Language
- Content-Language
- Last-Event-ID
- Content-Type:只限于三个值application/x-www-form-urlencoded、multipart/form-data、text/plain若不满足以上条件，就属于非简单请求了。

### （1）简单请求过程
对于简单请求，浏览器会直接发出CORS请求，它会在请求的头信息中增加一个Orign字段，该字段用来说明本次请求来自哪个源（协议+端口+域名)，服务器会根据这个值来决定是否同意这次请求。如果Orign指定的域名在许可范围之内，**服务器返回的响应**就会多出以下信息头:

```js
Access-Control-Allow-origin: http://api.bob.com // 和orign一致
Access-Control-Allow-Credentials: true // 表示是否允许发送Cookie
Access-Control-Expose-Headers: FooBar // 指定返回其他字段的值
Content-Type: text/html; charset=utf-8 // 表示文档类型
```

如果orign指定的域名不在许可范围之内，服务器会返回一个正常的HTTP回应，浏览器发现没有上面的Access-Control-Allow-Origin头部信息，就知道出错了。这个错误无法通过状态码识别，因为返回的状态码可能是200.

**在简单请求中，在服务器内，至少需要设置字段:**
`Access-Control-Allow-Origin`

#### JavaScript在客户端发起CORS跨域请求的简单示例：
下面是一个使用JavaScript在客户端发起CORS跨域请求的简单示例：

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>CORS简单请求示例</title>
</head>
<body>
  <button onclick="sendRequest()">发送请求</button>
  <script>
    function sendRequest() {
      // 创建XMLHttpRequest对象
      var xhr = new XMLHttpRequest();
      
      // 设置请求方法和请求地址
      xhr.open('GET', 'http://example.com/api/data', true);
      
      // 设置请求头，指定数据类型
      xhr.setRequestHeader('Content-Type', 'application/json');
      
      // 发送请求
      xhr.send();
      
      // 监听请求状态变化
      xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
          if (xhr.status === 200) {
            // 请求成功，处理返回数据
            console.log(xhr.responseText);
          } else {
            // 请求失败，处理错误信息
            console.error('请求失败');
          }
        }
      };
    }
  </script>
</body>
</html>
```

在这个示例中，客户端使用XMLHttpRequest对象发起了一个GET请求，请求地址为`http://example.com/api/data`，请求头中指定了数据类型为JSON格式。由于请求地址和客户端网页所在的域名不同，因此会触发CORS跨域请求。

服务端需要在响应头中添加`Access-Control-Allow-Origin`字段来允许来自客户端网页所在域名的跨域请求。在这个示例中，服务端需要响应以下HTTP头信息：

```js
Access-Control-Allow-Origin: http://example.com
Access-Control-Allow-Methods: GET, POST
Access-Control-Allow-Headers: Content-Type
```

其中，`Access-Control-Allow-Origin`字段指定了允许跨域请求的来源，这里设置为`http://example.com`，表示只允许来自该域名的请求。`Access-Control-Allow-Methods`字段指定了允许的请求方法，这里设置为`GET`和`POST`，表示只允许这两种请求方法。`Access-Control-Allow-Headers`字段指定了允许的请求头，这里设置为`Content-Type`，表示只允许指定的数据类型。

当服务端正确设置了响应头后，客户端就可以发起CORS跨域请求，并在收到响应后处理返回数据。注意，CORS跨域请求可能会带来一些安全风险，因此需要在服务端进行一定的防护措施，例如限制允许跨域请求的来源、请求方法和请求头等。

### （2）非简单请求过程
非简单请求是对服务器有特殊要求的请求，比如请求方法为` DELETE `或者` PUT `等。非简单请求的` CORS `请求会在正式通信之前进行一次` HTTP `查询请求，称为**预检请求**。

浏览器会询问服务器，当前所在的网页是否在服务器允许访问的范围内，以及可以使用哪些HTTP请求方式和头信息字段，只有得到肯定的回复，才会进行正式的HTTP请求，否则就会报错。

预检请求使用的**请求方法是OPTIONS**，表示这个请求是来询问的。他的头信息中的关键字段是Orign，表示请求来自哪个源。除此之外，头信息中还包括两个字段:
- Access-Control-Request-Method:该字段是必须的，用来列出浏览器的CORS请求会用到哪些HTTP方法。
- Access-Control-Request-Headers:该字段是一个逗号分隔的字符串，指定浏览器CORS请求会额外发送的头信息字段。

服务器在收到浏览器的预检请求之后，会根据头信息的三个字段来进行判断，如果返回的头信息在中有Access-Control-Allow-Origin这个字段就是**允许跨域请求**，如果没有，就是**不同意这个预检请求，就会报错。**

服务器回应的CORS的字段如下:
```js
Access-Control-Allow-origin: http://api.bob.com // 允许跨域的源地址
Access-Control-Allow-Methods: GET,POST,PUT // 服务器支持的所有跨域请求的方法Access-Control-Allow-Headers: x-Custom-Header // 服务器支持的所有头信息字段Access-Control-Allow-Credentials: true // 表示是否允许发送Cookie
Access-control-Max-Age: 1728000 // 用来指定本次预检请求的有效期，单位为秒
```

只要服务器通过了预检请求，在以后每次的CORS请求都会自带一个Origin头信息字段。服务器的回应，也都会有一个` Access-Control-Allow-Origin `头信息字段。

**在非简单请求中，服务器至少需要设置以下字段:**

```js
'Access-Control-Allow-origin'
'Access-Control-Allow-Methods'
'Access-Control-Allow-Headers'
```

####  JavaScript在客户端发起CORS跨域请求的非简单请求示例

下面是一个使用JavaScript在客户端发起CORS跨域请求的非简单请求示例：

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>CORS非简单请求示例</title>
</head>
<body>
  <button onclick="sendRequest()">发送请求</button>
  <script>
    function sendRequest() {
      // 创建XMLHttpRequest对象
      var xhr = new XMLHttpRequest();
      
      // 设置请求方法和请求地址
      xhr.open('POST', 'http://example.com/api/data', true);
      
      // 设置请求头，指定数据类型和自定义头信息
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.setRequestHeader('X-Custom-Header', 'custom value');
      
      // 设置请求体，包含JSON格式数据
      var data = { name: 'John', age: 30 };
      xhr.send(JSON.stringify(data));
      
      // 监听请求状态变化
      xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
          if (xhr.status === 200) {
            // 请求成功，处理返回数据
            console.log(xhr.responseText);
          } else {
            // 请求失败，处理错误信息
            console.error('请求失败');
          }
        }
      };
    }
  </script>
</body>
</html>
```

在这个示例中，客户端使用XMLHttpRequest对象发起了一个POST请求，请求地址为`http://example.com/api/data`，请求头中指定了数据类型为JSON格式，并且添**加了一个自定义的请求头**`X-Custom-Header`。此外，客户端还向服务端发送了一个JSON格式的请求体，包含了一个名为`name`的字段和一个名为`age`的字段。

由于请求头中包含了自定义的请求头信息，因此这个请求不属于CORS跨域请求的简单请求，需要进行预检。客户端会先发送一个**OPTIONS请求**，询问服务端是否允许跨域请求，并携带了一些预检请求头信息。服务端需要在响应中设置`Access-Control-Allow-Origin`等响应头信息，并允许预检请求头中携带的信息。只有当服务端正确响应了预检请求后，客户端才会发送正式的POST请求。

服务端需要在响应头中设置以下字段来允许CORS跨域请求：

```
Access-Control-Allow-Origin: http://example.com
Access-Control-Allow-Methods: POST
Access-Control-Allow-Headers: Content-Type, X-Custom-Header
Access-Control-Max-Age: 86400
```

其中，`Access-Control-Allow-Origin`字段指定了允许跨域请求的来源，这里设置为`http://example.com`，表示只允许来自该域名的请求。`Access-Control-Allow-Methods`字段指定了允许的请求方法，这里设置为`POST`，表示只允许POST请求。`Access-Control-Allow-Headers`字段指定了允许的请求头，这里设置为`Content-Type`和`X-Custom-Header`，表示允许这两个请求头。`Access-Control-Max-Age`字段指定了预检请求的有效期，这里设置为86400秒（一天），表示在这个时间段内不需要再进行预检请求。

当服务端正确设置了响应头后，客户端就可以发起CORS跨域请求，并在收到响应后处理返回数据。注意，CORS跨域请求可能会带来一些安全风险，因此需要在服务端进行一定的防护措施，例如限制允许跨域请求的来源、请求方法和请求头等。

#### 减少OTIONS请求次数
OPTIONS请求次数过多就会损耗页面加载的性能，降低用户体验度。所以尽量要减少OPTIONS请求次数，可以后端在请求的返回头部添加: 
` Access-Control-Max-Age: number `
它表示预检请求的返回结果可以被缓存多久，单位是秒。该字段只对完全一样的URL的缓存设置生效，所以设置了缓存时间，在这个时间范围内，再次发送请求就不需要进行预检请求了。

#### CORS中Cookie相关问题
在CORS请求中，如果想要传递Cookie，就要满足以下三个条件:
- **在请求中设置withcredentials**

默认情况下在跨域请求，浏览器是不带cookie 的。但是我们可以通过设置withCredentials来进行传递cookie.

```js
//原生 xml 的设置方式
var xhr = new XMLHttpRequest();
xhr.withcredentials = true; // axios 设置方式
axios.defaults.withcredentials = true;
```

- Access-Control-Allow-Credentials设置为true
- Access-Control-Allow-Origin设置为非*

### （3）CORS跨域请求失败情况

如果CORS跨域请求失败，可能会出现以下一些情况：

1. 服务端没有正确设置响应头。在CORS跨域请求中，服务端需要设置`Access-Control-Allow-Origin`等响应头信息来允许跨域请求。如果服务端没有正确设置响应头，浏览器就会拒绝跨域请求，导致请求失败。

2. 客户端请求头中包含了不被允许的字段。在CORS跨域请求中，浏览器会对请求头进行预检，检查请求头中是否包含了不被允许的字段。如果客户端请求头中包含了不被允许的字段，浏览器就会拒绝跨域请求，导致请求失败。

3. 客户端请求方法不被允许。在CORS跨域请求中，服务端需要设置`Access-Control-Allow-Methods`响应头来指定允许的请求方法。如果客户端请求方法不在允许的列表中，浏览器就会拒绝跨域请求，导致请求失败。

4. 客户端请求头中包含了敏感信息。在CORS跨域请求中，浏览器会对请求头进行预检，检查请求头中是否包含了敏感信息。如果客户端请求头中包含了敏感信息，浏览器就会拒绝跨域请求，导致请求失败。

5. 客户端网络连接不稳定。在跨域请求过程中，如果客户端网络连接不稳定，可能会导致请求失败。此时可以重试请求，或者检查网络连接是否正常。

6. 服务端出现了错误。在CORS跨域请求过程中，服务端可能会出现错误，例如请求处理超时、数据库连接失败等。此时可以检查服务端日志，或者联系服务端管理员进行排查。

在实际开发过程中，需要根据具体情况来排查CORS跨域请求失败的原因，并采取相应的措施来解决问题。