


## 测试题

1. 使用TypeScript写下面的代码

```
function typeIs(val) {
  let type = typeof val;
  if (type === 'object') {
    type = val === null ? 'null' : val instanceof Array ? 'array' : 'object';
  }
  return type;
}
```

2. 下面写法正确是：

a.

```
function myFunc(maybeString: string | undefined | null) {
  const onlyString: string = maybeString;
}
```

b.

```
function myFunc(maybeString: string | undefined | null) {
  const onlyString: string = maybeString!; 
}
```

c.

```
function myFunc(numGenerator: NumGenerator | undefined) {
  const num1 = numGenerator();
}
```

d.

```
function myFunc(numGenerator: NumGenerator | undefined) {
  const num2 = numGenerator()!;
}
```

3. 使用TypeScript写下面的代码

```
function tryGetArrayElement(arr, index = 0) {
  if (Array.isArray(arr)) return arr[index] || undefined
}
```

4. 输出下面的代码的console结果

```
const foo = null ?? 'default string';
console.log(foo); 
const baz = 0 ?? 42;
console.log(baz); 
```

5. 一道面试题：https://github.com/LeetCode-OpenSource/hire/blob/master/typescript_zh.md， 答案：https://juejin.cn/post/6850418113859551239