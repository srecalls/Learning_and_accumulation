好的，这里汇总一下之前提到的所有常见 DOM 元素属性：


- `offsetTop`：`offsetTop`属性返回一个元素相对于其父元素的偏移量（offset）。偏移量是指元素的顶部边缘相对于其最近的已定位祖先元素（position为relative、absolute或fixed）的顶部边缘的距离。如果没有已定位的祖先元素，则偏移量是相对于文档的顶部边缘。返回值是一个整数。

  例子：

  ```html
  <div id="parent" style="position: relative; top: 50px;">
    <div id="child" style="position: relative; top: 20px;"></div>
  </div>
  ```

  ```javascript
  const parent = document.getElementById('parent');
  const child = document.getElementById('child');

  console.log(child.offsetTop); // 输出: 20
  ```

- `offsetLeft`：`offsetLeft`属性返回一个元素相对于其父元素的偏移量（offset）。偏移量是指元素的左侧边缘相对于其最近的已定位祖先元素（position为relative、absolute或fixed）的左侧边缘的距离。如果没有已定位的祖先元素，则偏移量是相对于文档的左侧边缘。返回值是一个整数。

  例子：

  ```html
  <div id="parent" style="position: relative; left: 50px;">
    <div id="child" style="position: relative; left: 20px;"></div>
  </div>
  ```

  ```javascript
  const parent = document.getElementById('parent');
  const child = document.getElementById('child');

  console.log(child.offsetLeft); // 输出: 20
  ```

- `offsetWidth`：`offsetWidth`属性返回一个元素的整体宽度，包括其内容区域、内边距和边框的宽度。返回值是一个浮点数（包含小数部分）。

  例子：

  ```html
  <div id="element" style="width: 200px; padding: 10px; border: 1px solid black;">
    Hello, World!
  </div>
  ```

  ```javascript
  const element = document.getElementById('element');

  console.log(element.offsetWidth); // 输出: 212（200 + 2*10 + 2*1）
  ```

- `offsetHeight`：`offsetHeight`属性返回一个元素的整体高度，包括其内容区域、内边距和边框的高度。返回值是一个浮点数（包含小数部分）。

  例子：

  ```html
  <div id="element" style="height: 100px; padding: 10px; border: 1px solid black;">
    Hello, World!
  </div>
  ```

  ```javascript
  const element = document.getElementById('element');

  console.log(element.offsetHeight); // 输出: 122（100 + 2*10 + 2*1）
  ```

- `getComputedStyle()`方法：`getComputedStyle()`是一个用于获取计算样式（computed style）的方法。它返回一个对象，包含指定元素的所有计算样式属性和对应的值。

  例子：

  ```html
  <div id="element" style="width: 200px; height: 100px; padding: 10px; border: 1px solid black;">
    Hello, World!
  </div>
  ```

  ```javascript
  const element = document.getElementById('element');
  const computedStyle = window.getComputedStyle(element);

  console.log(computedStyle.width); // 输出: "200px"
  console.log(computedStyle.padding); // 输出: "10px"
  console.log(computedStyle.border); // 输出: "1px solid rgb(0, 0, 0)"
  ```

  `getComputedStyle()`方法返回的是一个只读对象，其中包含了计算后的样式信息，包括继承的样式和通过CSS样式表定义的样式。





1. `id`: 返回或设置元素的 id 属性值。

2. `className` 或 `classList`: 返回或设置元素的类名。
   
3. `document.documentElement` 是文档元素对象，它代表整个 HTML 页面。它是 `document` 对象的一个属性，可以通过 `document.documentElement` 来访问。

4. `nodeName` 或 `tagName`: 返回元素的标签名。

5. `nodeValue`: 返回或设置元素的节点值。

6. `textContent`: 返回或设置元素的文本内容。

7. `style`: 返回一个表示元素样式的 CSSStyleDeclaration 对象。

8. `attributes`: 返回一个表示元素属性的 NamedNodeMap 对象。

9. `parentElement`: 返回元素的父元素。

10. `childNodes`: 返回元素的所有子节点，是一个 NodeList 对象。

11. `firstChild`: 返回元素的第一个子节点。

