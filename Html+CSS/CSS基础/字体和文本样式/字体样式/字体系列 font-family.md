# 字体系列 font-family
#### ➢ 属性名：
**font-family** 
#### ➢ 常见取值：
**具体字体1,具体字体2,具体字体3,具体字体4,...,字体系列** 
**• 具体字体："Microsoft YaHei"、微软雅黑、黑体、宋体、楷体等……**


![[Pasted image 20220905154240.png]]

**• 字体系列：sans-serif、serif、monospace等……** 

#### ➢ 渲染规则： 
**1. 从左往右按照顺序查找，如果电脑中未安装该字体，则显示下一个字体** (从左往右按顺序找)
**2. 如果都不支持，此时会根据操作系统，显示最后字体系列的默认字体** （如果都没有就用默认的）

![[Pasted image 20220905154250.png]]

#### ➢ 注意点： 
**1. 如果字体名称中存在多个单词，推荐使用引号包裹** 
**2. 最后一项字体系列不需要引号包裹** 
**3. 网页开发时，尽量使用系统常见自带字体，保证不同用户浏览网页都可以正确显示**


在 CSS 中，`font-family` 属性用于设置文本的字体系列，即指定要在文本中使用的字体。

`font-family` 属性可以接受以下类型的值：

- 一个字体系列名称：例如，`Arial`、`Helvetica`、`Times New Roman` 等。
- 多个字体系列名称，以逗号分隔：例如，`Arial, Helvetica, sans-serif`。
- 通用字体系列：`serif`（衬线字体）、`sans-serif`（非衬线字体）、`monospace`（等宽字体）、`cursive`（草书字体）和 `fantasy`（幻想字体）。

以下是一个示例，展示了 `font-family` 属性的使用：

```html
<style>
  .container {
    font-family: Arial, sans-serif;
  }
</style>

<div class="container">
  <p>This is a paragraph with a custom font family.</p>
</div>
```

在上述示例中，`.container` 类选择器的 `<div>` 元素应用了 `font-family: Arial, sans-serif;` 属性。这将使容器中的文本采用 Arial 字体，如果不可用，则回退到 sans-serif 字体。

您可以设置多个字体系列，并按优先顺序列出它们。如果浏览器支持第一个字体系列，则使用该字体；如果不支持，则依次检查后续的字体系列，直到找到一个可用的字体为止。

这种设置多个字体系列的方式称为字体回退（font fallback），它可以确保在用户的计算机上可能没有安装某个特定字体时，仍能够显示合适的字体。

以下是一个示例，展示了如何设置多个字体系列并进行字体回退：

```html
<style>
  .container {
    font-family: "Helvetica Neue", Arial, sans-serif;
  }
</style>

<div class="container">
  <p>This is a paragraph with a font fallback.</p>
</div>
```

在上述示例中，`.container` 类选择器的 `<div>` 元素应用了 `font-family: "Helvetica Neue", Arial, sans-serif;` 属性。这将首先尝试使用 "Helvetica Neue" 字体，如果不可用，则回退到 Arial 字体，如果还不可用，则回退到 sans-serif 字体。

通过设置多个字体系列并进行字体回退，可以提供更广泛的字体兼容性，确保在不同的设备和环境中都能够正确显示文本。确保选择常见的字体系列作为回退选项，以增加成功找到可用字体的可能性。

## 怎么知道有没有安装某个字体
在网页上，您无法直接确定用户的计算机是否安装了特定的字体。但是，您可以通过一些技巧来间接检测用户计算机上是否存在某个字体。

一种常用的方法是使用 JavaScript 和浏览器提供的 `FontFaceSet` 接口来检测字体是否可用。以下是一个示例代码：

```javascript
// 创建一个包含要检测的字体名称的数组
var fontFamilies = ['Arial', 'Helvetica Neue', 'sans-serif'];

// 检查字体是否可用
function checkFontAvailability(fontFamily) {
  var fontSet = document.fonts;
  return fontSet.check(`1em "${fontFamily}"`);
}

// 检测每个字体是否可用
fontFamilies.forEach(function(font) {
  var isAvailable = checkFontAvailability(font);
  console.log(font + ' is ' + (isAvailable ? 'available' : 'not available'));
});
```

在上述示例中，我们创建了一个包含要检测的字体名称的数组 `fontFamilies`。然后，使用 `FontFaceSet` 的 `check()` 方法来检测每个字体是否可用。

请注意，这种检测方式并不是绝对准确的，因为浏览器可能会对字体进行某些优化或替代处理。而且，由于浏览器的安全限制，您可能无法访问用户计算机上的完整字体列表。

因此，在网页设计中，通常建议选择常见的字体系列，并提供合适的字体回退选项，以确保在大多数情况下都能提供良好的字体兼容性。