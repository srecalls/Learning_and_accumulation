## 一. 2XX (Success 成功状态码)
状态码2XX表示请求被正常处理了。

### \*(1) 200 OK
200 OK表示客户端发来的请求被服务器端正常处理了

### \*(2) 204 No Content
该状态码表示客户端发送的请求已经在服务器端正常处理了，但是没有返回的内容，响应报文中不包含实体的主体部分。一般在只需要从客户端往服务器端发送信息，而服务器端不需要往客户端发送内容时使用。

### (3) 206 Partial Content
该状态码表示客户端进行了范围请求，而服务器端执行了这部分的 GET 请求。响应报文中包含由 Content-Range指定范围的实体内容。

## 二. 3XX (Redirection 重定向状态码)
3XX 响应结果表明浏览器需要执行某些特殊的处理以正确处理请求

### \*(1) 301 Moved Permanently
**永久重定向。**
该状态码表示请求的资源已经被分配了新的 URI，以后应使用资源指定的 URI。新的 URI 会在 HTTP响应头中的Location 首部字段指定。若用户已经把原来的URI保存为书签，此时会按照 Location 中新的URI重新保存该书签。同时，搜索引擎在抓取新内容的同时也将旧的网址替换为重定向之后的网址。
**使用场景:**
- 当我们想换个域名，旧的域名不再使用时，用户访问旧域名时用301就重定向到新的域名。其实也是告诉搜索引擎收录的域名需要对新的域名进行收录。
- 在搜索引擎的搜索结果中出现了不带www的域名，而带www的域名却没有收录，这个时候可以用301重定向来告诉搜索引擎我们目标的域名是哪一个

### \*(2) 302 Found
**临时重定向。**
该状态码表示请求的资源被分配到了新的 URI，希望用户(本次)能使用新的 URI 访问资源。和 301 MovedPermanently 状态码相似，但是 302 代表的资源不是被永久重定向，只是临时性质的。也就是说已移动的资源对应的 URI 将来还有可能发生改变。若用户把 URI 保存成书签，但不会像 301 状态码出现时那样去更新书签，而是仍IE保留返回 302 状态码的页面对应的 URI。同时，搜索引警会抓取新的内容而保留旧的网址。因为服务器返回302代码，搜索引擎认为新的网址只是暂时的。

**使用场景:**
- 当我们在做活动时，登录到首页自动重定向，进入活动页面
- 未登陆的用户访问用户中心重定向到登录页面。
访问404页面重新定向到首页。

好的，以下是两个 URL 返回的响应头的示例：

1. `301 Moved Permanently`：

```
HTTP/1.1 301 Moved Permanently
Location: https://www.example.com/new-url
```

在这个示例中，服务器返回了 `301` 状态码，并在响应头中添加了一个 `Location` 字段，指向重定向后的 URL `https://www.example.com/new-url`。

2. `302 Found`：


```
HTTP/1.1 302 Found
Location: https://www.example.com/temporary-url
```

在这个示例中，服务器返回了 `302` 状态码，并在响应头中添加了一个 `Location` 字段，指向重定向后的临时 URL `https://www.example.com/temporary-url`。

需要注意的是，这只是示例中的响应头，实际的响应头可能会包含其他字段，比如说 `Content-Type`、`Cache-Control` 等。

