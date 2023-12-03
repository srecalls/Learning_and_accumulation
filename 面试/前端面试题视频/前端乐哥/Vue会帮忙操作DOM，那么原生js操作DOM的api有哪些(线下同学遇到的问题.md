
## 节点获取/查询
```js
document.getElementsByTagName('')
document.getElementById('')
document.getElementsByName('')
document.getElementsByClassName('')
document.querySelector('')
document.querySelectorAll('')
```


## 创建节点
```js
createElement
createTextNode
cloneNode
createDocumentFragment // 用来解决大量节点时候的性能问题
```

## 页面修改节点
```js
appendChild
insertBefore
removeChild
replaceChild
```

## 联想到 节点和节点之间的关系
```js
// 父：
parentNode // 父亲节点
parentElement // 父亲元素
// 兄弟：
previousSiblings // 前一个兄弟节点
previousElementSiblings // 前一个兄弟元素
nextSiblings // 后一个兄弟节点
nextElementSiblings // 后一个兄弟元素
// 子
childNodes // NodeList
children // Element IE9以下不支持
firstNode
lastNode
hasChildNodes // 判断是否有子节点
```


以下是关于节点获取/查询、创建节点和页面修改节点的示例代码和说明：

```js
// 节点获取/查询
document.getElementsByTagName('div'); // 获取所有<div>元素，返回HTMLCollection
document.getElementById('myElement'); // 获取id为myElement的元素
document.getElementsByName('myInput'); // 获取name为myInput的元素，返回NodeList
document.getElementsByClassName('myClass'); // 获取class为myClass的元素，返回HTMLCollection
document.querySelector('p'); // 获取第一个匹配的<p>元素
document.querySelectorAll('.myClass'); // 获取全部匹配的.myClass元素，返回NodeList

// 创建节点
var newElement = document.createElement('div'); // 创建一个<div>元素节点
var textNode = document.createTextNode('Hello'); // 创建一个文本节点，内容为Hello
var clonedNode = oldNode.cloneNode(true); // 克隆一个节点，参数为true表示深度克隆
var fragment = document.createDocumentFragment(); // 创建一个文档片段，用于高性能插入多个节点

// 页面修改节点
var parentElement = document.getElementById('parent');
var childElement = document.getElementById('child');

parentElement.appendChild(childElement); // 将childElement作为最后一个子节点插入parentElement中
parentElement.insertBefore(newElement, childElement); // 在childElement之前插入newElement节点
parentElement.removeChild(childElement); // 移除childElement节点
parentElement.replaceChild(newElement, childElement); // 用newElement节点替换childElement节点

// 节点和节点之间的关系
var parentNode = childElement.parentNode; // 获取父节点
var parentElement = childElement.parentElement; // 获取父元素节点
var previousSibling = childElement.previousSibling; // 获取前一个兄弟节点
var previousElementSibling = childElement.previousElementSibling; // 获取前一个兄弟元素节点
var nextSibling = childElement.nextSibling; // 获取后一个兄弟节点
var nextElementSibling = childElement.nextElementSibling; // 获取后一个兄弟元素节点
var childNodes = parentElement.childNodes; // 获取所有子节点，返回NodeList
var children = parentElement.children; // 获取所有子元素节点，返回HTMLCollection
var firstNode = parentElement.firstChild; // 获取第一个子节点
var lastNode = parentElement.lastChild; // 获取最后一个子节点
var hasChildNodes = parentElement.hasChildNodes(); // 判断是否有子节点
```

以上代码示例涵盖了节点获取/查询、创建节点和页面修改节点的常见操作。通过这些方法和属性，你可以方便地操作和管理DOM树结构中的各个节点及其关系。请根据实际需求和场景选择适当的方法进行节点操作。

## childNodes和children区别

`parentElement.childNodes`和`parentElement.children`是用于获取指定元素节点的子节点的属性，它们之间的区别如下：

1. `parentElement.childNodes`：
   - `childNodes`返回的是一个`NodeList`对象，包含了指定元素节点的所有子节点，包括元素节点、文本节点、注释节点等。
   - `NodeList`是一个类似数组的对象，它表示一个动态的节点列表，可以使用索引访问其中的节点。
   - `childNodes`包含了所有类型的子节点，无论是元素节点、文本节点还是其他类型的节点，都会被包括在内。
   - 注意，`childNodes`返回的列表中包含了所有类型的节点，而不仅仅是元素节点。

示例：
```html
<div id="parent">
  <p>Paragraph 1</p>
  Text Node
  <span>Span Element</span>
</div>
```
```javascript
var parentElement = document.getElementById('parent');
var childNodes = parentElement.childNodes;

console.log(childNodes); // 输出: NodeList [ <p>, #text "Text Node", <span> ]
```

在上述示例中，`parentElement`是一个包含了多个子节点的元素节点。通过`childNodes`属性获取到的是一个`NodeList`对象，其中包含了所有子节点，包括`<p>`元素节点、文本节点和`<span>`元素节点。

2. `parentElement.children`：
   - `children`返回的是一个`HTMLCollection`对象，包含了指定元素节点的所有子元素节点。
   - `HTMLCollection`也是一个类似数组的对象，表示一个动态的元素节点列表，可以使用索引访问其中的元素节点。
   - `children`只包含元素节点，不包括文本节点、注释节点等其他类型的节点。
   - `children`返回的列表中只包含元素节点。

示例：
```html
<div id="parent">
  <p>Paragraph 1</p>
  Text Node
  <span>Span Element</span>
</div>
```
```javascript
var parentElement = document.getElementById('parent');
var children = parentElement.children;

console.log(children); // 输出: HTMLCollection [ <p>, <span> ]
```

在上述示例中，`parentElement`是一个包含了多个子节点的元素节点。通过`children`属性获取到的是一个`HTMLCollection`对象，其中只包含了子元素节点，即`<p>`元素节点和`<span>`元素节点。

总结：
- `childNodes`返回的是一个包含所有子节点的`NodeList`对象，包括元素节点、文本节点等。
- `children`返回的是一个包含所有子元素节点的`HTMLCollection`对象，只包括元素节点。

根据你的需求，选择适合的属性来获取子节点或子元素节点列表。如果你需要获取所有类型的子节点，包括文本节点等，可以使用`childNodes`。如果你只关心元素节点，可以使用`children`来获取子元素节点列表。
