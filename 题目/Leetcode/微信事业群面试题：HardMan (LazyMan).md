这道题是面试腾讯暑期实习生时，被WXG捞起来视频面时做的一道题，当时一脸懵逼，想了好一会，不过确实是不会做。主要是因为当时对类的使用以及Promise的掌握都还不够熟练，今天刚好想到这道题，于是翻出来好好地做了一下！

# 题目重述
```js
实现一个 HardMan:  
HardMan(“jack”) 输出:  
I am jack

HardMan(“jack”).rest(10).learn(“computer”) 输出  
I am jack  
//等待10秒  
Start learning after 10 seconds  
Learning computer

HardMan(“jack”).restFirst(5).learn(“chinese”) 输出  
//等待5秒  
Start learning after 5 seconds  
I am jack  
Learning chinese
```

[[class类的用法]]

## 
在这个问题中，我们需要创建一个名为 `HardMan` 的类或函数，该类或函数可以链式调用 `rest`, `learn` 和 `restFirst` 等方法。每个方法的效果如下：

- `rest(n)`：等待 n 秒，然后输出 "Start learning after n seconds"
- `learn(subject)`：输出 "Learning subject"
- `restFirst(n)`：首先等待 n 秒，然后输出 "Start learning after n seconds"

这个问题涉及到JavaScript的异步编程，因为 `rest` 和 `restFirst` 需要等待一定的时间。在JavaScript中，我们可以使用 `Promise` 来处理这种异步操作。

以下是一个可能的实现：

```javascript
class HardMan {
    constructor(name) {
        console.log(`I am ${name}`);
        this.promise = Promise.resolve();
    }

    rest(time) {
        this.promise = this.promise.then(() => {
            return new Promise(resolve => {
                setTimeout(() => {
                    console.log(`Start learning after ${time} seconds`);
                    resolve();
                }, time * 1000);
            });
        });
        return this;
    }

    learn(subject) {
        this.promise = this.promise.then(() => {
            console.log(`Learning ${subject}`);
        });
        return this;
    }

    restFirst(time) {
        this.promise = Promise.resolve().then(() => {
            return new Promise(resolve => {
                setTimeout(() => {
                    console.log(`Start learning after ${time} seconds`);
                    resolve();
                }, time * 1000);
            });
        }).then(() => this.promise);
        return this;
    }
}
```

在这个实现中，每个 `HardMan` 实例都有一个 `promise` 属性，这个 promise 代表一系列的操作。`rest` 方法会增加一个新的操作到这个 promise 中，这个操作会等待指定的时间，然后输出一条信息。`learn` 方法同样会增加一个新的操作，这个操作会立即输出一条学习的信息。最后，`restFirst` 方法会首先等待指定的时间，然后再执行剩余的操作。

我们可以使用 `new HardMan('jack').rest(10).learn('computer')` 来创建一个新的 `HardMan` 实例，然后使它等待 10 秒，然后学习 computer。类似地，我们可以使用 `new HardMan('jack').restFirst(5).learn('chinese')` 来首先等待 5 秒，然后再学习 chinese。

注意，由于 `setTimeout` 函数的时间单位是毫秒，所以我们需要将时间参数乘以 1000。