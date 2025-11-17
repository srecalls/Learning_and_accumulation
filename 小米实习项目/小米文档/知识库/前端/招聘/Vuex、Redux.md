Vuex、Redux

## 17. Redux,Vuex , dva √

### 1. Vuex的实现

### 　需要解决的问题

> 1. **如何使用Vuex**

> 2. **如何在全局使用$store**

> 3. **如何实现$store中state的动态更新**

> 4. **如何实现$store中getters中属性动态更新**

> 5. **如何实现modules,namespaced**

> 6. **如何实现mutations,actions,如何触发对应的函数**

> 7. **如何实现mapState**

### (1) .**如何使用Vuex**

```
Vue.use(Vuex)
Vue.use()使用自定义组件
  需要自定义install属性的函数或者方法
才能在全局使用组件中的方法
Vue.use() 方法至少传入一个参数，该参数类型必须是 Object 或 Function，如果是 Object 那么这个 Object 需要定义一个 install 方法，如果是 Function 那么这个函数就被当做 install 方法。在 Vue.use() 执行时 install 会默认执行，当 install 执行时第一个参数就是 Vue，其他参数是 Vue.use() 执行时传入的其他参数。      
(2) . 如何在全局使用$store
new Vue({
  name:&#39;root&#39;,
  render: h =&gt; h(App),
  store
}).$mount(&#39;#app&#39;)
在对Vue初始化的时候,传递的属性store会挂载在Vue对象的options中,
可以通过Vue.mixin()进行全局混入
```

![](https://xiaomi.f.mioffice.cn/space/api/file/out/tkGZyB8vKigrRsm7YrZtcx8DjxbRkcfGMQJTYTrRrgY1XPpLJT/)

1. ```
    
    export default function install(_Vue){
      Vue = _Vue;
      //将$store混合到每个实例中
      Vue.mixin({
          beforeCreate() {
            if(this.$options.store){
              this.$store = this.$options.store;
            }else{
              if(this.$options.parent &amp;&amp; this.$options.parent.$store){
                this.$store = this.$options.parent.$store
              }
            }
          },
      })
    }
    (3). 如何实现$store中state的动态更新
    > 1. 对store中的配置项进行递归遍历得到处理后的state对象
    > 2. 定义一个Vue实例,将state值当成Vue的data,进行数据的监听
          js
    {
        "state": {
            "name": "hwt",
            "count": 44,
            "test": {
                "age": 24,
                "three": {
                    "name": "a"
                }
            }
        }
    }
    (4). 如何实现$store中getters中属性动态更新
    > 1. 在声明的Vue实例中，通过Vue中的computed属性来动态监听getters函数的变化　
    > 2. 将计算属性(key,value)代理到this.getters中
     在state数据发生变化的时候，会触发页面重新更新，this.getters会被重新调用，得到此时computed属性返回最新的值，实现数据的动态更新
    可能是计算属性更改，导致get函数反复运行
    可能是页面刷新，调用$store.getters.add,从而得到计算属性
    　state数据发生变化时候
            this._computer = {
            }
            this.getters = {};
            let self = this;
            Object.keys(this._getters).forEach(item=>{
                let func = this._getters[item];
                this._computer[item] = function(){
                    return func(this)
                }
                Object.defineProperty(this.getters,item,{
                    get:function(){
                        return self._vm[item];
                    }
                })
            })
    (5) 如何实现modules,namespaced
    ```
    
    进行递归遍历的时候，modules会作为path逐级传递
2. 没有namespaced，会把同名的函数存储在一个数组中
3. 在store遍历阶段会注册_**mutation函数**_存储对象
4. 然后通过commit方法进行触发

```
['test']
//没有namespaced
this.mutation = {
    change:[function(){
},function(){

}],
change2:[function(){

}]
```

}

```
//有namespaced
this.mutation = {
    change:[function(){
}],
&#39;test/change&#39;:[function(){

}]
```

}

```
(6) 如何实现mutations,actions,如何触发对应的函数
　　通过commit,dispath,触发对应的函数
 this.$store.commit('change',num)
 this.$store.commit('test/change',num)
    /*
      触发mutation函数
    */
commit = (type,payload)=>{
    if(this._mutations[type]){
        this._mutations[type].forEach((item)=>{
            item(payload);
        })
    }else{
        throw new Error(`${type} is not a function!`)
    }
}
(7) 如何实现mapState
将用到的state属性放在Vue的计算属性中
function mapState(params,extra){
    let {type , path } = handleMap(params,extra);
    let res = {}
    type.forEach((item)=>{
        res[item] = function(){
           let state =　{};
           let root = this.$store.state;
           state = path.length > 0 ? getContextState(root,item,path) : root[item];
           return state; 
        }
    })

    return res;
}
2. Redux的实现
　　　 ### 需要解决的问题
> 1. 如何在全局使用Redux中的state
> 2. 如何实现state的动态更新
> 3. 如何触发state的更新(dispatch)
> 4. redux中如何进行异步操作
Redux的组成解构
let store =  createStore(reducer,10,applyMiddleware());
let action = {
    type:'',
    payload:''
}
function reducer(state,action){
    switch(action.type){
        case 'add':
            return state + action.payload;
        default:
            return state;
    }
}
let store = createStore(reducer);
store.dispatch(action);
function dispath(aciton){
   state = reducer(state,action);
}
```

