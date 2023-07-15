### 1. 说一下BFC

 BFC就是块级元素格式化上下文，相当于一个容器，里面的布局不会影响到外面的元素。

 可以用来解决的问题：

1. 垂直方向的margin重叠（两种情况，情况一：父子，给父触发BFC；情况二：兄弟：给其中一个包上个BFC)。
2. 清除浮动。
3. 两列布局（两个元素，第一个为float，则两个元素会重叠，给第二个元素触发BFC，消除重叠）

 创建或触发BFC：

1. html就是BFC;
2. float不为none时；
3. position为absolute或者fixed;
4. display值为flex、inline-flex、inline-block、table-cell、table-caption；
5. overflow为hidden或者auto。

### 2. 为什么要清除浮动？如何清除浮动？

为什么要清除浮动：

1. 父元素高度无法被撑开；
2. 浮动元素与非浮动元素重叠在一块；

如何清除浮动:

1. 父级设置为BFC；

2. 父级设置高度；

3. 在最后面添加空标签，并设置css样式：{clear: both}；

4. 使用伪元素

   ```css
   .xx::after{
   	content: '';
       display: block;
       clear: both;
   }
   ```

### 3.盒模型

通过box-sizing属性切换，content-box为标准模式，border-box为怪异模式。

1. 标准模式：width和height包含content，不包括border和padding；
2. 怪异模式：width和height包含content、border和padding。

### 4. link和@import

1. link是html标签引入，import是css引入；
2. link在页面加载时被加载，import在页面加载完毕后再加载；
3. link的样式权重大于import；
4. 通过js操作DOM时，可以使用link来改变页面样式，无法使用@import；
5. import存在兼容性问题。

建议使用link的方式引入css。

### 5. href和src

href：加载时不会暂停对其他资源的下载或行为，常用在a、link；

src：加载时暂停对其他资源的下载，直到当前资源加载、执行，并且把当前资源替换到src引用处，常用在img、iframe、script。

### 6. alt和title的作用及区别

title是大多数标签都有的，alt图片特有的，在图片不能正常显示时，alt优先级大于title。

鼠标滑动到元素上的时候显示。

共同点是都有利于SEO。

### 7. >>>、/deep/、:deep()、::v-deep

样式穿透，在scoped中使用可以影响子组件。

'>>>'只作用于CSS，/deep/和::v-deep被弃用了，现在用:deep()。

### 8. 几种隐藏的区别

visibility: hidden：隐藏元素，会继续在文档流中占位，隐藏后不能触发点击事件，会触发重绘，修改子元素可以让子元素显示出来；

opacity: 0：透明，会继续在文档流中占位，隐藏后能触发点击事件，会触发重绘，修改子元素可以让子元素显示出来；

rgba:  透明，会继续在文档流中占位，隐藏后能触发点击事件，会触发重绘，子元素不会继承透明效果；

display: none：隐藏元素，不会在文档流中占位，隐藏后不能触发点击事件，会触发重排重绘，修改子元素不可以让子元素显示出来；

position: absolute：通过绝对定位将元素移出可视区。

### 9. 精灵图

将多张图片合成到一张大图中，通过background-image、background-repeat、background-position进行背景定位。

优点：减少网页的http请求，提高页面性能，减少图片字节，四张图片合成一张图片，一张图片的字节数总小于四张图片的总合。

缺点：需要用到测量工具测量其准确位置，页面背景改动的时候需要改图片和CSS，比较麻烦。

### 10. 伪类和伪元素

区别：伪类是添加样式，伪元素是伪造一个不存在DOM文档树中的元素。伪类用:，伪元素之前用:，CSS3之后用::。伪类可以叠加、伪元素只能出现一次。

伪类：

1. link：设置a标签在未访问前的样式；
2. visited：设置a标签在被访问后的样式；
3. hover：设置鼠标经过时的样式；
4. active：设置元素被鼠标点击到释放之间的样式；
5. focus：设置元素在成为输入焦点时的样式；
6. nth-child(n)：设置第n个子元素的样式。（n是从1开始的）

