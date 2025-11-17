# pdd前端一面

一上来就聊项目，完全不问八股…准备了一星期啥都不问……  
  
题目：倒计时组件，promise p 1s没resolve就返回超时  
  以下是一个基于 Promise 的倒计时组件，如果在 1 秒内没有解析（resolve），则返回超时。

```js
	function countDown() {
		return Promise((resolve, reject) => {
			let timer = setTimeout(() => {
				clearTimeout(timer)
				reject(new Error('timeout'))
			}, 1000)
		})
	}
	countDown().then(() => {
	})
```

```js
function countdown(timeout) {
  return new Promise((resolve, reject) => {
    const timeoutId = setTimeout(() => {
      clearTimeout(timeoutId);
      reject(new Error('Timeout'));
    }, timeout);

    // 假设这里是异步操作，比如发送请求或执行一段耗时的代码
    // 在异步操作完成后，调用 resolve 来解析 Promise
    // 这里使用 setTimeout 模拟异步操作
    setTimeout(() => {
      clearTimeout(timeoutId);
      resolve('Operation completed successfully');
    }, 2000);
  });
}

countdown(1000)
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.log(error.message); // 输出 "Timeout"
  });
```

在上述示例中，`countdown` 函数接受一个超时时间（以毫秒为单位）作为参数。它返回一个 Promise，该 Promise 在超时时间内解析（resolve）或拒绝（reject）。

在 Promise 的构造函数中，我们设置一个超时定时器 `setTimeout`，在超时时间到达后，清除定时器并拒绝 Promise，返回一个超时错误。然后，模拟一个异步操作，通过 `setTimeout` 来模拟异步操作的完成，在异步操作完成后，清除定时器并解析 Promise，返回一个成功的消息。

在使用该倒计时组件时，我们可以调用 `countdown` 函数，并使用 `.then` 和 `.catch` 来处理解析和拒绝的情况。在超时时间内完成异步操作时，会打印出成功的消息；如果超时时间内没有完成异步操作，会打印出超时错误的消息。
然后就是问项目，聊了40多分钟，但是感觉啥问题都没有问，都是自顾自再说，是不是遇到kpi面了![](https://uploadfiles.nowcoder.com/images/20220815/318889480_1660553763930/8B36D115CE5468E380708713273FEF43)

  
  
作者：牛客239317158号  
链接：[https://www.nowcoder.com/users/history](https://www.nowcoder.com/users/history)  
来源：牛客网