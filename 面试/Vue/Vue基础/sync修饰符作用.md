## **.sync修饰符**

> .sync是一个语法糖。是父组件监听子组件更新某个props的请求的缩写语法。

- Vue规则：组件不能修改props外部数据
- Vue规则：$emit可以触发事件并传参
- Vue规则：$event可以获取$emit的参数
- 以上三条规则，都是尤雨溪定的

场景描述：爸爸给儿子钱，儿子要花钱怎么办，[示例](https://link.zhihu.com/?target=https%3A//codesandbox.io/s/laughing-banach-6d4nn)  
答：儿子打电话（触发事件）向爸爸要钱


### 实例

> **Child.vue（子级）**

![[sync修饰符作用.png]]


**Vue规则：组件不能修改props外部数据**

Vue中的 props 是单向向下绑定的  
即：每次父组件更新时，子组件中的所有 props 都会刷新为最新的值。  
但是如果在子组件中修改 props ，Vue会向你发出一个警告。（无法通过修改子组件的props来更改父组件。）

> **App.vue(父级)**

![[sync修饰符作用-1.png]]



由于无法通过修改子组件的props来更改父组件，所以我们在父组件使用子组件的标签上**声明一个监听事件**

```js
<Child :money="total" v-on:update:money="total  = $event" />
```

在子组件想要修改时使用 **$emit**触发事件并传入新的值，让父组件进行修改。

Vue帮我们做了一个修饰符，简化我们声明监听事件的写法，即.sync 修饰符。

```js
<Child :money.sync="total" />
```

> **main.js（渲染）**

![[sync修饰符作用-2.png]]

### 由于这种场景很常见

所以尤雨溪发明了.sync ,[示例](https://link.zhihu.com/?target=https%3A//codesandbox.io/s/small-leftpad-zzvpp)

```js
:money.sync ="total"
等价于
:money = "total" v-on:update:money="total =$event"
```

### .sync 重新引入

从 2.3.0 Vue重新引入了 .sync 修饰符，但是这次它只是作为一个编译时的**语法糖**存在。它**会被扩展为一个自动更新父组件属性的 v-on 监听器**。

示例代码如下：（父组件.vue）

```js
<comp :foo.sync="bar"></comp>
```

会被扩展为：

```js
<comp :foo="bar" @update:foo="val => bar = val"></comp>
```

当子组件需要更新 foo 的值时，它需要显式地触发一个更新事件：

```js
this.$emit('update:foo', newValue)
```

猛一看不明白，下边我么通过一个实例（弹窗的关闭事件）来说明这个代码到底是怎么运用的。

```js
<template>
    <div class="details">
        <myComponent :show.sync='valueChild' style="padding: 30px 20px 30px 5px;border:1px solid #ddd;margin-bottom: 10px;"></myComponent>
        <button @click="changeValue">toggle</button>
    </div>
</template>

<script>
import Vue from 'vue' //导入
//子组件
Vue.component('myComponent', { 
      template: `<div v-if="show">
                    <p>默认初始值是{{show}}，所以是显示的</p>
                    <button @click.stop="closeDiv">关闭</button>
                 </div>`,
      props:['show'],
      methods: {
        closeDiv() {
          this.$emit('update:show', false); //触发 input 事件，并传入新值
        }
      }
})
//父组件
export default{
    data(){
        return{
            valueChild:true,
        }
    },
    methods:{
        changeValue(){
            this.valueChild = !this.valueChild
        }
    }
}
</script>
```

动态效果如下：
![[sync修饰符作用-3.png]]

[https://www.jianshu.com/p/6b062af8c](https://link.zhihu.com/?target=https%3A//www.jianshu.com/p/6b062af8cf01)

今天学习了 Vue 的模板、指令和修饰符，对于 .sync 这个修饰符不是能特别好地理解，所以写一篇博客来整理下思路。

### 场景描述

想象一下这样一个场景，爸爸给儿子设定一个月10000的零花钱，儿子每次要用零花钱的时候跟爸爸要，然后花钱并且扣除相应的额度。

### 相应的代码

main.js：

```js
new Vue({
  render: h => h(App)
}).$mount("#app")
```

然后我们写一个Child组件的vue文件：

```js
<template>
  <div class="child">
    {{money}}
    <button @click="$emit('update:money', money-100)">
      <span>花钱</span>
    </button>
  </div>
</template>

<script>
export default {
  props: ["momey"]
}
</script>

<style>
.child {
  border: 3px solid green;
}
</style>
```

然后我们在App.vue文件里用这个组件：

```js
<template>
  <div class="app">
    App.vue 我现在有 {{total}}
    <hr>
    <Child :money="total" v-on:update:money="total = $event" />
  </div>
</template>

<script>
import Child from "./Child.vue"
export default {
    data() {
      return {total: 10000}
    },
    components: {Child: Child}
}
</script>

<style>
.app {
  border: 3px solid red;
  padding: 10px;
}
</style>
```

界面大概是这样的：

![[sync修饰符作用-4.png]]

点击花钱，就可以让两边的10000都同时改变。

### .sync

因为这种情况用到的很多，所以Vue用.sync修饰符来给这个模式提供了一个缩写。  
我们把`<Child :money="total" v-on:update:money="total = $event" />`这行简化一下变成`<Child :money.sync="total" />`就可以了，与上面一行完全等价。

这就是 Vue 的 .sync 修饰符的作用。

---

在某些场景下我们需要通过子组件对父组件的数据进行修改，但是vue不建议我们使用子组件直接修改父组件的数据，虽然可以通过父组件提供一个修改数据的函数让子组件调用来到达目的，但是vue提供了另一种方式让我们修改数据  
在父组件中接受子组件传递的值，对指定的属性进行修改

```js
<demoTemplate :message="n" @update:message="val => n = val" />
```

在子组件中传递要修改的属性和属性值

```js
<button @click="$emit('update:message',message+1)">+1</button>
```

而.sync修饰符就是第一行代码的语法糖

```js
<demoTemplate :message.sync="n" />
```

vue会将有.sync的属性进行扩展

```js
attribute.sync="value" => attribute="value" @update:attribute="val => value = val "
```



https://zhuanlan.zhihu.com/p/264840667