12. `lastChild`: 返回元素的最后一个子节点。

13. `nextSibling`: 返回元素的下一个兄弟节点。

14. `previousSibling`: 返回元素的上一个兄弟节点。

15. `offsetParent`: 返回最近的已定位祖先元素，通常是父元素。

16. `offsetLeft`: 返回元素的左边界到 offsetParent 元素的左边界之间的像素距离。

17. `offsetTop`: 返回元素的上边界到 offsetParent 元素的上边界之间的像素距离。

18. `clientWidth`: 返回元素的可见宽度，包括内边距但不包括滚动条和边框。

19. `clientHeight`: 返回元素的可见高度，包括内边距但不包括滚动条和边框。

20. `offsetWidth`: 返回元素的宽度，包括内边距、滚动条和边框。

21. `offsetHeight`: 返回元素的高度，包括内边距、滚动条和边框。

22. `scrollWidth`: 返回元素的内容区域宽度，包括未显示的内容。

23. `scrollHeight`: 返回元素的内容区域高度，包括未显示的内容。

24. `scrollTop`: 返回元素内容区域顶部隐藏的像素数。

25. `scrollLeft`: 返回元素内容区域左侧隐藏的像素数。

26. `disabled`: 返回或设置元素是否被禁用，通常用于表单元素。

27. `checked`: 返回或设置元素是否被选中，通常用于单选框和复选框元素。

28. `innerHTML`: 获取或设置元素的 HTML 内容。

29. `outerHTML`: 获取或设置元素及其所有子元素的 HTML 内容。

30. `focus()`: 让元素获得焦点。

31. `blur()`: 让元素失去焦点。

32. `addEventListener()`: 用于为元素添加事件监听器。

33. `removeEventListener()`: 用于移除元素的事件监听器。

34. `getBoundingClientRect()`: 返回元素的大小及其相对于视口的位置。

35. `contains()`: 用于检查一个元素是否是另一个元素的后代节点。

36. `setAttribute()`: 设置元素的属性值。

37. `getAttribute()`: 获取元素的属性值。

38. `removeAttribute()`: 移除元素的属性。

39. `querySelector()`: 返回第一个匹配选择器的元素。

40. `querySelectorAll()`: 返回所有匹配选择器的元素列表。

41. `dataset`: 返回一个表示元素自定义数据属性的 DOMStringMap 对象。

42. `getElementsByClassName()`: 返回所有具有指定类名的元素的集合。

43. `getElementsByTagName()`: 返回所有具有指定标签名的元素的集合。

44. `createElement()`: 创建一个新的元素节点。

45. `appendChild()`: 将一个新的子元素添加到元素的子节点列表的末尾。

46. `removeChild()`: 从元素的子节点列表中移除一个子节点。

47. `replaceChild()`: 用一个新的子节点替换元素的子节点列表中的一个子节点。

48. `insertBefore()`: 在元素的子节点列表中的指定位置插入一个新的子节点。

49. `classList`: 返回一个表示元素类名的 DOMTokenList 对象，可以用于添加、删除和查找类名。

50. `scrollIntoView()`: 让元素滚动到可见区域。

51. `scrollBy()`: 将元素滚动指定的偏移量。

52. `scrollTo()`: 将元素滚动到指定的坐标。

53. `getComputedStyle()`: 返回一个表示元素最终计算样式的 CSSStyleDeclaration 对象。

54. `offset()`: 返回一个包含元素的位置和尺寸信息的对象。

55. `clientX` 和 `clientY`: 返回鼠标事件的客户端坐标，即相对于视口的坐标。

56. `pageX` 和 `pageY`: 返回鼠标事件的页面坐标，即相对于文档的坐标。

57. `offsetX` 和 `offsetY`: 返回鼠标事件的相对坐标，即相对于事件目标的坐标。

58. `contentEditable`：设置元素是否可编辑。

59. `document`：返回文档对象，可以用于访问和操作整个文档。

60. `window`：返回窗口对象，可以用于访问和操作浏览器窗口。

61. `localStorage`：返回一个表示本地存储的 Storage 对象，可以用于存储和读取数据。

