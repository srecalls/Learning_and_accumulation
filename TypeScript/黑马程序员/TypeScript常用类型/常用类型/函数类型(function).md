

## 函数类型
**作用: 1. 单独指定参数、返回值的类型**
```ts
function add(number1: number, number2: number): number {
	return number1 + number2
}
const add = (number1: number, number2: number): number => {
	return number1 + number2
}
```
**2.同时指定参数、返回值类型（只适用于函数表达式）**
```ts
const add = (number1: number, number2: number) => number = (num1, num2) => {
	return num1 + num2
}
```

1.单独指定参数、返回值的类型
![[Pasted image 20230327000211.png]]
![[Pasted image 20230327000619.png]]

2. 同时指定参数、返回值的类型
![[Pasted image 20230327001405.png]]
![[Pasted image 20230327001802.png]]