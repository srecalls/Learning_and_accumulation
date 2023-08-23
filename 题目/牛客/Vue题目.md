## 2.在Vue中，下列哪个选项对数组的操作不会触发视图的更新（   ）
- [ ] A.push()
- [ ] B.shift()
- [x] C.concat()
- [ ] D.reverse()


官方解析：concat()返回一个新的数组，还需要用新数组替换原数组才能实现视图的更新。

push()在该数组最尾添加新的元素，然后**返回更新后的数组长度，方法将改变原始数组的长度**；

shift()删除该数组第一个元素，并且把该数组剩下的元素索引往前挪一位，**然后返回删除的元素，方法将改变原始数组的长度；**

reverse()反转该数组中元素的顺序，方法将**改变原始数组**。

**concat()把两个以上的数字连接起来，该方法不会改变现有的数组，而仅仅会返回被连接数组的一个副本**。

push(),shift(),reverse()改变原数组，会触发视图跟新；  

concat()不更改数组，会返回新数组，因此没有替换原数组，不触发视图更新，要用新数组替换原数组才能实现视图更新。


## 4.下列关于scoped的描述错误的是（   ）
- [ ] A.scoped原理是在标签上添加data-v属性，然后使用属性选择器实现样式局部化
- [x] B.使用scoped，父组件的样式会渗透到子组件内部的元素
- [ ] C.使用scoped不会造成全局污染
- [ ] D.">>>"可以实现样式穿透


官方解析：使用scoped后，父组件的样式将不会渗透到子组件中。不过一个子组件的根节点会同时受其父组件的scoped css和子组件的scoped css的影响。这样设计是为了让父组件可以从布局的角度出发，调整其子组件根元素的样式。

使用scoped，父组件的样式不会渗透到子组件，如果要渗透，可以在需要渗透的样式前面加>>>或::v-deep或/deep/

样式穿透的方法有三种：>>>，/deep/，::v-deep, :deep

## 5.关于keep-alive说法错误的是（   ）
- [ ] A.keep-alive可以通过include属性，匹配要进行缓存的组件
- [ ] B.当组件在keep-alive内被切换，它的activated和deactivated这两个生命周期钩子函数将会被对应执行
- [ ] C.keep-alive自身不会渲染为一个 DOM 元素，也不会出现在组件的父组件链中
- [x] D.max属性控制最多可以缓存多少组件实例。一旦这个数字达到了，新创建的实例则不能再进行缓存

官方解析：max属性控制最多可以缓存多少组件实例。一旦这个数字达到了，**在新实例被创建之前，已缓存组件中最久没有被访问的实例会被销毁掉**。

  关于keep-alive的总结： 
```js
<keep-alive> 
	<loading></loading>  
</keep-laive>
``` 
 
  include、exclude：匹配要进行缓存的组件 
 
  max：max属性控制最多可以缓存多少组件实例。一旦这个数字达到了，在新实例被创建之前，已缓存组件中最久没有被访问的实例会被销毁掉。

`<keep-alive>` 是 Vue.js 中的一个内置组件，用于缓存动态组件或组件树，以提高应用的性能和响应速度。它具有以下属性：

1. `include` 和 `exclude` 属性：
   - `include` 属性用于指定需要被缓存的组件的名称，可以是字符串或正则表达式。
   - `exclude` 属性用于指定不需要被缓存的组件的名称，可以是字符串或正则表达式。
   - 通过使用这两个属性，可以精确地控制哪些组件应该被缓存，哪些组件不应该被缓存。

示例：

```html
<keep-alive :include="['ComponentA', /^ComponentB/]" :exclude="['ComponentC']">
  <loading></loading>
</keep-alive>
```

在上述示例中，`include` 属性指定了需要被缓存的组件，其中 `'ComponentA'` 和以 `'ComponentB'` 开头的组件将会被缓存。而 `exclude` 属性指定了不需要被缓存的组件，其中 `'ComponentC'` 组件不会被缓存。

2. `max` 属性：
   - `max` 属性控制最多可以缓存多少组件实例。
   - 一旦缓存的组件实例数量达到 `max` 的值，在创建新的组件实例之前，已缓存组件中最久没有被访问的实例会被销毁。
  
示例：

```html
<keep-alive :max="5">
  <loading></loading>
</keep-alive>
```

在上述示例中，`max` 属性被设置为 `5`，表示最多可以缓存 5 个组件实例。如果超过了这个数量，在创建新的组件实例之前，最久没有被访问的实例会被销毁。

