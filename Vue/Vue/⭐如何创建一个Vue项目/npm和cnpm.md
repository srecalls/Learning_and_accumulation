# 1、 npm 和 cnpm 的区别
（1） 两者之间只是 [node](https://so.csdn.net/so/search?q=node&spm=1001.2101.3001.7020) 中包管理器的不同。  
（2） npm是node官方的包管理器。cnpm是个中国版的npm，是淘宝定制的 cnpm (gzip 压缩支持) 命令行工具代替默认的 npm。  
（3）如果因为网络原因无法使用npm下载，那cnpm这个就派上用场了。

一定切记切记，npm和cnpm只是下载的地址不同，npm是从国外下载东西，cnpm是从国内下载东西。
![[Pasted image 20230326154041.png]]

# 2.nrm 的使用
`npm install -g cnpm --registry=https://registry.npm.taobao.org
`
![[Pasted image 20230326154133.png]]
![[Pasted image 20230326154144.png]]
# 3.npm介绍
![[Pasted image 20230326154201.png]]

##### 安装 -D 和-S的区别  
小Tips: npm 安装 -D 和-S的区别  
1、-D 是在开发环境中协助开发需要使用的

2、-S是生产环境打包时需要的

3、在package.json中 -D在devDependencies对象中，-S在dependencies对象中
https://blog.csdn.net/qq_42909053/article/details/108053431