### \*(3) 303 See Other
该状态码表示由于请求对应的资源存在着另一个 URI，应使用 GET 方法定向获取请求的资源
303 状态码和 302 Found 状态码有着相似的功能，但是 303 状码明确表示客户端应当采用 GET 方法获取资源
303 状态码通常作为 PUT 或 POST 操作的返回结果，它表示重定向接指向的不是新上传的资源，而是另外一个页面，比如消息确认页面或上传进度页面。而请求重定向页面的方法要总是使用 GET。
注意:
- 当 301、302、303 响应状态码返回时，几乎所有的浏览器都会把 POST 改成GET，并删除请求报文内的主体之后请求会再次自动发送
- 301、302 标准是禁止将 POST 方法变成 GET方法的，但实际大家都会这么做

		- 302 Found：表示请求的资源已暂时移动到了一个新的位置。客户端应该使用相同的HTTP方法重复请求，并且应该使用新的URI作为请求目标。但是，由于历史原因，许多客户端会将POST请求自动转换为GET请求，并在新的URI上执行GET请求。因此，如果你不想让客户端自动转换HTTP方法，可以考虑使用303状态码。
		- 303 See Other：表示请求的资源已经移动到了一个新的位置，并且客户端应该使用GET方法请求新的URI。这个状态码可以用于POST或PUT操作的响应中，以指示客户端重定向到一个不同的资源，例如确认页面或上传进度页面。
		- 307 Temporary Redirect：表示请求的资源已暂时移动到了一个新的位置，和302状态码类似，但客户端必须使用相同的HTTP方法重复请求新的URI。与302不同的是，307状态码禁止客户端自动转换HTTP方法。

当客户端提交一个包含表单数据的POST请求时，服务器通常会处理这些数据并返回一个响应，告诉客户端请求已成功完成。如果服务器希望在完成请求后将客户端重定向到另一个资源，例如一个确认页面或上传进度页面，可以使用HTTP 303状态码。客户端收到303状态码后，应该使用GET方法请求Location头指定的新资源。

下面是一个简单的例子：

客户端向服务器提交一个包含表单数据的POST请求：

```http
POST /submit-form HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 21

name=John&age=30
```

服务器处理表单数据，并返回一个HTTP 303响应，告诉客户端应该使用GET方法请求一个确认页面：

```http
HTTP/1.1 303 See Other
Location: https://example.com/confirm-page
```

客户端收到303响应后，应该使用GET方法请求Location头指定的新资源：

```http
GET /confirm-page HTTP/1.1
Host: example.com
```

在这个例子中，服务器收到客户端的POST请求，处理表单数据并返回一个HTTP 303响应，告诉客户端应该使用GET方法请求一个确认页面。客户端收到303响应后，使用GET方法请求Location头指定的新资源，以查看确认页面。这个例子中的确认页面可以显示提交表单的结果，例如"您的表单已成功提交"等信息。

HTTP 303状态码的响应体通常是一个HTML文档，其中包含一个重定向消息和一个指向新资源的链接。

例如，以下是一个简单的HTTP 303响应示例：

```http 
HTTP/1.1 303 See Other
Location: https://example.com/new-page
Content-Type: text/html

<!DOCTYPE html>
<html>
  <head>
    <title>303 See Other</title>
  </head>
  <body>
    <h1>Redirecting...</h1>
    <p>This page has moved. Please visit the new page at:</p>
    <a href="https://example.com/new-page">https://example.com/new-page</a>
  </body>
</html>
```

在这个示例中，服务器返回了一个303状态码，告诉客户端应该使用GET方法请求新资源。响应头中的Location字段指向新资源的URL，而响应体中包含一个HTML文档，其中包含一个重定向消息和一个指向新资源的链接。客户端可以解析这个HTML文档，并根据其中的链接进行重定向。

### \*(4) 304 Not Modified
**浏览器缓存相关。**

	HTTP 304状态码表示客户端发送了一个条件请求，但服务器确认客户端缓存的资源仍然有效并且未被修改。在这种情况下，服务器不会返回请求的资源，而是返回一个空的响应体和304状态码，告诉客户端可以使用缓存的资源。

该状态码表示客户端发送附带条件的请求时，服务器端允许请求访问资源，但未满足条件的情况。
304 状态码返回时，不包含任何响应的主体部分。304 虽然被划分在 3XX 类别中，但是和重定向没有关系。

带条件的请求 (Http 条件请求) : 使用 Get方法 请求，请求报文中包含( `if-match` 、`if-none-match`  、`if-modified-since`、`if-unmodified-since` 、`if-range` ) 中任意首部。modified-since 、

