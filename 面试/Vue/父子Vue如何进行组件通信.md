# 1.父传子
## props
父组件使用自定义属性，然后子组件使用props|
父组件：
![[Pasted image 20230412022347.png]]

子组件：
![[Pasted image 20230412022409.png]]

## $ref
引用信息会注册在父组件的$refs对象上
父组件：
![[Pasted image 20230412022631.png]]

子组件：
![[Pasted image 20230412022816.png]]

# 2.子传父
## $emit
子组件绑定自定义事件，触发执行后，传给父组件，父组件需要用事件监听来接收参数
父组件:
![[Pasted image 20230412023900.png]]
子组件：
![[Pasted image 20230412023823.png]]


# 3.兄弟传
[[4.兄弟组件之间的数据共享 Vue2.x]]
[[4.兄弟组件之间的数据共享 Vue3.x]]
new一个新的vue实例，用on和emit来对数据进行传输
![[Pasted image 20230412024100.png]]
![[Pasted image 20230412024119.png]]
![[Pasted image 20230412024137.png]]

4.vuex传值
