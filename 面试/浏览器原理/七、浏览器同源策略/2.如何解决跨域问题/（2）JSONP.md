

## （2）JSONP
jsonp的原理就是利用` <script> `标签没有跨域限制，通过` <script> `标签src属性，发送带有` callback `参数的` GET `请求，服务端将接口返回数据拼凑到` callback `函数中，返回给浏览器，浏览器解析执行，从而前端拿到` callback `函数返回的数据。

### （1）原生JS实现
```js
<script>
	var script = document.createElement('script')
	script.type = 'text/javascript'
	// 传参一个回调函数名后端, 方便后端返回时执行这个在前端定义的回调函数
	script.src = 'http://www.domain2.com:8080/login/user=admin&callback=handleCallback'
	document.head.appendChild(script)
	// 回调执行函数
	function handleCallback(res) {
		alert(JSON.stringify(res))
	}
</script>
```

服务端返回如下(返回时执行全局函数)

```js
handleCallback({"success": true, "user": "admin"})
```

#### 为什么服务端返回的callback会被浏览器执行

JSONP利用的是浏览器对`<script>`标签的跨域支持，而不是服务端的特殊处理。**浏览器在解析HTML页面时，如果遇到`<script>`标签，就会将标签的`src`属性指向的JavaScript文件下载下来，并在当前页面中执行该文件中的代码。**

在JSONP中，客户端通过`<script>`标签的`src`属性向服务端请求数据，并传递一个名为`callback`的参数，该参数的值是一个在客户端定义的JavaScript函数名。服务端在收到请求后，将数据封装在该函数中返回，例如：

```js
callback({ name: 'John', age: 30 });
```

浏览器在解析到该`<script>`标签时，会下载服务端返回的JavaScript文件，并在当前页面中执行其中的代码。由于客户端已经在页面中定义了名为`callback`的JavaScript函数，因此当浏览器执行服务端返回的JavaScript代码时，就会调用该函数，并将数据作为参数传递给它。客户端就可以在该函数中获取到数据，并进行处理。

因此，JSONP的原理是利用浏览器对`<script>`标签的跨域支持，通过在客户端定义一个回调函数，将服务端返回的数据作为回调函数的参数传递给客户端。

### （2）Vue axios实现
```js
this.$http = axios
this.$http.jsonp('http://www.domain2.com::8080/login', {
	params: {},
	jsonp: 'handleCallback'
}).then((res) => {
	console.log(res)
})
```

后端node.js代码
```node.js
var querystring = require('querystring')
var http = require('http')
var server = http.createServer()
server.on('request', function(req, res)) {
	  var fn = params.callback
	  // json返回设置
	  res.writeHead(200, {'Content-type': 'text/javascript'})
	  res.write(fn + '(' + JSON.stringify(params) + '）')
	  res.end()
}
```


#### Axios实现JSONP
Axios是一个基于Promise的HTTP客户端，可以用于浏览器和Node.js平台。它支持多种请求方式，包括GET、POST、PUT、DELETE等，并提供了丰富的配置选项和拦截器，使得开发者可以轻松地与后端API进行交互。

在Vue中使用Axios时，通常会将Axios实例挂载到Vue的原型上，以便在整个应用程序中使用。例如：

```js
import axios from 'axios'

Vue.prototype.$http = axios.create({
  baseURL: 'http://api.example.com',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
})
```

在这段代码中，我们使用`axios.create`方法创建了一个Axios实例，并将其挂载到Vue的原型上，命名为`$http`。我们还配置了一些选项，例如`baseURL`、`timeout`和`headers`，以便在发送请求时使用。

Axios支持使用JSONP发送跨域请求，通过设置`jsonp`选项为回调函数的名称，即可使用JSONP方式进行数据传输。例如：

```js
this.$http.jsonp('http://www.domain2.com::8080/login', {
  params: {},
  jsonp: 'handleCallback'
}).then((res) => {
  console.log(res)
})
```

在这段代码中，我们调用了Axios实例的`jsonp`方法，传递了请求的URL、参数和回调函数的名称。**Axios会在请求中自动添加一个名为`callback`的参数**，并将其值设置为回调函数的名称。当后端接收到请求后，将数据封装在回调函数中返回给前端，前端就可以通过回调函数来获取数据。

