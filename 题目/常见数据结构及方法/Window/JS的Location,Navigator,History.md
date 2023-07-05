Location,Navigator,History三个对象是window对象常用属性，

- `window.location`
- `window.navigator`
- `window.history`,window.history属性它表示当前窗口的浏览历史；

## window.location
`window.location`属性提供 **URL 相关的信息和操作方法**。通过`window.location`和`document.location`属性，可以拿到这个对象。

### 1. location属性：
##### location.href
	- `location.href `设置或获取当前页面 URL;

##### location.protocol
	- `location.protocol `设置或获取当前 URL 的协议，包括冒号（:）;

##### location.host
	- `location.host `设置或获取当前 URL域名，包括冒号（:）和端口;

##### location.hostname
	- `location.hostname `设置或获取当前 URL域名,不包括端口;

##### location.port
	- `location.port `设置或获取当前 URL端口;

##### location.pathname
	- `location.pathname `设置或获取当前 URL路径部分，从根路径/开始;

##### location.search
	- `location.search `设置或获取当前 URL查询字符串部分，从问号?开始;

##### location.hash
	- `location.hash `设置或获取当前 URL哈希值，从#开始;

##### location.origin
	- `location.origin `获取URL 的协议、域名和端口;

```js
// 当前网址为
// http://www.baidu.com:8080/path/new.html?id=123#anchors

document.location.href
// "http://www.baidu.com:8080/path/new.html?id=123#anchors" // 完整URL

document.location.protocol
// "http:"      // URL 协议

document.location.hostname
// "www.baidu.com"  // URL域名

document.location.port
// "8080"   // URL端口

document.location.host
// "www.baidu.com:8080" // URL域名加端口

document.location.pathname
// "/path/new.html" // URL路径部分

document.location.search
// "?id=123"    // URL查询字符串部分，从问号?开始

document.location.hash
// "#anchors"       // 哈希值

document.location.origin
// "http://www.baidu.com:8080"      // 协议、域名和端口
```

在这些属性里面，只有origin属性是只读的，其他属性都可读写，唯一需要特别说明的是location.href 设置新的URL后，是立即跳往新地址。

### 2.location方法
##### Location.assign()
	Location.assign() 接收一个URL字符串参数，浏览器立即跳往这个新地址;

##### Location.replace()
	location.replace() 接收一个URL字符串参数，浏览器立即跳往这个新地址，用新的文档替换当前文档。
	注意: 使用 Location.replace() 跳转后，是不可以在回退到原来的页面，因为在浏览器的 History 里的记录是被替换掉的。

##### Location.reload()
	location.reload() 重新加载当前页面


## Window.navigator

window.navigator属性指向一个包含浏览器和系统信息的 Navigator 对象。**js代码通过这个属性了解用户的浏览器环境信息。**
### 1. navigator属性
##### navigator.userAgent
1. `navigator.userAgent` 返回浏览器的 User Agent 字符串，浏览器的厂商和版本信息

```js
navigator.userAgent;
//谷歌： Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
//火狐：Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0
//IE：Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; rv:11.0) like Gecko
```

通过`userAgent`也可以大致准确地识别手机浏览器，方法就是检测当前`navigator.userAgent`是否包含了`mobile`字符串。
```js
var ua = navigator.userAgent;
	if (/mobile/i.test(ua)) {
		console.log('手机浏览器')   // 手机浏览器
	} else {
		console.log('非手机浏览器')  // 非手机浏览器
	}
```

如果想要识别所有移动设备的浏览器，可以测试更多的特征字符串

```js
/mobile|android|touch|mini/i.test(ua)
```

##### navigator.platform
2. `navigator.platform`属性返回用户的操作系统信息，比如MacIntel、Win32、Linux x86_64等;
```js
navigator.platform
// Win32
```

##### navigator.language
3. `navigator.language，navigator.languages`属性返回一个字符串，表示浏览器的首选语言。该属性只读；

