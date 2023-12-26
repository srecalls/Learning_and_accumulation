# 索引签名类型
场景：**无法确定对象中有哪些属性（或者对象中可以出现任意多个属性）**

```ts
interface AnyObject { // 针对对象
	[key: string]: number // [key: string]表示只要是string类型的属性名称，都可以出现在对象里，不是一个就对应一个
	// 注意这里key就是个占位符，可以更换名称的
}

interface MyArray<T> { // 针对数组
	[n: number]: T // 数组使用[n: number]来作为索引签名类型
}
// 表示只要是number类型的键（索引）都可以出现在数组中。
let arr: MyArray<number> = [1, 3, 5]
数组是一类特殊的对象，特殊在数组的键（索引）是数值类型

```

![[Pasted image 20230328031844.png]]
![[Pasted image 20230328032622.png]]
n:number 表示索引是数字
![[Pasted image 20230328032752.png]]
![[Pasted image 20230328032835.png]]
![[Pasted image 20230328033018.png]]
