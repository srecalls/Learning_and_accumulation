**两种写法**
```js
let numbers: number[] = [1,2, 3] // 写法1
let numbers: Array<number> = [1, 2, 3] // 写法2
``` 
**数组内如果有多种类型（联合类型）**
```ts
let arr: (number | string)[] = [1, 'a', 3, 'b']
```
## 数组类型 number\[\]  Array\<string\>
![[Pasted image 20230326235055.png]]
![[Pasted image 20230326235514.png]]