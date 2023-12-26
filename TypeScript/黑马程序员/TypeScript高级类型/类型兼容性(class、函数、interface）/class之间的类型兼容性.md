# 对象之间的类型兼容性
作用：对于对象类型来说，y的成员至少于x相同，则x兼容y（成员多的可以复制给少的）
```ts
class Point { x: number;, y: number }
class Point3D { x: number; y: number; z: number }
const p: Point = new Point3D() // 因为point3D的成员“相同”大于等于Point的成员
所以成员多的Point3D可以兼容成员少的Point
```

![[Pasted image 20230327164641.png]]


![[Pasted image 20230327164732.png]]