需要注意的是，由于JSONP存在一定的安全风险，因此在实际应用中应该尽量避免使用JSONP，而使用更为安全的跨域解决方案，例如CORS（Cross-Origin Resource Sharing）等技术。

#### node返回的数据
这段Node.js代码实现了一个JSONP接口的响应处理逻辑。它从请求中获取到参数`callback`的值，即回调函数的名称，然后将数据封装在该回调函数中返回给前端。

具体来说，返回的数据格式为`callback({data})`，其中`callback`就是从请求参数中获取到的回调函数的名称，`{data}`是一个JSON对象，包含了需要返回给前端的数据。在这段代码中，`params`应该是一个JSON对象，它被使用`JSON.stringify()`方法转换为字符串格式并封装在回调函数中返回给前端。

例如，如果`params`的值为`{ name: 'John', age: 30 }`，则返回的内容应该为：

```js
handleCallback({"name":"John","age":30})
```

其中，`handleCallback`就是从请求参数中获取到的回调函数的名称，`{"name":"John","age":30}`是一个JSON格式的字符串，包含了需要返回给前端的数据。当浏览器接收到该响应时，会自动执行名为`handleCallback`的JavaScript函数，并将数据作为参数传递给它。前端就可以在该函数中获取到数据，并进行处理。

####   后端传回的回调函数我前端不用定义吗

**Vue.js 中的 `jsonp` 方法使用了第三方库 Axios 来发送 JSONP 请求，Axios 会自动处理回调函数的定义和调用，因此客户端不需要显式地定义回调函数。**
是的，如果你使用的是 JSONP 请求方式，那么客户端**不需要显式地定义回调函数**，而是由后端来定义回调函数，客户端只需要指定回调函数的名称即可。

具体来说，当客户端发送 JSONP 请求时，需要在请求 URL 中指定一个名为 `callback` 的查询参数，该参数的值是一个由后端定义的回调函数名。例如，在以下代码中，回调函数的名称由后端定义为 `handleCallback`：

```js
this.$http.jsonp('http://www.domain2.com::8080/login', {
  params: {},
  jsonp: 'handleCallback'
}).then((res) => {
  console.log(res.data)
})
```

在这里，`this.$http.jsonp` 方法发送了一个 JSONP 请求，其中 `jsonp` 参数指定了回调函数的名称。当请求成功后，Axios 会将响应数据封装在一个对象 `res` 中，其中 `res.data` 属性包含了响应数据。在这里，`res.data` 就是从后端返回的 JSON 数据。

需要注意的是，在 JSONP 请求中，后端需要将响应数据放在指定名称的回调函数中返回给客户端，这是为了跨域请求时绕过浏览器的同源策略。因此，客户端不需要显式地定义回调函数，而是由后端来定义回调函数。


对于**原生的 JavaScript**，如果你使用的是 **JSONP 请求方式，那么客户端需要显式地定义回调函数**，以便后端服务能够将响应数据放在该函数中返回给客户端。

具体来说，你需要在 JavaScript 代码中定义一个全局函数，该函数的名称应该与后端服务指定的回调函数名称相同。例如，在以下代码中，回调函数的名称由后端定义为 `handleCallback`：

```js
function handleCallback(data) {
  console.log(data);
}

var script = document.createElement('script');
script.src = 'http://www.domain2.com::8080/login?callback=handleCallback';
document.head.appendChild(script);
```

在这里，我们定义了一个全局函数 `handleCallback`，用于处理从后端返回的数据。然后，我们使用 `document.createElement` 方法创建一个 `<script>` 元素，并将其 `src` 属性设置为后端服务的 URL，其中 `callback` 参数指定了回调函数的名称。最后，我们将该 `<script>` 元素添加到文档头部，以便浏览器能够加载该脚本并执行回调函数。

当后端服务返回数据时，它会将数据放在指定名称的回调函数中返回给客户端。在这里，客户端使用定义的回调函数 `handleCallback` 来接收数据，并将数据输出到控制台中。

需要注意的是，在 JSONP 请求中，客户端需要确保回调函数名称的正确性，以便后端服务能够正确地处理请求。

**总结：axios的不用显示定义，但是原生的要显式定义，不是说vue的jsonp方法**