![](https://xiaomi.f.mioffice.cn/space/api/file/out/tkGZyB8vKigrRsm7YrZtcx8DjxbRkcfGMQJTYTrRrgY1XPpLJT/)

```
(1) 如何在全局使用Redux中的state
在React中不存在混入到React全局的方法，需要借助执行期上下文context
let ctx = React.createContext();//执行期上下文
//在Provider组件内的子组件都可以拿到执行上下文的值
 <ctx.Provider value={store}>
     {this.props.children}
 </ctx.Provider>
//Consumer拿到store中的值
<ctx.Consumer>
    (store)=>{

    }
</ctx.Consumer>
上下文提供者（Context.Provider）中的value属性发生变化(Object.is比较)，会导致该上下文提供的所有后代元素全部重新渲染，无论该子元素是否有优化（无论shouldComponentUpdate函数返回什么结果）
(2)  如何实现state的动态更新
//createStore()提供subscribe监听函数，在state值变化的时候会触发函数,
//this.setState()使组件的更新
function connect(mapStateToProps,mapDispatchToProps){
    return function Hoc(Comp) {
        //对于该组件，只有它需要的数据发生变化时才会重新渲染
        return class CompWrap extends PureComponent {
            static contextType = ctx;//得到上下文数据
            constructor(props,context){
                super(props);
                let {dispatch,getState,subscribe} = context;//得到执行期上下文中的仓库
                this.state = mapStateToProps(getState());//仓库中值的初始化
                subscribe(()=>{//监听仓库中值的改变
                    this.setState(mapStateToProps(getState()))
                })
                this.eventHandles = mapDispatchToProps(dispatch);
            }
            render() {
                return (
                    <Comp {...this.state} {...this.eventHandles}/> 
                )
            }
        }
    }
}
function mapStateToProps(state){
    return {
        number:state.numberReducer
    }
}
function mapDispatchToProps(dispatch){
    return {
        onIncrease:()=>{
            console.log('increase')
            dispatch(createIncreaseAction());
        },
        onDecrease:()=>{
            console.log('decrease')
            dispatch(createDecreaseAction());
        } 
    }
}
(3). 如何触发state的更新(dispatch)
通过封装的mapDispatchToProps,将dispatch方法映射到组件中
(4). redux中如何进行异步操作
通过在中间件对dispatch方法进行修饰,然后处理完异步操作后，继续dispatch改变state
    js
//(1)中间件redux-thunk
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
export function fetchStudent(){
    return async function(dispatch,getState){
        let msg = await getAllStudents();
        dispatch(getAddUserAction(msg))
    }
}
store.dispatch(fetchStudent())
//(2) 中间件redux-promise
export default ({ dispatch }) => next => action => {
    if (!isFSA(action)) {
        //如果不是一个标准的action
        //如果action是一个promise，则将其resolve的值dispatch，否则，不做任何处理，交给下一个中间件
        return isPromise(action) ? action.then(dispatch) : next(action);
    }
    return isPromise(action.payload) ?
        action.payload
            .then(payload => dispatch({ ...action, payload }))
            .catch(error => dispatch({ ...action, payload: error, error: true })) :
        next(action)
}
export function fetchStudents() {
    return new Promise(resolve => {
        setTimeout(() => {
            const action = setStudentsAndTotal([{ id: 1, name: "aaa" }, { id: 2, name: "bbb" }], 2);
            resolve(action)
        }, 3000);
    })
}
store.dispatch(fetchStudent())
//(3) saga
function* fetchStudents() {
    //设置为正在加载中
    yield put(setIsLoading(true))
    const condition = yield select(state => state.students.condition); //select指令：用于得到当前仓库中的数据
    //使用call指令，按照当前仓库中的条件
    const resp = yield call(searchStudents, condition);//触发异步事件
    yield put(setStudentsAndTotal(resp.datas, resp.cont))//put相当于dispatch
    yield put(setIsLoading(false));//
}
export default function* () {
    yield takeEvery(actionTypes.fetchStudents, fetchStudents);
    console.log("正在监听 fetchStudents")
}
```