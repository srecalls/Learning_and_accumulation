# CSS三角强化巧妙运用


![[Pasted image 20220918123629.png]]
#### 原理：
![[Pasted image 20220918123650.png]]
#### 代码：
```css
width: 0;
			height : 0;
			/*1.只保留右边的边框有颜色*/
			border-color: transparent red transparent transparent;
			/*2.样式都是solid*/
			border-style: solid;
			/*3.上边框宽度要大，右边框宽度稍小，其余的边框该为0*/
			border-width: 22px 8px 0 0;
```
