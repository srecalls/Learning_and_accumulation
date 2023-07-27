组件从创建到销毁的过程就是它的生命周期  [[组件的生命周期]]
Vue的生命周期可以分为8个阶段，分别是：

好的，我来详细举例说明一下Vue的生命周期各个阶段及其作用：

## 1. beforeCreate：
在这个阶段，**Vue实例已经被创建出来了，但是数据和方法都还没有被初始化**。这时候，我们不能够使用任何数据和方法，因为它们还没有被初始化。这个阶段通常用于插件开发或者一些需要在实例创建之前完成的初始化操作。

假设我们正在开发一个Vue插件，并希望在Vue实例被创建之前对其进行一些初始化操作。在这种情况下，我们可以使用`beforeCreate`生命周期函数来执行这些操作。

例如，我们可以在`beforeCreate`函数中向Vue实例添加一个全局事件侦听器，以便在整个应用程序中跟踪特定事件：

```javascript
export default {
  data() {
	  message: 'Hello, world!'
  },
  beforeCreate() {
    // 添加全局事件侦听器
    this.$root.$on('my-event', this.handleEvent);
	console.log(this.message) // 报错
  },
  methods: {
    handleEvent() {
      // 处理事件逻辑
    }
  }
}
```

在这个例子中，我们将一个事件侦听器添加到Vue实例的根节点上，以便在整个应用程序中跟踪`my-event`事件。由于在`beforeCreate`函数中，Vue实例的数据和方法还没有被初始化，因此我们不能在这里访问它们。但是，我们可以访问Vue实例的根节点，并向其添加全局事件侦听器。

这是一个简单的例子，但是`beforeCreate`生命周期函数可以用于执行各种初始化操作，例如添加全局样式、注册Vue插件或加载配置文件等。
## 2. created：
在这个阶段，**Vue实例已经完成了数据的初始化，可以使用数据和方法，但是还没有挂载到DOM上**。这个阶段通常用于发送异步请求，初始化一些数据，或者在数据初始化之后进行数据监测。

```javascript
export default {
  data() {
	  message: 'Hello, world!'
  },
  created() {
    console.log('created');
	console.log(this.message) // 'Hello, world!'
    // 发送异步请求
    fetch('https://api.example.com/data')
      .then(response => response.json())
      .then(data => {
        // 对返回的数据进行处理
      });
  }
}
```

## 3. beforeMount：
在这个阶段，**Vue实例已经完成了模板的编译，但是还没有把编译好的模板挂载到DOM上**。这个阶段通常用于修改数据，因为此时修改数据不会触发updated钩子。

```javascript
export default {
  beforeMount() {
    console.log('beforeMount');
    // 修改数据
    this.message = 'Hello, Vue!';
  }
}
```

## 4. mounted：
在这个阶段，**Vue实例已经把编译好的模板挂载到了DOM上，此时可以访问DOM节点，发送异步请求等等**。这个阶段通常用于初始化一些需要访问DOM节点的插件或者组件。

```javascript
export default {
  mounted() {
    console.log('mounted');
    // 访问DOM节点
    const element = document.getElementById('app');
    // 发送异步请求
    fetch('https://api.example.com/data')
      .then(response => response.json())
      .then(data => {
        // 对返回的数据进行处理
      });
  }
}
```

## 5. beforeUpdate：
在这个阶段，**Vue实例已经完成了数据的更新，但是还没有重新渲染DOM**。此时，数据是新的，但是页面上的数据还是旧的，可以在这个阶段修改数据，因为此时修改数据不会触发updated钩子。

```javascript
export default {
  beforeUpdate() {
    console.log('beforeUpdate');
    // 修改数据
    this.message = 'Hello, Vue!';
  }
}
```

## 6. updated：
在这个阶段，**Vue实例已经重新渲染了DOM，数据和页面都是最新的**。

```javascript
export default {
  updated() {
    console.log('updated');
  }
}
```

## 7. beforeDestroy：
在这个阶段，Vue实例即将被销毁，在这里可以清理定时器，取消事件监听等等。**此时实例还可以使用，但是已经不能访问DOM节点。**

