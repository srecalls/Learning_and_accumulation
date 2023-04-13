网页中常见一些三角形，使用CSS直接画出来就可以，不必做成图片或者字体图标一张图，你就知道CSS三角是怎么来的了,做法如下:
![[Pasted image 20220916170631.png]]

```css
div {
			width : 0;height: 0;
			line-height : 0;font-size: 0;
			border: 50px solid transparent;border-left-color: pink;
		}
```