**例子**
是的，Vue.js 也可以使用原生 JavaScript 方法来实现 JSONP 跨域请求。具体来说，你可以使用 `XMLHttpRequest` 对象来发送 JSONP 请求，然后在回调函数中处理响应数据。

以下是一个使用原生 JavaScript 实现 JSONP 请求的示例：

```js
function jsonp(url, callback) {
  var script = document.createElement('script');
  script.src = url + '&callback=' + callback;
  document.head.appendChild(script);
}

jsonp('http://www.domain2.com::8080/login', 'handleCallback');

function handleCallback(data) {
  console.log(data);
}
```

在这里，我们定义了一个 `jsonp` 函数，用于发送 JSONP 请求。该函数接受两个参数：URL 和回调函数名称。首先，我们创建一个 `<script>` 元素，并将其 `src` 属性设置为 URL，同时在 URL 中添加回调函数名称。然后，我们将该 `<script>` 元素添加到文档头部，以便浏览器能够加载该脚本并执行回调函数。最后，我们定义了回调函数 `handleCallback`，用于处理从后端返回的数据。

需要注意的是，在 JSONP 请求中，客户端和后端服务需要约定好回调函数的名称以及如何将数据放在该函数中返回给客户端。客户端和后端服务之间的约定应该是一致的，否则请求将无法成功响应。

### JSONP的缺点:
##### 1.具有局限性，仅支持get方法

  JSONP 的局限性是因为它是一种跨域请求技术，而浏览器对于跨域请求有一些安全限制，其中之一就是限制了跨域请求的方法只能是 GET 方法。

具体来说，当浏览器执行 `<script>` 标签加载跨域 JavaScript 脚本时，它会将脚本的 URL 解析为 GET 请求，并向该 URL 发送 GET 请求，以便加载并执行脚本。因此，JSONP 只能使用 GET 方法。

需要注意的是，虽然 JSONP 只支持 GET 方法，但是它可以通过将请求参数拼接到 URL 中来发送复杂的数据。例如，可以使用 URL 查询参数来传递 JSON 数据。这种方式虽然不如 POST 方法安全，但是可以满足一些简单的数据交换需求。

**把URL解析为GET请求是什么意思**
当浏览器执行 `<script>` 标签加载 JavaScript 脚本时，它会将 `<script>` 标签的 `src` 属性值解析为 URL，并使用 GET 方法向该 URL 发送请求，以便加载并执行对应的 JavaScript 脚本。这个过程中，将 URL 解析为 GET 请求是指将 URL 中的参数以及其他信息作为 GET 请求的参数，附加到请求 URL 的末尾，然后将整个 URL 作为 GET 请求的目标。这样，服务器就可以根据 GET 请求中的参数来生成响应，并返回给客户端。

举个例子，如果你在 HTML 中使用以下代码来加载 JavaScript 脚本：

```html
<script src="http://www.example.com/script.js"></script>
```

那么浏览器就会将 `http://www.example.com/script.js` 解析为一个 GET 请求，并向该 URL 发送请求，以便加载并执行 `script.js` 中的 JavaScript 脚本。

需要注意的是，当脚本 URL 是跨域的时候，浏览器可能会对其进行跨域限制，需要使用 JSONP 或者其他跨域技术来处理。

##### 2.不安全，可能会遭受XSS攻击
JSONP 虽然可以用于跨域请求，但它的安全性存在一些问题，容易受到 XSS（跨站脚本攻击）攻击。

XSS 攻击是指攻击者在目标网站上注入恶意脚本，然后让受害者在浏览器中执行这些脚本。在 JSONP 中，如果服务器返回的 JSONP 响应中包含恶意脚本，那么在执行 JSONP 回调函数时，这些恶意脚本就会被执行，从而导致 XSS 攻击。

例如，攻击者可以构造一个 JSONP 请求，将恶意脚本作为响应数据返回，并将该脚本嵌入到 JSONP 回调函数中。当客户端加载这个 JSONP 请求并执行回调函数时，恶意脚本就会被执行，从而导致 XSS 攻击。

为了防止 JSONP 遭受 XSS 攻击，通常需要对 JSONP 响应进行过滤和验证。具体来说，可以在服务器端对 JSONP 响应进行过滤，只返回安全的数据，避免返回恶意脚本。此外，也可以使用其他跨域请求技术，例如 CORS 或者使用代理服务器等方式，来替代 JSONP，以提高安全性。
