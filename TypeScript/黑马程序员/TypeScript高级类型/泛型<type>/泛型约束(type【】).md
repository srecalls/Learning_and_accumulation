# 泛型约束

**泛型约束：因为默认情况下，泛型函数的类型变量Type可以代表多个类型，这就导致无法访问任何属性**
```ts
fuction id<Type>(value: Type): Type {
	console.log(value.length)
	return value
}
因为Type可以表示任意类型，无法保证一定有lenght属性。
这时候就需要为泛型添加约束来收缩类型。

收缩主要有两种方法
1. 指定更加具体的类型
function id<Type>(value: Type[]): Type[] {
	console.log(value.length)
	return value
}
将类型修改为Type[] 也就是 Type类型的数组，因为数组就一定存在length属性，就可以访问了


2. 添加约束
interface Ilength { length: number }
function id<Type extends ILength>(value: Type): Type {
	console.log(value.length)
	return value
}
创建描述约束的接口Ilength，里面按要求提供length属性
然后extends来使用这个接口，添加泛型约束

这个约束就表明，传入的类型必须有length属性
```

![[Pasted image 20230328013855.png]]
1. 指定更加具体的类型
2. ![[Pasted image 20230328013951.png]]
![[Pasted image 20230328014045.png]]
2.添加约束
![[Pasted image 20230328021512.png]]
![[Pasted image 20230328021605.png]]