## 一、nextTick 作用

- Vue 在更新 DOM 时是异步执行的，当数据发生变化，Vue 将开启一个异步更新队列，视图需要等队列中所有数据变化完成之后，再统一进行更新
    
- this.$nextTick() 的作用就是可以将里面的回调函数延迟下次 DOM 更新循环结束之后执行。在修改数据之后立即使用这个方法，获取更新后的 DOM。
    
- this.$nextTick() 和 Vue.nextTick 一样，不同的就是回调的 this 自动绑定到调用他的实例上
    
```js
<template>
  <section>
    <h1 ref="hello">{{ value }}</h1>
    <el-button type="danger" @click="get">点击</el-button>
  </section>
</template>
<script>
  export default {
    data() {
      return {
        value: '原始值'
      };
    },
    methods: {
      get() {
        this.value = '更新值';
        console.log(this.$refs['hello'].innerText); // 原始值
        this.$nextTick(() => {
          console.log(this.$refs['hello'].innerText); // 更新值
        });
      }
    }
  }
</script>

```

代码解析：  
第一次 console.log 的时候，获取的到的是旧值，这是因为 value 数据发生变化的时候，Vue 没有立刻去更新 DOM ，而是将修改数据的操作放在了一个异步操作队列中，如果一直修改相同数据，异步操作队列还会进行去重，等待同一事件循环中的所有数据变化完成之后，会将队列中的事件拿来进行处理，进行 DOM 的更新  
第二次的 console.log 是放到 this.$nextTick 回调函数中的，此时获取到的是新值，是因为 nextTick 的回调函数是在 DOM 更新之后触发的

  

## 二、nextTick 原理

### 2-1 异步更新原理

1. vue 里面用到了观察者模式，默认组件渲染的时候，会创建一个 watcher，并且渲染视图
2. 当渲染视图的时候，会取 data 中的数据，触发属性的 get 方法，就让这个属性的 dep 记录watcher（注意：每一个data属性都对应一个dep）
3. 同时让 watcher 也记住 dep ，dep 和 watcher 是多对多的关系，因为一个属性可能对应多个视图，一个视图对应多个数据
4. 如果数据发生变化，也就是在 set 的时候，会触发 dep.notify() ，通知 dep 中存放的 watcher 去更新
5. 每次更新数据都会同步调用 watcher 中 update 方法，此时就可以将更新的逻辑缓存起来，等会同步更新数据的逻辑执行完毕后，依次调用 (去重的逻辑)

### 2-2 代码实现

当一个 Data 更新时，会执行以下步骤

1. 触发 Data.set
2. 调用 dep.notify
3. Dep 会遍历所有相关的 Watcher 执行 update 方法
4. 使用 queueWatcher 来缓存更新的 Watcher

```js

// watcher.js
import Dep from "./dep";
import { queueWatcher } from "./scheduler";
class Watcher {
    constructor() { 
        this.id = id++;
    }
    update() {
        console.log('缓存更新')
        queueWatcher(this); // 把要更新的 Watcher 缓存起来
    }

    run() {
        console.log('真正执行更新')
        this.get(); // render() 取最新的vm上的数据
    }
}


export default Watcher


// scheduler.js
import { nextTick } from "../utils";

let queue = []; // 这里存放要更新的 watcher
let has = {};   // 用来存储已有的 watcher 的 id


function flushSchedulerQueue() {
    // beforeUpdate
    queue.forEach(watcher => watcher.run());
    queue = []; // 这里存放要更新的 watcher
    has = {};
    pending = false
}

let pending = false; // 是否需要等待

export function queueWatcher(watcher) {

    // 一般情况下 写去重 可以采用这种方式 ，如果你不使用set的时候
    let id = watcher.id
    if (has[id] == null) {
        has[id] = true;
        queue.push(watcher); // [watcher1,watcher2]
        if (!pending) { // 防抖 多次执行 只走1次
            nextTick(flushSchedulerQueue);
            pending = true
        }
    }
}
```

```js
let callbacks = [];
let waiting = false;
function flushCallbacks() {
    callbacks.forEach(fn => fn()); // 按照顺序清空nextTick
    callbacks = [];
    waiting = false;
}
export function nextTick(fn) { // vue3 里面的 nextTick 就是 promise ， vue2 里面做了一些兼容性处理
    callbacks.push(fn);
    if (!waiting) {
        Promise.resolve().then(flushCallbacks);
        waiting = true
    }
}
```