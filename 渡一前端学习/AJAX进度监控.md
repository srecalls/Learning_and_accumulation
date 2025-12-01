## AJAX
[[了解Ajax]]
[[ajax是什么？怎么实现的？]]

页面上做请求是基于AJAX

AJAX有两种原生实现方式
- 一种传统 XHR 全称 XMLHttpRequest
	- axios（第三方库，内部使用的是XHR）
- 一种较新 Fetch
	- umi-request


这两个API有什么区别
![[AJAX进度监控.png]]



Fetch是基于Promise，Promise只有成功和失败，没有成功了多少


进度监控两种
- 请求进度监控
- 响应进度监控

## 响应进度监控
### XHR
![[AJAX进度监控-1.png]]
当服务端不断向客户端传数据的时候就会触发这个事件

loaded传了多少，total总的
![[AJAX进度监控-2.png]]

数字单位是字节


### Fetch
需要知道
总的和已有的


![[AJAX进度监控-3.png]]
![[AJAX进度监控-5.png]]

响应头里有个字段“content-length”
表示响应体有多少个字节
![[AJAX进度监控-4.png]]


调用完fetch后有个响应对象 resp，resp里有个body是一个可读流，流里面有个方法叫getReader（）


## 请求上传进度
### XHR
![[AJAX进度监控-6.png]]

xhr.upload也有个progress事件



您提供的笔记非常清晰和专业，完美地总结了 AJAX 的两种实现方式（XHR 和 Fetch）及其在进度监控上的关键差异。

下面我将根据您的笔记内容，详细梳理和对比 XMLHttpRequest (XHR) 和 Fetch 这两个 API 的核心区别，尤其侧重于 **请求和响应的进度监控**。

---

## AJAX 核心 API 对比：XHR vs. Fetch

|**特性**|**XMLHttpRequest (XHR)**|**Fetch API**|
|---|---|---|
|**诞生时间**|传统、较老（AJAX 初代）|较新、现代化|
|**API 基础**|基于回调函数（Callback）和事件监听|基于 **Promise**|
|**外部依赖**|Axios 等第三方库通常基于 XHR|Umi-request 等库通常基于 Fetch|
|**请求进度监控**|**原生支持，API 简单** (`xhr.upload.onprogress`)|**原生不支持**，需要复杂封装（如使用 `TransformStream`）|
|**响应体处理**|需设置 `responseType`，返回整个数据块|默认返回 **Stream (可读流)**|
|**响应进度监控**|**原生支持，API 简单** (`xhr.onprogress`)|**需手动实现**：结合 `content-length` 头部和 `Response.body.getReader()` 读取流|

---

## 进度监控的实现机制对比

进度监控分为两个核心部分：**响应下载进度**（客户端接收数据）和**请求上传进度**（客户端发送数据）。

### 1. 响应下载进度监控 (Downloading Progress)

这是监控服务器向客户端传输数据的过程。

#### XHR 实现方式（简单直接）

XHR 的设计理念是**事件驱动**，它将进度信息直接封装在事件对象中。

- **API：** 直接监听 `XMLHttpRequest` 对象本身的 `progress` 事件。
    
- **数据：** 事件对象 `event` 中包含两个关键属性：
    
    1. `loaded`：已传输的字节数。
        
    2. `total`：总共需要传输的字节数（服务器必须提供 `Content-Length` 头部）。
        
- **优势：** 实现简单，浏览器负责所有进度计算。
    

#### Fetch 实现方式（基于 Stream）

如您笔记所言，Fetch 是基于 Promise 的，Promise 只关注成功或失败，因此**没有内置的进度事件**。它必须利用其 **流式（Streaming）** 特性来实现。

1. **获取总字节数 (`total`)：**
    
    - 通过读取响应头（Response Headers）中的 `content-length` 字段来获取文件的总字节数。如果服务器没有提供此头部，则无法获得总大小。
        
2. **获取已下载字节数 (`loaded`)：**
    
    - 调用 `resp.body.getReader()` 获取一个 **`ReadableStreamDefaultReader`**。
        
    - 通过循环调用 `reader.read()` 方法来读取数据块（Chunk）。
        
    - 每次读取到数据块时，根据数据块的长度累加 `loaded` 字节数。
        
    - 当 `read()` 返回 `{ done: true }` 时，表示下载完成。
        

|**对比点**|**XHR onprogress**|**Fetch (手动实现)**|
|---|---|---|
|**总大小来源**|`event.total`|`resp.headers.get('content-length')`|
|**已读大小来源**|`event.loaded`|每次 `reader.read()` 返回的数据块长度累加|
|**技术基础**|事件模型|`ReadableStream` 可读流|

### 2. 请求上传进度监控 (Uploading Progress)

这是监控客户端向服务器传输数据的过程（例如文件上传）。

#### XHR 实现方式（特殊对象）

XHR 提供了一个专门用于监控上传进度的对象。

- **API：** 监听 `xhr.upload` 对象的 `progress` 事件。
    
- **数据：** 事件对象与下载进度事件相同，包含 `loaded` 和 `total` 属性。
    
- **优势：** 结构清晰，上传逻辑和下载逻辑分离，且有原生事件支持。
    

#### Fetch 实现方式（原生缺失）

**标准的 Fetch API 原生不支持请求上传进度监控**，因为它在设计上将请求体视为一个静态的、已经准备好的数据块，没有内置的机制来报告数据块发送到服务器的进度。

**解决方法（非原生）：**

开发者必须使用更复杂的 Web API（如 `TransformStream` 或 `ReadableStream`）来拦截请求体的数据流，在数据被发送出去之前，手动注入进度跟踪逻辑。但这不是 Fetch API 本身的特性，属于高级封装手段。

---

## 总结：何时选择 XHR 或 Fetch

1. **对进度监控有刚需时：** 尤其是**上传进度**，使用 **XHR (或基于 XHR 的 Axios)** 是目前最简单、最可靠的原生解决方案。
    
2. **需要处理流式数据时：** Fetch 在处理大量数据流（例如处理下载响应体的进度，或分块处理数据）方面表现更优秀、更现代化。
    
3. **追求现代化 Promise 风格代码时：** Fetch 的 Promise 链式调用更符合现代 JavaScript 的异步编程范式，代码更简洁。