`URL.createObjectURL()` 是一个用于创建一个指向本地文件的 URL 的 API。它接收一个 `File` 或 `Blob` 对象作为参数，并返回一个指向该对象的 URL。

`URL.createObjectURL()` 方法的作用是将 `File` 或 `Blob` 对象转换为指向本地文件的 URL，从而可以在浏览器中预览或处理文件，例如在 `<img>` 元素中显示图片或在 `<audio>` 或 `<video>` 元素中播放音频或视频。

`URL.createObjectURL()` 方法创建的 URL 是一个 `blob:` 协议的 URL，它类似于 `http:` 或 `https:` 协议的 URL，但实际上并不指向网络上的资源，而是指向本地的一个临时文件。这个临时文件在页面卸载后会自动被浏览器删除，因此不需要手动清除。

以下是一个使用 `URL.createObjectURL()` 方法将本地图片显示在 `<img>` 元素中的示例代码：

```
<input type="file" onchange="handleFileSelect(event)">
<img id="preview">

<script>
function handleFileSelect(event) {
  const file = event.target.files[0];
  const preview = document.getElementById('preview');
  preview.src = URL.createObjectURL(file);
}
</script>
```

在这个示例中，当用户选择一个文件后，我们将文件对象传递给 `URL.createObjectURL()` 方法，从而创建一个指向本地文件的 URL。然后，我们将该 URL 赋值给 `<img>` 元素的 `src` 属性，从而在页面上显示图片。需要注意的是，在页面卸载前，应该调用 `URL.revokeObjectURL()` 方法，将创建的 URL 释放掉，以避免内存泄漏。