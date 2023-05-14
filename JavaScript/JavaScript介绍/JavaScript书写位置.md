![[Pasted image 20230308214409.png]]

## 内部JavaScript
![[Pasted image 20230308214547.png]]

您的描述是准确的。将\<script>标签放在HTML文件的底部附近是为了确保在JavaScript代码执行之前，HTML文档的主要内容已经被加载和渲染完成。这样做可以防止由于JavaScript代码期望修改HTML但HTML尚未被加载而导致的错误。

当浏览器遇到\<script>标签时，它会立即开始下载和解析JavaScript代码。如果\<script>标签位于HTML文件的头部，那么浏览器可能会在加载JavaScript代码之前尝试渲染HTML。如果JavaScript代码期望修改位于其下方的HTML，那么这些修改可能会由于HTML尚未被加载而失败。

将\<script>标签放在HTML文件的底部附近可以解决这个问题，因为在JavaScript代码执行之前，HTML文档的主要内容已经被加载和渲染完成了。这样做可以确保JavaScript代码在修改HTML之前，HTML已经被加载和渲染完成了。这种方法可以提高代码的可靠性和性能。

## 外部JavaScript
![[Pasted image 20230308214842.png]]

## 内联JavaScript
![[Pasted image 20230308214933.png]]
![[Pasted image 20230308215036.png]]



HTML文档的基本结构应该是`<html>`标签包含`<head>`和`<body>`标签，而且在`<head>`标签中通常包含元数据和链接到外部资源的标签，如`<meta>`、`<link>`和`<script>`等。在这种情况下，`<script>`标签必须放在`<head>`或`<body>`标签内，否则它将无法正常工作。

如果您想将JavaScript代码放在`<html>`标签之外，建议将代码保存在一个独立的文件中，然后在HTML文件中引用这个文件。这样做可以将JavaScript代码与HTML代码分离，使它们更易于维护和管理，如果将`<script>`标签放在`<html>`标签之外，它可能无法正常工作，这是因为这不符合HTML语法规则。