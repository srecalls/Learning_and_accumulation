
**注意： 指定对象的多个属性类型时，使用;  （分号）来分割，而是，逗号**
```ts
let person: { name: string; age: number; sayHi(): void} = {
	name: 'jack',
	age: 10,
	sayHi(name) {}
}
```
**特点：在对象类型中，TS更加细化，每个具体的对象（数组Array、对象Object、函数（Function）都有自己的类型语法。**
# 对象类型
![[Pasted image 20230327011341.png]]
![[Pasted image 20230327011255.png]]
一行内不用加分号
![[Pasted image 20230327011429.png]]