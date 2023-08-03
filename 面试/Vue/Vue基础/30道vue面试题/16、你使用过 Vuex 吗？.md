Vuex 是一个专为 Vue.js 应用程序开发的状态管理模式。每一个 Vuex 应用的核心就是 store（仓库）。“store” 基本上就是一个容器，它包含着你的应用中大部分的状态 ( state )。

（1）Vuex 的状态存储是响应式的。当 Vue 组件从 store 中读取状态的时候，若 store 中的状态发生变化，那么相应的组件也会相应地得到高效更新。

（2）改变 store 中的状态的唯一途径就是显式地提交 (commit) mutation。这样使得我们可以方便地跟踪每一个状态的变化。

主要包括以下几个模块：

- State：定义了应用状态的数据结构，可以在这里设置默认的初始状态。
- Getter：允许组件从 Store 中获取数据，mapGetters 辅助函数仅仅是将 store 中的 getter 映射到局部计算属性。
- Mutation：是唯一更改 store 中状态的方法，且必须是同步函数。
- Action：用于提交 mutation，而不是直接变更状态，可以包含任意异步操作。
- Module：允许将单一的 Store 拆分为多个 store 且同时保存在单一的状态树中。


好的，下面是一个更完整的示例：

```javascript
// store.js
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// 定义状态
const state = {
  count: 0
}

// 定义 getters
const getters = {
  doubleCount(state) {
    return state.count * 2
  }
}

// 定义 mutations
const mutations = {
  increment(state) {
    state.count++
  },
  decrement(state) {
    state.count--
  }
}

// 定义 actions
const actions = {
  incrementAsync({ commit }) {
    setTimeout(() => {
      commit('increment')
    }, 1000)
  },
  decrementAsync({ commit }) {
    setTimeout(() => {
      commit('decrement')
    }, 1000)
  }
}

// 定义子模块
const moduleA = {
  state: {
    countA: 0
  },
  mutations: {
    incrementA(state) {
      state.countA++
    }
  },
  actions: {
    incrementAAsync({ commit }) {
      setTimeout(() => {
        commit('incrementA')
      }, 1000)
    }
  }
}

// 创建 store 实例
const store = new Vuex.Store({
  state,
  getters,
  mutations,
  actions,
  modules: {
    a: moduleA
  }
})

export default store
```

在上面的代码中，我们创建了一个 Vuex 的 store 实例，并定义了 state、getters、mutations、actions 和 modules，以及一个名为 moduleA 的子模块。

在组件中使用这些 store 中的属性、方法、状态，可以使用以下代码：

```javascript
// MyComponent.vue
<template>
  <div>
    <p>count: {{ count }}</p>
    <p>doubleCount: {{ doubleCount }}</p>
    <p>countA: {{ countA }}</p>
    <button @click="increment">increment</button>
    <button @click="decrement">decrement</button>
    <button @click="incrementAsync">incrementAsync</button>
    <button @click="decrementAsync">decrementAsync</button>
    <button @click="incrementA">incrementA</button>
    <button @click="incrementAAsync">incrementAAsync</button>
  </div>
</template>

<script>
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex'

export default {
  computed: {
    ...mapState({
      count: state => state.count,
      countA: state => state.a.countA
    }),
    ...mapGetters([
      'doubleCount'
    ])
  },
  methods: {
    ...mapMutations([
      'increment',
      'decrement'
    ]),
    ...mapActions([
      'incrementAsync',
      'decrementAsync',
      'a/incrementAAsync'
    ]),
    incrementA() {
      this.$store.commit('a/incrementA')
    },
    incrementAAsync() {
      this.$store.dispatch('a/incrementAAsync')
    }
  }
}
</script>
```

在组件中使用 `mapState`、`mapGetters`、`mapMutations` 和 `mapActions` 辅助函数可以帮助我们更方便地访问 store 中的属性、方法、状态。对于子模块中的 mutation 和 action，我们需要使用 `$store.commit` 和 `$store.dispatch` 来分别提交和分发。