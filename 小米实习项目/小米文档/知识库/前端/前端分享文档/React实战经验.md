React实战经验

## 03 以组件方式思考UI

组件设计原则

- 单一职责
- DRY，组件尽量小（1. 好维护，2.性能比较好）；少用state，多传递props

## 04 jsx，不是模版语言，是一个语法糖，实际上就是React.createElement

React.createElement(tagName||component,props, ...children)

## 05 生命周期

|   |   |   |   |
|---|---|---|---|
||创建|更新阶段|销毁阶段|
||constructor|props改变 、setState、forceUpdate||
||getDerivedStateFromProps|getDerivedStateFromProps（不建议使用这个方法）||
|||shouldComponentUpdate(PureComponent)||
||render|render||
|pre-commit(获取DOM)||getSnapshotBeforeUpdate||
|commit(操作DOM)|componentDidMount(once)|componentDidUpdate|componentWillUnMount|

## 06 Virtual DOM及key属性

算法时间复杂度优化：O(n^2m(1+logmn)) -> o(n)

diff算法：广度优先算法

节点变化：新增、删除、移动

Virtual DOM的两个假设：

1、组件的DOM结构相对稳定；

2、类型相同的兄弟节点可以被唯一标识（设置key属性）

## 07 组件设计模式：高阶组件和函数作为子组件

高阶组件：传入组件，返回组件 const

函数作为子组件：

![[React实战经验.png]]

## 08 Context API

父组件：provider

子组件：consumer

redux基于这个原理

缺点：Context 没包含修改值的方法，如果子节点中一个button设置全局样式，就需要各显神通，这时用redux更方便

connect(mapStateToProps, mapDistpatchToProps)(ReactComponent) : ReactComponent

Provider store={store}

react-redux

## 09 react脚手架

1. create react app : 适合新手的react脚手架
2. Rekit 集成了比create react app更多的生态
3. codesandbox： 在线IDE

## 10 打包与部署

#### 为什么打包

- 对各个语法糖进行编译（ES6-> ES5）
- 对各个资源的整合
- js、css文件的混淆与压缩

#### 如何进行打包

webpack

运行 npm run eject 命令到处create react app可以自定义webpack配置

#### 打包的注意事项

- 注意 NODE_ENV 、babel环境等是开发环境(development) 还是生产环境(production)
- 不同环境可以运行不同的代码，process.env.NODE_ENV === 'development'时webpack不会打包进production
- 注意设置资源根路径

## 11 redux

#### 为什么需要redux

- 组件状态传递复杂，简化组件与数据模型之间的关系
- 简化组件之间的通信

#### redux三大特性

- 单一数据源
- 纯函数（没有任何副作用的函数）/State 是只读的 ，
- 单向数据流

#### 讨论问题

- redux和flux的思想有什么区别
    
- redux与mobx有什么区别
    

## 12 redux核心概念与工具方法

react-redux

subcribe(()=> {

//更新dom

})

#### 核心概念

- [actions](https://www.redux.org.cn/docs/basics/Actions.html)
- [reducers](https://www.redux.org.cn/docs/basics/Reducers.html)
- [state](https://www.redux.org.cn/docs/basics/Store.html)

#### 工具方法

- [combineReducers](https://www.redux.org.cn/docs/recipes/reducers/UsingCombineReducers.html)
- [bindActionCreators](https://www.redux.org.cn/docs/api/bindActionCreators.html)
- dispatch

## 13 在React中使用Redux

- connect方法如何使用(形成高阶组件)
- connect参数的作用(mapStateToProps,mapDispatchToProps)

## 14 理解异步Action、Redux中间件

- 中间件的使用**applyMiddleware()**
- 异步action的实现(redux-thunk)

```
export default function thunk(store){
    return function(next){
        return function(action){
            if(typeof action == 'function') {
                action(store.dispatch,store.getState)
            }else{
                next(action);
            }   
        }
    }
}
```

## 15 组织action reducer

- 一个action文件 一个reducer文件 ，文件会很长，适合简单小项目
- 一个文件中（包含action和reducer），引入和导出会越来越复杂，中级
- 按业务逻辑分模块，第一种按照业务分，复杂项目。action命名方式：user/userlist

## 16 不可变数据

### 含义

不能直接修改state，只能新生产一个新的state，state+action = new state

### 为什么不可变

- 性能：只对比state引用即可。
- 易于调试和追踪
- 可预测

### 操作修改state

- 原生：{...} Object.assign
- 第三方库：immutability-helper 复杂的数据
- 第三方库：immer 复杂的数据 性能差点

## 17 react-router

#### 1、什么是前端路由

根据URL显示不同的页面组件

#### 2、React router如何实现路由

对应的路由，显示不同页面

三种方式 ： HashRouter、BroswerRouter、memoryRouter

#### 3、基于路由思考页面的组织

懒加载、项目页面形式组织

#### 4、React Router核心API

<Link />: 不会刷新浏览器的跳转标签

<NavLink />: 会添加显示状态

<Route />: 根据路由显示对应的组件

<Promp />: 推出页面时触发的

<Switch />: 切换界面标签

<Redict />:重定向组件

#### 5、React-router原理

Context

## 18 嵌套路由

#### 1、参数传递

params传递： path to route/:id

#### 2、嵌套路由

## 19 react 同构NEXT.js

1、什么是同构应用

服务端与客户端基本使用同一份代码

2、Next基本用法---请参考官网

## 20 react单元测试与工具
![[React实战经验-1.png]]
## 21 开发调试工具

ESLint、prettier、react devtool、redux devtool

## 23 前端项目的理想架构

|   |   |   |   |   |
|---|---|---|---|---|
|易开发|易维护|易测试|易扩展|易构建|
|开发成本低|统一的规范|功能分层|增加新功能是否容易|通用构建工具|
|社区活跃|代码是否容易理解|副作用少|增加新功能是否大大增加系统复杂度||
|工具完善|文档健全|纯函数写法|||
||||||

## 24-26 拆解复杂项目

领域模型：按业务feature来拆分组织目录

component: 组件和样式分开引入（这个有点过时），每一个feature里面单独管理，common也是一个feature

reducer和action：每一个feature下有一个reducer和action的加载器，然后在最外层去加载各加载各feature的加载器

路由：每一个feature下有一个路由，根路径下有一个中的路由配置，路由使用json的方式配置，加上一个json转react-router的配置方法