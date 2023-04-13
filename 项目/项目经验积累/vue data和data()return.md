# vue data声明区别 data:{} 与 data(){return {}}
#  data:{}
这种可以直接挂在[vue](https://so.csdn.net/so/search?q=vue&spm=1001.2101.3001.7020)实例上
```JS
var vm = new Vue({
        el:'#app',
        data:{
            title:'HELLO,WORLD!'
        }
    })

```
# data(){ return{} }
组件是一个可复用的实例，当你引用一个组件的时候，组件里的data是一个普通的对象，所有用到这个组件的都引用的同一个data，就会造成数据污染。

不使用return包裹的数据会在项目的全局可见，会造成变量污染； 使用return包裹后数据中变量只在当前组件中生效，不会影响其他组件。

es6中的箭头函数
```JS
data:()=>({
  obj
})

```

ES6/EcmaScript 2015表示法
```JS
data () {
  return {
    obj
  }
}
```

常规，ES5和之前，符号）
```JS
data: function () {
  return {
    count: 0
  }
}
```

在声明Vue方法时不要使用箭头功能(() => {}).他们从当前范围(可能是window)中拾取this，并且不会反映Vue实例.
请注意，您不应将箭头功能与data属性一起使用(例如，data: () => { return { a: this.myProp }}).原因是箭头函数绑定了父上下文，因此this不会是您期望的Vue实例，而this.myProp将是未定义的.