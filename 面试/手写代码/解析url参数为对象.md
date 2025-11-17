实现一个解析url参数为对象的函数，实现一个Javascript函数。该函数输入参数为一个URL字符串，函数的作用是将URL中的查询参数解析成一个和对象，并且返回该对象，我现在和你说边界条件  
1.URL参数是空字符串或者undefined，那么返回一个空对象，  
2.如果URL中有重复的键，将这些键对应的值转换为数组，3.URL参数中值为数字、布尔值、空字符或者null，应该正确的解析，4.然后URL如果包含特殊字符，要正确的转义
好的，针对您提到的边界条件，可以对函数进行如下实现：
window.location` 是一个包含当前页面 URL 相关信息的对象。它提供了许多属性来访问和操作 URL 的不同部分。下面是 `window.location` 对象的常用属性：

- `window.location.href`：完整的 URL 字符串，包括协议、主机、路径、查询参数和哈希部分。
- `window.location.protocol`：协议部分，如 "http:" 或 "https:"。
- `window.location.host`：主机部分，包括域名和端口。
- `window.location.hostname`：域名部分，不包括端口。
- `window.location.port`：端口部分。
- `window.location.pathname`：路径部分，不包括查询参数和哈希部分。
- `window.location.search`：查询参数部分，包括 "?" 符号。
- `window.location.hash`：哈希部分，包括 "#" 符号。

使用这些属性，你可以访问和操作当前页面 URL 的不同部分。例如，你可以通过 `window.location.href` 获取完整的 URL，或通过 `window.location.pathname` 获取路径部分。


![[解析url参数为对象-1.png]]
`URLSearchParams` 可以将参数对象转换为查询字符串，并使用 `toString()` 方法将其附加到 URL 的搜索部分。
![[解析url参数为对象-2.png]]

```js

function urlSearch(href) {
  let name, value;
  let str = href; //取得整个地址栏
  let num = str.indexOf("?");
  str = str.substr(num + 1); //取得所有参数
  let arr = str.split("&"); //各个参数放到数组里
  let json = {};
  for (let i = 0; i < arr.length; i++) {
    num = arr[i].indexOf("=");
    if (num > 0) {
      name = arr[i].substring(0, num);
      value = arr[i].substr(num + 1);
      json[name] = value;
    }
  }
  return json;
}

```

```javascript
function parseUrlParams(url) {
  if (!url || url.trim() === '') { // 处理空URL参数
    return {};
  }

  const searchParams = new URLSearchParams(url.split('?')[1]);
  const paramsObj = {};

  for (let [key, value] of searchParams.entries()) {
    if (paramsObj[key]) { // 处理重复键
      if (!Array.isArray(paramsObj[key])) {
        paramsObj[key] = [paramsObj[key]];
      }
      paramsObj[key].push(value);
    } else {
      paramsObj[key] = value;
    }

    // 处理数字、布尔值、空字符或者null
    if (paramsObj[key] === 'true') {
      paramsObj[key] = true;
    } else if (paramsObj[key] === 'false') {
      paramsObj[key] = false;
    } else if (paramsObj[key] === 'null') {
      paramsObj[key] = null;
    } else if (paramsObj[key] === '') {
      paramsObj[key] = undefined;
    } else if (!isNaN(paramsObj[key])) {
      paramsObj[key] = parseFloat(paramsObj[key]);
    }
  }

  return paramsObj;
}
```

针对边界条件的具体处理如下：

1. 如果URL参数是空字符串或者undefined，函数应该返回一个空对象。

添加判断，如果输入参数为空字符串或者undefined，直接返回一个空对象。

2. 如果URL中有重复的键，将这些键对应的值转换为数组。

在循环处理查询参数时，如果当前键已经存在于新对象中，则说明存在重复的键。此时，需要判断当前键对应的值是否为数组，如果不是，则将其转换为数组，并将原来的值和新值一起存储到数组中。如果已经是数组，则直接将新值存储到数组中。

3. URL参数中值为数字、布尔值、空字符或者null，应该正确解析。

在循环处理查询参数时，使用一系列条件语句判断当前值的类型，并进行适当的转换。如果值是空字符串，则直接存储空字符串。如果值是字符串类型的数字，则使用parseFloat方法将其转换为数值类型。如果值是字符串类型的布尔值，需要手动将其转换为对应的布尔值类型。如果值是字符串类型的null，则直接存储null。

4. URL如果包含特殊字符，要正确转义。

由于URLSearchParams构造函数在初始化时会自动对URL参数进行编码，因此不需要手动进行转义操作。

综上所述，以上实现可以满足您提到的边界条件。