62. `sessionStorage`：返回一个表示会话存储的 Storage 对象，可以用于存储和读取数据。

63. `requestAnimationFrame()`：用于在下一次重绘之前执行指定的动画函数。

64. `cancelAnimationFrame()`：用于取消之前通过 requestAnimationFrame() 方法添加的动画函数。

65. `setTimeout()`：用于在指定的时间后执行指定的函数。

66. `clearTimeout()`：用于取消之前通过 setTimeout() 方法添加的函数。

67. `setInterval()`：用于每隔指定的时间执行指定的函数。

68. `clearInterval()`：用于取消之前通过 setInterval() 方法添加的函数。

这些属性和方法是进行 DOM 操作时常用的工具，可以用于创建、添加、删除、替换和查找元素，或者操作元素的类名、样式、位置、尺寸、属性、事件、滚动、内容等。需要注意的是，某些属性和方法可能只在特定的浏览器中受支持，因此在使用时需要进行兼容性处理


好的，下面是加上二级标题后的举例说明：

## 1. `id`

```html
<div id="example">Example</div>
```

```javascript
const element = document.getElementById('example');
console.log(element.id); // "example"
element.id = 'new-example';
console.log(element.id); // "new-example"
```

## 2. `className` 或 `classList`

```html
<div class="example">Example</div>
```

```javascript
const element = document.querySelector('.example');
console.log(element.className); // "example"
element.classList.add('new-class');
console.log(element.classList); // ["example", "new-class"]
element.classList.remove('example');
console.log(element.classList); // ["new-class"]
```

## 3. `nodeName` 或 `tagName`

```html
<div>Example</div>
```

```javascript
const element = document.querySelector('div');
console.log(element.nodeName); // "DIV"
console.log(element.tagName); // "DIV"
```

## 4. `nodeValue`

```html
<div>Example</div>
```

```javascript
const element = document.querySelector('div');
console.log(element.childNodes[0].nodeValue); // "Example"
element.childNodes[0].nodeValue = 'New Example';
console.log(element.childNodes[0].nodeValue); // "New Example"
```

## 5. `textContent`

```html
<div>Example</div>
```

```javascript
const element = document.querySelector('div');
console.log(element.textContent); // "Example"
element.textContent = 'New Example';
console.log(element.textContent); // "New Example"
```

## 6. `style`

```html
<div style="color: red;">Example</div>
```


```javascript
const element = document.querySelector('div');
console.log(element.style.color); // "red"
element.style.backgroundColor = 'yellow';
console.log(element.style.backgroundColor); // "yellow"
```

## 7. `attributes`

```html
<div id="example" class="example" data-name="example">Example</div>
```

   ```javascript
   const element = document.querySelector('div');
   console.log(element.attributes); // [id, class, data-name]
   console.log(element.getAttribute('id')); // "example"
   element.setAttribute('data-name', 'new-example');
   console.log(element.getAttribute('data-name')); // "new-example"
   element.removeAttribute('class');
   console.log(element.attributes); // [id, data-name]
   ```

## 8. `parentElement`

   ```html
   <div>
     <p>Example</p>
   </div>
   ```

   ```javascript
   const element = document.querySelector('p');
   console.log(element.parentElement.tagName); // "DIV"
   ```

## 9. `childNodes`

   ```html
   <div>
     <p>Example 1</p>
     <p>Example 2</p>
   </div>
   ```

   ```javascript
   const element = document.querySelector('div');
   console.log(element.childNodes); // [p, text, p, text]
   console.log(element.childNodes[1].nodeValue); // " "
   ```

## 10. `firstChild`

```html
<div>
 <p>Example 1</p>
 <p>Example 2</p>
</div>
```

   ```javascript
   const element = document.querySelector('div');
   console.log(element.firstChild.tagName); // "P"
   ```

好的，接下来是剩下的属性的举例说明：

## 11. `firstElementChild`

   ```html
   <div>
     <p>Example 1</p>
     <p>Example 2</p>
   </div>
   ```

   ```javascript
   const element = document.querySelector('div');
   console.log(element.firstElementChild.tagName); // "P"
   ```