```js
navigator.language
//  zh-CN
```

`navigator.languages` 属性返回一个数组，表示可以接受的所有语言。`navigator.language`总是这个数组的**第一个**成员。HTTP 请求头信息的`Accept-Language`字段，就来自这个数组
```js
navigator.languages
//  [ "zh-CN", "zh", "zh-TW", "zh-HK", "en-US", "en" ]
```

##### navigator.cookieEnabled
4. `navigator.cookieEnabled`检测浏览器是否开启cookie功能，返回一个布尔值。

##### navigator.onLine
5. `navigator.onLine`属性返回一个布尔值，表示用户当前在线还是离线（浏览器断线）。用户变成在线会触发online事件，变成离线会触发offline事件，可以通过`window.ononline`和`window.onoffline`指定这两个事件的回调函数。

##### navigator.geolocation
6. `navigator.geolocation`属性返回一个 Geolocation 对象，包含用户地理位置的信息。注意，该 API 只有在 HTTPS 协议下可用，否则调用下面方法时会报错。

		- Geolocation.getCurrentPosition()：得到用户的当前位置
		- Geolocation.watchPosition()：监听用户位置变化
		- Geolocation.clearWatch()：取消watchPosition()方法指定的监听函数

## Window.history
window.history属性指向 History 对象，它**表示当前窗口的浏览历史**。 History 对象保存了当前窗口访问过的所有页面网址。由于安全原因，浏览器不允许脚本读取这些地址，但是允许在地址之间导航。
##### history.length
- `history.length`：当前窗口访问过的网址数量（包括当前网页）
```js
history.length // 1`
```

##### history.state
- `history.state`：History 堆栈最上层的状态值 

##### history.back()
- `history.back()`：返回到上一个网址，等同于点击浏览器的后退键。对于第一个访问的网址，该方法无效果。

##### history.forward()
- `history.forward()`：前进到下一个网址，等同于点击浏览器的前进键。对于最后一个访问的网址，该方法无效果。

##### history.go()
- `history.go()`：接受一个整数作为参数，以当前网址为基准，跳转到参数指定的网址，比如go(1)相当于forward()，go(-1)相当于back()。如果参数超过实际存在的网址范围，该方法无效果；如果不指定参数，默认参数为0，相当于刷新当前页面。

##### history.pushState()
- `history.pushState()`方法用于在历史中添加一条记录。该方法接受三个参数，依次为：

		- state：一个与添加的记录相关联的状态对象，主要用于popstate事件。该事件触发时，该对象会传入回调函数。也就是说，浏览器会将这个对象序列化以后保留在本地，重新载入这个页面的时候，可以拿到这个对象。如果不需要这个对象，此处可以填null。 
		- title：新页面的标题。但是，现在所有浏览器都忽视这个参数，所以这里可以填空字符串。 
		- url：新的网址，必须与当前页面处在同一个域。浏览器的地址栏将显示这个网址。

```js
history.pushState(null, '', 'http://www.baidu.com');// 页面会跳往百度页面
```

 **pushState()方法不会触发页面刷新，只是导致 History 对象发生变化，地址栏会有变化**
##### history.replaceState()
- `history.replaceState()`方法用来修改 History 对象的当前记录。

##### popstate
- `popstate` 事件,**每当同一个文档的浏览历史（即history对象）出现变化时**，就会触发popstate事件。 注意，仅仅调用pushState()方法或replaceState()方法 ，并不会触发该事件，只有用户点击浏览器倒退按钮和前进按钮，或者使用 JavaScript 调用History.back()、History.forward()、History.go()方法时才会触发。另外，该事件只针对同一个文档，如果浏览历史的切换，导致加载不同的文档，该事件也不会触发
```js
window.onpopstate = function (event) {
  console.log('location: ' + document.location);
  console.log('state: ' + JSON.stringify(event.state));
};
```
https://juejin.cn/post/6844903695373565960  
来源：稀土掘金  