伪元素：

1. first-letter：设置文本首字母的样式；
2. first-line：设置文本首行样式；
3. before：在元素之前插入某些内容；
4. after：在元素之后插入某些内容。

### 11. 权重和优先级

内联：1000；

id： 100；

类、伪类、属性选择器：10；

元素选择器、伪元素：1；

通配符、继承：0。

优先级：!important最大优先级，权重相同后面的生效。

### 12. 当一个元素被设置为浮动或绝对定位后，它的display值变为什么呢？

block。

### 13. px、em、rem、vw、vh

px：固定的像素，一旦设置了就无法因为适应页面大小而改变；

em：相对于父元素的字体大小倍数；

rem：相对于html的字体大小倍数；

vw：1vw相当于视口宽度的百分之一；

vh：1vh相当于视口高度的百分之一；

rpx：微信小程序特有的，不管你屏幕大小是多少，就规定为750rpx，会自己去适应。

### 14. position有哪些值

static：默认值，top、left等无效。

relative：不脱离文档流。

absolute：脱离文档流，参照物是往上找一个relative/absolute/fixed的元素，如果没有就相对于浏览器窗口进行定位。

fixed：脱离文档流，参照物是屏幕视口。

inherit：继承。

### 15. 溢出文字省略号效果

```css
//单行
.box{
    white-space: nowrap;//强制文本不换行
	overflow: hidden;
    text-overflow: ellipsis;
}
//多行
.box{
	display: -webkit-box;//设置为弹性伸缩盒子
    -webkit-box-orient: vertical;//使文本纵向排列，就是从左到右，再从上到下
    -webkit-line-clamp: 2;//设置行数
    overflow: hidden;
    text-overflow: ellipsis;
}
```



### 16. 行内元素有哪些？块级元素有哪些？区别是什么？

行内元素有：a b span img input select strong

块级元素有：div ul ol li dl dt dd h1 h2...h6 p

行内元素不独占一行，不可以设置宽高，可以设置padding，margin的left和right；块级元素独占一行，可以设置宽高。

### 17. display:inline-block 产生间隙

原因：换行和空格会占据一定的位置使之产生间隙

解决方法：

1. 写在同一行；
2. 使用margin负值；
3. 设置font-size:0；
4. 父元素设置letter-spacing或word-spacing为负的字体的一半；
5. 设置为float。

### 18. 如何实现小于12px的字体效果

使用`transform: scale(0.7)`，但是这个属性只能设置于可以定义宽高的元素，如果想设置行内元素需要先把该行内元素设置为display:inline-block。

### 19.如何画一条0.5px的线

使用二维`transform: scale(0.5,0.5)`

### 20. HTML语义化的理解

语义化就是选择合适的标签，不要只使用div。

1. 能和搜素引擎建立良好的沟通，爬虫更容易抓取有效信息，有利于SEO；
2. 语义化更好的支持读屏软件，方便其它设备解析；
3. 便于团队开发和维护，代码更具有可读性。

常见的语义化标签：<header>头部、<nav>导航栏、<section>区块、<main>主要区域、<article>主要内容、<aside>侧边栏、<footer>底部

### 21. 如何实现元素水平垂直居中

块级元素：

1. 已知父子元素的宽高，父元素相对定位，子元素绝对定位，子元素的top、bottom、left、right设置为0，margin设置为auto；

   ```css
   .parent{
       position: relative;
       width: 200px;
       height: 200px;
   }
   .child{
       position: absolute;
       width: 100px;
       height: 100px;
       top: 0;
       bottom: 0;
       left: 0;
       right: 0;
       margin: auto;
   }
   ```

2. 已知子元素的宽高

   ```css
   .parent{
       position: relative;
       width: 200px;
       height: 200px;
   }
   .child{
       position: absolute;
       width: 100px;
       height: 100px;
       top: 50%;
       left: 50%;
       margin-top: -50px;
       margin-left: -50px;
   }
   ```

