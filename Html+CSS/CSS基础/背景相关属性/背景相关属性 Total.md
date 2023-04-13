
# 背景相关属性 Total
属性 | 作用 | 值 
:-: | :-: | :-:  
[[背景颜色 background-color\|background-color]] | 背景颜色|预定义的颜色值/十六进制/RGB代码
[[背景图片 background-image\|background-image]] | 背景图片 | url(图片路径)
[[背景平铺 background-repeat\|background-repeat]] | 是否平铺 | repeat/no-repeat/repeat-x/repeat-y
[[背景位置 background-position\|background-position]] | 背景位置|length/position 分别是x和y坐标
 background-attachment| 背景附着 | scroll（背景滚动) / fixed （背景固定）
[[背景相关属性的连写形式 background\|背景简写]] | 书写更简单 | 背景颜色/背景图片地址/背景平铺/背景滚动/背景位置
背景色半透明 | 背景颜色半透明 | background:rgba(0,0,0,0.3)；后面必须是四个值最后一个可以略写 0.3 ---->  .3

#### img标签和背景图片的区别

#### ➢ 需求：
**需要在网页中展示一张图片的效果？** 
#### ➢ 方法一：
**直接写上img标签即可 • img标签是一个标签，不设置宽高默认会以原尺寸显示** 
#### ➢ 方法二：
**div标签 + 背景图片 • 需要设置div的宽高，因为背景图片只是装饰的CSS样式，不能撑开div标签**
