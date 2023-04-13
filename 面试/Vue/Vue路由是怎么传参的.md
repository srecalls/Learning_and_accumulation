params传参

	this.$router.push({name: 'index' , params :{id:item.id}})
	this.$route.params.id
	
路由属性传参

	this.$router.push( {name:'/index/${item.id}'})
	路由配置{ path:'/index:id' 
	
query传参(可以解决页面刷新参数丢失的问题)

	this.$router.push({
		name:' index' ,
		query:{id:item. id}
	})
	



# vue路由里面query是什么
在Vue路由中，`query`是一种参数传递方式，可以通过在路由路径后面添加`?`和一组键值对来传递参数。例如：

```
// 定义路由
const router = new VueRouter({
  routes: [
    {
      path: '/user',
      component: User,
    }
  ]
})

// 跳转到路由，并携带参数
this.$router.push({
  path: '/user',
  query: { name: 'John', age: 30 }
})
```

在上面的例子中，当用户跳转到`/user`路径时，路由会将`query`参数解析为一个对象，即`{ name: 'John', age: 30 }`，可以在组件中通过`this.$route.query`来获取这些参数。

`query`参数通常用于传递较小的数据量，比如搜索关键字、筛选条件等等。与之相对的是`params`参数，它是另一种参数传递方式，可以通过路由路径的占位符来传递参数，通常用于传递较大的数据量，比如文章内容、用户详情等等。

#   query params 和路由参数
在Vue路由中，`query params`和`路由参数`（也称为`params`）都是用于在路由之间传递数据的方法，但它们有一些区别。

1.  参数的传递方式不同

`query params`是通过在URL中添加查询字符串的方式来传递参数，例如：`/user?name=John&age=30`。这些参数可以通过`this.$route.query`来获取。

而`路由参数`则是通过在路由路径中添加占位符（例如`/user/:id`）来传递参数，例如：`/user/123`。这些参数可以通过`this.$route.params`来获取。

2.  参数的大小限制不同

`query params`通常用于传递较小的数据量，例如搜索关键字、筛选条件等等，因为查询字符串的长度是有限制的。

而`路由参数`则可以用于传递较大的数据量，例如文章内容、用户详情等等，因为它们可以通过路由路径的占位符来传递，而不会受到长度限制。

3.  参数的用途不同

`query params`通常用于表示当前页面的状态或用户的操作，例如搜索结果、排序方式等等。

而`路由参数`通常用于表示实体对象或资源的唯一标识符，例如用户ID、文章ID等等。

总的来说，`query params`和`路由参数`都有各自的适用场景，开发者需要根据具体的需求和场景来选择合适的参数传递方式。