总结：
- `<keep-alive>` 组件用于缓存动态组件或组件树，提高应用性能和响应速度。
- `include` 和 `exclude` 属性用于指定需要或不需要被缓存的组件。
- `max` 属性控制最多可以缓存的组件实例数量，超过该数量时最久未访问的实例会被销毁。
 
  ```js
export default [
  { 
    path: '/',
    name: 'home',
    component: Home,
    meta: { 
      keepAlive: true // 需要被缓存的组件
    }
  },
  { 
    path: '/book',
    name: 'book',
    component: Book,
    meta: { 
      keepAlive: false // 不需要被缓存的组件
    }
  }
];
‘```

keep-alive 是一个抽象组件：它自身不会渲染成一个 DOM 元素，也不会出现在父组件链中。在组件切换过程中将状态保留在内存中，防止重复渲染DOM，减少加载时间及性能消耗，提高用户体验性。include定义缓存白名单，keep-alive会缓存命中的组件；exclude定义缓存黑名单，被命中的组件将不会被缓存；max定义缓存组件上限，超出上限使用` LRU的策略 `置换缓存数据  


## 1.下列不属于Vue的特点的是（   ）
- [ ] A.Vue.js的核心是一个允许采用简洁的模板语法来声明式地将数据渲染进DOM的系统
- [ ] B.实现了双向数据绑定
- [ ] C.Vue.js可以进行组件化开发，使代码编写量大大减少，读者更加易于理解
- [x] D.Vue虽然也提供了渲染函数，默认使用模板渲染，且不支持JSX

官方解析：Vue 支持 JSX

Vue的特点可以总结如下：

1. 轻量级：相比Angular，Vue的学习成本较低，使用起来更加简单直接，对初学者更加友好。
2. 数据绑定：Vue采用双向数据绑定的MVVM模式，数据变化时视图自动更新，视图变化时数据也会同步更新，使得处理表单等操作更加方便。
3. 指令：Vue提供了丰富的指令，包括内置指令和自定义指令，通过指令可以给HTML元素添加特殊行为，如动态绑定、条件渲染、列表渲染等。
4. 插件：Vue支持插件扩展，通过编写插件并进行简单的配置，可以全局使用扩展功能，常用的插件有vue-router、Vuex等。
5. 性能优化：Vue采用基于依赖追踪的观察系统和异步队列更新，数据独立触发，提高了数据处理能力，具有较好的性能表现。
6. 组件化：Vue和React都以组件为中心思想，组件可以嵌套使用。React使用JSX语法，Vue推崇以`.vue`后缀命名的文件格式，对文件内容有一些规定，需要编译后使用。
7. 模板操作：Vue提供了指令、过滤器等在模板中操作DOM的便捷方式，使得操作DOM更加方便快捷。

总之，Vue是一个功能丰富、简单易用、性能优秀的JavaScript框架，特别适合用于构建具有复杂交互逻辑的前端应用，以提供良好的用户体验。


## 3.关于v-model的修饰符说法错误的是（   ）

- [ ] A.lazy修饰符让内容在“change”事件时而非“input”事件时更新
- [ ] B.v-model添加number修饰符,可以自动将用户的输入值转为数值类型
- [ ] C.可以给v-model添加trim修饰符,自动过滤用户输入的首尾空白字符
- [x] D.v-model添加number修饰符,如果这个值无法被parseFloat()解析，则会返回null


让我们逐个检查每个选项并提供相应的例子：

### A. lazy 修饰符让内容在 "change" 事件时而非 "input" 事件时更新。

这个说法是正确的。使用 `v-model` 默认情况下会在 "input" 事件时即时更新绑定的数据，但是可以通过 `lazy` 修饰符来改变更新的时机为 "change" 事件。

```html
<template>
  <input v-model.lazy="message" />
</template>

<script>
export default {
  data() {
    return {
      message: ""
    };
  }
};
</script>
```

在上述示例中，`v-model.lazy` 修饰符会在输入框失去焦点或按下回车键时才更新 `message` 的值。

### B. v-model 添加 number 修饰符，可以自动将用户的输入值转为数值类型。

这个说法是正确的。使用 `v-model.number` 修饰符可以将用户的输入值自动转换为数值类型。

```html
<template>
  <input v-model.number="quantity" type="number" />
</template>

<script>
export default {
  data() {
    return {
      quantity: 0
    };
  }
};
</script>
```

在上述示例中，`v-model.number` 修饰符将用户在输入框中输入的值自动转换为数值类型，并将其绑定到 `quantity` 变量上。

### C. 可以给 v-model 添加 trim 修饰符，自动过滤用户输入的首尾空白字符。

这个说法是正确的。使用 `v-model.trim` 修饰符可以自动去除用户输入内容的首尾空白字符。

```html
<template>
  <input v-model.trim="name" />
</template>

<script>
export default {
  data() {
    return {
      name: ""
    };
  }
};
</script>
```

在上述示例中，`v-model.trim` 修饰符会自动过滤用户在输入框中输入的内容的首尾空白字符。

