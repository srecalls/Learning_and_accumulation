在 JavaScript 中，可以使用不同的方法来遍历一个字符串。以下是常用的几种方法：

1. `for` 循环

使用 `for` 循环可以遍历字符串中的每个字符。语法如下：

```javascript
const str = "hello";
for (let i = 0; i < str.length; i++) {
  console.log(str[i]);
}
```

在这个例子中，使用 `for` 循环遍历了字符串中的每个字符，并将其输出到控制台。

2. `for...of` 循环

ES6 引入了 `for...of` 循环语法，可以方便地遍历字符串中的每个字符。语法如下：

```javascript
const str = "hello";
for (const char of str) {
  console.log(char);
}
```

在这个例子中，使用 `for...of` 循环遍历了字符串中的每个字符，并将其输出到控制台。

3. `forEach` 方法

对于字符串来说，也可以使用 `Array.prototype.forEach()` 方法来遍历每个字符。语法如下：

```javascript
const str = "hello";
Array.prototype.forEach.call(str, function(char) {
  console.log(char);
});
```

在这个例子中，使用 `Array.prototype.forEach()` 方法来遍历字符串中的每个字符，并将其输出到控制台。需要注意的是，由于 `forEach()` 方法是数组的方法，而不是字符串的方法，因此需要使用 `call()` 方法来将字符串转化为数组来使用。

4. `split` 方法

可以使用 `split()` 方法将字符串转化为字符数组，然后使用 `for` 循环或 `for...of` 循环遍历数组中的每个字符。语法如下：

```javascript
const str = "hello";
const arr = str.split("");
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}
```

或者：

```javascript
const str = "hello";
const arr = str.split("");
for (const char of arr) {
  console.log(char);
}
```

在这个例子中，使用 `split()` 方法将字符串转化为字符数组，然后使用 `for` 循环或 `for...of` 循环遍历数组中的每个字符，并将其输出到控制台。

需要注意的是，在遍历字符串时，需要使用字符串的 `length` 属性来获取字符串的长度，而不能像数组那样使用 `arr.length`。