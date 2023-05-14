当 `<input type="file">` 元素的值发生改变时，会触发 `change` 事件，并将一个 `Event` 对象作为参数传递给事件处理函数。该 `Event` 对象包含有关事件的详细信息，包括用户选择的文件。

以下是关于 `Event` 对象、`event.target` 和 `event.target.files` 的说明：

- `Event` 对象：表示发生的事件，包含有关事件的详细信息。在 `<input type="file">` 元素的 `change` 事件中，`Event` 对象通常被简称为 `event`。
- `event.target`：表示触发事件的元素。在 `<input type="file">` 元素的 `change` 事件中，`event.target` 是指触发事件的 `<input>` 元素。
- `event.target.files`：表示用户选择的文件列表。在 `<input type="file">` 元素的 `change` 事件中，`event.target.files` 是一个 `FileList` 对象，它包含用户选择的一个或多个文件。`FileList` 对象类似于数组，可以使用数组的方法进行操作。

例如，当用户选择一个文件后，可以使用以下代码打印出 `event`、`event.target` 和 `event.target.files` 的值：

```js
<input type="file" id="fileInput" onchange="handleFileSelect(event)">
<script>
function handleFileSelect(event) {
  console.log(event); // 打印 Event 对象
  console.log(event.target); // 打印触发事件的元素
  console.log(event.target.files); // 打印用户选择的文件列表
}
</script>
```

当用户选择一个名为 `example.jpg` 的文件后，控制台将显示如下信息：

```js
Event {
  ...
  target: input#fileInput,
  ...
}
input#fileInput
FileList [File]
  0: File {name: "example.jpg", type: "image/jpeg", size: 12345}
  length: 1
  __proto__: FileList
```

可以看到，`event.target` 是指触发事件的 `<input>` 元素，`event.target.files` 是一个包含一个文件的 `FileList` 对象。如果用户选择了多个文件，则 `event.target.files` 将包含多个文件。