```javascript
export default {
  beforeDestroy() {
    console.log('beforeDestroy');
    // 清理定时器
    clearInterval(this.timerId);
    // 取消事件监听
    this.$off();
  }
}
```

## 8. destroyed：
在这个阶段，**Vue实例已经被销毁，所有的事件监听和定时器都已经被清除，组件已经被完全销毁**。

```javascript
export default {
  destroyed() {
    console.log('destroyed');
  }
}
```

在使用了Vue的keep-alive组件之后，还会多出两个钩子函数：

## 9. activated：
在这个阶段，**被缓存的组件被激活了，可以访问DOM节点**，发送异步请求等等。

```javascript
export default {
  activated() {
    console.log('activated');
  }
}
```

## 10. deactivated：
在这个阶段，**被缓存的组件被销毁了，所有的事件监听和定时器都已经被清除，组件已经被完全销毁**。

```javascript
export default {
  deactivated() {
    console.log('deactivated');
  }
}
```

这些生命周期钩子函数可以帮助我们在组件的不同阶段做出不同的操作，例如在mounted阶段访问DOM节点，或者在beforeDestroy阶段清理定时器和取消事件监听等等。同时，钩子函数的执行顺序是固定的，这可以帮助我们更好地理解Vue组件的生命周期，更好地掌握Vue组件的工作原理。


## 哪些钩子中可以获取到DOM节点？
在Vue.js的生命周期钩子函数中，只有在`mounted`和`updated`函数中可以获取到DOM节点。因为在这两个函数中，组件已经挂载到了DOM上，可以访问和操作DOM节点。

- `mounted`函数：当组件挂载到DOM之后调用。在这个阶段，组件已经被成功挂载到页面上，可以访问和操作DOM元素。

- `updated`函数：当组件更新之后调用。在这个阶段，组件的数据和DOM都已经被更新，并且可以进行访问和操作。

除了这两个钩子函数外，在其他钩子函数中访问DOM节点可能会导致不可预测的行为，因为在这些钩子函数中，DOM节点可能还没有被成功挂载或者还没有完成更新。

在Vue.js的生命周期钩子函数中，只有在`mounted`和`updated`函数中可以获取到DOM节点。因为在这两个函数中，组件已经挂载到了DOM上，可以访问和操作DOM节点。

- `beforeCreate`函数：在实例初始化之后、数据观测之前调用，此时组件的数据、方法等还未初始化，**无法访问或操作DOM节点。**

- `created`函数：在实例创建完成后调用，此时组件的**数据和方法已经被初始化**，但是还**没有被挂载到DOM上，无法访问或操作DOM节点。**

- `beforeMount`函数：在**模板编译完成后**，但是还**没有被挂载到DOM上调用**，此时**可以访问Vue实例中的数据，但是还不能访问或操作DOM节点**。

- `mounted`函数：当组件挂载到DOM之后调用。在这个阶段，**组件已经被成功挂载到页面上，可以访问和操作DOM元素**。

- `beforeUpdate`函数：在组件更新之前调用，此时可以访问Vue实例中的数据，但是**DOM还没有被更新**，因此**不能**访问或操作**最新的DOM节点**。

- `updated`函数：当组件更新之后调用。在这个阶段，**组件的数据和DOM都已经被更新，并且可以进行访问和操作**。

- `beforeDestroy`函数：在组件销毁之前调用，**此时Vue实例不可以访问DOM节点。

- `destroyed`函数：在组件销毁之后调用，**此时Vue实例已经被销毁，无法访问或操作DOM节点**。

除了`mounted`和`updated`函数外，在其他钩子函数中访问DOM节点可能会导致不可预测的行为，因为在这些钩子函数中，DOM节点可能还没有被成功挂载或者还没有完成更新。

需要注意的是，尽管在`mounted`和`updated`函数中可以访问和操作DOM节点，但是在Vue.js中通常建议尽量避免直接操作DOM元素，而是使用Vue.js提供的数据绑定和计算属性等功能来实现页面交互和动态更新。这样可以使代码更加简洁、可读性更高，并且使Vue.js可以更好地控制DOM元素的变化和更新。





