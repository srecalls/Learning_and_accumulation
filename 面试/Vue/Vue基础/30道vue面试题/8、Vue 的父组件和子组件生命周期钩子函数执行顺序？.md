Vue 的父组件和子组件生命周期钩子函数执行顺序可以归类为以下 4 部分：

- 加载渲染过程

    父 beforeCreate -> 父 created -> 父 beforeMount -> 子 beforeCreate -> 子 created -> 子 beforeMount -> 子 mounted -> 父 mounted

- 父组件的ref状态值有更新，且作为参数传给子组件时，更新时
	beforeUpdate -> 子 beforeUpdate -> 子 updated -> 父 updated

- 子组件更新过程

   子 beforeUpdate -> 子 updated

- 父组件更新过程

    父 beforeUpdate -> 父 updated

- 销毁过程

    父 beforeDestroy -> 子 beforeDestroy -> 子 destroyed -> 父 destroyed



对此我也是专门写了父子两个组件做测试，发现当父组件的ref状态值有更新，且作为参数传给子组件时，更新时就会执行父 beforeUpdate -> 子 beforeUpdate -> 子 updated -> 父 updated，  
当没有给子组件传参时，父组件更新时就只会执行父 beforeUpdate -> 父 updated，当然在子组件更新时，只会执行子 beforeUpdate -> 子 updated，子组件更新怎么可能执行父组件的生命周期呢。

子的生命周期都会被先结束，父的才结束。先由父到子，再从子到父。  
生命周期遵从“从外到内，再从内到外，mixins先于组件”的原则。  
总的来说，从创建到挂载，是从外到内，再从内到外，且mixins的[钩子函数]总是在当前组件之前执行




## beforeDestroy干了什么
在 Vue 实例被销毁之前，会触发 `beforeDestroy` 钩子函数，用于进行一些清理工作。

在 `beforeDestroy` 钩子函数中，可以执行一些清理工作，例如取消定时器、清除非 Vue 插件的事件绑定、解除手动绑定的事件等等。

以下是一些在 `beforeDestroy` 钩子函数中常见的清理工作：

- 取消定时器：

```javascript
export default {
  data() {
    return {
      timerId: null
    };
  },
  created() {
    this.timerId = setInterval(() => {
      console.log('timer tick');
    }, 1000);
  },
  beforeDestroy() {
    clearInterval(this.timerId);
    this.timerId = null;
  }
};
```

在上面的示例中，我们在 `created` 钩子函数中创建了一个定时器，并将其存储在 `this.timerId` 中。在 `beforeDestroy` 钩子函数中，我们取消定时器并将 `this.timerId` 设置为 `null`，以避免内存泄漏。

- 清除非 Vue 插件的事件绑定：

```javascript
export default {
  mounted() {
    document.addEventListener('click', this.onClick);
  },
  methods: {
    onClick(event) {
      console.log('document clicked');
    }
  },
  beforeDestroy() {
    document.removeEventListener('click', this.onClick);
  }
};
```

在上面的示例中，我们在 `mounted` 钩子函数中向 `document` 添加了一个点击事件监听器，并在 `beforeDestroy` 钩子函数中将该事件监听器移除，以避免内存泄漏。

- 解除手动绑定的事件：

```javascript
export default {
  mounted() {
    const button = document.querySelector('button');
    button.addEventListener('click', this.onClick);
  },
  methods: {
    onClick(event) {
      console.log('button clicked');
    }
  },
  beforeDestroy() {
    const button = document.querySelector('button');
    button.removeEventListener('click', this.onClick);
  }
};
```

在上面的示例中，我们在 `mounted` 钩子函数中手动向一个按钮添加了一个点击事件监听器，并在 `beforeDestroy` 钩子函数中将该事件监听器移除，以避免内存泄漏。

需要注意的是，在 `beforeDestroy` 钩子函数中，Vue 实例的数据和事件监听器仍然可用，因此如果需要在销毁之前对数据进行处理，可以在 `beforeDestroy` 钩子函数中进行。但是，在 `destroyed` 钩子函数中，Vue 实例的数据和事件监听器已经被销毁，不再可用。