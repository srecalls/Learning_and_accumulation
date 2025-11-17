```js
Promise.race = function (args) {
  return new Promise((resolve, reject) => {
    for (let i = 0, len = args.length; i < len; i++) {
      args[i].then(resolve, reject)
    }
  })
}
```

```js
const pRace = (promises) => {
  return new Promise((resolve, reject) => {
    promises.forEach((p) => {
      p.then(
        (value) => {
          resolve(p);
        },
        (reason) => {
          reject(reason);
        },
      );
    });
  });
};
```