3. 未知元素的宽高

   ```csss
   .parent{
   	position: relative;
       width: 200px;
       height: 200px;
   }
   .child{
   	position: absolute;
   	top: 50%;
   	left: 50%;
   	transform: translate(-50%,-50%);
   }
   ```

4. flex

   ```css
   .parent{
   	display: flex;
       align-items: center;
       justify-content: center;
   }
   ```

行内元素：

```css
.parent{
    height: 20px;
    line-height: 20px;
    text-align: center;
}
```

### 22. 实现一个扇形

```css
.box{
	width: 0;
    height: 0;
    border: 100px solid transparent;
    border-radius: 100px;
    border-top-color: red;
}
```

### 23. 实现三栏布局，左右固定，中间自适应

1. 浮动+margin：左浮动，右浮动，中间设置margin

   ```html
   <div class="left"></div>
   <div class="right"></div>
   <div class="content"></div>
   ```

   ```css
   .left,
   .right{
   	width: 300px;
       height: 100px;
       background-color: skyblue;
   }
   .left{
       float: left;
   }
   .right{
       float: right;
   }
   .content{
       margin: 0 300px;
       height: 100px;
       background-color: aqua;
   }
   ```

2. 圣杯布局（使用margin负值)

   ```html
   <div class="main">
   	<div class="content"></div>
   </div>
   <div class="left"></div>
   <div class="right"></div>
   ```

   ```css
   .main{
       float: left;
   	width: 100%;
       height: 100px;
   }
   .content{
       margin: 0 300px;
       height: 100px;
       background: blue;
   }
   .left,.right{
       float: left;
       width: 300px;
       height: 100px;
       background: red;
   }
   .left{
   	margin-left: 100%;
   }
   .rigth{
       margin-right: -300px;
   }
   ```

3. flex

   ```html
   <div class="main">
   	<div class="left"></div>
   	<div class="content"></div>
   	<div class="right"></div>
   </div>
   ```

   ```css
   .main{
       display: flex;
   	height: 100px;
   }
   .left,.right{
       width: 300px;
   	height: 100px;
       background-color: red;
   }
   .content{
       flex: 1;
       height:100px
       background-color: blue;
   }
   ```


### 24. CSS3的新特性

1. border-radius 圆角效果

   ```css
   border-radius: 1px 1px 1px 1px; //左上开始顺时针
   ```

2. box-shadow 边框阴影

   ```css
   box-shadow: 1px 1px 1px 1px skyblue; //x偏移量 y偏移量 模糊 阴影扩展 颜色 不设置阴影向外，设置为inset阴影向内
   ```

3. background 背景

   ```css
   background-image:url(''); //背景图片
   background-clip:border-box/padding-box/content-box; //背景裁剪到边框/内边距/内容，默认为边框
   background-origin:border-box/padding-box/content-box; //设置起始位置，相对于边框/内边距/内容，默认为边框
   background-repeat:repeat/no-repeat/repeat-x/repeat-y;
   background-size:number/%/cover/contain; //cover和contain都是维持原宽高比，cover是一定要填满，contain是先到哪一边就停
   ```

4. background: liner-gradient/radial-gradient; //线性渐变、径向渐变

   ```css
   background:liner-gradinet(to top,blue,red);//从下到上蓝变红
   //最近边、最近角、最远边、最远角
   background:radial-gradient(closest-side/closest-corner/farthest-side/farthest-corner,circle/ellipse,blue,red)
   ```

5. transition 过渡

   ```css
   transition-porperty: all/width; //所有或者某一属性值
   transition-duratino: 1s; //过渡的时间
   transition-timing-funciton: linear; //过渡效果
   transition-delay: 2s; //延迟时间
   ```

6. transform 

   ```css
   transform: translate(1px,1px); //位移
   transform: rotate(xxdeg); //旋转
   transform: scale(0.5,0.5); //缩放
   transform: skew(10deg); //倾斜
   ```

7. animation

8. 选择器

   属性选择器、伪类选择器：nth-child()、nth-of-type()、伪元素选择器：::before、::after。

9. flex
