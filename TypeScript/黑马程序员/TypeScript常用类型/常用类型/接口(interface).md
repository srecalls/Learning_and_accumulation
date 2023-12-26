# 接口 interface

作用：**当一个对象类型被多次使用**，就会使用接口来描述对象类型来达到**复用**效果

```ts
// 接口结尾用逗号，分号；不写都行
interface GalleryData {
	avatar: string,
	imgUrl: string;
	username: string
	sayHi(): void
}
let gallery: Gallery {
	avatar: '1',
	imgUrl: '1'
	username: '1',
	sayHi() {}
}
```


**区别**
```ts
interface和typ的区别
同：
1. 都能给对象指定类型
不同
1. 接口interface只能给对象指定类型
2. 别名type，不仅可以为对象指定类型，还可以为任意类型指定别名
interface IPerson {
	name: string,
	age: number,
	sayHi(): void
}

type IPerson {
	name: string,
	age: number,
	sayHi(): void
}
type NumStr = number | string
```
![[Pasted image 20230327012026.png]]
![[Pasted image 20230327012118.png]]

# 接口和类型别名的对比
![[Pasted image 20230327012213.png]]
