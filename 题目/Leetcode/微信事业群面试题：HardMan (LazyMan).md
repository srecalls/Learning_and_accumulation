这道题是面试腾讯暑期实习生时，被WXG捞起来视频面时做的一道题，当时一脸懵逼，想了好一会，不过确实是不会做。主要是因为当时对类的使用以及Promise的掌握都还不够熟练，今天刚好想到这道题，于是翻出来好好地做了一下！
# 题目重述
```js
实现一个 HardMan:  
HardMan(“jack”) 输出:  
I am jack

HardMan(“jack”).rest(10).learn(“computer”) 输出  
I am jack  
//等待10秒  
Start learning after 10 seconds  
Learning computer

HardMan(“jack”).restFirst(5).learn(“chinese”) 输出  
//等待5秒  
Start learning after 5 seconds  
I am jack  
Learning chinese
```