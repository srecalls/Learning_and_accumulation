```js
function allSettled(promises) {
  return new Promise((resolve, reject) => {
    const results = [];
    const len = promises.length;
    let resolvedCount = 0;
    for (let i = 0; i < len; i++) {
      promises[i]
        .then((value) => {
          results[i] = { status: "fulfilled", value };
        })
        .catch((reason) => {
          results[i] = { status: "rejected", reason };
        })
        .finally(() => {
          resolvedCount++;
          if (resolvedCount === len) {
            resolve(results);
          }
        });
    }
  });
}

```

### 代码解释

我们首先创建一个新的Promise对象，并在该对象中执行所有Promise对象。

在Promise对象中，我们定义一个results数组，用于存储每个Promise对象的状态和值。我们还定义了resolvedCount变量，用于跟踪已解决的Promise对象的数量。

接下来，我们循环遍历所有Promise对象，并对每个Promise对象执行以下操作：

1. 如果Promise对象成功执行，则将其状态和值存储在results数组中。
2. 如果Promise对象失败，则将其状态和原因存储在results数组中。
3. 无论Promise对象成功或失败，我们都会增加resolvedCount计数器。
4. 最后，如果所有Promise对象都已解决，则Promise对象的状态将设置为已解决，并返回包含所有Promise对象状态的results数组。

### 示例

我们来看一个使用手动实现的Promise.allSettled()方法的示例

  ```js
  const promises = [
  Promise.resolve("Promise 1 fulfilled"),
  Promise.reject("Promise 2 rejected"),
  Promise.resolve("Promise 3 fulfilled"),
  Promise.reject("Promise 4 rejected"),
];

allSettled(promises)
  .then((results) => console.log(results))
  .catch((error) => console.log(error));

```

作者：茶老师  
链接：https://juejin.cn/post/7210285753351536700  
来源：稀土掘金  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。