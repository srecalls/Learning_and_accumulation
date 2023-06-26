[[操作事件的方法]]
[[查找节点]]
[[删除节点]]
[[增加节点]]
[[获取DOM对象]]
可以使用 JavaScript 的 DOM API 来实现将第一个 `<li>` 元素放到最后的位置。具体实现步骤如下：

1. 使用 `querySelector()` 方法找到第一个 `<li>` 元素。
2. 使用 `querySelector()` 方法找到 `<ul>` 元素。
3. 使用 `appendChild()` 方法将第一个 `<li>` 元素添加到 `<ul>` 元素的末尾。

示例代码如下：

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Move First li Element to Last</title>
  </head>
  <body>
    <ul>
      <li>Item 1</li>
      <li>Item 2</li>
      <li>Item 3</li>
      <li>Item 4</li>
      <li>Item 5</li>
    </ul>
    <script>
      // 找到第一个 <li> 元素
      var firstLi = document.querySelector('li');

      // 找到 <ul> 元素
      var ul = document.querySelector('ul');

      // 将第一个 <li> 元素添加到最后
      ul.appendChild(firstLi);
    </script>
  </body>
</html>
```

在这个例子中，首先使用 `querySelector()` 方法找到了第一个 `<li>` 元素和 `<ul>` 元素，然后使用 `appendChild()` 方法将第一个 `<li>` 元素添加到了 `<ul>` 元素的末尾，从而实现了将第一个 `<li>` 元素放到最后的位置。