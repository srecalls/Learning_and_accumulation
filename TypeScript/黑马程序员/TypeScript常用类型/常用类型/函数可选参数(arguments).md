**注意: 可选参数只能出现在参数列表的最后，也就是说可选参数后面不能再出现必选参数**
# 函数可选参数 ？
```ts
function mySlice(start?: number, end?: number): void {
	console.log('起始索引: ', start, '结束索引: ': end)
	mySlice()
	mySlice(1)
	mySlice(1, 3)
}
```
![[Pasted image 20230327005336.png]]
![[Pasted image 20230327003115.png]]