**作用：可以表示一组明确的可选值。定义一组命名常量。他描述一个值，值可以是这些命名常量种的一个。**
**定义好枚举后，可以用枚举做类型注解**
枚举是TS 为数不多的非JavaScript类型级扩展(不仅仅是类型)的特性之一因为:其他类型仅仅被当做类型，而**枚举不仅用作类型，还提供值** (枚举成员都是有值的)也就是说，其他的类型会在编译为J5代码时自动移除。但是，**枚举类型会被编译为JS 代码**!
```ts
enum Direction {
	Up,
	Down,
	Left,
	Right
}
// 形参direction类型为枚举Direction, 实参的值就是枚举Direction中的任意一个
function changeDirection(direction: Direction): void {
	console.log(direction)
}
changeDirection(Direction.Up) // 访问枚举内成员通过(.)点语法访问枚举内成员
```

```ts
// 形参类型是有值的。默认从0开始自增的数值,这种称为数字枚举
enum Direction {
	Up = 10,
	Down, // 11
	Left, // 12
	Right // 13
}
// 也可以给枚举中成员初始值
enum Direction {
	Up = 2,
	Down = 4,
	Left = 9,
	Right: 10
}
```

```ts
// 枚举成员的值可以是字符串, 字符串枚举没有自增长行为，字符串枚举每个成员必须有初始值
enum Direction {
	Up = 'UP',
	Down = 'DOWN',
	Left = 'LEFT',
	Right = 'RIGHT
}
```


# 枚举类型 enum
![[Pasted image 20230327015727.png]]

# 访问枚举成员 .
![[Pasted image 20230327015848.png]]
![[Pasted image 20230327015901.png]]

# 枚举成员的值及数字枚举
![[Pasted image 20230327020046.png]]

![[Pasted image 20230327020214.png]]

# 字符串枚举
![[Pasted image 20230327020406.png]]
![[Pasted image 20230327020354.png]]

# 枚举的特点及原理
![[Pasted image 20230327020607.png]]
自调用函数，如果Direction为空则传入后面为空的参数，然后为Direction赋值