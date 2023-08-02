keep-alive 是 Vue 内置的一个组件，可以使被包含的组件保留状态，避免重新渲染 ，其有以下特性：

- 一般结合路由和动态组件一起使用，用于缓存组件；
- 提供 include 和 exclude 属性，两者都支持字符串或正则表达式， include 表示只有名称匹配的组件会被缓存，exclude 表示任何名称匹配的组件都不会被缓存 ，其中 exclude 的优先级比 include 高；
- 对应两个钩子函数 activated 和 deactivated ，当组件被激活时，触发钩子函数 activated，当组件被移除时，触发钩子函数 deactivated。

  好的，下面举一个简单的例子来说明 `keep-alive` 的用法。

假设我们有两个组件：`Home` 和 `About`，其中 `Home` 组件包含一个计数器，每次切换到 `About` 组件时，计数器的值会被重置为 0。我们可以使用 `keep-alive` 组件来缓存 `Home` 组件，避免重复渲染和计数器的重置。

首先，在父组件中使用 `router-view` 标签来展示子组件：

```html
<template>
  <div>
    <router-view></router-view>
  </div>
</template>
```

然后，在 `Home` 组件中添加一个计数器，以及一个按钮来增加计数器的值：

```html
<template>
  <div>
    <h2>Home</h2>
    <p>Count: {{ count }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      count: 0
    };
  },
  methods: {
    increment() {
      this.count++;
    }
  }
};
</script>
```

接着，在 `About` 组件中添加一个按钮来切换到 `Home` 组件：

```html
<template>
  <div>
    <h2>About</h2>
    <button @click="goHome">Go Home</button>
  </div>
</template>

<script>
export default {
  methods: {
    goHome() {
      this.$router.push('/');
    }
  }
};
</script>
```

现在，我们可以在父组件中使用 `keep-alive` 组件来缓存 `Home` 组件：

```html
<template>
  <div>
    <keep-alive>
      <router-view></router-view>
    </keep-alive>
  </div>
</template>
```

最后，在 `Home` 组件中添加 `activated` 和 `deactivated` 钩子函数，以便在组件被缓存和移除时执行一些操作：

```html
<template>
  <div>
    <h2>Home</h2>
    <p>Count: {{ count }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      count: 0
    };
  },
  methods: {
    increment() {
      this.count++;
    }
  },
  activated() {
    console.log('Home activated');
  },
  deactivated() {
    console.log('Home deactivated');
  }
};
</script>
```

现在，当我们从 `Home` 组件切换到 `About` 组件时，`Home` 组件的计数器值会被缓存下来，不会被重置为 0。当我们再次切换回 `Home` 组件时，计数器值会恢复到上次的值。同时，当 `Home` 组件被缓存和移除时，分别会触发 `activated` 和 `deactivated` 钩子函数。