状态码304并不是一种错误，而是告诉客户端有缓存，直接使用缓存中的数据。返回页面的只有头部信息，是没有内容部分的，这样在一定程度上提高了网页的性能。
[[1.对浏览器缓存的理解 （强缓存、协商缓存）]]

### (5) 307 Temporary Redirect
**307表示临时重定向。**
该状态码与 302 Found 有着相同含义，尽管 302 标准禁止 POST 变成 GET，但是实际使用时还是这样做了

307 会遵守浏览器标准，**不会从 POST 变成 GET**。但是对于处理请求的行为时，不同浏览器还是会出现不同的情况。规范要求浏览器继续向 Location 的地址 POST 内容。规范要求浏览器继续向 Location 的地址 POST 内容

## 三. 4XX (Client Error 客户端错误状态码）
4XX 的响应结果表明客户端是发生错误的原因所在

### \*(1) 400 Bad Request
该状态码表示请求报文中存在语法错误。当错误发生时，需修改请求的内容后再次发送请求。另外，浏览器会像200 0K 一样对待该状态码

#### 例子
假设用户在使用一个在线商店的搜索功能时，输入了一个无效的搜索词，例如一个包含非法字符的搜索词。在这种情况下，客户端会向服务器发送一个包含错误搜索词的请求。由于搜索词包含非法字符，服务器将返回400 Bad Request状态码，提示客户端请求存在语法错误：

```http
GET /search?q=inv@lid HTTP/1.1
Host: example.com
```

服务器收到请求后，检测到搜索词包含一个非法字符（即@符号），因此返回400 Bad Request响应：


```http
HTTP/1.1 400 Bad Request
Content-Type: text/plain

The request contains bad syntax or cannot be fulfilled.
```

客户端收到400响应后，应该修改请求的内容（例如，更改搜索词以排除非法字符），然后再次发送请求，以便服务器能够正确处理请求。

总之，400 Bad Request状态码表示请求报文中存在语法错误，客户端应该修改请求的内容并重新发送请求。如果客户端忽略了该状态码，浏览器将会像200 OK一样对待它，因此客户端应该适当处理该状态码以确保请求能够正确处理。

### \*(2) 401 Unauthorized
该状态码表示发送的请求需要有通过 HTTP 认证(BASIC 认证、DIGEST 认证)的认证信息。若之前已进行过一次请求，则表示用户认证失败
返回含有 401 的响应必须包含一个适用于被请求资源的 WWW-Authenticate 首部用以质询(challenge)用户信息。
当浏览器初次接收到 401 响应，会弹出认证用的对话窗口。
#### 例子
好的，下面是一个401 Unauthorized状态码的例子：

假设一个网站需要用户进行身份验证才能访问某些资源，例如用户的个人资料页面。当用户尝试访问该页面时，如果用户尚未进行身份验证，服务器将返回401 Unauthorized状态码，并要求用户进行身份验证。

例如，假设用户尝试访问其个人资料页面，但未进行身份验证。在这种情况下，服务器将返回401 Unauthorized状态码，并要求用户提供身份验证信息：

```http
GET /profile HTTP/1.1
Host: example.com
```

服务器检测到用户没有进行身份验证，因此返回401 Unauthorized响应，并要求用户提供身份验证信息：

```http
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Basic realm="User Profile"
Content-Type: text/plain

Access denied.
```

客户端收到401响应后，应该弹出认证用的对话窗口，要求用户提供身份验证信息（例如，用户名和密码）。如果用户提供了正确的身份验证信息，客户端将使用Authorization头将该信息包含在请求中，再次向服务器发送请求。如果身份验证信息无效，则服务器将继续返回401 Unauthorized响应，直到用户提供有效的身份验证信息。

总之，401 Unauthorized状态码表示发送的请求需要通过HTTP认证（例如Basic认证或Digest认证）进行身份验证。当浏览器初次接收到401响应时，会弹出认证用的对话窗口要求用户提供身份验证信息。客户端应该根据服务器提供的WWW-Authenticate头提供正确的身份验证信息，以便访问受保护的资源。