## 12. `lastChild`

   ```html
   <div>
     <p>Example 1</p>
     <p>Example 2</p>
     Text Node
   </div>
   ```

   ```javascript
   const element = document.querySelector('div');
   console.log(element.lastChild.nodeType); // 3 (text node)
   ```

## 13. `lastElementChild`

   ```html
   <div>
     <p>Example 1</p>
     <p>Example 2</p>
   </div>
   ```

   ```javascript
   const element = document.querySelector('div');
   console.log(element.lastElementChild.tagName); // "P"
   ```

## 14. `nextSibling`

   ```html
   <div>
     <p>Example 1</p>
     <p>Example 2</p>
   </div>
   ```

   ```javascript
   const element = document.querySelector('p:first-child');
   console.log(element.nextSibling.nodeType); // 3 (text node)
   console.log(element.nextSibling.nodeValue); // "\n     "
   console.log(element.nextSibling.nextSibling.tagName); // "P"
   ```

## 15. `nextElementSibling`

   ```html
   <div>
     <p>Example 1</p>
     <p>Example 2</p>
   </div>
   ```

   ```javascript
   const element = document.querySelector('p:first-child');
   console.log(element.nextElementSibling.tagName); // "P"
   ```

## 16. `previousSibling`

   ```html
   <div>
     <p>Example 1</p>
     <p>Example 2</p>
   </div>
   ```

   ```javascript
   const element = document.querySelector('p:last-child');
   console.log(element.previousSibling.nodeType); // 3 (text node)
   console.log(element.previousSibling.nodeValue); // "\n     "
   console.log(element.previousSibling.previousSibling.tagName); // "P"
   ```

## 17. `previousElementSibling`

   ```html
   <div>
     <p>Example 1</p>
     <p>Example 2</p>
   </div>
   ```

   ```javascript
   const element = document.querySelector('p:last-child');
   console.log(element.previousElementSibling.tagName); // "P"
   ```

## 18. `children`

   ```html
   <div>
     <p>Example 1</p>
     <p>Example 2</p>
   </div>
   ```

   ```javascript
   const element = document.querySelector('div');
   console.log(element.children); // [p, p]
   console.log(element.children[0].tagName); // "P"
   ```

## 19. `classList`


   ```html
   <div class="example">Example</div>
   ```

   ```javascript
   const element = document.querySelector('.example');
   console.log(element.classList); // ["example"]
   element.classList.add('new-class');
   console.log(element.classList); // ["example", "new-class"]
   element.classList.remove('example');
   console.log(element.classList); // ["new-class"]
   ```

## 20. `dataset`

   ```html
   <div data-name="example" data-age="25">Example</div>
   ```

   ```javascript
   const element = document.querySelector('div');
   console.log(element.dataset.name); // "example"
   console.log(element.dataset.age); // "25"
   element.dataset.name = 'new-example';
   console.log(element.dataset.name); // "new-example"
   ```

好的，下面是剩余的属性的举例说明：

## 21. `clientWidth` 和 `clientHeight`

   ```html
   <div style="width: 200px; height: 100px; border: 1px solid black;">Example</div>
   ```

   ```javascript
   const element = document.querySelector('div');
   console.log(element.clientWidth); // 200
   console.log(element.clientHeight); // 100
   ```

## 22. `offsetWidth` 和 `offsetHeight`

   ```html
   <div style="width: 200px; height: 100px; padding: 20px; border: 1px solid black;">Example</div>
   ```

   ```javascript
   const element = document.querySelector('div');
   console.log(element.offsetWidth); // 242 (200 + 20 + 20 + 1 + 1)
   console.log(element.offsetHeight); // 142 (100 + 20 + 20 + 1 + 1)
   ```

