
**作用： 根据已有变量的值, 获取该值的类型，来简化书写**
**注意: typeof智能化用来查询变量或属性的类型，无法查询其他形式的类型(比如，函数调用的类型)**
```ts
console.log(typeof "Hello World") // string


let p = { x: 1, y: 2 }
function formatPoint(point: { x: number, y: number }): void{}
formatPoint(p)

function formatPont(point: typeof p): void{}
```

![[Pasted image 20230327021908.png]]

![[Pasted image 20230327022042.png]]

3.
![[Pasted image 20230327022144.png]]