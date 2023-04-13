get和post在传输上没有什么区别，只是http协议中两种请求方式
http是基于tcp/ip的应用层协议
1.get一般是获取数据，post一般是提交数据
2.get参数会放在url上，所以安全性比较差，post 是放在body中
3.get请求刷新服务器或退回是没有影响的，post请求退回时会重新提交数据
4.get请求时会被缓存, post请求不会被缓存
5.get请求会被保存在浏览器历史记录中,post不会
6.get请求只能进行ur1编码，post请求支持很多种