## 23. `scrollWidth` 和 `scrollHeight`

   ```html
   <div style="width: 200px; height: 100px; overflow: scroll; border: 1px solid black;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac leo lobortis, volutpat nibh nec, commodo orci. Donec venenatis, ante nec malesuada fringilla, tellus nibh malesuada libero, vitae feugiat enim nunc a libero. Donec ut velit eget elit venenatis maximus. Phasellus bibendum, quam vel eleifend ultrices, mauris ipsum tincidunt velit, et varius dui elit vitae est. Sed vel tincidunt ante. Praesent ut lectus vitae velit pharetra imperdiet a vitae ipsum. Nam cursus enim vel sagittis pharetra. Praesent vel ante finibus, interdum metus eget, interdum ligula. Proin iaculis sapien ligula, nec luctus lorem luctus quis. Fusce sit amet bibendum mauris. Nam mollis pulvinar lacinia. Donec euismod enim vitae velit iaculis, at consequat velit bibendum. Curabitur ut nulla sit amet sapien congue suscipit. Nunc ac felis nisl.</div>
   ```

   ```javascript
   const element = document.querySelector('div');
   console.log(element.scrollWidth); // 2262 (2000 + 20 + 20 + 1 + 1 + 200 (scrollbar))
   console.log(element.scrollHeight); // 142 (100 + 20 + 20 + 1 + 1)
   ```

## 24. `scrollTop` 和 `scrollLeft`

   ```html
   <div style="width: 200px; height: 100px; overflow: scroll; border: 1px solid black;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac leo lobortis, volutpat nibh nec, commodo orci. Donec venenatis, ante nec malesuada fringilla, tellus nibh malesuada libero, vitae feugiat enim nunc a libero. Donec ut velit eget elit venenatis maximus. Phasellus bibendum, quam vel eleifend ultrices, mauris ipsum tincidunt velit, et varius dui elit vitae est. Sed vel tincidunt ante. Praesent ut lectus vitae velit pharetra imperdiet a vitae ipsum. Nam cursus enim vel sagittis pharetra. Praesent vel ante finibus, interdum metus eget, interdum ligula. Proin iaculis sapien ligula, nec luctus lorem luctus quis. Fusce sit amet bibendum mauris. Nam mollis pulvinar lacinia. Donec euismod enim vitae velit iaculis, at consequat velit bibendum. Curabitur ut nulla sit amet sapien congue suscipit. Nunc ac felis nisl.</div>
   ```

   ```javascript
   const element = document.querySelector('div');
   console.log(element.scrollTop); // 0
   console.log(element.scrollLeft); // 0
   element.scrollTop = 50;
   element.scrollLeft = 50;
   console.log(element.scrollTop); // 50
   console.log(element.scrollLeft); // 50
   ```

## 25. `scrollIntoView()`

   ```html
   <div id="example" style="margin-top: 1000px;">Example</div>
   <button onclick="scrollToExample()">Scroll to Example</button>
   <script>
     function scrollToExample() {
       const element = document.querySelector('#example');
       element.scrollIntoView({ behavior: 'smooth' });
     }
   </script>
   ```

   当点击 "Scroll to Example" 按钮时，页面会平滑滚动到带有 `id="example"` 的元素，而不是瞬间跳转。

