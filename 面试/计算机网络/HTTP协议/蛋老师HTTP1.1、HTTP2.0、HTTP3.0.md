
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-29.png]]
## HTTP1.1 1997
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-1.png]]
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0.png]]

## 链接
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-2.png]]
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-3.png]]
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-4.png]]


服务器会先发送HTML文件给我们，但其它文件不会发给我们，我们的浏览器在收到HTML文件以后，根据HTML里面的内容，再向服务器依次请求CSS，JS等文件，这个过程都是浏览器在帮我们完成，所以用户的直接感受是只有一次请求，如果请求队伍里，有一个文件没有收到。后面的文件也没法收到了，这就导致了HTTP的队头阻塞

一个一个太慢了，太多了又会被DDos，每个浏览器的允许的持久链接数不太相同

![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-5.png]]

![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-6.png]]
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-7.png]]
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-8.png]]

了解决这个问题，其实HTTP/1.1里有个叫管线化的技术
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-9.png]]
虽然可以一次发送多份，但是响应的时候必须按照发送的顺序接收


![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-10.png]]
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-11.png]]
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-12.png]]

所以我们比较难能看到有浏览器实际会用管线化这个技术，
因此用到了精灵图（雪碧图）
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-13.png]]


![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-14.png]]

![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-15.png]]

多个请求数
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-16.png]]
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-17.png]]


## HTTP2.0。2015
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-18.png]]
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-19.png]]

![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-20.png]]
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-21.png]]

![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-22.png]]

头部压缩
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-23.png]]

HPACK
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-24.png]]

HPACK算法要求浏览器和服务器都保存一张静态只读的表
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-25.png]]

比方说经典的"HTTP/1.1 200 0K"起始行
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-26.png]]
从肉眼看只是少了3个字节

但因为是重复的首部
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-27.png]]

![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-28.png]]

可以作为动态信息加入动态表里


## HTTP3.0 2019
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-31.png]]
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-32.png]]
![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-30.png]]。


![[蛋老师HTTP1.1、HTTP2.0、HTTP3.0-33.png]]