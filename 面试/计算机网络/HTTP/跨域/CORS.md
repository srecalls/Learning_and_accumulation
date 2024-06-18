**CORS 需要浏览器和后端同时支持。IE 8 和9 需要通过 XDomainRequest 来实现**
浏览器会自动进行 CORS 通信，实现 CORS 通信的关键是后端。只要后端实现了 CORS，就实现了跨域
服务端设置` Access-Control-Allow-Origin `就可以开启 CORS。 该属性表示哪些域名可以访问资源，如果设置通配符则表示所有网站都可以访问资源
虽然设置 CORS 和前端没什么关系，但是通过这种方式解决跨域问题的话，会在发送请求时出现两种情况，分别为**简单请求**和**复杂请求**

[[HTTP协议规定的协议头和请求头有什么]]

#### 1) 简单请求

只要同时满足以下两大条件，就属于简单请求
条件1：使用下列方法之一：

	- GET
	- HEAD
	- POST

条件2：Content-Type 的值仅限于下列三者之一：

	- text/plain
	- multipart/form-data
	- application/x-www-form-urlencoded

这几个是常见的HTTP请求的Content-Type类型，表示请求体中的数据格式。下面分别介绍一下它们的含义：

	1. text/plain：表示普通文本格式，即纯文本数据，没有任何格式和样式。在HTTP请求中，通常用于向服务器传递少量的简单数据，比如一些参数或者配置信息等。
	2. multipart/form-data：表示多部分表单数据，通常用于文件上传，或者提交表单数据中包含二进制数据的情况。在multipart/form-data格式中，请求体中的数据被划分为多个部分，每个部分都有自己的Content-Type和Content-Disposition头信息，用于描述该部分数据的类型和名称等属性。
	3. application/x-www-form-urlencoded：表示URL编码表单数据，通常用于提交表单数据中的简单文本数据。在application/x-www-form-urlencoded格式中，请求体中的数据被编码成键值对的形式，使用等号（=）连接键和值，使用&符号分隔不同的键值对。

请求中的任意 XMLHttpRequestUpload 对象均没有注册任何事件监听器； XMLHttpRequestUpload 对象可以使用 XMLHttpRequest.upload 属性访问。
##### http请求头中，contentType有哪些
在HTTP请求头中，用于指定请求体的内容类型的字段是"Content-Type"。Content-Type字段用于告知服务器发送请求时正文部分的媒体类型。

常见的Content-Type值包括但不限于以下几种：

1. application/json：表示请求体中的数据是JSON格式。
2. application/x-www-form-urlencoded：表示请求体中的数据是经过URL编码的表单数据。
3. multipart/form-data：表示请求体中的数据是通过多部分形式进行编码的，通常用于文件上传。
4. text/plain：表示请求体中的数据是纯文本格式。
5. application/xml：表示请求体中的数据是XML格式。
6. application/octet-stream：表示请求体中的数据是二进制流数据。
7. image/jpeg、image/png、image/gif等：表示请求体中的数据是相应的图片格式。
#### 2) 复杂请求

不符合以上条件的请求就肯定是复杂请求了。 复杂请求的CORS请求，会在正式通信之前，增加一次HTTP查询请求，称为"预检"请求,该请求是 option 方法的，通过该请求来知道服务端是否允许跨域请求。

"预检"请求（Preflight request）是在进行跨域请求时，浏览器自动发送的 OPTIONS 请求，用于确定服务端是否允许实际的跨域请求。

当使用某些特定的 HTTP 方法（如PUT、DELETE）或自定义的请求头（如Content-Type: application/json）时，浏览器会首先发送一个 OPTIONS 请求，以确定是否允许实际的跨域请求。这个 OPTIONS 请求包含一组预检请求头（Preflight request headers），用于提供关于实际请求的信息。

服务端需要正确处理 OPTIONS 请求，并返回适当的响应，以指示是否允许实际的跨域请求。

以下是 OPTIONS 请求的一般流程：

