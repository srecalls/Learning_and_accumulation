[  
illusion_me](https://www.nowcoder.com/users/209470135)[![](https://static.nowcoder.com/fe/file/site/www-web/prod/1.0.344/imageAssets/884461a539e786582202.png)](https://www.nowcoder.com/users/209470135)

05-11 16:01已编辑美团_核心本地商业_前端开发(实习员工)![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAADvUlEQVR4Aa2WA7A0RxDHY9tJIUYhtp1CzEJsuxibZcT5zGfbtm1bh91bz9fdt9vv9Pyu6n/Ymenf/bt7dvag1bxKhDg+TvNu36O6XNt98yYKv+M1HDtoM15xqvTjDmVB2yLPikjaCWNxuvTjugEphvQI/OsZJ+Bu34LI1BRRpBui2DBEBnyHawzcC3NxzaoB+cJ3XpTiadjmm7MwwHZ5TqSpsig3LFGum6QKY1HpmoxzCIZrYhR3A8ZYFpKgy79h/nHRVlCC4hXF4KAMARTYYoCjSlAZOExUPLiGgBgjUZd/jQiJVaUoJw37FZco0HR0YUMsULibygBVmSb8KU1EwVonToIuRQVBkgz5ya12qpIUKTA4fi4HABkEqYLv1SYIfqerEoEwZirEZtA+xdWFA3GKlyBlAYAPRrrEEWUJpOtbip3g7OLf+WlxZHmC+Hy8DyGkGhNSqXoJFg2xGbTTbt88XQ9L0yNdteKg0jjWNtesH0IyxBcAwOtnVqcDwLSFddUItAtiMwi7BQtZxl1lceGvai4MAt3bXmGnyiDY8/3NdP2M6jS/G1CtiTKpOTA2g5zigRNHXItTqlIp0OkQCD8PAcVLHgRRTe5sL6frVzQVkJPaADldGAaqCCl8rqqyk09Hu8VpVX7YMz31XPjz6rLp2sNd1eiCHS0HCnBigcD6wiyD/pybEB8Md9L3o8oT4U8oMNcQh5XF07X3htoZUGeBlgMRhGGG+HZykEHpigx7SxXHVSTT77eH2kSC7Obx36eH/RCWviKI9epAKwU5pjxJVNs1ebm/Ba9h7TA4g6K980Gg+mUcOQDuqvvaKynIZQ15XJNsVcZ9Q9cvqs+hz4NBFYbGTuotBIU74vamXY4gG3ZpQy4FeqCz0r8/7M34TG9dUMufU5OxCLHdNACM2zt0w5bqOgGq/Y64tV8fbLVb16TPZKjNoaXxDLqltQRBDECVGkr4ho2iWxDdrRHAe+TFgWZK089TQ07bsh7qquZb03N9jU66WEmqh0CxqquTQakBN1W4ISIk8L4VBqkLEAHo03Gjw6Eo8fmUAbFDjmwPHxPgEKxrnKoIgLCaoIsKQxUxAcdEou6JingmJcPBtyPg4EtWvdAgeoAbnWtBEHKArjWRoi4efBgjVff+uuJRHqu4+SjfAcd0liZHTBdCsjUJ53Cq4lQ+ylf3SocHjf0BDyd74UEkB4BV4KQSUpQH3/Eapxvm4ppVA8LTKf3ktH8kYfumwpx1A0IfIBPhYXGf6nJh/lH4PXkND5AHANpa/ejWVr67AAAAAElFTkSuQmCC)

关注

# 拼多多前端一二面（HR 面后挂）

一面  
补个一面面经，感觉面得稀烂，等了一周多没动静一度以为是挂了  
一来先是拿出之前笔试的一道题，让我看看为啥没得满分，看半天没看出来，原来是函数后面没加括号(吐槽下 pdd 的 txt 编辑器)，然后问项目和实习，讲完感觉面试官比较认可，然后问了下八股，然后又是两道算法题，第一道没撕出来，脑子抽了还用 forEach 遍历字符串，直接把面试官整笑了，说字符串没有 forEach 方法...，第二道题直接不让我写代码了，叫我说一下思路，感觉应该是说对了。  
总之面试官还是挺好的，出现低级错误的时候安慰说不要紧。  
  
二面 全程 45min  
前 20 分钟问项目，讲了十多分钟被打断了  
穿插问了一些项目首屏优化相关的问题  
然后开始写题：实现一个倒计时组件，防抖节流 ，最后一个是 promise 有关  
```js
<template>
	<div>
		<div>{{count}}</div>
		<button @click="countdown"></button>
	</div>
</template>
<script>
export default {
	name: 'CountDown',
	data() {
		count: 0
	},
	methods: {
		countdown() {
			this.count++
		}
	}

}
</script>
```
最后问了一下 webpack 有用过哪些插件  
  
反问：  
有几轮技术面(答：一般两轮，个别有三轮)  
  
许愿 hr 面![](https://uploadfiles.nowcoder.com/images/20220815/318889480_1660553876118/CAEB30813C5D910A6FBAAC41F8914E38)![](https://uploadfiles.nowcoder.com/images/20220815/318889480_1660553876118/CAEB30813C5D910A6FBAAC41F8914E38)  
  
----------4.23 更新  
今天收到HR 面通知了，但是约的时间是 5 月 6 号，还有比我更晚的吗![](https://uploadfiles.nowcoder.com/images/20220815/318889480_1660553763930/8B36D115CE5468E380708713273FEF43)![](https://uploadfiles.nowcoder.com/images/20220815/318889480_1660553763930/8B36D115CE5468E380708713273FEF43)  
  
---------5.11  
今天看了一眼应聘终止![](https://uploadfiles.nowcoder.com/images/20220815/318889480_1660553875690/B1C6F40D385519F732A9BE8EDD9E9C6C)...  
不是很理解（也说了接受加班，想转正留上海..）  
安心当团孝子了