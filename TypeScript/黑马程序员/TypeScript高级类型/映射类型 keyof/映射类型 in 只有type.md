# 映射类型 
作用： **基于旧类型创建新类型（对象类型），减少重复，提升开发效率。**
```ts
type Props = { a: number; b: string; c: boolean }
keyof Props // 'a' | 'b' | 'c'
```

```ts
type PropKeys = 'x' | 'y' | 'z'
type Type1 = { x: number; y: number; z: number }
// 相当于x/y/z重复了两遍。
可以利用映射类型简化
type Type2 = { [key in PropKeys]: number }
映射类型基于索引签名类型，所以语法也类似于，使用[]

映射类型除了根据联合类型创建新类型外，还可以根据"对象类型"来创建
type Props = { a: number; b: string; c: boolean }
type Type3 = { [key in keyof Props]: number }
先执行keyof Props获取对象类型Props中所有键的联合类型'x' | 'y' | 'z'
然后key in 表示Key可以是Props中所有键名中的任何一个
相当于
type Type3  {
	a: number,
	b: number,
	c: number
}
注意： 类型映射只能在类型别名（type）中使用，不能在接口interface中使用
```

![[Pasted image 20230328033339.png]]


![[Pasted image 20230328033439.png]]
![[Pasted image 20230328033537.png]]
![[Pasted image 20230328033833.png]]