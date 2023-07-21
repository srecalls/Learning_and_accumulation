https://juejin.cn/post/6928775439016001543


在 JavaScript 中，可以使用 `toFixed()` 方法来将数字四舍五入并保留指定位数的小数。该方法将返回一个字符串表示四舍五入后的数字。

例如，如果要将数字 `3.1415926` 四舍五入并保留两位小数，可以使用以下代码：

```javascript
const num = 3.1415926;
const roundedNum = num.toFixed(2); // roundedNum 的值为 "3.14"
```

在这个示例中，`toFixed()` 方法将数字 `3.1415926` 四舍五入并保留两位小数，返回值为字符串 `"3.14"`。

需要注意的是，`toFixed()` 方法返回的是一个字符串，如果需要将其转换为数字，可以使用 `parseFloat()` 或 `Number()` 方法。

```javascript
const num = 3.1415926;
const roundedNum = parseFloat(num.toFixed(2)); // roundedNum 的值为 3.14
```

在这个示例中，使用 `parseFloat()` 方法将字符串 `"3.14"` 转换为数字 `3.14`。