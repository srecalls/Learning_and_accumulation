Vue CLI提供了一种配置代理服务器的方式，可以通过修改`vue.config.js`文件来实现代理服务器的配置。代理服务器可以将客户端（前端）的请求转发到后端服务器，从而解决跨域问题。

具体来说，当客户端（前端）向代理服务器发送请求时，代理服务器会将请求头部中的`Origin`字段删除，并将请求转发到目标服务器。由于删除了`Origin`字段，后端服务器无法检测到请求的来源地址，因此就不会出现跨域问题。代理服务器接收到后端服务器的响应后，将响应头部中的`Access-Control-Allow-Origin`字段设置为客户端请求的域名，从而允许客户端访问响应资源。

例如，以下是一个使用Vue CLI配置代理服务器的示例代码：

```javascript
// vue.config.js
module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:3000',
        changeOrigin: true
      }
    }
  }
};
```

上述代码将所有以`/api`开头的请求都代理到`http://localhost:3000`上，通过`changeOrigin`选项将请求头部中的`Origin`字段删除，从而解决跨域问题。在前端代码中，可以使用`axios`等HTTP客户端库向代理服务器发送请求，而不是直接向后端服务器发送请求。

总的来说，代理服务器能够解决跨域问题，是因为代理服务器能够在客户端和后端服务器之间进行中转，从而修改请求头部和响应头部，绕过同源策略限制。





在实现前端应用和后端 API 服务器没有运行在同一个主机上，需要在开发环境下将 API 请求代理到 API 服务器。这个问题可以通过 vue.config.js 中的 devServer.proxy 选项来配置。

解决方式：

通常是在vue.configh.js中去对proxy进行配置普通代理方式

```text
module.exports = {
  devServer: {
    proxy: {
      '^/api': {
        ws: true,  //是否启用websockets
        changeOrigin: true,  //开启代理： 在本地会创建一个虚拟服务端，然后发送请求数据，并且同时接收请求数据，这样客户端和服务端进行数据的交互就不会有跨域问题
        target: ''  // 要访问的跨域的域名
      }
    }
  },
}
```

/api 表示需要去匹配请求时的 url，然后替换成 target 的值：

比如你页面里是写的

```text
axios.post('/api/list/gd')
```

	最终 node 去请求后台的地址是：http://\*************/api/list/gd

  

但是你在浏览器里看到的还是：http://localhost:8888/api/list/gd，这时候就不存在跨越的问题的，node 服务已经代理拿到数据了。

上述代码将所有以`/api`开头的请求都代理到`http://localhost:3000`上，通过`changeOrigin`选项将请求头部中的`Origin`字段删除，从而解决跨域问题。在前端代码中，可以使用`axios`等HTTP客户端库向代理服务器发送请求，而不是直接向后端服务器发送请求。
