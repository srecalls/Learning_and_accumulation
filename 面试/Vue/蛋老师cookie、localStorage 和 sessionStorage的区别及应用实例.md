服务器在收到请求以后会在HTTP响应里添加头部Set-Cookie并且在Set-Cookie里进行标识在下一次请求的时候浏览器就会在HTTP请求里添加头部Cookie并且用上Set-Cookie里的标识这样服务器就可以给不同用户匹配不同的内容了

给了Set-Cookie之后以后每一次HTTP请求都要把Cookie数据传送给服务器
![[Pasted image 20230524055243.png]]
![[Pasted image 20230524055410.png]]




当用户第一次请求服务器的时候，服务器响应内容，并且附加可操控网页的JS，当用户操作JS进行个人设置的时候，这些个人设置就可以通过Web存储机制保存在浏览器里了

![[Pasted image 20230524060101.png]]