## DOM的事件模型是什么？

DOM之事件模型分脚本模型、内联模型(同类一个，后者覆盖)、动态绑定(同类多个)

## 

```
<body><!--行内绑定：脚本模型--><button onclick="javascrpt:alert('Hello')">Hello1</button><!--内联模型--><button onclick="showHello()">Hello2</button><!--动态绑定--><button id="btn3">Hello3</button></body><script>/*DOM0：同一个元素，同类事件只能添加一个，如果添加多个，
* 后面添加的会覆盖之前添加的*/function shoeHello() {alert("Hello");}var btn3 = document.getElementById("btn3");
btn3.onclick = function () {alert("Hello");}/*DOM2:可以给同一个元素添加多个同类事件*/
btn3.addEventListener("click",function () {alert("hello1");});
btn3.addEventListener("click",function () {alert("hello2");})if (btn3.attachEvent){/*IE*/
btn3.attachEvent("onclick",function () {alert("IE Hello1");})}else {/*W3C*/
btn3.addEventListener("click",function () {alert("W3C Hello");})}</script>

```

DOM的事件流是什么？

事件就是文档或浏览器窗口中发生的一些特定的交互瞬间，而事件流(又叫事件传播)描述的是从页面中接收事件的顺序。

### 事件冒泡

事件冒泡(event bubbling)，即事件开始时由最具体的元素(文档中嵌套层次最深的那个节点)接收，然后逐级向上传播到较为不具体的节点。

看如下例子：

```
<!DOCTYPE HTML><html lang="en"><head><meta charset="UTF-8"><title>Document</title><body><div></div></body>    </html>
```

如果单击了页面中的`<div>`元素，那么这个click事件沿DOM树向上传播，在每一级节点上都会发生，按照如下顺序传播：

1. div
2. body
3. html
4. document

### 事件捕获

事件捕获的思想是不太具体的节点应该更早接收到事件，而最具体的节点应该最后接收到事件。事件捕获的用意在于在事件到达预定目标之前就捕获它。

还是以上一节的html结构为例:

在事件捕获过程中，document对象首先接收到click事件，然后事件沿DOM树依次向下，一直传播到事件的实际目标，即`<div>`元素

5. document
6. html
7. body
8. div

### 事件流

事件流又称为事件传播，DOM2级事件规定的事件流包括三个阶段：事件捕获阶段(capture phase)、处于目标阶段(target phase)和事件冒泡阶段(bubbling phase)。
![[DOM面试题（持续更新中...）.png]]
触发顺序通常为

9. 进行事件捕获，为截获事件提供了机会
10. 实际的目标接收到事件
11. 冒泡阶段，可以在这个阶段对事件做出响应

## 什么是事件委托

事件委托就是利用事件冒泡，只指定一个事件处理程序，就可以管理某一类型的所有事件.

在绑定大量事件的时候往往选择事件委托。

```
<ul id="parent">
  <li class="child">one</li>
  <li class="child">two</li>
  <li class="child">three</li>
  ...</ul>
<script type="text/javascript">
  //父元素
  var dom= document.getElementById('parent');

  //父元素绑定事件，代理子元素的点击事件
  dom.onclick= function(event) {
    var event= event || window.event;
    var curTarget= event.target || event.srcElement;

    if (curTarget.tagName.toLowerCase() == 'li') {
      //事件处理
    }
  }</script>

```

优点:

- 节省内存占用，减少事件注册
- 新增子对象时无需再次对其绑定事件，适合动态添加元素

局限性:

- focus、blur 之类的事件本身没有事件冒泡机制，所以无法委托
- mousemove、mouseout 这样的事件，虽然有事件冒泡，但是只能不断通过位置去计算定位，对性能消耗高，不适合事件委托

## DOM变动事件的用法

DOM2级的変动事件是为XML或html的DOM设计的，不特定于某种语言。

一：变动事件的分类有7种，最常用的浏览器支持最多的有3种，下面黑体？

12. **DOMSubtreeModified**：在DOM结构中发生任何变化时触发；
13. **DOMNodeInserted**：在一个节点作为子节点被插入到另一个节点中时触发；
14. **DOMNodeRemoved**：在节点从其父节点中被移除时触发；
15. DOMNodeInsertedIntoDocument：在一个节点被直接插入文档中或者通过子树间接插入文档后触发。在DOMNodeInserted之后触发；
16. DOMNodeRemovedFromDocument：在一个节点被直接从文档中删除或通过子树间接从文档中移除之前触发。在DOMNodeRemoved之后触发。
17. DOMAttrModified：在特性被修改之后触发；
18. DOMCharacterDataModified：在文本节点的值发生变化的时候触发。

二：删除节点检测？

首先触发的是DOMNodeRemoved事件，它对应的event对象中的target属性值是被删除的节点，relatedNode属性值是被删除节点的父节点，该事件会冒泡； 其次出发的是DOMNodeRemovedFromDocument事件，它对应的event对象中的target属性值为指定的被删除的子节点。只有绑定到它的子节点上才能被触发。 最后触发的是DOMSubtreeModified事件。这个事件对应event对象中的target属性是被移除节点的父节点。