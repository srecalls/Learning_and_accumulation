
**作用：为任意类型起别名，简化改类型的使用**

```ts
type CustomArray = (number | string)[]
let arr1: CustomArray = [1, 'a', 3, 'b']
let arr2: CustomArray = ['x', 'y', 6, 7]
```

![[Pasted image 20230327002910.png]]
![[Pasted image 20230326235932.png]]