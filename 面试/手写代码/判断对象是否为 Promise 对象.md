### 方法一

将传入的对象转成 `Promise` 对象，判断是否相等，如果相等，则说明是 `Promise` 对象。

```js
function isPromise(obj) {
  if (Promise && Promise.resolve) {
    return Promise.resolve(obj) == obj
  } else {
    throw new Error('当前环境不支持 Promise !')
  }
}

```


### 方法二

判断对象原型是否为字符串 `"[object Promise]"`。
```js
function isPromise(obj) {
  return obj && Object.prototype.toString.call(obj) === '[object Promise]'
}

```

### 错误示例

Promise 有 then 方法，判断对象是否有 then 方法。

错误原因：如果一个对象中有 then 属性，且该属性是函数，就会判断失败。
```js
function isPromise(obj) {
  return obj && (typeof obj === 'object' || typeof obj === 'function') && typeof obj.then === 'function'
}

const obj = {
  then: function() {
    console.log('我不是 Promise 对象');
  }
}

```