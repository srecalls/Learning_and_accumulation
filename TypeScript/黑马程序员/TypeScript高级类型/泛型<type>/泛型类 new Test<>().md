# 泛型类
```ts
class GenericNumber<NumType> {
	defalutValue: NumType
	add: (num1: numType, num2: numType) => numType
	add1(num1: numType, num2: numType) {}
}
const myNum = new GernericNumber<number>()
类似于泛型接口，在class名称后添加<类型变量>，这个类就成了泛型类

const myNum = new GernericNumber(10)
此时也可以省略变量类型不写
```
![[Pasted image 20230328025440.png]]



![[Pasted image 20230328025631.png]]
![[Pasted image 20230328025954.png]]
![[Pasted image 20230328025856.png]]