`new FileReader()` 是 JavaScript 中的一个构造函数，用于创建一个新的 `FileReader` 对象。这个对象允许 Web 应用程序异步读取存储在用户计算机上的文件（或原始数据缓冲区）的内容，使用 `File` 或 `Blob` 对象指定要读取的文件或数据。下面我们将详细介绍 `FileReader` 的各个方面。

### 创建实例

创建一个 `FileReader` 实例非常简单，只需调用构造函数即可：

```javascript
var reader = new FileReader();
```

这行代码将生成一个新的 `FileReader` 对象，该对象可以用来读取文件内容。

### 属性

`FileReader` 提供了几个重要的属性来帮助我们了解读取的状态和结果：

- **`FileReader.error`**：这是一个只读属性，表示在读取文件时发生的错误。如果读取过程中没有发生错误，则此属性为 `null`。
  
- **`FileReader.result`**：这也是一个只读属性，它返回文件的内容。只有在读取操作完成后，此属性才有效，返回的数据的格式取决于使用哪种读取方法来执行读取操作。
  
- **`FileReader.readyState`**：这个只读属性表示 `FileReader` 的状态，可能的值包括：
  - `EMPTY` (0)：还没有加载任何数据。
  - `LOADING` (1)：数据正在被加载。
  - `DONE` (2)：已完成全部的读取请求。

### 方法

`FileReader` 提供了几种方法来启动文件读取操作：

- **`FileReader.abort()`**：终止读取操作。在返回时，`readyState` 属性为 `DONE`。
  
- **`FileReader.readAsArrayBuffer(blob)`**：开始读取指定的 `Blob` 中的内容。一旦完成，`result` 属性中保存的是被读取文件的 `ArrayBuffer` 数据对象。
  
- **`FileReader.readAsBinaryString(blob)`**：开始读取指定的 `Blob` 中的内容。一旦完成，`result` 属性中将包含所读取文件的原始二进制数据。注意，这个方法已经被废弃，推荐使用 `readAsArrayBuffer` 和 `TextDecoder` 来替代。
  
- **`FileReader.readAsDataURL(blob)`**：开始读取指定的 `Blob` 中的内容。一旦完成，`result` 属性中将包含一个 `data:` URL 格式的 Base64 字符串以表示所读取文件的内容。
  
- **`FileReader.readAsText(blob, encoding)`**：开始读取指定的 `Blob` 中的内容。一旦完成，`result` 属性中将包含一个字符串以表示所读取的文件内容。可以指定可选的编码名称，默认为 UTF-8。

### 事件

`FileReader` 支持一系列事件，这些事件可以帮助开发者跟踪读取过程中的各个阶段：

- **`onabort`**：当读取操作被中断时触发。
- **`onerror`**：当读取操作发生错误时触发。
- **`onload`**：当读取操作成功完成时触发。
- **`onloadend`**：当读取操作完成时触发，不管是成功还是失败。
- **`onloadstart`**：当读取操作即将开始之前触发。
- **`onprogress`**：在读取数据过程中周期性触发。

### 使用示例

#### 读取文本文件

以下是一个简单的例子，展示如何使用 `FileReader` 来读取文本文件：

```javascript
const input = document.querySelector('input[type=file]');
input.addEventListener('change', () => {
    const reader = new FileReader();
    reader.readAsText(input.files[0], 'utf8');
    reader.onload = () => {
        document.body.innerHTML += reader.result;
    };
}, false);
```

在这个例子中，当用户选择了一个文件后，`FileReader` 将会读取该文件的内容，并将其显示在页面上。

#### 读取图片文件

另一个常见的用例是预览用户选择的图片：

```javascript
const input = document.querySelector('input[type=file]');
input.addEventListener('change', () => {
    console.log(input.files);
    const reader = new FileReader();
    reader.readAsDataURL(input.files[0]);
    reader.onload = () => {
        const img = new Image();
        img.src = reader.result;
        document.body.appendChild(img);
    };
}, false);
```

这段代码展示了如何使用 `FileReader` 来读取图片文件，并将其作为图像元素添加到页面中。

### 注意事项

- `FileReader` 只能访问用户明确选择的文件内容，无论是通过 `<input type="file">` 元素还是通过拖放操作。它不能用于从用户的文件系统中按路径名读取文件。
- 如果需要按路径名读取客户端文件系统上的文件，请使用文件系统访问 API。
- 要读取服务器端文件，请使用 `fetch()`，如果跨源读取，则需要 CORS 权限。

综上所述，`new FileReader()` 是一个强大的工具，能够帮助开发者轻松实现文件的异步读取功能，适用于多种场景，如文件上传、图片预览等。