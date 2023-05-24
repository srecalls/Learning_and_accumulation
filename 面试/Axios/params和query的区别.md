## version 1
**用法:** query要用path来引入, params要用name来引入,接收参数都是类似的，分别是`this.$route.query.name`和`this.$route.params.name`

**url地址显示**: query更加类似于ajax中get传参，params则类似于post, 说的再简单一点， 前者在浏览器地址栏中显示参数，后者则不显示

**注意**: query刷新不会丢失query里面的数据params刷新会秩params里面的数据。


## version 2
query语法：
```js
this.$router.push({path:'地址',query:{id:"123"}}) // 这是传递参数
this.$router.query.id // 这是接受参数
```

params语法：
```js
this.$router.push({name:'地址',params:{id:"123"}}) // 这是传递参数
this.$router.params.id // 这是接受参数
```

区别：

1.首先就是写法得不同，query 得写法是 用 path 来编写传参地址，而 params 得写法是用 name 来编写传参地址，你可以看一下编写路由时候得相关属性，你也可以输出一下 路由对象信息 看一下

2.接收方法不同， 一个用 query 来接收， 一个用 params 接收 ，总结就是谁发得谁去接收

3.query 在刷新页面得时候参数不会消失，而 params 刷新页面得时候会参数消失，可以考虑本地存储解决

4.query 传得参数都是显示在url地址栏当中，而 params 传参不会显示在地址栏


在Web开发中，params和query的区别不仅在于它们的使用方式和含义，也在于它们的生命周期和作用范围。具体来说，params是在URL的路径中指定的参数，是一种静态参数，一旦设置后就不会变化，除非手动修改URL。而query是在URL的查询字符串中指定的参数，是一种动态参数，可以根据用户的输入或其他条件进行变化。

在刷新页面时，query参数不会消失是因为浏览器会自动将URL中的查询参数保存在浏览器的历史记录中，因此在刷新页面时，浏览器会重新加载保存在历史记录中的URL，并将其中的查询参数再次附加到URL的末尾。这样就可以保留原来的查询参数，不会丢失。

相比之下，params参数是在URL的路径中指定的，不会保存在浏览器的历史记录中，因此在刷新页面时不会自动保留。如果要在刷新页面时保留params参数，可以考虑使用本地存储（如localStorage）来保存参数值，然后在页面加载时从本地存储中读取参数值并使用。这样就可以保留params参数，避免在刷新页面时丢失。

## version 3
在Web开发中，params和query都用于从URL中获取信息，但它们的使用方法和含义有所不同。

params（路径参数）是URL的一部分，用于传递可变数量的参数，通常用于标识特定的资源。在RESTful API中，路由通常包含params，例如：

```
/users/:userId
```

在这个例子中，:userId是一个参数，它可以在URL中被替换成具体的值。这个参数可以通过在服务器端的路由处理程序中访问来进行处理。

query（查询参数）是在URL的查询部分中指定的参数，用于向服务器传递附加信息。查询参数通常用于过滤、排序、分页等操作，例如：

```
/users?sort=desc&limit=10&page=2
```

在这个例子中，sort、limit和page都是查询参数，它们指定了对返回结果进行排序、限制返回结果数量和所请求的页码。

从URL的结构来看，params通常是在URL的路径中，而query通常是在URL的查询字符串中。同时，params和query的语法也有所不同。在路由中，params通常使用冒号（:）或大括号（{}）来指定参数，而在查询字符串中，参数名和值之间使用等号（=）来分隔，参数之间使用&符号进行分隔。