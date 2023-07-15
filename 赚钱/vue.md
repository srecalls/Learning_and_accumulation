### 1. v-if和v-show的区别

v-if是动态的进行增删DOM元素，有更高的切换消耗；v-show是通过设置样式display；有更高的初始渲染消耗。

v-if作用于普通元素时会触发beforeUpdate和updated钩子函数，作用于组件时父组件会触发beforeUpdate和updated钩子函数，

子组件：当v-if从false到true时，触发beforeCreate，created，beforeMount，mounted钩子；

​			    当v-if从true到false时，触发beforeDestroy和destroyed钩子函数。

v-show不影响生命周期。

v-show不支持<template>语法

### 2. vue中的单向数据流（props)

1. 在父传子的前提下，父组件的数据发生改变会通知子组件自动更新
2. 子组件内部，不能直接修改父组件传递过来的props => props是只读的

特殊情况：
父传给子一个引用数据类型，子组件修改后不会报错，且父组件的数据也会被修改。建议用深拷贝。

### 3. computed和watch的区别和使用场景

computed会进行缓存，watch不会。

使用场景：

​	computed：一个数据受多个数据影响。

​	watch：一个数据影响多个数据，或者是执行异步和开销较大的操作。

### 4. Vue 的父组件和子组件生命周期钩子函数执行顺序？

Vue 的父组件和子组件生命周期钩子函数执行顺序可以归类为以下 4 部分：

- 加载渲染过程

  父 beforeCreate -> 父 created -> 父 beforeMount -> 子 beforeCreate -> 子 created -> 子 beforeMount -> 子 mounted -> 父 mounted

- 子组件更新过程

  父 beforeUpdate -> 子 beforeUpdate -> 子 updated -> 父 updated

- 父组件更新过程

  父 beforeUpdate -> 父 updated

- 销毁过程

  父 beforeDestroy -> 子 beforeDestroy -> 子 destroyed -> 父 destroyed

### 5. 谈谈你对 keep-alive 的了解？

keep-alive是vue自带的组件，用来缓存组件的

有三个属性，max：最大缓存数，include：只有组件名称匹配会被缓存，exclude：组件名称匹配的不会被缓存。

exclude优先级比include高。

对应两个钩子函数：activated和deactivated

### 6. 组件中data为什么必须是一个函数？

当组件中的data写成一个函数时，每复用一次data，都会返回一份新的data，拥有自己的作用域；当组件中的data写成一个对象时，它会共用一个内存地址，该组件被多次复用时会共用一个data，产生数据污染。

### 7. vue-router 路由模式有几种？

两种模式都是改变url，更新视图，但不向服务器请求网页，也不会刷新页面；

hash模式：使用了hashChange事件监听地址栏hash的变化，使用window.location.hash获取hash值；

history模式：使用pushState和replaceState去修改浏览器的历史记录栈，router-link本质是个a标签，它会禁用a标签的默认行为，点击router-link后会去调用pushState，再判断url上的路由去加载组件，同时监听popState事件去实现点击浏览器前进后退按钮切换路由；

pushState与replaceState的区别：pushState会添加新的历史记录，而replaceState不会，它只替换当前历史记录；

history与hash模式的区别：

1. 直观的体现是hash模式会带#，而history模式不会；

2. history模式比hash模式更利于seo；（hash模式带有#，搜索引擎的爬虫难以理解这种URL的含义，而history不会带#，搜索引擎能更好的理解站点结构和页面之间的关系）

3. history模式直接地址栏去访问路由或者刷新会导致404，需要服务器去配置，而hash模式是不用的；

   （因为你平时切换路由是不会向服务器发送请求的，直接去输入地址栏或者刷新页面是会的，hash模式下发起请求服务器会不管#后面的内容，但是history模式下是没有#的，服务器就会去找相应的资源，但肯定是找不到，因为路由只是在前端使用，所以就会返回404页面，需要服务器设置找不到资源时重定向到index.html页面，再走路由的配置获取对应页面，但这里有个问题是找不到资源不会返回404页面，这就需要前端配置路由，将未匹配到的路由重定向到404页，这个要放在最后）

4. hash兼容更好，如果你使用history模式，vue-router里面也会先判断浏览器是否支持history模式，如果不支持就自动切换成hash模式。