### D. v-model 添加 number 修饰符，如果这个值无法被 parseFloat() 解析，则会返回 null。

这个说法是错误的。`v-model.number` 修饰符在无法被 parseFloat() 解析的情况下，并不会返回 null，而是会将输入值绑定为 NaN（Not a Number）。

```html
<template>
  <input v-model.number="price" type="number" />
</template>

<script>
export default {
  data() {
    return {
      price: 0
    };
  }
};
</script>
```

在上述示例中，如果用户输入的值无法被解析为有效的数值，`price` 的值将被绑定为 NaN。

因此，选项 D 是说法错误的。

官方解析：v-model添加number修饰符,如果这个值无法被parseFloat()解析，则会返回原始的值。

在默认情况下，v-model 在每次 input 事件触发后将输入框的值与数据进行同步 。你可以添加 lazy 修饰符，从而转为在 change 事件_之后_进行同步：

如果想自动将用户的输入值转为数值类型，可以给 v-model 添加 number 修饰符：如果这个值无法被 parseFloat() 解析，则会返回原始的值。

## 5.关于路由守卫说法错误的是（   ）

- [ ] A.Vue路由守卫分为全局路由、单个路由守卫、组件内部路由
- [x] B.全局路由守卫的钩子函数有：beforeRouteEach（全局前置守卫）、beforeRouteResolve（全局解析守卫）、afterRouteEach（全局后置守卫）
- [ ] C.单个路由独享的钩子函数只有一个：beforeEnter
- [ ] D.组件路由守卫相关的钩子函数：beforeRouteEnter、 beforeRouteUpdate、beforeRouteLeave

官方解析：全局路由守卫的钩子函数有： beforeEach（全局前置守卫）、beforeResolve（全局解析守卫）、afterEach（全局后置守卫）

全局路由守卫的钩子函数有：beforeEach（全局前置守卫）、beforeResolve（全局解析守卫）、afterEach（全局后置守卫） 名字中间没有“Route”， 组件级路由守卫的钩子函数才有“Route”  

- 路由导航守卫分为 3 种：全局路由守卫、路由独享的守卫、组件内的守卫
### 全局路由守卫：
- 全局前置守卫：beforeEach
- 全局解析守卫：beforeResolve
- 全局后置钩子：afterEach

### 路由独享的守卫：
- beforeEnter

### 组件内的守卫：
- beforeRouteEnter
- beforeRouteUpdate
- beforeRouteLeave

## 1.关于Vue组件生命周期说法错误的是（   ）
- [ ] A.Vue组件的生命周期可以分成三个大阶段：挂载、更新、卸载
- [ ] B.挂载阶段中涉及到的钩子函数有：beforeCreate、created、beforeMount、mounted
- [x] C.更新阶段涉及的钩子函数有：beforeUpdate、updated、activated、deactivated
- [ ] D.首次进入页面钩子函数的执行顺序：beforeCreate、created、beforeMount、mounted

官方解析：Vue组件的生命周期涉及到的钩子函数和执行顺序是：beforeCreate、created、beforeMount、mounted、beforeUpdate、updated、beforeDestroy、destroyed，activated和deactivated是组件设置了keep-alive时，进入组件和离开组件时分别触发的两个函数

## 2.下列关于Vue和React的描述错误的是（   ）

- [ ] A.Vue进行数据拦截/代理，对数据更敏感，数据驱动视图自更新，而React需要手动驱动数据更新视图
- [x] B.Vue和React的this都指向当前组件实例
- [ ] C.Vue和React都能使用jsx进行编程
- [ ] D.Vue和React都是数据驱动视图的更新

官方解析：React中组件的this并不是当前实例，需要通过bind或箭头函数来修改指向。

   React 函数式组件中 this 为 undefined    
   React 类式组件中：   
    constructor、render 中的 this 指向组件实例      
    普通函数被组件实例调用，this 指向组件实例       
    普通函数作为事件回调调用，严格模式下 this 指向 undefined，非严格模式下 this 指向 window，需要通过 bind 修改指向       
    箭头函数没有自己的 this，this 为创建时的上下文，即指向组件实例


## 3.现有以下代码, 打印的结果是（   ）
```js
new Vue({
    data: { a: 'first', b: 'second' },
    created: function () { console.log(this.a) },
    mounted(){ console.log(this.b) }
})
```

- [x] A.'first'
- [ ] B.'first' 'second'
- [ ] C.undefined undefined
- [ ] D.空

官方解析：由于Vue实例没有执行DOM挂载，所以不会执行mounted钩子函数

mounted是vue中的一个钩子函数，一般在初始化页面完成后，再对dom节点进行相关操作。但是题例中没有执行dom挂载，所以mounted不会执行

new的时候有el属性会自动挂载，没有的话需要后面手动挂载