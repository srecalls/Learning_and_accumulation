# 泛型接口
**作用：接口也可以配合泛型来使用，增加其灵活性，增强其复用性**
```ts
在接口名称后面添加<类型变量>，接口就成了泛型接口
interface IdFunc<Type> {
	id: (value: Type) => Type
	ids: () => Type[]
}

let obj: IdFunc<number> = {
	id(value) { return value }
	ids() { return [1,3,4 ]}
}
此处使用泛型接口的时候就需要显式的去指定具体的类型了
```
![[Pasted image 20230328023136.png]]
![[Pasted image 20230328023246.png]]
![[Pasted image 20230328023358.png]]

# 数组是泛型接口
![[Pasted image 20230328023523.png]]
![[Pasted image 20230328025245.png]]
![[Pasted image 20230328025232.png]]