### 8. MVVM和MVC

**MVVM**

​	M：model数据层，V：view视图层，VM：viewmodel层

​	MVVM框架实现了双向绑定，即当数据发生变化的时候，视图也就发生变化，当视图发生变化的时候，数据也会跟着同步变化。

​	view层和model层是通过vm层去连接的，这样解耦了 View 层和 Model 层，不用自己去操作DOM。

​	vm层实现的方式是：DOM 事件监听。

​	vue没有完全遵循MVVM，因为MVVM中view层和model层不能直接通信，但vue中有ref

**MVC**

​	M：model数据层，V：view视图层，C：controller控制层

​	MVVM解决了 MVC 中大量的 DOM 操作使页面渲染性能降低，加载速度变慢的问题，同时也能使我们更加专注于处理业务逻辑。

​	当 Model 频繁发生变化，开发者需要主动更新到 View。

### 9. v-model的实现原理

v-model本质上是语法糖。

text和textarea元素使用的是value属性和input事件

radio和checkbox使用是的checked属性和change事件

select将value作为prop并将change作为事件

```js
<input v-model="searchText">
// 相当于
<input :value="searchText" @input="searchText = $event.target.value">
```

### 10. vue的优缺点(对vue的理解)

优点：渐进式，轻量级，MVVM，响应式，虚拟dom，组件化，单页面应用；

缺点：首屏加载时间长，不利于SEO。

渐进式：你想用啥就用啥，你可以使用component、router、vuex等，也可以不用；

单页面应用：是局部刷新，不用每次跳转页面都请求所有的数据和DOM，加快访问速度；

组件化：可以进行复用，提升开发效率；

虚拟DOM、响应式：略。

首屏加载时间长：引入过多插件，路由全部引入，图片没有压缩；解决方法是：筛选删除不要的插件，使用路由懒加载，使用图片懒加载。

### 11. vue的响应式原理？

劫持data中的属性，通用defineReactive方法使用Object.defineProperty()给属性加上get和set，数组方面是通过重写数组方法来实现，get中会收集依赖，set中更新依赖。每个属性都有自己的依赖收集器Dep，当设置属性值时触发set，set调用函数dep.notify()去通知Dep，Dep会通知Watcher触发render函数，render函数会根据watcher的数据生成新的虚拟DOM，进行新旧虚拟DOM的对比，最后生成真实DOM，完成页面的渲染。

### 12. vue的修饰符

1. lazy：改变输入框的时候value不会变，光标离开输入框的时候value才改变；
2. trim：光标离开后，value的首尾空格符会去掉；
3. number：将值转化为数字，先输入数字再输入字符就取数字部分，先输入字符再输入数字number修饰符就失效；
4. stop：阻止冒泡；
5. capture：变成捕获；
6. self：只有点击事件本身才会触发事件；
7. once：只能执行一次；
8. prevent：阻止默认事件，例如a标签的跳转；
9. native：当我们给组件绑定原生事件的时候，如果不使用native修饰，可能会不起作用；
10. left、middle、right：分别是鼠标的左中右按键触发的事件；
11. passive：当在移动端使用scroll事件时会很卡，加个passive事件修饰符相当于加了个lazy修饰符；
12. keycode：绑定在keyup、keydown、keypress上的，可以设置多按键触发，如`@keyup.ctrl.shift=''`需要同时按ctrl和shift才能触发事件。

### 13. 为什么v-if和v-for不建议一起使用？

vue2：v-for的优先级高于v-if，会先使用v-for全部渲染出来，再一个一个使用v-if判断，会造成渲染无用的节点。

vue3：v-if的优先级高于v-for，这意味着v-if不能访问到v-for中的变量，官方推荐加一个template标签，把v-for放在上面，里面放内容加v-if

ps：template标签页面渲染的时候不生成DOM节点，vue2中一个.vue文件只能有一个template，vue3中可以有多个，才能有这个解决方案。

```html
<template v-for="item in textValue">
      <div v-if="item.show" :key="item.id">{{item.text}}</div>
</template>
```

### 14. 定义不需要响应式的数据

```js
//方法一：将数据定义在return之外
data(){
    this.num = 0
	return{}
}
//方法二：使用Object.freeze()
data(){
    return{
        this.nums = Object.freeze(0)
    }
}
```