1. 浏览器发送 OPTIONS 请求到服务端。
2. 服务端收到 OPTIONS 请求后，进行处理。
3. 服务端根据请求头中的信息，判断是否允许实际的跨域请求。
   - 如果允许跨域请求，服务端应该返回响应状态码 200，同时设置响应头 Access-Control-Allow-Origin 来指定允许访问的源。
   - 如果不允许跨域请求，服务端可以返回响应状态码 403（禁止访问）或 405（方法不允许）等，或者不设置 Access-Control-Allow-Origin 响应头。
4. 浏览器根据服务端的响应进行判断，如果允许跨域请求，则继续发送实际的跨域请求；如果不允许，则阻止实际的跨域请求。

需要注意的是，"预检"请求仅在以下情况下发送：
- 使用某些特定的 HTTP 方法，如 PUT、DELETE 等。
- 使用自定义的请求头（非简单请求头）。
- 跨域请求时，浏览器检测到请求为非简单请求。

对于简单请求（Simple Request），浏览器会直接发送实际的跨域请求，而不进行预检请求。简单请求需要满足一定的条件，如使用 GET、POST、HEAD 方法之一，并且不包含自定义请求头，Content-Type 仅限于以下几种类型：application/x-www-form-urlencoded、multipart/form-data、text/plain。

需要注意的是，服务端需要正确配置 CORS（跨域资源共享）来处理跨域请求，以允许或禁止跨域访问。通过设置响应头中的 Access-Control-Allow-Origin、Access-Control-Allow-Methods、Access-Control-Allow-Headers 等来控制跨域访问的权限。

我们用`PUT`向后台请求时，属于复杂请求，后台需做如下配置：
```js
// 允许哪个方法访问我
res.setHeader('Access-Control-Allow-Methods', 'PUT')
// 预检的存活时间
res.setHeader('Access-Control-Max-Age', 6)
// OPTIONS请求不做任何处理
if (req.method === 'OPTIONS') {
  res.end() 
}
// 定义后台返回的内容
app.put('/getData', function(req, res) {
  console.log(req.headers)
  res.end('我不爱你')
})
```

接下来我们看下一个完整复杂请求的例子，并且介绍下CORS请求相关的字段
```js
// index.html
let xhr = new XMLHttpRequest()
document.cookie = 'name=xiamen' // cookie不能跨域
xhr.withCredentials = true // 前端设置是否带cookie
xhr.open('PUT', 'http://localhost:4000/getData', true)
xhr.setRequestHeader('name', 'xiamen')
xhr.onreadystatechange = function() {
  if (xhr.readyState === 4) {
    if ((xhr.status >= 200 && xhr.status < 300) || xhr.status === 304) {
      console.log(xhr.response)
      //得到响应头，后台需设置Access-Control-Expose-Headers
      console.log(xhr.getResponseHeader('name'))
    }
  }
}
xhr.send()
```


```js
//server1.js
let express = require('express');
let app = express();
app.use(express.static(__dirname));
app.listen(3000);
```


```js
//server2.js
let express = require('express')
let app = express()
let whitList = ['http://localhost:3000'] //设置白名单
app.use(function(req, res, next) {
  let origin = req.headers.origin
  if (whitList.includes(origin)) {
    // 设置哪个源可以访问我
    res.setHeader('Access-Control-Allow-Origin', origin)
    // 允许携带哪个头访问我
    res.setHeader('Access-Control-Allow-Headers', 'name')
    // 允许哪个方法访问我
    res.setHeader('Access-Control-Allow-Methods', 'PUT')
    // 允许携带cookie
    res.setHeader('Access-Control-Allow-Credentials', true)
    // 预检的存活时间
    res.setHeader('Access-Control-Max-Age', 6)
    // 允许返回的头
    res.setHeader('Access-Control-Expose-Headers', 'name')
    if (req.method === 'OPTIONS') {
      res.end() // OPTIONS请求不做任何处理
    }
  }
  next()
})
app.put('/getData', function(req, res) {
  console.log(req.headers)
  res.setHeader('name', 'jw') //返回一个响应头，后台需设置
  res.end('我不爱你')
})
app.get('/getData', function(req, res) {
  console.log(req.headers)
  res.end('我不爱你')
})
app.use(express.static(__dirname))
app.listen(4000)

```