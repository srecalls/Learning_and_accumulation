### 什么是WebSocket
WebSocket 是一种协议
设计用于提供**低延迟**、**全双工**和**长期运行**的连接
*全双工:通信的两个参与方可以同时发送和接收数据，不需要等待对方的响应或传输完成

WebSocket的出现就是为了解决实时通信的问题

### 什么是实时通信
传统通信: 电子邮件、网页浏览，存在延迟，需要用户主动请求来获取更新数据

实时通信: 即时消息传递、音视频通话、在线会议和实时数据传输等，可以实现即时的数据传输和交流，不需要用户主动请求或刷新来获取更新数据

### WebSocket之前的世界
实时通信问题主要通过以下几种技术解决
1. 轮询
客户端定期向服务器发送请求询问是否有新的数据可以用，服务器在接收到请求后，在检查是否有更新的数据并将其返回给客户端
缺点：会产生大量的请求和响应，导致不必要的开销和延迟
![[WebSocket.png]]
2. 长轮询
在客户端发起请求后，服务端会保持连接打开一段时间，在有新的数据可用时立即响应，然后再关闭连接
缺点：解决了无效轮询的数量，但还是需要频繁的建立和关闭连接
![[WebSocket-1.png]]

3. comet
   ![[WebSocket-2.png]]
Comet和长轮询一样是基于HTTP的技术，和长轮询不同的是，他可以在返回请求后继续保持连接打开，他的核心思想是同过保持长连接来模拟实时通信，并允许服务器通过流式传输，iframe等推送技术来主动向客户端推送数据，不过 Comet 虽然可以模拟实时通信，但它仍然是基于 HTTP 的模型。在Comet中，服务器推送数据给客户端的方式，通常还是通过延长响应或使用推送技巧来实现

### WebSocket的优势
![[WebSocket-3.png]]

WebSocket的出现，填补了传统HTTP协议在实时通信方面的不足，它允许客户端和服务器之间，通过单个TCP连接进行双工通信并且进行实时的数据交换。所以，WebSocket 的协议非常适用于基于 Web 的游戏，聊天应用以及任何需要低延迟实时连接的应用程序，目前的WebSocket已经得到了主流浏览器的支持，而且由于websocket的标准定义了一套通信规范

### WebSocket的常见库
![[WebSocket-4.png]]
所以无论是JavaScript还是c#、python、java还是其他编程语言都存在相应的库，框架或者模块来支持 WebSocket 的实现和使用


### 如何建立WebSocket的连接
![[WebSocket-6.png]]
WebSocket的建立需要通过 HTTP 发送一次常规的 Get 请求，并在请求头中带上 Upgrade，告诉服务器，我想把HTTP升级成WebSocket，连接就建立成功了，之后客户端和服务器双方便可以随时向彼此发送信息，就如图中，客户端向服务器发送WebSocket的升级请求到服务器，服务器做出响应，从此刻起，连接就被升级为了WebSocket到连接。

### 具体实现代码
#### 前端方面
```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <button onclick="sendMsg()">发消息</button>
</body>
<script>
    const socket = new WebSocket("ws://localhost:8080")

    // 监听WebSocket的事件，包括连接打开，收到消息和连接关闭等
    socket.onopen = function(event) { 
        console.log("WebSocket连接已打开")
    }

    socket.onmessage = function(event) {
        console.log("收到回复: " + event.data)
    }

    socket.onclose = function(event) {
        console.log("WebSocket连接已关闭")
    }
    
    function sendMsg() {
        socket.send("Hello World!")
    }
</script>
</html>
```


#### 后端部分
```js
const http = require('http')
const WebSocket = require('ws')

const server = http.createServer()
const wss = new WebSocket.Server({ server })

wss.on('connection', (socket) => { // 当有用户连接到WebSocket服务器时，就会触发Connection事件
    console.log('WebSocket连接已打开')

    socket.on('message', (message) => { // 从客户端接收到消息时会触发Message事件，会接收到一个参数，表示从客户端那接收到的信息内容
        console.log('收到消息: ' + message) // 在这个方法中就可以处理收到的消息
	        socket.send('Hello friend') // 并且通过Socket.send方法向客户端发送消息
    })

    socket.on('close', () => { // 最后当客户端关闭WebSocket时会触发Close事件
        console.log('WebSocket连接已关闭')
    })
})

server.on('request', (request, response) => {
    response.writeHead(200, { 'Content-Type': 'text/plain'})
    response.end('Hello, World')
})

server.listen(8000, () => {
    console.log('服务器已启动，端口号为8080')
})
```

#### 页面展示
![[WebSocket-7.png]]
![[WebSocket-8.png]]

![[WebSocket-9.png]]

![[WebSocket-10.png]]

当有用户连接到WebSocket服务器时，就会触发Connection事件，然后当从客户端接收到消息时会触发Message事件


### WebSocket的心跳机制
#### 为什么需要心跳机制
![[WebSocket-11.png]]
由于WebSocket的连接是长连接，连接状态可能因为各种原因发生变化，为了保持连接的稳定性，开发中，我们通常采用心跳机制。他是WebSocket保持长连接的关键。

#### 什么是心跳包
![[WebSocket-14.png]]
心跳包就是一种特殊的数据包。
通常情况下，心跳包由客户端和服务器端，定期发送一个空数据帧以确保双方之间的连接仍然有效。

#### WebSocket的限制

![[WebSocket-15.png]]

1. 不提供加密功能
如果有安全上的需求，需采用其他方式来确保安全性，如:SSL协议，或者限制访问权限，在服务端设置黑或白名单，只允许特定IP地址或域名的客户端进行连接
2. 浏览器限制。不支持古老的浏览器
虽然WebSocket的协议已经成为标准，并且广泛使用，但还是存在一些浏览器不支持的情况。这时候需要Ajax或其他方式来替代
3. 当连接过多会对服务器性能造成影响

https://www.bilibili.com/video/BV1ac411c7vr/?spm_id_from=333.788&vd_source=8d6fb7b59b6cb13b7bf0f3383fc26f3f
