基于Snort配置IDS系统

1. 基于Windows或Linux系统安装Snort并进行配置；

2. 配置规则实现对目标端口为小于1023方案设置告警；

进阶作业（选做）：

3. 配置规则实现域名中包含game的网址的方案设置告警；

3. 配置规则实现对使用root用户尝试访问ftp（21端口）进行告警。

提示：可以用nmap、wireshark等工具产生扫描特定主机的数据包。

参考文档

[1] http://www.kaiyuanba.cn/content/network/snort/Snortman.htm

[2] https://www.jianshu.com/p/c6cc43facd20


## 1. 基于Windows或Linux系统安装Snort并进行配置；
此处参考参考文档\[2]进行操作

### 环境

环境如下：

- windows 10
- Snort 2.9.17
- npcap 1.20

### 软件下载及安装

#### 1.npcap

![[Pasted image 20230619054717.png]]
![[Pasted image 20230619054757.png]]

#### Snort
![[Pasted image 20230619054950.png]]

![[Pasted image 20230619055037.png]]
![[Pasted image 20230619055050.png]]

验证下载完成
![[Pasted image 20230619055540.png]]

#### Snort规则下载
需要登录
![[Pasted image 20230619055358.png]]

解压到安装目录下的 `rules`文件夹中：

![[Pasted image 20230619055912.png]]

### Snort配置

#### 规则配置
##### 规则配置1
使用记事本或编辑器打开安装目录下`/etc/snort.conf`文件，更改以下位置的配置代码（其中的路径改为自己的安装目录）：
![[Pasted image 20230619060112.png]]
![[Pasted image 20230619060401.png]]

##### 规则配置2
![[Pasted image 20230619060726.png]]

##### 规则配置3
![[Pasted image 20230619060842.png]]

##### 规则配置4
![[Pasted image 20230619060924.png]]


### Snort运行
打开cmd，进入到安装目录下的`bin`目录中，执行命令
```shell
snort -dev -l D:\Snort\log -h 192.168.1.0/24 -c D:\Snort\etc\snort.conf
```

![[Pasted image 20230619062347.png]]


### 2. 配置规则实现对目标端口为小于1023方案设置告警；
打开Snort安装目录下的etc文件夹，复制snort.conf文件并将其重命名为snort-local.conf（或者其他名字）
![[Pasted image 20230619062520.png]]

然后，打开这个新的配置文件，在其中添加以下配置：
![[Pasted image 20230619062724.png]]

在这个配置文件中，我们定义了网络接口，开启了警告模式，并添加了两个规则来监控目标端口小于1023的TCP和UDP流量，并在命中时输出警告消息。
在命令行中输入以下命令来启动Snort：
```js
snort -c D:\Snort\etc\snort-local.conf
```

Snort将开始捕获流量，并根据你的配置文件检测潜在的攻击行为。如果检测到违规行为，将在命令行中输出警告消息。



## 结论

基于Snort配置IDS系统可以提供以下几方面的用途：

1. 检测网络攻击：IDS系统可以监控网络流量，检测和报告各种网络攻击，如拒绝服务攻击、漏洞利用、恶意软件等。通过配置Snort规则，可以根据攻击特征或行为模式来识别和阻止攻击。
    
2. 提高网络安全性：IDS系统可以及时识别和响应网络攻击，防止攻击者进一步侵入或泄露敏感信息。通过实时监控网络活动，IDS系统还可以发现并修复网络安全漏洞，提高网络的整体安全性。
    
3. 减少安全风险：IDS系统可以提供实时的安全事件报告和警报，使网络管理员能够及时采取行动，减少安全风险和数据泄露的可能性。
    
4. 遵守法律法规：IDS系统可以帮助企业或机构遵守法律法规，如HIPAA、PCI、SOX等。通过实时监控和报告网络活动，IDS系统可以保证网络安全合规性，并提供必要的审计和报告。