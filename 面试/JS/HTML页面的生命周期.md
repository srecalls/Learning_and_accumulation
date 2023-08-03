当用户在浏览器中输入网址或点击链接时，浏览器开始加载Web页面，这个生命周期可以分为以下几个阶段：

## 1. 加载阶段（Loading Phase）：

在加载阶段，浏览器会发送请求获取HTML文档，并解析HTML文档中的资源，包括CSS、JavaScript、图片等。在这个阶段中，可以使用以下API来监听和控制页面的加载过程：

- `DOMContentLoaded`事件：当HTML文档被解析完成，DOM树被构建完成时触发。通常在此事件中执行一些初始化操作，如绑定事件监听器、修改DOM节点等。
- `window.onload`事件：当所有资源（包括CSS、JavaScript、图片等）都被加载并完成解析时触发。通常在此事件中执行一些耗时操作，如渲染图表、加载动画等。

## 2. 解析阶段（Parsing Phase）：

在解析阶段，浏览器会解析HTML文档，并下载HTML文档中所引用的资源。在这个阶段中，可以使用以下API来监听和控制文档的解析过程：

- `document.readyState`属性：表示文档的加载状态，有三个可取值，分别是"loading"、"interactive"和"complete"。可以通过监听该属性的变化来控制页面的加载过程。
    - loading 文档仍然在加载
    - interactive 文档结束加载并且被解析，但是像图片，样式，frame之类的子资源仍在加载
    - complete 文档和子资源已经结束加载，该状态表明将要触发load事件。
- `document.onreadystatechange`事件：当文档的`readyState`属性发生变化时触发。通常可以在此事件中执行一些状态判断，如判断页面是否已加载完成。

## 3. 渲染阶段（Rendering Phase）：

在渲染阶段，浏览器会根据HTML文档和CSS样式对页面进行渲染，并执行JavaScript代码。在这个阶段中，可以使用以下API来监听和控制页面的渲染过程：

- `requestAnimationFrame()`方法：该方法可以在浏览器下一次重绘之前执行指定的函数，可以用来优化页面的动画性能。
- `window.getComputedStyle()`方法和`style`属性：用于获取和修改元素的CSS样式，可以用来控制页面的外观。
- `Intersection Observer API`：用于监测元素与视口的交叉状态，可以用来实现懒加载等功能。

## 4. 卸载阶段（Unloading Phase）：

在卸载阶段，当用户关闭或离开当前页面时，浏览器会卸载当前页面，释放相关资源。在这个阶段中，可以使用以下API来监听和控制页面的卸载过程：

- `window.onbeforeunload`事件：当用户尝试离开当前页面时触发，可以用来提示用户保存数据等操作。
- `window.onunload`事件：当页面被完全卸载时触发，可以用来清理资源等操作。

总的来说，了解Web页面的生命周期和相应的API，可以帮助我们更好地理解和掌控页面的加载、解析、渲染和卸载过程，从而优化页面性能，提升用户体验。


一般浏览器的加载顺序如下：

- script executed
- readyState : interactive
- DOMContentLoaded
- image onload
- iframe onload
- readyState : complete
- window onload

从以上可以看出同步的Script总是先于其它事件执行，而window.onload事件总是最后执行。而image onload和iframe onload的先后顺序并不确定。


onload页面加载完成时触发，onpageshow页面显示时触发，onbeforeunload页面跳转前触发。