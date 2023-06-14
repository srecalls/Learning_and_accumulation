## 非懒加载：
```JS
import List from '@/components/list.vue'
const router = new VueRouter({
    routes: [
        { path:'/list', component: List }
    ]
})
```

## （1）方案一(常用): 使用箭头函数+import动态加载
```js
const List = () => import('@/components/list.vue')
const router = new VueRouter({
    routes: [
        { path:'/list', component: List }
    ]
})
```