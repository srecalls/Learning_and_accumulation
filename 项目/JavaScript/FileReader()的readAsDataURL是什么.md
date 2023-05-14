`FileReader` 是一个用于读取文件内容的 JavaScript API，它提供了多种读取文件的方法，其中包括 `readAsDataURL()` 方法。

`readAsDataURL()` 方法是 `FileReader` 对象的一个方法，它可以将指定的 `File` 或 `Blob` 对象读取为一个 base64 编码的字符串，即 data URL。data URL 是一种将小型数据嵌入到文档中的方便方式，可以用于直接在浏览器中显示图片、视频、音频等媒体文件，或将文本文件以 URL 的形式发送到服务器。

以下是一个使用 `readAsDataURL()` 方法将本地图片转换为 data URL 的示例代码：

```
<input type="file" onchange="handleFileSelect(event)">
<img id="preview">

<script>
function handleFileSelect(event) {
  const file = event.target.files[0];
  const reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = function () {
    const preview = document.getElementById('preview');
    preview.src = reader.result;
  };
}
</script>
```

在这个示例中，当用户选择一个文件后，我们创建了一个 `FileReader` 对象，并调用 `readAsDataURL()` 方法将文件读取为 data URL。然后，我们在 `onload` 事件处理程序中将 data URL 赋值给 `<img>` 元素的 `src` 属性，从而在页面上显示图片。

需要注意的是，使用 `readAsDataURL()` 方法读取大文件时，可能会导致浏览器性能问题，因为 data URL 的长度会随着文件大小的增加而增加。因此，建议仅在读取小型文件时使用 `readAsDataURL()` 方法。



# reader.onload()是干什么的
`reader.onload` 是 `FileReader` 对象的一个事件处理函数，它会在读取文件完成后被触发。该事件的 `event.target.result` 属性包含了读取的文件内容。

当使用 `FileReader` 对象读取文件时，我们通常需要在 `onload` 事件处理函数中处理读取的文件内容。例如，当我们使用 `readAsText()` 方法将文本文件读取为字符串时，可以在 `onload` 事件处理函数中调用字符串处理函数来处理读取的文本内容。

以下是一个使用 `reader.onload` 处理读取的文本文件的示例代码：

```
<input type="file" onchange="handleFileSelect(event)">
<pre id="text"></pre>

<script>
function handleFileSelect(event) {
  const file = event.target.files[0];
  const reader = new FileReader();
  reader.readAsText(file);
  reader.onload = function () {
    const text = document.getElementById('text');
    text.textContent = reader.result;
  };
}
</script>
```

在这个示例中，我们创建了一个 `FileReader` 对象，并使用 `readAsText()` 方法将选择的文本文件读取为字符串。然后，我们在 `onload` 事件处理函数中将读取的文本内容赋值给 `<pre>` 元素的 `textContent` 属性，从而在页面上显示文本内容。

需要注意的是，`reader.onload` 事件只有在读取完成后才会被触发，因此在处理文件内容时应该放在 `onload` 事件处理函数中。