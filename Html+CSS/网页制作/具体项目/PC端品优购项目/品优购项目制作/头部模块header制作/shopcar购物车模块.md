# shopcar购物车模块
#### 内容
![[Pasted image 20220928152311.png]]
让文字居中 
line-height等于盒子的height
再加上text-align：center；
![[Pasted image 20220928152802.png]]

前后的符号利用伪元素::after和::before
![[Pasted image 20220928153107.png]]
字体声明直接在icommon文件夹里style.css搜索复制
![[Pasted image 20220928153728.png]]
![[Pasted image 20220928153652.png]]
右上角的小图标利用子绝父绝进行定位，里面的气泡利用border-radius进行修改
● count统计部分要用绝对定位做
● <font color=red>count统计部分不要给宽度</font>，因为可能买的件数比较多，让件数撑开就好了，给一个高度
● 左右用padding撑开
![[Pasted image 20220928155153.png]]
![[Pasted image 20220928155139.png]]
● 一定注意左下角不是圆角，其余三个是圆角，写法：border-radius：7px 7px 7px 0；
●注意position 
right是右对齐，为了符合书写习惯，注意改成左对齐
![[Pasted image 20220928155312.png]]