DOM树是和HTML标签一一对 应的，包括head和隐藏元素
渲染树是不包含head和隐藏元素


DOM树和渲染树都是Web页面在浏览器中的结构表示方式，但它们有着不同的目的和结构。

DOM树（Document Object Model）是HTML文档在浏览器中的对象表示方式，它表示了整个文档的结构和内容，包括HTML标签、文本、属性和事件等。DOM树是一个树形结构，由多个节点（Node）组成，每个节点表示文档中的一个元素、属性或文本。

渲染树（Render Tree）是浏览器渲染引擎根据DOM树和CSS样式生成的用于渲染页面的树形结构。渲染树只包含需要显示的节点，例如可见的文本和元素节点，同时还考虑CSS样式的影响，如布局、样式和绘制等。渲染树是为了更高效地渲染页面而设计的，它与DOM树的不同点在于，**它忽略了一些不需要显示的节点**，例如head、script等节点，同时还考虑了CSS样式的影响，如display:none的节点不会出现在渲染树中。

因此，DOM树和渲染树的区别在于它们的目的和结构。DOM树表示文档的结构和内容，而渲染树表示页面的可视化呈现。渲染树包含了DOM树中需要显示的节点，同时还考虑了CSS样式的影响，这使得浏览器能够更快地渲染页面。




以下是一个简单的HTML文档，它包含了一些HTML标签和CSS样式：

```html
<!DOCTYPE html>
<html>
  <head>
    <title>DOM Tree and Render Tree</title>
    <style>
      #content {
        background-color: yellow;
        width: 300px;
        height: 200px;
        display: flex;
        justify-content: center;
        align-items: center;
      }

      p {
        color: red;
        font-size: 24px;
        font-weight: bold;
      }

      .highlight {
        background-color: blue;
        color: white;
      }
    </style>
  </head>
  <body>
    <div id="content">
      <p>Hello, World!</p>
      <p class="highlight">This is a highlighted text.</p>
    </div>
  </body>
</html>
```

这个文档生成的DOM树如下所示：

```
HTML
├── HEAD
│   ├── TITLE
│   └── STYLE
└── BODY
    └── DIV#content
        ├── P
        │   └── "Hello, World!"
        └── P.highlight
            └── "This is a highlighted text."
```

这个文档的渲染树如下所示：

```
HTML
└── BODY
    └── DIV#content
        ├── P
        │   └── "Hello, World!"
        └── P.highlight
            └── "This is a highlighted text."
```

可以看到，渲染树与DOM树的结构非常相似，但渲染树忽略了head、title等节点，同时还考虑了CSS样式的影响，例如p.highlight节点应用了.highlight类的样式。