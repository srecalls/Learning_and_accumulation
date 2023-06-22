[[手写call函数]]
[[手写apply函数]]
都是改变this指向和函数的调用，call和apply的功能类似， 只是传参的方法不同
call方法传的是一个参数列表
apply传递的是一个数组
bind传参后不会立刻执行，会返回一个改变了this指向的函数，这个函数还是可以传参的，bind()()
call方法的性能要比apply好-一些，所以call用的更多一点。
call用扩展运算符代替apply
bind不能作为构造函数
