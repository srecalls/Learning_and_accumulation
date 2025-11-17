# 拼多多 前端 base上海（23届秋招面试记录）

部门：快团团

### 一面（2022-09-15）

忘记录屏了...

### 二面（2022-09-23）（47min）

- 实习经历
- 代码题

![](https://uploadfiles.nowcoder.com/images/20230724/760167885_1690209810060/74B3E7D1C2B7B31FCCEBE2EC524D6975)

```js
操作 -> 次数

```

```js
为了解决这个问题，我们可以按照以下步骤进行操作：

1. 首先，我们需要对用户的操作记录进行过滤，只选择在指定时间段内的记录。我们可以使用`Array.filter()`方法来实现这个过滤过程。

2. 接下来，我们需要统计每个用户的操作次数。我们可以创建一个空对象来存储每个用户的操作次数，并使用`Array.forEach()`方法遍历过滤后的操作记录，对每个用户进行计数。

3. 统计完每个用户的操作次数后，我们将操作次数作为键，用户个数作为值，存储到一个新的对象中。我们可以使用`Object.entries()`方法将对象转换为键值对数组，并使用`Array.reduce()`方法来统计操作次数和对应的用户个数。

4. 最后，我们将统计结果按照操作次数（cnt）从大到小进行排序，得到最终的输出结果。

下面是一个实现上述步骤的JavaScript函数：

function getUserActivityDistribution(records, timeRange) {
  const [startTime, endTime] = timeRange;

  // 过滤出在指定时间范围内的操作记录
  const filteredRecords = records.filter(record => record.time >= startTime && record.time <= endTime);

  // 统计每个用户的操作次数
  const userCounts = {};
  filteredRecords.forEach(record => {
    const { id } = record;
    if (userCounts[id]) {
      userCounts[id]++;
    } else {
      userCounts[id] = 1;
    }
  });

  // 统计操作次数和对应的用户个数
  const distribution = {};
  for (const id in userCounts) {
    const count = userCounts[id];
    if (distribution[count]) {
      distribution[count]++;
    } else {
      distribution[count] = 1;
    }
  }

  // 将结果按照操作次数从大到小排序
  const sortedDistribution = Object.entries(distribution)
    .map(([cnt, num]) => ({ cnt: Number(cnt), num }))
    .sort((a, b) => b.cnt - a.cnt);

  return sortedDistribution;
}

// 示例用法
const records = [
  { id: 1, time: 1 },
  { id: 2, time: 1 },
  { id: 1, time: 9 },
  { id: 2, time: 11 },
  { id: 3, time: 5 }
];
const timeRange = [1, 10];

const result = getUserActivityDistribution(records, timeRange);
console.log(result); // 输出 [{ cnt: 2, num: 1 }, { cnt: 1, num: 2 }]
```

以上代码会输出按照操作次数从大到小排序的用户操作次数分布结果。每个对象包含了操作次数（cnt）和对应的用户个数（num）。

- let const var
[[1.let、const、var的区别]]
[[var、let、const的使用及区别，什么是暂时性死区？]]
- 闭包
- 手撕节流函数
  ```js
function throttle(fn, wait) {
  return function() {
	let timer = null
	let context = this
	let args = arguments
	let judge = true
	if (judge) {
		fn.apply(context, args)
		judge = false
		timer = setTimeout(() => {
			judge = true
		}, wait)
	}
  }
}
```
[[手写节流函数]]

[[对防抖与节流的理解]]

- 节流防抖区别
[[对防抖与节流的理解]]
- 箭头函数和普通函数
[[箭头函数和普通函数的区别]]
- flex
[[Flex布局]]
- 代码题

![](https://uploadfiles.nowcoder.com/images/20230724/760167885_1690209817961/C497944A585CE414D1D6EAC0A798AE02)

- 哪些行为阻塞页面的渲染
```js
以下是一些可能阻塞页面渲染的行为：

1. JavaScript执行：当浏览器遇到需要执行的JavaScript代码时，它会停止渲染页面，并执行JavaScript代码。如果JavaScript代码较长或运行时间较长，会导致页面渲染被阻塞。

2. CSS样式计算和加载：浏览器在渲染页面时需要计算和应用CSS样式。如果CSS文件较大或复杂，并且在渲染过程中需要进行样式计算和加载，会导致页面渲染被阻塞。

3. 大量资源加载：当页面包含大量的外部资源（如图片、视频、字体等）时，浏览器需要进行资源的下载和加载。如果这些资源较大或数量较多，会导致页面渲染被阻塞。

4. 解析和构建DOM树：浏览器在渲染页面时需要解析HTML代码并构建DOM树。如果HTML代码较大或嵌套层级较深，浏览器需要花费更多时间来解析和构建DOM树，从而导致页面渲染被阻塞。

5. Render-Blocking JavaScript：当浏览器遇到位于页面头部的阻塞JavaScript脚本时，它会停止渲染，先执行JavaScript脚本，然后再继续渲染页面。这可能导致页面的首次渲染延迟。

6. 阻塞的外部资源：如果页面包含位于`<head>`标签内的阻塞外部资源，比如CSS文件和JavaScript文件，浏览器会在加载和执行这些资源之前阻塞页面的渲染。

要优化页面的加载和渲染性能，可以采取以下措施：

- 将JavaScript脚本放在`<body>`标签底部，以便在渲染页面之后再加载和执行脚本。
- 使用`async`或`defer`属性来异步加载外部JavaScript文件，以减少对页面渲染的阻塞。
- 压缩和合并CSS和JavaScript文件，减少文件大小和数量。
- 使用图片压缩和懒加载等技术来优化资源加载。
- 避免在页面加载时执行复杂的计算或操作，尽可能将其延迟到页面加载完成后再执行。

通过优化上述阻塞页面渲染的行为，可以提升页面的加载速度和用户体验。
```
- defer和async
- [[async和awiat用法详解]]
- 重排重绘
- 设计方案计算从拿到资源到首屏渲染的时间

### 三面（2022-10-13）（36min）

- 实习经历，难点
- vue和react
- 代码题

![](https://uploadfiles.nowcoder.com/images/20230724/760167885_1690209825895/2B13964EA750412829569A8250BD5687)

- 个人规划

### 四面（2022-10-15）（17min）

- 自我介绍
- 学校经历
- pdd相关
- 为什么投pdd
- 加班接受吗（每天11-12小时）
- 实习经历
- 其他公司秋招情况
- 希望薪酬（说低了，大家往高了说！）

最后开奖一般般，考虑到pdd有点累，最后没去。

  
  
作者：Chenyibo  
链接：[https://www.nowcoder.com/discuss/513122089889521664](https://www.nowcoder.com/discuss/513122089889521664)  
来源：牛客网