### (3) 403 Forbidden
该状态码表明请求资源的访问被服务器拒绝了，服务器端没有必要给出详细理由，但是可以在响应报文实体的主体中进行说明。进入该状态后，不能再继续进行验证。该访问是永久禁止的，并且与应用逻辑密切相关
#### 例子
好的，下面是一个403 Forbidden状态码的例子：

假设一个网站有一个目录，其中包含一些敏感文件，只有特定的用户或组才能访问。当非授权用户尝试访问该目录或其中的文件时，服务器将返回403 Forbidden状态码，表明请求资源的访问被服务器拒绝了。

例如，假设一个非授权用户试图访问该目录中的某个文件：

```http
GET /private-files/confidential.txt HTTP/1.1
Host: example.com
```

服务器检测到该请求来自一个非授权用户，因此返回403 Forbidden响应：

```http
HTTP/1.1 403 Forbidden
Content-Type: text/plain

Access to the requested resource is forbidden.
```

客户端收到403响应后，应该向用户显示错误消息，说明该请求无法完成。由于服务器不需要给出详细的拒绝理由，因此错误消息可能很简单（例如，“无法访问请求的资源”）。

总之，403 Forbidden状态码表示请求资源的访问被服务器拒绝了，通常由于权限不足或请求的资源与应用逻辑不相符。客户端应该向用户显示错误消息，说明该请求无法完成。

### \*(4) 404 Not Found
该状态码表明服务器上无法找到请求的资源。除此之外，也可以在服务器端拒绝请求且不想说明理由时使用。
#### 例子
好的，下面是一个404 Not Found状态码的例子：

假设一个网站上有一个页面，但用户试图访问该页面的URL时，该页面不存在。在这种情况下，服务器将返回404 Not Found状态码，表明无法找到请求的资源。

例如，假设用户试图访问一个不存在的页面：

```http
GET /nonexistent-page HTTP/1.1
Host: example.com
```

服务器检测到该页面不存在，因此返回404 Not Found响应：

```http
HTTP/1.1 404 Not Found
Content-Type: text/plain

The requested resource could not be found.
```

客户端收到404响应后，应该向用户显示错误消息，说明请求的资源不存在。由于服务器无法找到请求的资源，因此客户端无法修改请求以使其成功，而只能向用户显示错误消息。

总之，404 Not Found状态码表示服务器无法找到请求的资源。客户端应该向用户显示错误消息，说明请求的资源不存在。

### (5) 405 Method Not Allowed
该状态码表示客户端请求的方法虽然能被服务器识别，但是服务器禁止使用该方法。GET 和 HEAD 方法，服务器应该总是允许客户端进行访问。客户端可以通过 OPTIONS 方法(预检)来查看服务器允许的访问方法,如下

`Access-Control-A11ow-Methods: GET,HEAD,PUT,PATCH,POST,DELETE`

#### 例子
好的，下面是一个405 Method Not Allowed状态码的例子：

假设一个网站的某个资源只能通过POST方法进行修改。但是，当用户尝试使用PUT方法进行修改时，服务器将返回405 Method Not Allowed状态码，表明服务器禁止使用该方法。

例如，假设用户试图使用PUT方法修改该资源：

```http
PUT /resource HTTP/1.1
Host: example.com
```

服务器检测到该请求使用了禁止的方法，因此返回405 Method Not Allowed响应，并在Allow头中列出允许的方法：

```http
HTTP/1.1 405 Method Not Allowed
Allow: POST
Content-Type: text/plain

The requested method is not allowed for the requested resource.
```

客户端收到405响应后，应该根据Allow头中列出的允许的方法，修改请求使用允许的方法，然后再次发送请求。

总之，405 Method Not Allowed状态码表示客户端请求的方法虽然能被服务器识别，但是服务器禁止使用该方法。客户端应该根据Allow头中列出的允许的方法，修改请求使用允许的方法，然后再次发送请求。客户端还可以使用OPTIONS方法来查看服务器允许的访问方法。

