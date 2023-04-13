# :after[[伪元素选择器|伪元素]]
#### 介绍
**:after方式是额外标签法的升级版。也是给父元素添加**
![[Pasted image 20220919154625.png]]

#### 代码：
```css
.clearfix::after {
			content: "";
			display: block;
			height: 0;
			clear: both;
			visibility: hidden;
		}
		
		.clearfix { /* IE6、7专有*/
			*zoom: 1;
		}

```


#### 优缺点：
**●优点:没有增加标签,结构更简单
●缺点: 照顾低版本浏览器
●代表网站:百度、淘宝网、网易等**