## version2
当使用Vue.js创建组件时，组件的生命周期钩子函数是非常重要的部分。这些函数允许您在组件的创建、更新和销毁过程中对其进行控制和修改。

以下是Vue.js组件的生命周期钩子函数及其作用：

1. beforeCreate：
在组件实例化之前调用。此时，组件的数据和方法都没有被初始化，因此无法访问它们。这个钩子函数通常用于在实例化之前进行一些必要的设置，例如添加全局事件侦听器或混合其他选项。

2. created：
在组件实例化之后调用。此时，组件的数据和方法已经被初始化，可以进行修改和使用。这个钩子函数通常用于在组件创建后进行一些初始化操作，例如设置默认数据或进行异步请求。

```js
Vue.component('example-component', {
  data() {
    return {
      message: 'Hello, world!'
    }
  },
  beforeCreate() {
    console.log('beforeCreate')
    // 这里无法访问this.message
  },
  created() {
    console.log('created')
    console.log(this.message) // "Hello, world!"
  }
})
```

3. beforeMount：
在组件挂载到DOM之前调用。此时，组件的模板已经编译成虚拟DOM，但还没有挂载到页面上。这个钩子函数通常用于在组件挂载之前进行最后的修改操作。

4. mounted：
在组件挂载到DOM之后调用。此时，组件已经被成功挂载到页面上，可以访问和操作DOM元素。这个钩子函数通常用于在组件挂载后进行一些DOM操作或异步请求。

```js
Vue.component('example-component', {
  mounted() {
    console.log('mounted')
    console.log(this.$el) // 组件挂载的DOM元素
  }
})
```

5. beforeUpdate：
在组件更新之前调用。此时，组件的数据已经被更新，但DOM尚未更新。这个钩子函数通常用于在组件更新之前进行一些最后的修改操作。

6. updated：
在组件更新之后调用。此时，组件的数据和DOM都已经被更新，并且可以进行访问和操作。这个钩子函数通常用于在组件更新之后进行一些DOM操作或异步请求。

```js
Vue.component('example-component', {
  data() {
    return {
      message: 'Hello, world!'
    }
  },
  updated() {
    console.log('updated')
    console.log(this.$el.textContent) // "Hello, Vue!"
  },
  mounted() {
    setInterval(() => {
      this.message = 'Hello, Vue!'
    }, 1000)
  }
})
```

7. beforeDestroy：
在组件销毁之前调用。此时，组件仍然可用，可以进行访问和操作。这个钩子函数通常用于在组件销毁之前进行一些清理操作，例如取消事件侦听器或定时器。

8. destroyed：
在组件销毁之后调用。此时，组件已经被完全销毁，无法再进行访问和操作。这个钩子函数通常用于在组件销毁之后进行一些清理操作，例如释放内存或取消异步请求。

```js
Vue.component('example-component', {
  data() {
    return {
      message: 'Hello, world!'
    }
  },
  beforeDestroy() {
    console.log('beforeDestroy')
    // 这里仍然可以访问this.message
  },
  destroyed() {
    console.log('destroyed')
    // 这里不再可以访问this.message
  }
})
```

9. activated：
当使用keep-alive组件缓存时，当组件被激活时调用。这个钩子函数通常用于在组件缓存后重新启用组件时执行必要的操作。

10. deactivated：
当使用keep-alive组件缓存时，当组件被停用时调用。这个钩子函数通常用于在组件缓存之前执行必要的操作，例如清除定时器或取消异步请求。

```js
Vue.component('example-component', {
  activated() {
    console.log('activated')
    // 组件被重新激活时执行的操作
  },
  deactivated() {
    console.log('deactivated')
    // 组件被停用时执行的操作
  }
})
```

需要注意的是，这些生命周期钩子函数都是可选的，您可以根据需要选择使用它们。同时，在使用时也要注意不要滥用生命周期钩子函数，否则可能会导致代码难以理解和维护。