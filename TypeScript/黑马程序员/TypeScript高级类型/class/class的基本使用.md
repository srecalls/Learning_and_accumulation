作用：**不仅提供了class的语法功能，也作为一种类型存在**
添加了类型注解和其他语法（比如可见性修饰符），**也就是说ts的class比es2015的class多了一些语法**

```ts
class Person {
	age: number,
	gender: '男' // gender: string = '男'
	1. 声明成员age，类型为number（无初始值）
	2. 声明成员gender，并设置初始值，这时候ts类型推论为string
}
```
# class的基本使用
![[Pasted image 20230327160227.png]]
![[Pasted image 20230327160329.png]]
![[Pasted image 20230327160407.png]]