[![头像](https://uploadfiles.nowcoder.com/images/20230303/125033699_1677805970971/9D3B0FFE1D00F6BEB6769CBB10802AFD?x-oss-process=image%2Fresize%2Cw_72%2Ch_72%2Cm_mfit)](https://www.nowcoder.com/users/125033699)

[每日一摆](https://www.nowcoder.com/users/125033699)[![](https://static.nowcoder.com/fe/file/site/www-web/prod/1.0.344/imageAssets/88032122636d38847d40.png)](https://www.nowcoder.com/users/125033699)

2023-10-19 17:54字节跳动_前端开发工程师(准入职员工)![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAC5ElEQVR4AayWg5YrWxCG5wXuO9ynuLbvsW3btm3btk80tj1xTiYa2/xPatVK6nSPkbX+1Tu1u/+vq7Y6pDc/lJi+gktzG9ZHVci71UaiNsWoL2QwfnAZ9sN4rxnZV9GpqM9j2N9/gDdyBKxPS4OGlkdAcSJQbfbLAhTFU0yAdK83bETvARXxX8PxOgM519vJwF8moDAWqHcBdfkkavuVT6I+uodgoGfoWfLoHpKvPUL157e8Brh1QI0dYk5SgUi1NsCtpWcYSB5uzeEuIB+eBMtgfwlU5EoWbExtAamBDS6gMhewv5By+j2VEJ9+bLBUnnCgjgxEPWbUoLoWREkp/d4Csr208BtolabUTr8A3PmZ9WG+CuACXFruy7kJjjsZ6NIEqmMRkPEuT9/y7I5ZRG4Bbn4roowFRuPB8SdDCSCqNhII5B0Ecdmusbm6TO9mKUGGVVIiUsIBjj/+X5ERiTzJW0CBWSYAGYuH/4oRXW99D5Qky5jol3H87QwBCAjk3RGknmVVJskk4xLw6D9ux+6SrJ6P5VjEJopBMnJ2B1JMXxoPATk/AOnnuH33F6AqF6j7BNz+kWOpp9mcII09ZSQQlvGegMozgWoTcP8P/p9yEihJkn7rU0jZnL3KSJR0FJzBbzImiYcpRmNH5gIqjBVAz6Vzyfqgq2E1m7yeLPWvzOZ1Q/GXE8Cg74A6qwAaOwfJ9Fav9leT2ChsjXL1x+yguOjpcIEITDW9ZcHyGFA2bCpTO/kYxUSlScCtHwSkWUjmAiBVZHayYO28BcGlUWaUeJDLZH4ksYAiNsjWFLdXyhWQ62NgCzJ3vqnShigrX7U2pDwylaVULCfgC1Nsqt0cEy9onYh5p3J2VFUO4JBjAm45JpQwt/YIjF8efFqg1tqJuSqLOqvy4DPKwde3o7woRgGTcjmpr+9HuQLoDevk4yQWqLH4ZfS3Ewb2cdIB6Pm8nW2EmlsgNYTMobABuY3oBiQACQEkk1uoNAwAAAAASUVORK5CYII=)

关注

# boss直聘一二面

牛客上没看到面boss直聘的面经，更新一下记得的点  
  
一面  
1.说说你对变量提升的理解？以及一道变量提升的输出题  
2.jsBridge的原理  
3.如果让你写一个埋点监控方案你会怎么设计  
4.首屏加载速度优化  
5.输入url后浏览器的工作流程  
6.浏览器缓存  
7.http1/1.1/2/3的升级点  
8.tcp和udp的区别  
  
二面  
1.vue keep-alive原理  
[[17.对keep-alive的理解，它是如何实现的，具体缓存的是什么？]]
2.EventBus原理  
[[组件通信]]
3.flex布局场景题  

4.虚拟列表实现原理，intersectionObserver怎么用  

5.事件循环输出题  

6.一行代码写输出（a，b）之间的随机数  
```js
function abRandom(a, b) {
	return b * Math.random() + a
}

function abRandom2(a, b) {
	return Math.floor((b - a + 1) * Math.random() + a) // a, b + 1
}
```
[[Js取随机数的方法]]
7.如何跨页面通信？用localStorage安全吗，跟cookie之间有什么区别？  
[[前端跨页面通信，你知道哪些方法]]
[[7.如何实现浏览器内多个标签页之间的通信？]]
8.如果有一个一百万个li的滚动列表，如何优化？  

9.滚动组件上拉会有回弹，如何禁止这个事件  

10.虚拟DOM如何转换成真实DOM  

11.promise会产生闭包吗