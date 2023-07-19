ES6引入了BigInt数据类型，它可以表示任意长度的整数。它是一种原始数据类型，与Number类型不同，可以表示超过2的53次方-1的整数。

BigInt的字面量表示法是在整数末尾添加一个n，例如：

```javascript
const bigIntNum = 1234567890123456789012345678901234567890n;
console.log(bigIntNum); // 1234567890123456789012345678901234567890n
```

BigInt类型支持大多数Number类型的运算符，例如加减乘除运算、位运算、比较运算等，但是需要使用BigInt构造函数来创建BigInt对象，例如：

```javascript
const a = BigInt(10);
const b = BigInt(20);
const c = a + b;
console.log(c); // 30n
```

BigInt类型还支持一些方法，例如toString()、valueOf()等，与Number类型的方法类似。

需要注意的是，BigInt类型与Number类型不能混合使用，例如：

```javascript
const a = 123n;
const b = 456;
const c = a + b; // TypeError: Cannot mix BigInt and other types, use explicit conversions
```

在进行运算时，需要将Number类型转换为BigInt类型，例如：

```javascript
const a = 123n;
const b = BigInt(456);
const c = a + b;
console.log(c); // 579n
```

另外，由于BigInt类型是ES6新增的数据类型，某些老版本的浏览器可能不支持它，需要进行兼容性处理。