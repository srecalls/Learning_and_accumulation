在前端中，可以使用 `crypto` 模块提供的 `createHash()` 方法来计算文件的 MD5 值，并将其发送到后端进行比较以避免文件重复上传。

以下是一个使用 `createHash()` 方法计算文件 MD5 值的示例代码：

```js
/**
 * 计算文件的 MD5 值
 * @param {File} file 要计算的文件
 * @returns {Promise<String>} Promise 对象，计算完成后返回文件的 MD5 值
 */
function computeFileMD5(file) {
  return new Promise((resolve, reject) => {
    const chunkSize = 1024 * 1024; // 每次读取 1MB 数据
    const chunks = Math.ceil(file.size / chunkSize);
    let currentChunk = 0;
    const hash = crypto.createHash('md5');

    const fileReader = new FileReader();
    fileReader.onload = function(e) {
      const data = e.target.result;
      hash.update(data);
      currentChunk++;

      if (currentChunk < chunks) {
        loadNextChunk();
      } else {
        const md5 = hash.digest('hex');
        resolve(md5);
      }
    };

    fileReader.onerror = function() {
      reject(new Error('读取文件出错'));
    };

    function loadNextChunk() {
      const start = currentChunk * chunkSize;
      const end = Math.min(start + chunkSize, file.size);
      fileReader.readAsArrayBuffer(file.slice(start, end));
    }

    loadNextChunk();
  });
}
```

这个函数接受一个 `File` 对象作为参数，然后使用 `FileReader` 对象读取文件内容，并在读取的过程中计算文件的 MD5 值。由于文件可能非常大，因此将文件分成多个块逐个读取，以避免一次性读取整个文件导致内存不足。最后，返回一个 `Promise` 对象，计算完成后返回文件的 MD5 值。

在实际使用中，可以将文件的 MD5 值作为文件的唯一标识符，并将其发送到后端进行比较，以判断文件是否已经存在。如果文件存在，则避免重复上传。如果文件不存在，则可以上传文件。