### 15. el和$mount优先级

el>$mount

```js
//渲染app
new Vue({
  router,
  store,
  el: '#app',
  render: h => h(App)
}).$mount('#bpp')
```

### 16. vue单页面应用（SPA）和多页面应用的区别

单页面：只有一个主页面，组件公共资源只要加载一次，是局部更新，页面切换快，流畅度高，但不利于SEO，初次加载耗时。

多页面：多个页面之间跳转，每个页面都要加载公用的资源，页面切换慢，数据传递需要用cookie、localStorage、URL参数等方式，但SEO好。

### 17. vue中的异步渲染

vue的异步渲染是数据发生变化后不会马上去更新页面，会调用dep.notify方法去通知Watcher执行upate方法，updata中会让Wacther进入一个队列并进行去重，然后将队列放进异步API的回调函数中，异步API的会根据浏览器的兼容去选择，优先级是Promise.then>MutationObserver>setImmediate>setTimeout(fn,0)，待同步代码执行完毕，再去执行这个异步回调函数，然后执行队列中每个Watcher的run方法，最终执行一次渲染操作，这样减少DOM的操作，提高性能。

### 18. 组件通信

1. 父子间通信

   （1）父组件通过props向子组件传递数据，子组件通过$emit触发事件来向父组件传递数据。

   （2）使用$refs与$parent

2. 兄弟间通信

   eventBus使用$emit发送事件，$on接收事件。

3. vuex、pinia

### 19. 生命周期

1. beforeCreate：
2. created：可以访问到data、computed、watch、methods上的方法和数据，但不能访问到DOM，如果需要在此访问DOM可使用nextTick
3. beforeMount：render函数被调用，编译模版生成html，但未挂载到页面
4. mouted：挂载完毕，可以访问到DOM，可发一些axios请求
5. beforeUpdate：响应式数据已经更新，但未渲染到页面上
6. updated：渲染页面完毕，避免在此钩子中更改状态，否则可能会引起updated的无限调用
7. beforeDestory：实例销毁前，在这里实例还完全可以使用，可在此期间做一些事情解绑的工作
8. destoryed：实例完成被销毁

### 20. vuex和localStorage的区别

1. vuex存储在内存中，localStorage存储在硬盘中，vuex读取速度快；
2. vuex是响应式的，localStorage不是；
3. localStorage存储的是字符串，如果要存对象需要转化为json；
4. 刷新页面后vuex存储的值会消失，localStorage不会；（可做持久化）

### 21. $router和$route的区别

$router是用来路由的跳转，$route是获取路由的信息

### 22. vue-router跳转和location.href的区别

1. vue-router是使用pushState进行路由更新，静态跳转，页面不会重新加载，location.href会使页面重新加载一次；
2. vue-router使用的diff算法，按需加载，减少DOM的操作；

### 23. query和params传参的区别

1. query传参可以使用path或name，params只能使用name；
2. query传参会显示在地址上，params不会；
3. 页面刷新后query传参不会消失，params会消失；

### 24. 虚拟DOM

1. 虚拟DOM是将真实DOM抽象为js对象，当页面发生改变的时候会生成新的虚拟DOM，通过diff算法将新旧虚拟DOM进行对比，记录它们的差异，再将有差异的地方更新到真实DOM上。
2. 虚拟DOM能保证性能的下限，在不进行手动优化的情况下还能提供过得去的性能。
3. 使用虚拟DOM首次渲染会比不使用虚拟DOM慢，但在更新DOM的时候，使用diff算法最大限度的减少了操作DOM的次数，性能会更快。

### 25. diff算法

diff算法在vue里面也叫做patch，它是通过对比新旧虚拟DOM找出最小变化，再更新到真实DOM上，可以减少DOM的操作次数，diff算法放弃跨层级节点的比较，只对同层节点进行比较，使得时间复杂度从O(n3)降低至O(n)，。

页面在首次渲染的时候会调用一次patch，并创建新的虚拟DOM，不会进行深层次的比较，当数据发生改变的时候，会触发set去调用dep.notify()方法，去通知watch，watch会执行相应的render函数去获取新的虚拟DOM，然后执行patch进行新旧虚拟DOM对比，计算最小变化，更新真实DOM。

