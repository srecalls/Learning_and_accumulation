script标签里的async和defer有什么区别?
当没有async和defer这两个属性的时候，
浏览器会立刻加载并执行指定的脚本

有async   h5属性里有的
加载和渲染后面元素的过程将和script的加载和执行并行进行(异步)
有defer
加载和渲染后面元素的过程将和script的加载并行进行(异步)，但是它的执行事件要等
所有元素解析完成之后才会执行

浏览器在解析源文件的时候，遇到了script要引入一些脚本，解析过程就会暂停，并且发起请求，将script脚本下载下来，只有完全下载并执行后才进行DOM的解析，如果有很多脚本文件，就会阻塞页面的渲染

defer要比async的创建时间要早
defer会保证脚本下载的顺序


在使用 `<script>` 标签加载外部 JavaScript 文件时，可以使用 `async` 和 `defer` 属性来控制脚本的加载和执行行为。这两个属性有以下区别：

1. **async**: 当浏览器遇到带有 `async` 属性的 `<script>` 标签时，它会异步加载脚本，而不会等待脚本下载和执行完成后再继续解析 HTML 页面。这意味着脚本的下载和执行是并行进行的，不会阻塞页面的解析和渲染。一旦脚本下载完成，立即执行。多个带有 `async` 属性的脚本之间的执行顺序是不确定的，取决于其下载和执行的相对速度。

   ````html
   <script src="script1.js" async></script>
   <script src="script2.js" async></script>
   ```

2. **defer**: 使用 `defer` 属性的 `<script>` 标签也会异步加载脚本，但是它会在 HTML 页面解析完成后、`DOMContentLoaded` 事件触发之前执行。多个带有 `defer` 属性的脚本会按照它们在 HTML 页面中的顺序执行。与 `async` 不同，`defer` 保证了脚本的执行顺序。

   ````html
   <script src="script1.js" defer></script>
   <script src="script2.js" defer></script>
   ```

总结来说，`async` 属性用于异步加载并立即执行脚本，而 `defer` 属性用于异步加载脚本并在文档解析完成后执行。如果脚本之间的执行顺序很重要，可以使用 `defer` 属性。如果脚本之间的执行顺序不重要，可以使用 `async` 属性以提高页面加载性能。