## 26. `getBoundingClientRect()`

   ```html
   <div style="width: 200px; height: 100px; border: 1px solid black; margin-top: 100px;">Example</div>
   ```

   ```javascript
   const element = document.querySelector('div');
   const rect = element.getBoundingClientRect();
   console.log(rect.top); // 100
   console.log(rect.right); // 201 (200 + 1)
   console.log(rect.bottom); // 201 (100 + 1)
   console.log(rect.left); // 0
   console.log(rect.width); // 200
   console.log(rect.height); // 100
   ```

   ``getBoundingClientRect()` 方法返回一个 DOMRect 对象，该对象包含元素的位置、大小和其他信息。

## 27. `focus()` 和 `blur()`

   ```html
   <input type="text" id="example" placeholder="Example">
   <button onclick="focusInput()">Focus Input</button>
   <button onclick="blurInput()">Blur Input</button>
   <script>
     const input = document.querySelector('#example');
     function focusInput() {
       input.focus();
     }
     function blurInput() {
       input.blur();
     }
   </script>
   ```

   当点击 "Focus Input" 按钮时，输入框会获得焦点，光标会在输入框内闪烁。当点击 "Blur Input" 按钮时，输入框会失去焦点，光标会消失。

## 28. `click()`

   ```html
   <button id="example" onclick="alert('Example')">Example</button>
   <button onclick="clickButton()">Click Button</button>
   <script>
     const button = document.querySelector('#example');
     function clickButton() {
       button.click();
     }
   </script>
   ```

   当点击 "Click Button" 按钮时，页面会自动触发带有 `id="example"` 的按钮的点击事件，并弹出 "Example" 的提示框。

希望这些举例能够帮助你更好地理解和使用 DOM 元素的属性和方法。


好的，接下来是另外几个常用的 DOM 元素属性和方法：

## 29. `setAttribute()` 和 `getAttribute()`

   ```html
   <div id="example">Example</div>
   <button onclick="setAttributeExample()">Set Attribute</button>
   <button onclick="getAttributeExample()">Get Attribute</button>
   <script>
     const element = document.querySelector('#example');
     function setAttributeExample() {
       element.setAttribute('data-example', 'Hello, world!');
     }
     function getAttributeExample() {
       const value = element.getAttribute('data-example');
       alert(`The value of data-example is ${value}`);
     }
   </script>
   ```

   当点击 "Set Attribute" 按钮时，`data-example` 属性会被设置为 "Hello, world!"。当点击 "Get Attribute" 按钮时，会弹出一个提示框，其中显示 `data-example` 属性的值。

   ``setAttribute()` 方法用于设置指定元素的属性值，而 `getAttribute()` 方法用于获取指定元素的属性值。

## 30. `classList`

   ```html
   <div id="example" class="foo bar">Example</div>
   <button onclick="addExampleClass()">Add Class</button>
   <button onclick="removeExampleClass()">Remove Class</button>
   <button onclick="toggleExampleClass()">Toggle Class</button>
   <script>
     const element = document.querySelector('#example');
     function addExampleClass() {
       element.classList.add('baz');
     }
     function removeExampleClass() {
       element.classList.remove('bar');
     }
     function toggleExampleClass() {
       element.classList.toggle('foo');
     }
   </script>
   ```

   当点击 "Add Class" 按钮时，元素的类列表会添加一个名为 `baz` 的新类。当点击 "Remove Class" 按钮时，元素的类列表会移除名为 `bar` 的现有类。当点击 "Toggle Class" 按钮时，元素的类列表会在 `foo` 和 `baz` 之间切换。

   ``classList` 属性是一个只读属性，它返回一个 DOMTokenList 对象，该对象表示元素的类列表。可以使用 `add()`、`remove()` 和 `toggle()` 方法来修改元素的类列表。

## 31. `querySelector()` 和 `querySelectorAll()`

   ```html
   <ul>
     <li class="example">Example 1</li>
     <li>Example 2</li>
     <li class="example">Example 3</li>
     <li>Example 4</li>
   </ul>
   <button onclick="querySelectorExample()">Query Selector</button>
   <script>
     function querySelectorExample() {
       const element = document.querySelector('.example');
       console.log(element.textContent);
     }
   </script>
   ```

   当点击 "Query Selector" 按钮时，页面会输出所有带有 `class="example"` 的元素的文本内容，即 "Example 1" 和 "Example 3"。

   ``querySelector()` 方法用于返回匹配指定 CSS 选择器的第一个元素，而 `querySelectorAll()` 方法用于返回匹配指定 CSS 选择器的所有元素。

## 32. `createElement()` 和 `appendChild()`

   ```html
   <ul id="list"></ul>
   <button onclick="addElement()">Add Element</button>
   <script>
     const list = document.querySelector('#list');
     function addElement() {
       const element = document.createElement('li');
       element.textContent = 'New Example';
       list.appendChild(element);
     }
   </script>
   ```

   当点击 "Add Element" 按钮时，会向页面的无序列表 (`<ul>`) 中添加一个新的列表项 (`<li>`)，其文本内容为 "New Example"。

   ``createElement()` 方法用于创建一个新的元素节点，而 `appendChild()` 方法用于向指定元素的子节点列表的末尾添加一个新的子节点。

希望这些举例能够帮助你更好地了解和使用 DOM 元素的属性和方法。