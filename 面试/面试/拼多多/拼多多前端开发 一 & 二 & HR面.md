# 拼多多前端开发 一 & 二 & HR面

**岗位：前端开发，业务内容是h5电商**

**面试体验：流程是比较严格的八股问答，面试官挺好的对没答出来的会解答**

**结果：过了，薪资未达到预期**

## **一面**

### **主要面试内容：**

**做题和八股文穿插进行**

### 八股文

meta标签常用属性
[[meta属性]]
[[5.常⽤的meta标签有哪些]]
`<link rel="preload">的作用`

`proload 和 prefetch的区别`

`async 和 defer的区别`
[[script标签如何做异步加载]]
defer 与domContentLoaded的执行先后顺序



页面拿到html到展示出来的过程

缓存策略
[[2.协商缓存和强缓存的区别]]
[[http缓存（浏览器缓存）——强缓存、协商缓存]]

no cache 和 no store的区别

css加载失败了，页面会怎么样

常见的移动端适配方案

怎么触发BFC
[[3. 对BFC的理解，如何创建BFC]]
relative相对于什么布局的
[[相对定位 relative]]
[[9. 对 sticky 定位的理解]]
[[position的属性有哪些,区别是什么]]
js基本数据类型
[[基本数据类型和引用数据类型]]

[[基本数据类型和引用数据类型的区别]]
什么是跨域
[[了解同源策源和跨域]]
跨域的解决方案

[[（2）JSONP]]
[[（1）CORS]]
jsonp的原理
[[（2）JSONP]]
jsonp的缺点
[[（2）JSONP]]
预检请求什么时候用
[[（1）CORS]]


什么是闭包

promise常见的方法
[[手写Promise.all]]
[[手写Promise.race]]
[[Promise整理总结]]
事件的捕获和冒泡，怎么设置事件触发阶段
[[事件捕获]]
[[事件委托]]
[[事件冒泡]]
[[1.事件是什么?事件模型?]]

loader 和 plugin的区别

useEffect 与 useCallback的区别

axios 的 拦截器和适配器的使用和区别

react 的 ssr怎么实现的


### 代码题

1、下划线分割的小写字符串 改写成 驼峰字符串

'abc_de' => 'abcDe'

2、实现Promise.allSettled

考虑使用Promise.all来实现
[[实现Promise.allSettled]]
### 4.1 Promise.allSettled 方法

等待多个 promise 返回结果时，我们可以用 Promise.all([promise_1, promise_2])。但问题是，如果其中一个请求失败了，就会抛出错误。然而，有时候我们希望某个请求失败后，其他请求的结果能够正常返回。针对这种情况 ES11 引入了 Promise.allSettled 。

```
const promise1 = Promise.resolve(3);
const promise2 = new Promise((resolve, reject) => setTimeout(reject, 100, 'foo'));
const promises = [promise1, promise2];

Promise.allSettled(promises).
  then((results) => results.forEach((result) => console.log(result.status)));

// expected output:
// "fulfilled"
// "rejected"
```
[[手写Promise.all]]
[[手写Promise.race]]
[[实现Promise.allSettled]]

3、闭包测试题

——大概是下面这样吧

```js
function inc(i) {
  let a = 0;
  return function xx1() {
    a = a + i;
    console.log(a);
    let message = `value is ${a}`;
    return function log() {
      console.log(message);
    };
  };
}

const aa = inc(1);
const log = aa();
aa();
aa();
aa();

// 1
// 2
// 3
// 4
```


```js
[  
{id: 1, config: [2, 4]},  
{id: 2, config: [3, 4]},  
{id: 3, config: []},  
{id: 4, config: []},  
]  
输出  
3, 4, 2, 1

因为要先解析没有依赖的，3，4没有依赖率先打印，等3，4处理完后，处理2，这时候2处理完了，轮到1，写一个函数
function processElements(elements) {
  const graph = {}; // 图
  const visited = {}; // 记录节点是否已访问
  const result = []; // 存储结果

  // 构建图
  for (const element of elements) {
    const id = element.id;
    const dependencies = element.config;
    graph[id] = dependencies;
    visited[id] = false;
  }

  // 深度优先搜索
  for (const id in graph) {
    if (!visited[id]) {
      dfs(id);
    }
  }

  // 深度优先搜索函数
  function dfs(id) {
    visited[id] = true;
    const dependencies = graph[id];

    for (const dependency of dependencies) {
      if (!visited[dependency]) {
        dfs(dependency);
      }
    }

    result.push(id);
  }

  return result.reverse(); // 反转结果数组，按要求输出顺序
}

const elements = [
  { id: 1, config: [2, 4] },
  { id: 2, config: [3, 4] },
  { id: 3, config: [] },
  { id: 4, config: [] }
];

const output = processElements(elements);
console.log(output.join(', ')); // 输出: 3, 4, 2, 1
```
## **二面**

### **主要面试内容：**

**做题和八股文穿插进行**

### 八股文

react 设计hooks的初衷

react 代码复用的方式

Render Props 与 HOC的区别

React Fiber架构为什么可以中断

React状态管理

mobx 与 context的更新粒度的区

webpack的基本原理

webpack loader 与plugin的区别

webpack为什么要使用loader

webpack依赖图怎么构建的

webpack遇到了import语句，是怎么解析出路径的
[[1.2.2 安装webpack]]
AST了解吗

对webpack进行过那些配置

### 代码题

1、原型链

```js
function AA() {
  AA.a = function () {
    console.log(1);
  };
  this.a = function () {
    console.log(2);
  };
}
AA.a = function () {
  console.log(3);
};
AA.a();
AA.prototype.a = function () {
  console.log(4);
};
let aa = new AA();
aa.a();
AA.a();


// 3
// 2
// 1
```
[[this的四种绑定方式]]
[[手写new操作符]]
2、事件循环

类似于下面

```js
async function async1() {
  console.log('async1 start')
  await async2()
  console.log('async1 end')
}

async function async2() {
  console.log('async2')
    await async3()
}

// async function async3() {
//   console.log('async3')
// }

async function async3() {
 console.log('async3')
}
console.log('script start')

setTimeout(function () {
  console.log('setTimeout0')
}, 0)

async1();

Promise.resolve(1).then(function (data) {
  console.log('promise1',data)
}).then((res)=>{
   console.log('promise2', res);
  return Promise
})

console.log('script end')

script start
async1 start 
async2
script end
async1 end
promise1 1
settimeout0
websocket.html:58 Uncaught (in promise) ReferenceError: data is not defined

```
## HR面

对前两面的面试官的印象

多多的工作强度的了解

其他offer情况

薪资预期

  
  
作者：写代码的张无忌  
链接：[https://www.nowcoder.com/discuss/468370436103933952?sourceSSR=search](https://www.nowcoder.com/discuss/468370436103933952?sourceSSR=search)  
来源：牛客网