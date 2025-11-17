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

在 HTML 解析过程中，当遇到 `<script>` 标签时，浏览器会暂停解析 HTML，并开始解析和执行 `<script>` 标签内的 JavaScript 代码。这是因为 JavaScript 代码可能会对当前的 DOM 结构进行修改，或者执行一些与页面交互相关的操作。

解析和执行 JavaScript 代码需要一定的时间，如果在执行 JavaScript 代码时继续解析 HTML，可能会导致以下问题：

1. DOM 结构不一致：如果 JavaScript 代码修改了当前的 DOM 结构，而解析器继续解析 HTML，可能会导致解析器和 JavaScript 代码对 DOM 结构的理解不一致，从而引发错误。

2. JavaScript 依赖：JavaScript 代码可能会依赖于当前文档中的其他元素或资源，例如需要操作某个元素的属性或样式，或者需要获取某个外部脚本或样式表等。如果解析器继续解析 HTML，可能会导致 JavaScript 代码无法正确执行，因为它所依赖的资源还没有被解析和加载。

因此，为了确保 JavaScript 代码在正确的上下文中执行，并且能够正确地修改 DOM 结构和处理相关资源，浏览器在遇到 `<script>` 标签时会暂停解析 HTML，先执行 JavaScript 代码，待 JavaScript 代码执行完毕后再继续解析 HTML。这样可以保证 JavaScript 代码的正确性和一致性，并确保页面的正确渲染和交互行为。

当遇到如下的 HTML 代码时，解析器在遇到 `<script>` 标签时会暂停解析 HTML，执行 `<script>` 标签内的 JavaScript 代码：

```html
<html>
  <head>
    <title>Example</title>
  </head>
  <body>
    <h1>Hello, World!</h1>

    <script>
      // JavaScript 代码
      var heading = document.querySelector('h1');
      heading.textContent = 'Hello, JavaScript!';
    </script>

    <p>This is a paragraph.</p>
  </body>
</html>
```

在这个例子中，当解析器遇到 `<script>` 标签时，它会暂停解析 HTML，并执行 `<script>` 标签内的 JavaScript 代码。JavaScript 代码通过 `document.querySelector('h1')` 获取到 `h1` 元素，并将其文本内容修改为 `'Hello, JavaScript!'`。

如果解析器不暂停解析 HTML，而是继续解析下面的 `<p>` 标签，那么在执行 JavaScript 代码之前，`h1` 元素还是原始的 `'Hello, World!'`，而不是 `'Hello, JavaScript!'`。这会导致 JavaScript 代码与当前的 DOM 结构不一致，可能引发错误或不符合预期的结果。

因此，为了确保 JavaScript 代码能够正确地修改 DOM 结构，解析器会暂停解析 HTML，先执行 JavaScript 代码，待 JavaScript 代码执行完毕后再继续解析 HTML。

当使用 `<script>` 标签的 `async` 属性时，浏览器在遇到带有 `async` 属性的 `<script>` 标签时，会继续解析 HTML，而不会暂停解析。

使用 `async` 属性的 `<script>` 标签将异步加载 JavaScript 文件，并在加载完成后立即执行。这意味着浏览器可以继续解析后续的 HTML 内容，而不必等待 JavaScript 文件完全加载和执行。

例如，考虑以下示例：

```html
<html>
  <head>
    <title>Example</title>
  </head>
  <body>
    <h1>Hello, World!</h1>

    <script async src="script.js"></script>

    <p>This is a paragraph.</p>
  </body>
</html>
```

在这个例子中，带有 `async` 属性的 `<script>` 标签将异步加载名为 `script.js` 的 JavaScript 文件。浏览器会继续解析 HTML，并在加载和执行 JavaScript 文件时不会阻塞解析。

这意味着在 JavaScript 文件加载和执行期间，`<p>` 标签可以继续被解析和渲染，而不需要等待 JavaScript 文件的加载完成。这样可以提高页面的加载性能和响应速度。

但需要注意的是，由于异步加载和执行，`async` 属性的 `<script>` 标签的执行顺序可能会与其在 HTML 中的顺序不一致。因此，如果 JavaScript 代码依赖于其他 JavaScript 文件或 DOM 结构的特定状态，可能需要进行适当的处理和管理，以确保代码的正确执行。


在使用 `<script>` 标签加载外部 JavaScript 文件时，可以使用 `async` 和 `defer` 属性来控制脚本的加载和执行行为。这两个属性有以下区别：

1. **async**: 当浏览器遇到带有 `async` 属性的 `<script>` 标签时，它会异步加载脚本，而不会等待脚本下载和执行完成后再继续解析 HTML 页面。这意味着脚本的下载和执行是并行进行的，不会阻塞页面的解析和渲染。一旦脚本下载完成，立即执行。多个带有 `async` 属性的脚本之间的执行顺序是不确定的，取决于其下载和执行的相对速度。

   ```html
   <script src="script1.js" async></script>
   <script src="script2.js" async></script>
   ```

2. **defer**: 使用 `defer` 属性的 `<script>` 标签也会异步加载脚本，但是它会在 HTML 页面解析完成后、`DOMContentLoaded` 事件触发之前执行。多个带有 `defer` 属性的脚本会按照它们在 HTML 页面中的顺序执行。与 `async` 不同，`defer` 保证了脚本的执行顺序。
[[从URL到页面展示]]
   ```html
   <script src="script1.js" defer></script>
   <script src="script2.js" defer></script>
   ```
https://blog.csdn.net/zyj0209/article/details/79698430
总结来说，`async` 属性用于异步加载并立即执行脚本，而 `defer` 属性用于异步加载脚本并在文档解析完成后执行。如果脚本之间的执行顺序很重要，可以使用 `defer` 属性。如果脚本之间的执行顺序不重要，可以使用 `async` 属性以提高页面加载性能。