## 四、5XX (Server Error 服务器错误状态码)
5XX 的响应结果表明服务器本身发生错误

### \*(1) 500 Internal Server Error
该状态码表明服务器端在执行请求时发生了错误。也有可能是 Web 应用存在的 bug 或某些临时的故障
服务器端发生错误导致请求无法执行
#### 例子
好的，下面是一个500 Internal Server Error状态码的例子：

假设一个网站的服务器上运行着一些Web应用程序。当用户尝试访问某个页面时，服务器端的应用程序遇到了一个错误，导致无法完成请求。在这种情况下，服务器将返回500 Internal Server Error状态码，表明服务器端在执行请求时发生了错误。

例如，假设用户尝试访问某个页面，但服务器端的应用程序遇到了一个错误：

```http
GET /page HTTP/1.1
Host: example.com
```

服务器检测到应用程序发生了错误，因此返回500 Internal Server Error响应：

```http
HTTP/1.1 500 Internal Server Error
Content-Type: text/plain

An error occurred while processing the request.
```

客户端收到500响应后，应该向用户显示错误消息，说明请求无法完成。由于该错误是由服务器端的应用程序引起的，因此客户端无法修改请求以使其成功，而只能向用户显示错误消息。

总之，500 Internal Server Error状态码表明服务器端在执行请求时发生了错误，通常是由于Web应用程序存在bug或临时故障导致的。客户端应该向用户显示错误消息，说明请求无法完成。

### (2) 502 Bad Gateway
该状态码表明扮演网关或代理角色的服务器，从上游服务器中接收到的响应是无效的。注意，502 错误通常不是客户端能够修复的，而是需要由途经的 Web 服务器或者代理服务器对其进行修复。
#### 例子
好的，下面是一个502 Bad Gateway状态码的例子：

假设一个网站使用反向代理服务器来处理所有传入的请求。当代理服务器尝试将请求转发到上游服务器时，如果上游服务器未能响应或响应无效，代理服务器将返回502 Bad Gateway状态码，表明从上游服务器接收到的响应是无效的。

例如，假设代理服务器尝试将请求转发到上游服务器，但上游服务器未能响应：

```http
GET /resource HTTP/1.1
Host: example.com
```

代理服务器向上游服务器发送请求，但由于上游服务器未能响应，代理服务器返回502 Bad Gateway响应：

```http
HTTP/1.1 502 Bad Gateway
Content-Type: text/plain

The upstream server failed to respond.
```

客户端收到502响应后，应该向用户显示错误消息，说明请求无法完成。由于该错误通常是由代理服务器或上游服务器引起的，因此客户端无法修改请求以使其成功，而只能向用户显示错误消息。

总之，502 Bad Gateway状态码表明扮演网关或代理角色的服务器从上游服务器接收到的响应是无效的，通常是由于代理服务器或上游服务器故障引起的。客户端应该向用户显示错误消息，说明请求无法完成。

### (3) 503 Service Unavailable
该状态码表明服务器暂时处于超负载或正在进行停机维护，现在无法处理请求。，如果事先得知解除以上状况需要的时间，最好写入 RetryAfter 首部字段再返回给客户端。

**使用场景:**
- 服务器停机维护时，主动用503响应请求
- nginx 设置限速，超过限速，会返回503
#### 例子
好的，下面是一个503 Service Unavailable状态码的例子：

假设一个网站正在进行升级维护，因此服务器无法处理传入的请求。在这种情况下，服务器将返回503 Service Unavailable状态码，表明服务器暂时无法处理请求。

例如，假设用户尝试访问该网站的某个页面：

```http
GET /page HTTP/1.1
Host: example.com
```

服务器检测到正在进行维护，因此返回503 Service Unavailable响应，并在Retry-After头中指定解决问题所需的时间：

