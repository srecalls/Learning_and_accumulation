JSON.stringify() 方法用于将 JavaScript值转换为 JSON 字符串。  
语法：
```js
JSON.stringify(value[,replacer[,space]])
```

参数说明：

value：必需，要转换的 JavaScript 值（通常为对象或数组）。

replacer: 可选。用于转换结果的函数或数组。 如果 replacer 为函数，则 JSON.stringify 将调用该函数，并传入每个成员的键和值。使用返回值而不是原始值。 如果此函数返回 undefined，则排除成员。根对象的键是一个空字符串：""。如果 replacer 是一个数组，则仅转换该数组中具有键值的成员。成员的转换顺序与键在数组中的顺序一样。

space：可选，文本添加缩进、空格和换行符，如果 space 是一个数字，则返回值文本在每个级别缩进指定数目的空格，如果 space 大于 10，则文本缩进 10 个空格。space 也可以使用非数字，如：`\t`。

返回值：返回包含 JSON 文本的字符串。

JSON.stringify()特性挺多的，具体如下：
## 1、第一大特性
对于 undefined、任意的函数以及 symbol 三个特殊的值分别作为对象属性的值、数组元素、单独的值时 JSON.stringify() 将返回不同的结果。 来看这道题：
```js
const data = {
  a: "aaa",
  b: undefined,
  c: Symbol("dd"),
  fn: function () {
    return true;
  },
};
JSON.stringify(data); // 输出：？
 
// "{"a":"aaa"}"
```

这是因为 **undefined、任意的函数以及 symbol** 作为对象属性值时 JSON.stringify() 将跳过（忽略）对它们进行序列化。

假设 undefined、任意的函数以及 symbol 值作为**数组元素**会是怎样呢？
```js
JSON.stringify([
  "aaa",
  undefined,
  function aa() {
    return true;
  },
  Symbol("dd"),
]); // 输出：？
 
// "["aaa",null,null,null]"
```
这是因为 **undefined、任意的函数以及 symbol** 作为**数组元素值**时，JSON.stringify() 会将它们**序列化为 null**。

还有，undefined、任意的函数以及 symbol 被 JSON.stringify() 作为单独的值进行序列化时都会返回 undefined。
```js
JSON.stringify(function a() {
  console.log("a");
});
// undefined
JSON.stringify(undefined);
// undefined
JSON.stringify(Symbol("dd"));
// undefined
```

## 2、第二大特性
**非数组对象**的属性**不能保证**以特定的顺序出现在序列化后的字符串中。因为 JSON.stringify() 序列化时会**忽略一些特殊的值**，所以不能保证序列化后的字符串还是以特定的顺序出现（**数组除外**）
```js
const data = {
  a: "aaa",
  b: undefined,
  c: Symbol("dd"),
  fn: function () {
    return true;
  },
  d: "ddd",
};
JSON.stringify(data); // 输出：？
// "{"a":"aaa","d":"ddd"}"
 
JSON.stringify([
  "aaa",
  undefined,
  function aa() {
    return true;
  },
  Symbol("dd"),
  "eee",
]); // 输出：？
 
// "["aaa",null,null,null,"eee"]"
```

## 3、第三大特性
转换值如果有 **toJSON()** 函数，该函数返回什么值，序列化结果就是什么值，并且忽略其他属性的值。
```js
JSON.stringify({
    say: "hello JSON.stringify",
    toJSON: function() {
      return "today i learn";
    }
  })
// "today i learn"
```

## 4、第四大特性
JSON.stringify() 将会正常序列化 Date 的值
```js
JSON.stringify({ now: new Date() });
// "{"now":"2019-12-08T07:42:11.973Z"}"
```

## 5、第五大特性
**NaN 和 Infinity** 格式的数值及 **null** 都会被当做 **null**
```js
JSON.stringify(NaN)
// "null"
JSON.stringify(null)
// "null"
JSON.stringify(Infinity)
// "null"
```

## 6、第六大特性
**布尔值、数字、字符串**的**包装对象**在序列化过程中会自动转换成**对应的原始值。**
```js
JSON.stringify([new Number(1), new String("false"), new Boolean(false)]);
// "[1,"false",false]"
```

## 7、第七大特性
```js
// 不可枚举的属性默认会被忽略：
JSON.stringify( 
    Object.create(
        null, 
        { 
            x: { value: 'json', enumerable: false }, 
            y: { value: 'stringify', enumerable: true } 
        }
    )
);
// "{"y":"stringify"}"
```

## 8、第八大特性
**深拷贝**最粗暴的方式是**JSON.parse(JSON.stringify())**，这个方式实现深拷贝会因为序列化的诸多特性从而导致诸多的坑点：比如现在我们要说的循环引用问题。
```js
// 对包含循环引用的对象（对象之间相互引用，形成无限循环）执行此方法，会抛出错误。 
const obj = {
  name: "loopObj"
};
const loopObj = {
  obj
};
// 对象之间形成循环引用，形成闭环
obj.loopObj = loopObj;
 
// 封装一个深拷贝的函数
function deepClone(obj) {
  return JSON.parse(JSON.stringify(obj));
}
// 执行深拷贝，抛出错误
deepClone(obj)
/**
 VM44:9 Uncaught TypeError: Converting circular structure to JSON
    --> starting at object with constructor 'Object'
    |     property 'loopObj' -> object with constructor 'Object'
    --- property 'obj' closes the circle
    at JSON.stringify (<anonymous>)
    at deepClone (<anonymous>:9:26)
    at <anonymous>:11:13
 */
```