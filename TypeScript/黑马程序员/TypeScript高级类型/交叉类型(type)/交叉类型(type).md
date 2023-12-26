**作用：功能类似于接口继承（extends），用于组合多个类型为一个类型（常用与对象类型）**
注意： 常用于对象类型, 且作目的是组合多类型为一个类型

```ts
interface Person { name: string }
interface Contact { phone: string }
type PersonDetail = Person & Contact // 相当于type PersonDetail = { name: string; phone: string }
let obj: PersonDetail = {
	name: 'jack',
	phone: '123....'
}
```
# 交叉类型
![[Pasted image 20230328011808.png]]
extends展示
![[Pasted image 20230328011942.png]]
实例
![[Pasted image 20230328012020.png]]
![[Pasted image 20230328012102.png]]

