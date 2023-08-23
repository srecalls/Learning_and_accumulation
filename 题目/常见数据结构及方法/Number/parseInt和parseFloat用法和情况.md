## parseInt()
`parseInt()` 函数是 JavaScript 中用于将字符串转换为整数的方法。它接受两个参数：要转换的字符串和一个可选的基数（进制）。基数参数用于指定要解析的字符串是什么进制的数。

下面是 `parseInt()` 函数的语法：

```javascript
parseInt(string, radix)
```

- `string`: 要解析的字符串。
- `radix`（可选）：一个介于 2 到 36 之间的整数，表示 `string` 参数的基数。

`parseInt()` 函数从字符串的开头开始解析，直到遇到非数字字符为止。它会忽略开头的空格字符。如果字符串的第一个非空字符无法被解析为数字，则 `parseInt()` 返回 `NaN`（Not a Number）。

下面是一些 `parseInt()` 的示例和易错情况：

1. 基本用法：

```javascript
parseInt("123"); // 返回 123
parseInt("12.34"); // 返回 12，小数点后的部分会被忽略
```

2. 指定基数（进制）：

```javascript
parseInt("1010", 2); // 返回 10，将二进制数 1010 转换为十进制
parseInt("FF", 16); // 返回 255，将十六进制数 FF 转换为十进制
```

3. 特殊情况：

```javascript
parseInt("Hello"); // 返回 NaN，第一个非空字符 "H" 无法解析为数字
parseInt("10Hello"); // 返回 10，解析停止于非数字字符 "H"
parseInt("ABC", 16); // 返回 171，将十六进制数 ABC 转换为十进制
```

4. 使用 `parseInt()` 时要注意的陷阱：

```javascript
parseInt("010"); // 返回 10，被解析为十进制，而不是八进制
parseInt("0x10"); // 返回 16，被解析为十六进制
parseInt("0.5"); // 返回 0，小数点后的部分会被忽略
parseInt("1e1"); // 返回 1，指数形式字符串会被解析为整数部分
parseInt("3.14.15") // 返回3
```

需要注意的是，`parseInt()` 函数在处理非常大的数字时可能会出现精度问题。此外，如果要解析浮点数，请使用 `parseFloat()` 函数。

## parseFloat()

`parseFloat()` 函数是 JavaScript 中用于将字符串转换为浮点数的方法。它接受一个参数：要转换的字符串。

下面是 `parseFloat()` 函数的语法：

```javascript
parseFloat(string)
```

- `string`: 要解析的字符串。

`parseFloat()` 函数从字符串的开头开始解析，直到遇到非数字字符为止。它会忽略开头的空格字符。如果字符串的第一个非空字符无法被解析为数字，则 `parseFloat()` 返回 `NaN`（Not a Number）。

下面是一些 `parseFloat()` 的示例和易错情况：

1. 基本用法：

```javascript
parseFloat("3.14"); // 返回 3.14
parseFloat("12.34"); // 返回 12.34
```

2. 特殊情况：

```javascript
parseFloat("Hello"); // 返回 NaN，第一个非空字符 "H" 无法解析为数字
parseFloat("10Hello"); // 返回 10，解析停止于非数字字符 "H"
```

3. 使用 `parseFloat()` 时要注意的陷阱：

```javascript
parseFloat("3.14"); // 返回 3.14
parseFloat("0.5"); // 返回 0.5
parseFloat("1e1"); // 返回 10，指数形式字符串会被解析为相应的浮点数
parseFloat("10.00"); // 返回 10，末尾的零会被忽略
parseFloat("10.00ABC"); // 返回 10，解析停止于非数字字符 "A"
parseFloat("10.01ABC"); // 返回 10.01，解析停止于非数字字符 "A"
parseFloat("3.14.15") // 返回3.14
```

需要注意的是，`parseFloat()` 函数无法处理进制转换，它只能解析十进制数值。如果需要处理不同进制的字符串，应使用 `parseInt()` 函数。另外，当解析非常大或非常小的浮点数时，也可能会出现精度问题。