patch的流程是：

调用sameVnode函数判断新节点和旧节点是否为同一节点，主要是使用key和标签名去判断的，不同节点则创建新节点，删除旧节点，相同则调用patchVnode函数对比子节点；

patchVnode主要做了几个判断：

1. 新节点是否为文本节点，如果是，则直接更新文本；
2. 新节点有子节点，旧节点没有子节点，则创建新的子节点；
3. 新节点没有子节点，旧节点有子节点，则删除旧的子节点；
4. 如果都有子节点，则调用updateChildren更新子节点；

updateChildren对比子节点列表的流程主要是：

​	设置新旧列表的头尾指针，循环遍历两个列表，使用sameVnode判断是否为同一节点，有以下四种情况判断：

1. 新列表的头和旧列表的头对比；

2. 新列表的尾和旧列表的尾对比；

   上面这两种方法匹配上了就移动下标，真实DOM位置不变；

3. 新列表的头和旧列表的尾对比；

4. 新列表的尾和旧列表的头对比；

   这两种方法匹配上了也是移动下标，但真实DOM位置会变；

   如果都没匹配上则分两种情况：

   1. 新旧节点都有key，旧列表的key生成hash表，新列表的头拿key去hash表做匹配，匹配到了且是相同节点就把在真实DOM里移动节点到前面，如果没有则新建节点并插入真实DOM里；
   2. 没有key，则直接新建节点并插入真实DOM里；

结束的标志是其中一个列表的头和尾重合，新列表先遍历完，就删除旧列表中没有遍历过的节点，旧列表先遍历完，就添加新列表中没有遍历过的节点。

PS：为什么有头对尾，尾对头的操作？可以快速检测出reverse操作，加快diff效率。

### 26.vue中key的作用

key的作用主要是为了高效的更新DOM，key保证该元素的唯一性，在Diff算法中，会通过key值判断该元素是已存在的还是新创建的，如果是已经存在的元素就直接复用，避免不必要的渲染。v-for中一般用id作为key，不要使用index作为key。因为数组的索引值一直是按顺序的，如果你在数组中插入一项，插入项的后面所有项的key都会改变，造成多余的渲染。

还有一种情况是在v-if中，v-if切换的时候前后相同的元素会被复用，如果该元素是已经写入数据的input框，则会复用这个有数据的input框，切换前后用户的输入不会被清掉，不符合需求，所以需要用key保证它的唯一性。

### 27. style标签中scoped属性的原理

scoped是为了使样式私有化，不对全局造成污染，vue组件中的style标签如果加了scoped属性，则该标签中的样式只在该组件内生效。如果引用第三方组件，需要局部修改第三方组件的样式，又不想去掉scoped造成全局污染，可以再加一个不含scoped属性的style标签，也可以使用样式穿透:deep()。vue中的scoped主要是通过PostCSS转译实现的，原理是给元素加一个特别的属性，再用上css的属性选择器。样式穿透的原理是去掉那个特别的属性。

```html
<div class="myclass"></div>
<style scoped>.myclass{font-size:12px;}</style>
//上述代码相当于
<div data-v-fed36922></div>
<style>.myclass[data-v-fed36922]{font-size:12px;}</style>
```

### 28. vue中怎么重置data？

```js
//需要使用call，不然取不到data(){return {a:this.methodA}}中的this.methodA
Object.assign(this.$data,this.$options.data.call(this));
```

### 29. vue2与vue3的区别

1. 数据双向绑定原理

   vue2使用的是Object.defineProperty()进行数据劫持，结合发布订阅的方法实现的。

   vue3使用的是Proxy代理，使用ref和reactive将数据转化为响应式。

2. vue3的组合式api

   vue2使用的是Options API，vue3使用的是Composition API，新增了setup()。