```http
HTTP/1.1 503 Service Unavailable
Retry-After: 3600
Content-Type: text/plain

The server is currently unavailable due to maintenance. Please try again later.
```

客户端收到503响应后，应该向用户显示错误消息，并告知用户等一段时间后再尝试访问。由于服务器暂时无法处理请求，客户端无法修改请求以使其成功，而只能向用户显示错误消息。

总之，503 Service Unavailable状态码表明服务器暂时无法处理请求，通常是由于服务器超负载或维护引起的。客户端应该向用户显示错误消息，并告知用户等一段时间后再尝试访问。如果知道恢复时间，可以在Retry-After头中指定。
### (4) 504 Gateway Timeout
该状态码表示网关或者代理的服务器无法在规定的时间内获得想要的响应。他是HTTP 1.1中新加入的

**使用场景**:代码执行时间超时，或者发生了死循环

#### 例子
好的，下面是一个504 Gateway Timeout状态码的例子：

假设一个网站使用反向代理服务器来处理所有传入的请求。当代理服务器尝试将请求转发到上游服务器时，如果上游服务器未能及时响应，代理服务器将返回504 Gateway Timeout状态码，表明代理服务器无法在规定的时间内获得想要的响应。

例如，假设代理服务器尝试将请求转发到上游服务器，但上游服务器响应时间过长：

```http
GET /resource HTTP/1.1
Host: example.com
```

代理服务器向上游服务器发送请求，但由于上游服务器响应时间过长，代理服务器返回504 Gateway Timeout响应：

```http
HTTP/1.1 504 Gateway Timeout
Content-Type: text/plain

The gateway did not receive a timely response from the upstream server.
```

客户端收到504响应后，应该向用户显示错误消息，说明请求无法完成。由于该错误通常是由于代理服务器或上游服务器故障引起的，因此客户端无法修改请求以使其成功，而只能向用户显示错误消息。

总之，504 Gateway Timeout状态码表示网关或代理服务器无法在规定的时间内获得想要的响应，通常是由于代理服务器或上游服务器响应时间过长引起的。客户端应该向用户显示错误消息，说明请求无法完成。

##### 502和504
502 Bad Gateway状态码表示代理服务器无法从上游服务器获得有效的响应，而504 Gateway Timeout状态码表示代理服务器未能在规定的时间内从上游服务器获得响应，通常是由于上游服务器响应时间过长导致的。两者的区别在于，502通常是由于上游服务器无法执行或返回无效响应引起的，而504通常是由于上游服务器响应时间过长引起的。

## 五.总结
### (1) 2XX 成功
- 200 OK，表示从客户端发来的请求在服务器端被正确处理
- 204 No content，表示请求成功，但响应报文不含实体的主体部分
- 205 Reset Content，表示请求成功，但响应报文不含实体的主体部分，但是与 204 响应不同在于要求请求方重置内容
- 206 Partial Content，进行范围请求

### (2) 3XX 重定向
- 301 moved permanently，永久性重定向，表示资源已被分配了新的 URL
- 302 found，临时性重定向，表示资源临时被分配了新的 URL
- 303 see other，表示资源存在着另一个 URL，应使用 GET 方法获取资源
- 304 not modified，表示服务器允许访问资源，但因发生请求未满足条件的情况
- 307 temporary redirect，临时重定向，和302含义类似，但是期望客户端保持请求方法不变向新的地址发出请求

### (3)4XX 客户端错误
- 400 bad request，请求报文存在语法错误
- 401 unauthorized，表示发送的请求需要有通过 HTTP 认证的认证信息
- 403 forbidden，表示对请求资源的访问被服务器拒绝
- 404 not found，表示在服务器上没有找到请求的资源

### (4)5XX 服务器错误
- 500 internal sever error，表示服务器端在执行请求时发生了错误
- 501 Not Implemented，表示服务器不支持当前请求所需要的某个功能
- 503 service unavailable，表明服务器暂时处于超负载或正在停机维护，无法处理请求