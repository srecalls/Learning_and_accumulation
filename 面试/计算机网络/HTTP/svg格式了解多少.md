基于XML语法格式的图像格式，可缩放矢量图，其他图像是基于像素的，SVG是 属于对图像形状的描述，本质是文本文件，
体积小，并且不管放大多少倍都不会失真
1.SVG可直接插入页面中，成为DOM一部分， 然后用JS或CSS进行操作
\<svg>\</svg>

	当SVG作为DOM的一部分时，可以通过JavaScript或CSS对其进行操作和样式化。这种方式可以使SVG与页面中的其他元素进行交互，并且可以根据需要对其进行修改和更新。例如，可以通过JavaScript脚本动态生成SVG元素，并将其添加到页面中。

2.SVG可作为文件被引入\<img src="pic.svg" />

	当SVG作为文件被引入时，可以使用\<img>标签将其嵌入到页面中，与其他图像格式一样。这种方式可以使SVG独立于页面内容，便于维护和管理，并且可以通过缓存来提高页面加载速度。

3.SVG可以转为base64引入页面

	将SVG转换为Base64编码可以将其嵌入到CSS样式表中，或直接在HTML中使用data URI引用。这种方式可以避免额外的HTTP请求，可以提高页面加载速度，并且可以使SVG与CSS样式和动画效果一起使用。

### 3.SVG可以转为base64引入页面
将SVG转换为Base64编码可以使用在线工具或编程语言库来实现。以下是使用JavaScript和CSS的示例代码：

1. 使用JavaScript将SVG转换为Base64编码

```javascript
// 获取SVG文件的内容
const svgContent = document.querySelector('svg').outerHTML;

// 将SVG内容转换为Base64编码
const svgBase64 = btoa(svgContent);

// 将SVG Base64编码作为CSS样式表中的背景图像
document.body.style.backgroundImage = `url(data:image/svg+xml;base64,${svgBase64})`;
```

在上面的代码中，首先获取SVG元素的内容，然后使用JavaScript内置的btoa函数将其转换为Base64编码。最后，将SVG Base64编码作为CSS样式表中的背景图像，通过设置body元素的backgroundImage属性来显示SVG。

2. 在CSS中使用data URI引用SVG Base64编码

```css
.icon {
    background-image: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmc');
}
```

在上面的代码中，使用data URI引用SVG Base64编码，格式为data:image/svg+xml;base64,后面跟随SVG的Base64编码。然后将该CSS样式应用于具有.icon类的元素，以显示SVG。

需要注意的是，将SVG转换为Base64编码可能会使文件大小增加约1/3，因为每个字节都需要使用4个字符来表示。在使用该方法时，需要权衡额外的文件大小和避免HTTP请求的好处。

需要注意的是，SVG有一些限制和注意事项，例如：

1. SVG中的某些属性可能不被所有浏览器支持，需要进行兼容性测试。

2. SVG中的某些图形可能会导致性能问题，特别是在大型或复杂的图像中。

3. SVG的文件大小可能会比其他图像格式更大，特别是在包含大量复杂图形的情况下。

因此，在使用SVG时需要评估其优缺点，并根据具体需求进行选择和优化。