3. 生命周期

   ![](https://img-blog.csdnimg.cn/img_convert/4b52616e71eb80aef594f02d3c3f6ed5.webp?x-oss-process=image/format,png)

5. 更好的支持TypeScript

5. 支持tree shaking

   tree shaking是依赖于es6模块的静态编译的，需要按需导入，打包时它会删除你没有import进来的代码，减小打包体积，vue3很多像computed、watched都是需要按需导入的，webpack在生产环境默认开启，开发环境`optimization.usedExports: true`，在js文件中`import './test.css'`，这个css文件会被tree shaking掉，所以需要在loader的配置中加入`sideEffects: true`。

6. fragment：vue2只能有一个根元素，因为虚拟dom是用单根的树形结构去描述当前的视图，patch方法遍历的时候从根节点开始遍历，所以只能有一个根元素，vue3中引入fragment，如果组件是多根会自动创建一个fragment节点，把多根节点视为自己的children，patch的时候遍历这些children。

7. diff算法的更新

   vue2是全量diff，vue3是静态标记+非全量diff，会对节点作不同的标记，静态节点直接跳过不比较，动态节点根据标记去选择diff的过程，有些节点并不需要完整的diff；静态提升，创建虚拟DOM的时候，vue2每个节点无论是否参与更新都会被重新创建，vue3中会把虚拟DOM进行静态提升，不参与更新的元素只创建一次，后续直接复用就可以了；事件缓存，每次更新，无论是否有变化 ，都会重新生成新的事件函数，将旧的事件删除替换成新的事件函数，vue3中会缓存事件，只有发生实际变化时才会重新创建新的事件函数；对比时vue2中diff算法是头和头，尾和尾，头和尾，尾和头，都没有命中的对比，vue3中是头和头，尾和尾，中间算出最长递增序列，剩余节点根据这个序列进行移动、新增和删除。

8. 新增Teleport组件，应用场景是管理多个弹窗，传到body上去方便设置他们的z-index；

### 30. v-on绑定多个方法或绑定多个事件

1. 绑定多个事件

   ```js
   v-on="{click:clickFn,mousemove:mousemoveFn}"
   ```

 2. 一个事件绑定多个方法

    ```js
    @click="clickA,clickB"
    ```


### 31. 讲一下nextTick

vue是异步渲染的，数据更新的时候DOM不会马上更新，可以使用nextTick获取更新后的DOM，在created生命周期中也能使用nextTick去获取DOM。它是使用异步任务去实现的。异步任务会根据浏览器的兼容去选择，优先级是Promise.then > MutationObserver > setImmediate > setTimeout(fn,0)。

### 32. 组件中写name有什么好处

1. 递归调用自身组件;
2. 在调试工具vue-devtools里显示的名称是组件里的name;

3. 使用keep-alive可以搭配name进行缓存，import的名字为注册名称，组件中的name为声明名称，优先组件中的name，两者同时存在的时候声明名称会失效，无法使用它。

### 33.为什么不建议用index作为key

使用index作为key的话和没使用没什么区别，因为数组的数据的顺序不管怎么改变，它的index顺序都是0、1、2、3...这样排列，会导致vue错误复用子节点。

### 34. vue事件绑定的原理

vue中给普通元素绑定事件是通过addEventListener的，给组件绑定事件是通过vue自定义的$on实现的，$emit可以触发事件，如果要在组件上使用原生的事件，需要加.native修饰符。

### 35. vue中模板编译原理（vue template 到 render 的过程）

Vue的模板编译的过程主要是：template -> ast -> render函数

1. 生成AST树：解析模板，调用parse方法将template转化成AST树（一种用js对象的形式来描述整个模板），使用大量的正则表达式对模板进行解析，遇到标签、文本的时候都会调用对应的回调函数进行处理；
2. 优化：vue的数据是响应式的，但其实模板中不是所有数据都是响应式的，有一些数据首次渲染后就不会再改变了，对应的DOM也不会变化，那么我们就深度遍历AST树，按照相关条件对静态节点进行标记，更新的时候就可以跳过这些静态节点，这对运行时模板更新起到了极大的优化作用；
3. codegen：编译最后一步是被优化后的AST树转化为可执行的代码。

### 36. AST树和虚拟DOM

AST树是对源代码语法结构的抽象表示，虚拟DOM是对DOM节点的描述，两者的共同点是都是使用js对象表示。

模板语法->抽象语法树AST->渲染函数render->虚拟DOM->真正DOM

### 37. hash和history区别

1. 最直观的，使用hash模式url上会带#，history不会；
2. history需要后端配合设置，否则刷新页面会出现404，hash不用；
3. hash兼容比history好；

