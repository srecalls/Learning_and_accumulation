## Route
#### 路由选择原理
##### 路由信息来源
- 直连**C** **接口同网段** 接口配置I接口的物理层和数据链路层UP，通过接口感知到的直连网络
- 非直连 静态**S** 手动配置 | 动态 通过路由协议(OSPF EIGRP)学习
---
##### 选择原理
- **最长匹配原则** 逐位匹配长的的网段，最小的子网，最精确
- **管理距离**（Administrative distance）/ **度量值**（Metric）开销
	- ![[Pasted image 20230308115059.png]] `EIGRP汇总路由由管理员控制 null 0那一条`
	- `开销: 静态0 | 动态由协议控制`
- **递归查询** 目标-下一跳（目标）-下一跳…，查表查到直连（出接口）
- 匹配顺序：最长网段>AD>Metric ，都匹配负载均衡，不匹配丢弃
- 路由逐条途径都要由目标路由，路由和流量往返情况（路由学习方向和流量方向相反）

---
#### 静态路由
##### 静态路由汇总

使用CIDR简化路由表，增长掩码

但是如果三层交换机设置默认路由、路由器**汇总过头**将子网的发回给三层交换机。成环
![[Pasted image 20230308123347.png]]
配置静态路由，由于直连路由AD小，直连的不会被丢弃。路由器发回来的不合理数据丢弃

不如精确汇总

---
##### 静态路由配置
- 下一跳为IP，查看路由表转发
- 下一跳为端口，需要**APR代理**在广播域作用，路由器替自己能到达的IP地址回复

> 发送不基于端口，而基于MAC地址

---
##### 浮动静态路由
通过修改缺省的管理距离实现路由**冗余** 末尾添加AD值
``` purescript
Router(config)# ip route DESTINATION MASK NEXT_IP AD
``` 
不常用，不如叠加 

---
## OSPF-1
#### OSPF简介
（Open Shortest Path First，开放最短路径优先）
- 是一种**链路状态**路由协议，无路由循环（全局拓扑）。
- 公有协议。
- 每一台路由器拥有**整个拓扑结构**，能根据网络拓扑信息**独立**地作出决策。
- OSPF采用**SPF算法**计算达到目的地的最短路径：
	- 链路(LINK)= 路由器接口
	- 状态(State)= 描述接口以及其与邻居路由器之间的关系
- 管理性距离：110
- 组播地址：224.0.0.5, 224.0.0.6

![[Pasted image 20230308141534.png]]
链路状态：与该路由器端口相连的邻居路由器

而距离矢量路由协议只根据下一跳查询，通告的是路由表

---
#### OPSF三张表
##### 邻居表（neighbor table）
OSPF用邻居机制来发现和维持路由的存在，邻居表存储了双向通信的邻
居关系OSPF路由器列表的信息。
10s 一次hello报文，四次hello时间 没收到邻居死亡

---
##### 拓扑表（topology table）
OSPF用LSA（Link State Advertisement 链路状态通告）来描述网络拓
扑信息，然后OSPF路由器用拓扑数据库来存储网络的这些LSA。

---
##### OSPF路由表（routing table）
对链路状态数据库进行SPF（Dijkstra）计算，而得出的OSPF路由表。

---
#### OSPF的基本运行步骤
1. 建立邻接关系（Establish router adjacencies）
2. 必要的时候进行DR的选举（Elect the DR / BDR）
3. 发现路由（ Discover routes ）
4. 选择合适的路由器（Select appropriate routes）
5. 维护路由信息（Maintain routing information）

---
#### OSPF优化
##### Router-id优化
- 为了提高路由器稳定性，建议手动设置路由器的Router-ID
- 在OSPF进程下配置router-id <192.168.254.254> 一般也是telnet地址 **跨区域也不能重复**
- 项目中常用loopback做为Router-ID

---
##### 邻居优化（自动）
- 使用DR和BDR，DRohter只会与这DR和BDR建立全互联的邻接关系
- DRother保持Two-way状态
- 点对点链路没有DR/BDR

---
##### 链路数据库优化
分区域
- 中转区域（骨干区域 0）
- 常规区域（非骨干区域）
- 最大限度地减少路由表条目。限制本区域内拓扑变化造成的影响。
- 骨干路由器属于区域 0，区域边界路由器(ABR)：属于骨干区域又属于非骨干区域，汇总区域信息发送给骨干路由器
- 区域边界路由器连接着骨干区域和非骨干区域。

---
#### SPF 算法
- 同一区域的路由器拥有相同的LSDB。
- 在区域中的每个路由器将自己作为根。
- 到特定目的地的链接总成本最低的路径优选。
- 最佳路由放入路由表中。

---
#### OSPF报文格式
##### 报头
OSPF报文封装在**IP报文**的负载中，**不使用TCP（不可靠）**，利用LSACK实现自己的确认机制。
Protocol ID Number 89

---
##### 五种报文
- **Hello** 认识，DR、BDR，**发往network的网段**
- **Database Description** 主从，目录
- **Link-State Request** 同步，明细
- **Link-State Update** 同步，明细
- **Link-State Acknowledgment** 确认

![[Pasted image 20230308152225.png]]

---

##### Hello报文
>==Router ID==
**Hello and dead intervals**
Neighbors
**Area ID**
Router priority
DR IP address
BDR IP address
**Authentication password**
**Stub area flag**

---
#### 邻居建立流程（7种状态）
1. **Down State** 未建立
2. **Init State** (Hello)相互通告邻居信息
之间 选举DR和BDR（一个广播域选一个DR和BDR）看Priority+RID
3. **Two-Way State** 相互列入邻居列表
4. **Exstart State** (DBD)选举主从关系 若双方没有DR或BDR就不进入 看RID
5. **Exchange State** (DBD)相互通告LSDB概要信息，从属先发送
6. **Loading State** (LSR)主向从请求LSDB详细信息，(LSU)从回复，再发送完整的LSDB信息
7. **Full State** 建立成功

> DR和BDR在广播域选举，全联通是之广播域的全联通，路由器之间不一定是全联通的
邻居彼此认识，邻接建立关系
224.0.0.6发送给DR和BDR，224.0.0.5发送给DRother

---
#### LSA 序列号
- 在LSDB中每一条LSA管理一个序列号.
- 序列号的长度为4个字节，范围是0x80000001 ~ 0x7FFFFFFF
- OSPF每隔30分钟泛洪每一条LSA以保持适当的数据库同步，每次
LSA泛洪序列号被加1，重置老化时间。如果老化时间达到最大老化
时间（60分钟），LSA就会从LSDB中删除。
- 最终，一个LSA序列号将返回到0x80000001的。当发生这种情况时，
现有的LSA达到最大老化时间，重新刷新LSA时间。
- 当路由器遇到一个LSA的两个实例，它必须确定哪个更新。具有较新
的（更高）LSA序列号的LSA更新。

![[Pasted image 20230308160450.png]]

---
#### 配置基本的OSPF
开启一个或多个OSPF进程，本地CPU进程号
```purescript
Router# router ospf process-id
```
定义哪些接口（网段）参与OSPF
```purescript
Router(config-router)# network ip-address wildcard-mask area area-id
```
可选模式：在接口下定义
```purescript
Router(config-if)# ip ospf process-id area area-id [secondaries none]
```
---
##### OSPF Router ID
- OSPF通过Router ID标识路由器，采用IPv4地址的格式表示。若没有手动设置RID且**自动选举**失败，则OSPF会提示无法工作。（自动选举看最大的loopback口或最大的双up物理口）
- 手动设置：
进程下用Router-id命令配置，也可以用于覆盖自动选举的Router ID。
- 自动选举：
若存在Loopback接口，则RID是活跃的Loopback接口中最大的IP地址；若不存在Loopback接口，则RID是其他活跃接口中最大的IP地址。


```purescript
Router(config-router)# router-id Ip-address
```
- 可以使用IP地址格式（32比特点分十进制）中的任意一个
- 如果在已经处于活动状态的OSPF进程上使用此命令, 必须重启路由器或者重启OSPF进程才能生效。
```purescript
Router# clear ip ospf process
```
```purescript
Router(config)# router ospf 1
Router(config-router)# router-id 172.16.1.1
Router# clear ip ospf process
```

---
##### 验证OSPF操作
- 验证配置的IP路由协议进程，参数和统计信息
 ```purescript
Router# show ip protocols
```
- 显示路由器学到的所有OSPF路由
```purescript
Router# show ip route ospf [Process-id]
```
- 显示OSPF的router ID、area ID和邻接关系
```purescript
Router# show ip ospf interface [type number]
```
- 显示接口在OSPF下的状态
```purescript
Router# show ip ospf interface brief
```

- 显示OSPF的router ID、计时器和状态
```purescript
Router# show ip ospf
```
- 显示OSPF邻居信息，包括广播网络中的DR和BDR信息
```purescript
Router# show ip ospf neighbor [type number] [neighbor-id] [detail]
```
- 显示OSPF接口信息
```purescript
Router# show ip ospf interface interface-id
```

---
##### 修改OSPF COST Metric
Cost或者Metric，是描述通过接口发送数据包的开销。
默认值= (100 Mbps) / (bandwidth in Mbps).
- 在接口下手动设置Cost来覆盖默认值，取值范围1 到65535
```purescript
RouterA(config-if)# ip ospf cost interface-cost
```
- 设置有别于100 Mbps的参考带宽，取值范围1 到4294967
```purescript
RouterA(config-router)# auto-cost reference-bandwidth ref-bw
```

---
## OSPF-2
#### OSPF网络类型
后三种不常见
- Loopback ：环回口
- point-to-point ：串口**S** 帧中继的点到点子接口
- broadcast ：以太口 快速以太口 **RJ45 E F**
- NBMA ：帧中继、X.25、ATM，非广播多路访问
- point-to-multipoint (Cisco)
- point-to-multipoint no-broadcast (Cisco)

---
##### 环回口类型
- 环回口在OSPF中式一类单独的网络类型。
- 环回口下配置的IP，不管掩码配置为多少，发出路由时都会当做/32的主机路由
- 除非更改网络类型，如P2P、broadcast。

---
##### 点到点类型
- 如果二层的协议为PPP、HDLC（认证协议如PPPoE）等，则OSPF网络类型为P2P
- 如果帧中继子接口类型为P2P的，则OSPF网络类型也为P2P
- 不选举DR、BDR
- 使用组播地址224.0.0.5
- OSPF能够根据二层封装自动检测到P2P网络类型

设置成P2P加快收敛

---
##### 广播型多路访问
- 通常出现在以太网
- 先选举BDR、再选举DR
- 所有路由器均与DR及BDR建立邻接关系
- 使用组播地址224.0.0.5及224.0.0.6

---
##### DR和BDR选举
- 具有最高优先级的OSPF成员成为DR，次高优先级的成为BDR
- 如果优先级一致，则比较RID。RID大的成为DR，第二大的成为BDR
- DR选举是非抢占式的，只能等DR die了。

---
##### 设置DR选举的优先级
```purescript
Router(config-if)# ip ospf priority number
```
- 默认优先级为1，取值范围0 到255
- 如果优先级为0，则**不参与**DR或者BDR选举
- 如果一个设备不是DR或者BDR，那就是DRother

>广播域上选举所以是在接口上配置
>广播多路环境内优先级全为0，卡在Two-Way状态

---
##### 修改OSPF的网络类型
```purescript
Router(config-if)# ip ospf network Network_type

broadcast           Specify OSPF broadcast multi-access network
non-broadcast       Specify OSPF NBMA network
point-to-multipoint Specify OSPF point-to-multipoint network
point-to-point      Specify OSPF point-to-point network
```

---
##### 非广播型多路访问
- 使用物理接口默认为NBMA
- 使用子接口默认为点对点
- 使用NBMA需要使用neighbor命令指定邻居

---
##### Debug建邻居过程
![[Pasted image 20230309212537.png]]
![[Pasted image 20230309212550.png]]

---
#### LSA 链路状态通告
LSU包含OSPF头部、LSA、校验码
![[Pasted image 20230309144221.png]]

---
##### 各类OSPF路由器
- 内部路由器
- 主干路由器
- ABR(area border router)兼主干路由器
- ASBR(Autonomous System Border Router) 与其他协议的交接路由

---
####  LSA类型
![[Pasted image 20230309144708.png]]

---
##### 1. Router LSA
报文字段：TYPE, Router ID, Numbers of Links, Link N Description···
- 每个路由器针对它所在的区域产生Type 1 LSA ，描述区域内部与路由器
**直连的链路**的信息（包括链路类型，Cost等）
- 只在**本区域**内泛洪，不允许跨越ABR。
- Link ID是通告该LSA的路由器RID。
```purescript
R1# show ip ospf database [router]
```
![[Pasted image 20230309150759.png]]
![[Pasted image 20230309150805.png]]

---
##### 2. Network LSA
报文字段：TYPE, Router ID, Subnet mask, Attached router ID···
- 由DR生成，描述其在该网络上连接的所有路由器和网段掩码信息。
- 只在**本区域**内泛洪，不允许跨越ABR；
- Link ID是DR进行宣告的那个接口的IP地址。
```purescript
R1# show ip ospf database [network]
```
Router LSA 和 Network LSA 在区域内洪泛，使区域内每个路由器的LSDB达到同步，计算生成标识为“O”的路由，解决区域内部的通信问题。
![[Pasted image 20230309150808.png]]
![[Pasted image 20230309150813.png]]

---
##### 3. Summary Net LSA
报文字段：TYPE, Subnet ip, Subnet mask, Metric（路由和开销）
- 由ABR生成，将区域内部Type1、2 LSA信息收集起来以路由子网的形式扩散出去。在除了某些特殊区域中传递。
- Link ID是**域间路由**的路由前缀，一条域间路由对应一条Type 3 SA。
- ABR收到来自同区域其它ABR传来的Type 3 LSA后重新生成新的Type 3 LSA（将ADV Router改为自己）然后继续在整个OSPF系统内扩散。
- 如果—台ABR与它本身相连的区域内有多条路由可以到达目的地，那么它将只会始发**单一**的一条网络汇总LSA到骨干区域，而且这条LSA是上述多条路由中开销**最低**的。
```purescript
R1# show ip ospf database [summary]
```
![[Pasted image 20230309150825.png]]
![[Pasted image 20230309150829.png]]
![[Pasted image 20230309154156.png]]

---
##### 5. AS External LSA
报文字段：TYPE, Router ID, Subnet mask, Metric （路由和开销）
- 由ASBR生成，用于描述OSPF自治域**系统外**的目标网段信息。
- ADV Router在传递过程中不改变。在除了某些特殊区域中传递。
- Link ID是域外路由的路由前缀，一条域外路由对应一条Type 5 LSA
- 外部路由通过重分布引入OSPF，相应信息（路由条目）由ASBR以Type 5 LSA的形式生成然后进入OSPF路由域
- 缺省情况下， Type 5 LSA生成路由用OE2表示，可指定为OE1
	- OE1 开销 = 外部开销+ OSPF内部开销
	- OE2 开销 = 外部开销 = 20（默认）
- Type 5 LSA不允许进入特殊区域—— Stub和NSSA区
```purescript
R1# show ip ospf database [summary]
```
![[Pasted image 20230309155401.png]]
![[Pasted image 20230309155404.png]]
![[Pasted image 20230309155407.png]]

---
##### 4. ASBR Summary LSA
报文字段：TYPE, Router ID, Subnet mask, Metric （路由和开销）
- 由ASBR所在区域的ABR生成，用于描述ABR能够到达的ASBR的信息。
- Link ID为目的ASBR的RID。在除了某些特殊区域中传递。
- ADV Router在经过ABR时会改变。

为什么需要LAS4？
- 3类LSA是由ABR产生，描述的是汇总的路由信息，里面有类型、掩码、metric等信息，并没有包含到ASBR的位置信息，3类LSA传递是路由信息。
- 5类lsa的设置是在整个路由域内泛洪，起源者的RID所有人看到的都是ASBR的RID，那么如果和这个ASBR在同一个区域内可以通过1类lsa知道此RID设备在哪里，但是当5类lsa跨越区域之后，其他区域的人并不能通过1类lsa获知这个RID的设备在哪里
```purescript
R1# show ip ospf database [asbr-summary]
```
![[Pasted image 20230309160336.png]]
![[Pasted image 20230309160341.png]]

---
##### 7. NSSA External LSA
报文字段：TYPE, Router ID, Subnet mask, Metric （路由和开销）
在NSSA中ASBR针对外部网络产生类似于Type 5 LSA的Type 7 LSA
- Type 7 LSA只能在**NSSA区域**中泛洪。到达NSSA区域ABR后，NSSA ABR将其转换成Type 5 LSA的外部路由传播到Area 0，从而传播到整个OSPF路由域。
  若有多个ARB，则由**RID大**的负责转换。
- 生成路由默认用ON2表示，也可指定为ON1（与OE2、OE1相似）

![[Pasted image 20230309202856.png]]
![[Pasted image 20230309202858.png]]
![[Pasted image 20230309202904.png]]

---
##### OSPF LSDB和路由表
- **O** OSPF域内路由
- **O IA** OSPF域间路由
- **O E1** 1类外部路由
- **O E2** 2类外部路由
- 优先级：O, O IA, O E1, O E2

> Router LSA 村民自我介绍+邻居
Network LSA 村长自我介绍+所有村民
Summary Net LSA 村边村民自我介绍+外村村民
AS External LSA 村边村民介绍+外星人
ASBR Summary LSA 村边村民自我介绍+认识外星人的村边村民


---
#### OSPF 路由汇总
目的
- 最小化路由表项的数量
- 局部拓扑变化的影响
- 减少LSA类型3和5洪泛并节省CPU资源

OSPF汇总特点
- 无自动汇总，只有手动汇总
- 路由汇总方式为：域间汇总、域外汇总
- 配置路由汇总后，邻居将学到汇总的路由。而配置路由汇总的路由器本身
- 将创建另一条指向Null 0接口的汇总路由，防止环路
```purescript
// 域间
Router1(config-router)# area Area-id range IP-addr Mask [advertise | not-advertise] [cost cost]
// 域外
Router1(config-router)# summary-address IP-addr Mask [not-advertise] [tag tag]
```
相同区域间的路由都要进行相同的汇总，否则没有汇总的路由存在详细和汇总的路由，继续使用明细，流量聚集到没有汇总的路由，反而加重开销

---
#### OSPF默认路由
以5类LSA向OSPF中注入默认路由
```purescript
Router1(config-router)# default-information originate [always] [metric Metric-value] [metric-type Type-value] [route-map Map-name]
```
- 只有当默认路由已经存在在路由表中才会通告默认路由
- 加always参数可以强制下发默认路由，没有always且路由不可达时，不通告默认路由，防止流量进来又丢弃。

---
## OSPF-3
#### OSPF特殊区域
- 骨干区域Backbone Area 0
本身是一个标准区域，负责连接非骨干区域。
其它区域(非骨干区域)必须保证和骨干区域有直接的物理连接
ABR上做汇总的好处是减少通告出去和进来的不必要信息
- 普通(标准)区域Standard Area
一个区域缺省是普通区域
##### 末梢区域 Stub Area
阻挡不必要的LSA4、5外部路由进入本地区域，从而精简路由表
ABR会生成**默认路由**(LSA3)通告进Stub区域内部，Metric为1

在区域内路由器和ABR
```purescript
Router(config-router)# area Area-id stub
```

---
##### 完全末梢区域 Totally Stub Area
**Cisco私有**
阻挡LSA3和LSA5，生成O IA* 的**默认路由**，Metric为1，
完全末梢区域是一种对末梢区域的改进，进一步精简路由表； 
区域路由器同末梢区域，ABR
```purescript
Router(config-router)# area Area-id stub no-summary
```
多ABR时，可通过设置开销设置默认路由主备，开销默认为1
```purescript
Router(config-router)# area Area-id default-cost Cost
```

注意：
- 不可在骨干区域配置。
- 区域内不能有ASBR和虚链路。
- 特殊区域内所有路由器都配置成Stub。
- 有多个以上ABR时，到其他区域或外部自治系统可能存在次优路径。需要注意选路（修改cost）

---
##### 非完全末梢区域 Not-so-stubby Area
NSSA既阻挡外部LSA5的进入，同时它的ASBR又可以引入外部路由LSA7；
LSA7在NSSA内洪泛，通过ABR时转换为LSA5；
域内路由和ABR
```purescript
Router(config-router)# area Area-id nassa
```
ABR宣告默认路由
```purescript
Router(config-router)# area Area-id nassa [default-information-originate]
```

---
##### 完全NSSA Totally NSSA
进一步由NSSA ABR阻挡LSA3进入NSSA区域内，同时ABR自动生成**默认路由**下发至完全NSSA区域。
ABR
```purescript
Router(config-router)# area Area-id nassa no-summary
```

---
##### OSPF特殊区域总结
![[Pasted image 20230309205023.png]]
末梢：不与外部网络相连，保留其他区域的信息
完全末梢：不与外部网络相连，不保留其他区域信息
NSSA：与外部网络相连，保留其他区域的信息
完全NSSA：与外部网络相连，不保留其他区域的信息
![[Pasted image 20230309205432.png]]
![[Pasted image 20230309205802.png]]
passive-interface 被动接口通告但是不发Hello报文，减小带宽开销，而且防止与下端建立OSPF，提高安全性

---
#### OSPF认证
- 认证算法 （无认证 type 0）
	- 简单**明文**密码身份验证 type 1
	 路由器发送数据包和密钥。 邻居检查密钥是否匹配。安全性低。
	- **MD5**身份验证 type 2
	 配置密钥ID和密钥。路由器发送数据包和消息摘要，密钥不发送。安全性高。
- 认证类型
	- 接口认证
	- 区域认证

明文接口认证
```purescript
Router(config-if)# ip ospf authentication-key Password
Router(config-if)# ip ospf authentication
```
明文区域认证
```purescript
Router(config-if)# ip ospf authentication-key Password
Router(config-router)# area Area-id authentication
```


密文接口认证（双方Key-id和Key都要一样）
```purescript
Router(config-if)# ip ospf message-digest-key Key-id md5 Key
Router(config-if)# ip ospf authentication message-digest
```
密文区域认证（双方Key-id和Key都要一样）
```purescript
Router(config-if)# ip ospf message-digest-key Key-id md5 Key
Router(config-router)# area Area-id authentication message-digest
```
出错消息
![[Pasted image 20230309212309.png]]

---
#### OSPF高级特性
##### 虚链路 Virtual-link
- 虚拟链路被用于一个不连续的区域连接到区域0。
- 逻辑连接是建立路由器A和路由器B之间。
- 虚拟链路被推荐用于备份或**临时**连接。

双方相互设置，两端必须用一个area，虚链路属于area 0
```purescript
Router(config-router)# area Area-id virtual-link Router-id
```
**虚链路认证**
明文接口认证
```purescript
Router(config-router)# area Area-id virtual-link Router-id authentication-key Key
Router(config-router)# area Area-id virtual-link Router-id authentication
```
明文区域认证
```purescript
Router(config-router)# area Area-id virtual-link Router-id authentication-key Key
Router(config-router)# area 0 authentication
```
密文接口认证
```purescript
Router(config-router)# area Area-id virtual-link Router-id message-digest-key Key-id md5 Key
Router(config-router)# area Area-id virtual-link Router-id authentication message-digest-key
```
密文区域认证
```purescript
Router(config-router)# area Area-id virtual-link Router-id message-digest-key Key-id md5 Key
Router(config-router)# area 0 authentication message-digest-key
```
查看
```purescript 
Router# show ip ospf virtual-links
```

---
## EIGRP-1
特性 **Csico私有** 使用 IP报文、协议号88、广播地址 224.0.0.10
1. 高级距离矢量协议——具有距离矢量性和链路状态协议特征
2. 无类路由协议——可划分子网、可聚合子网路由
3. 支持VLSM与不连续子网
4. 100%无环路——DUAL算法
5. 快速收敛——拥有备份路由
6. 触发更新，配置简单
7. 不等价负载（OSPF等价负载，开销不一样强制等价负载）

EIGRP 关键技术
- 邻居发现和恢复：两个邻居之间使用hello 报文。带宽大时hello间隔小 hold四倍hello时间
- 可靠传输协议(RTP)：保证向所有邻居交付EIGRP数据包。
- DUAL有限状态机：选择开销最低，没有环路的路径去往目的地。

---
#### 三张表
##### 邻居表
```purescript
Router# show ip eigrp neighbors
```
![[Pasted image 20230310145904.png]]
`Smoothed round trip time (SRTT)` 发送EIGRP数据包给邻居,直到本地路由器接收到邻居对该数据包发送确认包的平均时间(毫秒)，俗称：平滑回程时间
`RTO` 路由器在邻居的重传队列中，重传一个可靠的报文的等待确认时间(毫秒) ，俗称：重传超时计时器
`Q` 重传队列
`Seq` 更新次数计数

---
##### 拓扑表
```purescript
Router# show ip eigrp topology [all-links]
```
![[Pasted image 20230310150548.png]]
`P` 稳定状态
`A` 不稳定状态
`U` 更新状态
`Q` 查询状态
`R` 回应状态
`r` 已回应状态
`s` 持续不稳定状态
- 查看当前设备从邻居收到的满足FC条件的路由信息
- all-links 可以查看当前设备从邻居收到的所有路由信息，无论是否满足FC条件。

---
##### 路由表
```purescript
Router# show ip route eigrp
```
![[Pasted image 20230310150954.png]]
`D` 域内
`DEX` 域外
通过AD值区分类型

---
#### DUAL 算法术语
- FD (Feasible Distance 可行性距离)：从**本地路由器**算起到目标网络之间的开销。
- AD (Advertised Distance 通告距离)：从**下一跳节点**到目标网络之间的开销。 
- 最小开销 = 最小FD
- Successor(后继路由器)：具有到达目的网络开销最小的邻居。最小FD
- Feasible Successor (可行性后继路由器)：具有一条通向与后继路由器所连同一目的网络的无环**备用**路径，并且满足可行性条件的邻居。
- Feasible Condition (可行性条件)：次优路径的AD小于最优路径的FD 

防环机制
- 水平分割：学习到的路由不会原封不动发往来源接口
- 毒性逆转：学习到的路由发完来源接口，下一跳为自己且Metric无穷大
- Dual算法
- RID

---
#### EIGRP 数据包
- **Hello**: Establish neighbor relationships. 1.544mbps 5s/60s
- **Update**: Send routing updates.
- **Query**: Ask neighbors about routing information.
- **Reply**: Respond to query about routing information.
- **ACK**: Acknowledge a reliable packet.

---
#### EIGRP 邻居发现
相互发Hello、Update、ACK
![[Pasted image 20230310165742.png]]

---
#### EIGRP Metric
- Bandwidth：源和目地之间的**最小带宽**
- Delay：路径上接口的**累积延迟**
- Reliability：源和目地之间的**最低可靠性**、基于存活消息
- Loading：源和目地之间链路上的**最大负载**，基于速率和接口配置的带宽
- MTU：路径上**最小MTU**（传输单元），能通过的最大数据包大小

$$256\ast \left( K1\ast Scaled\ Bw+\frac{K2\ast Scaled\ Bw}{256-Load}+K3\ast Sclaled\ Delay\ast\frac{K5}{Reliability+K4}\right)$$
When $K5=0$ then $K5/ (Reliability+K4)$ is defined to be 1
Formula with default K values ($K1 = 1$，$K2 = 0$，$K3 = 1$，$K4 = 0$，$K5 = 0$)
**$$256\ast (Scaled\ Bw + Scaled\ Delay)$$**
$Scaled\ Bw = (10^7/minimum\ bandwidth\ in\ kbps)$
$Scaled\ Delay = (Delay / 10)$
$Metric = bandwidth (slowest\ link) + delay (sum\ of\ delays)$

修改接口带宽
```purescript
Router(config-if)# bandwidth Kilobits
```
修改接口延迟
```purescript
Router(config-if)# delay Throughput-delay
```

---
#### 配置EIGRP
- autonomous-system 参数称为“自治系统”编号。
- 需要建邻居的所有路由器必须具有相同的AS号。
```purescript
Router(config)# router eigrp Autonomous-system-number
```
- 配置Router-id
```purescript
Router(router)# eigrp router-id Router-id
```

- 标识参与EIGRP的网络范围。
- wildcard-mask 反掩码，0 表示严格匹配；1 表示无所谓。
- 配置正掩码会自动转换。
```purescript
Router(config-router)# network Network-number [Wildcard-mask]
```
查看相关配置，K值
```purescript
Router# show ip protocols
```
查看接口
```purescript
Router# show ip eigrp interfaces
```

---
#### EIGRP 默认路由配置
- Network 0.0.0.0 通告默认路由，OSPF不会
```purescript
Router(config)# ip route 0.0.0.0 0.0.0.0 Interface
Router(config)# router eigrp As-number
Router(config-router)# network 0.0.0.0
```
- Redistribute Static
```purescript
Router(config)# ip route 0.0.0.0 0.0.0.0 (Interface | Next_ip)
Router(config)# router eigrp As-number
Router(config-router)# redistribute static
```
- Summary address
```purescript
Router(config-if)# ip summary-address eigrp AS 0.0.0.0 0.0.0.0
```
边缘路由器连接内网的接口下配置

---
#### EIGRP 汇总
目的：更小的路由表，更小的路由更

自动汇总特性：
- 在主网边界，子网汇总为一个主类网络。
- 只汇总本地产生的路由，不汇总邻居传过来的路由。
- 启用自动汇总的路由器会创建一条指向Null 0接口的汇总路由，防止环路。
- 自动汇总默认开启（高版本IOS中已默认关闭）

手动汇总特性：
- 汇总可以配置在网络内的任何一台路由器的**任意接口**。
- 接口上配置路由汇总时，路由器会创建一条指向Null 0接口的
汇总路由，防止环路。
- 当汇总的所有细路由**都**不存在时，汇总路由也将被删除。
- 细路由中的最小度量作为汇总路由的度量。

---
## EIGRP-2
##### 配置EIGRP汇总
- 关闭自动汇总
```purescript
Router(config-router)# no auto-summary 
```
- 接口将生成汇总路由
```purescript
Router(config-if)# ip summary-address eigrp As-number Address Mask [admin-distance]
```
- 泄露路由图（部分细路由），使得部分非均衡负载
```purescript
Router(config-if)# ip summary-address eigrp As-number Address Mask leak-map Name
```

---
#### EIGRP 负载
- 具有相同且为最小Metric的路由加入路由表（等价负载）
- 在路由表中，去往同一目的地的路由最多有32个负载条目：
- 通过修改EIGRP的Variance值(V值) 设定负载条件：
V值设置成1表示等价负载，默认4条等价负载路径。
- 也可以修改负载的最大条目数，maximum-paths 1表示关闭负载。

##### EIGRP 不等价负载
Variance值设定
```purescript
Router(config-router)# variance Multiplier
```
不等价负载均衡计算公式用变量。默认为1，表示不进行不等价负载。
多条不等价负载：
新的负载路径要是次优路径 $AD<FD_{min}$，且 $FD<FD_{min}*V$

---
##### EIGRP 环路场景
![[Pasted image 20230311194432.png]]
由于重分布Metric的设置不好，AS2区域的Metric较小，路由在AS2区域成环，但是RID的机制防止学习错误的路由

---
#### EIGRP 认证
- EIGRP使用密钥链(Key Chain)管理密钥，可以指定密钥ID、密钥和密钥生存周期。
	- 一个密钥链是一些密钥的集合
	- 密钥链中包括Key ID、密钥、密钥的生命期
	- 路由器发送路由更新报文时，使用第一个有效的密钥
- EIGRP只支持**MD5**认证，生成一个消息摘要。
- 路由器生成并检查每一个EIGRP数据包，验证它接收每个路由更新报文的源。
- 路由器配置一个**密钥ID和密钥**，每个参与认证的邻居必须配置**相同**的密钥ID和密钥。
	- EIGRP认证时，路由器发送**最低ID**的key，并且携带ID。只有Key ID和Key值分别完全相同时才能成功认证。

- 加入key chain配置模式
```purescript
Router(config)# key chain Name-of-chain
```
- 进入key-id配置模式设置key id
```purescript
Router(config-keychain)# key Key-id
```
- 配置key-string
```purescript
Router(config-keychain-key)# key-string Text
```
- 可选：指定Key的有效期
```purescript
Router(config-keychain-key)# accept-lifetime Start-time {infinite | End-time | duration Seconds}
Router(config-keychain-key)# send-lifetime Start-time {infinite | End-time | duration Seconds}
```
- 指定EIGRP数据包的MD5认证
```purescript
Router(config-if)# ip authentication mode eigrp Autonomous-system md5
```
- 使用key-chain中的key启用EIGRP数据包的认证
```purescript
Router(config-if)# ip authentication key-chain eigrp Autonomous-system Name-of-chain
```
![[Pasted image 20230313133850.png]]
![[Pasted image 20230313133923.png]]

---
#### EIGRP 高级企业级应用
##### EIGRP Query 过程
- 当路由条目丢失时，EIGRP路由器向邻居发送Query，丢失的路由条目会置为Active state。
- 接收路由器收到Query报文，且有该路由信息：
	1. 如果查询者不是该路由的**可行后继路由器**，那接收路由器会把可行后继路由器以Reply发给查询者。
	2. 如果查询者是该路由的可行后继路由器，则该路由器会先判断本地拓扑表内是否有该路由的备份路由（其他可行后继路由）:
		1. 如果有备份路由，则该路由器将更新本地路由表，将最优路由切换至该路由，并将以该路由器以Reply方式发送给查询者。
		2. 如果没有备份路由，将该**路由条目置为Active**，然后转发查询给其他邻居。
	3. 如果接收者在路由表或拓扑表中没有该路由的信息，则该路由器会直接向查询者发送Reply，告知路由不可达。
- 路由器从邻居收到所有的Replies时，才重新计算丢失路由的可行后继路由器。
- 默认情况，如果邻居未能在**3分钟**内回复查询，丢失的路由条目将处于SIA状态，路由器重置对于未能答复邻居的邻居关系。

---
##### EIGRP Stub
- 提高网络稳定性，降低了资源开销，并简化了远程路由器配置。
- Stub路由器发送一个特殊的消息给所有邻居，报告其状态为Stub路由器。
- 邻居不会向Stub路由器发送任何Query消息。
- Stub路由器通常用于Hub-and-Spoke 拓扑

![[Pasted image 20230313135407.png]]
```purescript
Router(config-router)# eigrp stub [receive-only|connected|static|summary]
```
![[Pasted image 20230313135544.png]]
不加参数默认为Connected 和Summary ，只**通告**直连和汇总路由

---
##### 妥善关闭
发送goodbye消息：
1. no network
2. no router eigrp

发送goodbye消息：
1. 接口被关闭或者重启路由器

---
#### EIGRP 命名模式
背景：接口带宽超过10G则Metric值固定为256，会导致不理想等价负载均衡；K6模式；ipv4、ipv6混合

```purescript
Router(config)# router eigrp Name
Router(config-router)# address-family ipv4 unicast autonomous-system Autonomous-system
Router(config-router)# network IP-addres Wildcard-mask
```
配置好标准的直接升级成命令模式
```purescript
Router(config-router)# eigrp upgrade-cli Name
```
![[Pasted image 20230313150608.png]]

---
##### 命名模式 Metric
- EIGRP Wide Metrics 使用64-bit metric进行计算。
- 传统EIGRP的Metric为32-bit，最大Metric为：4294967296
- 64-bit Metric只在**命名模式**的EIGRP中使用，传统EIGRP使用32-bit Metric
- Metric计算公式也有所变化：

$$\left( K1\ast Scaled\ Bw+\frac{K2\ast Scaled\ Bw}{256-Load}+K3\ast Sclaled\ Delay+K6\ast Ext\ Attrib\right)\ast\frac{K5}{Reliability+K4}$$
- 默认K值: K1=K3=1，K2=K4=K5=K6=0，精简后

**$$K1 \ast Minimum\ Throughput + K3\ast Total\ Latency$$**
$$Latency=\begin{cases} (Delay\ast 65536)/10 & Bandwidth\leq 1G\\ (10^7\ast 65536/10)/Bandwidth & Bandwidth> 1G\end{cases}$$
```purescript
Router(config)# router eigrp Name
Router(config-router)# address-family ipv4 autonomous-system Autonomous-system
Router(config-router-af)# metric weights K1 K2 K3 K4 K5 K6
```

- Wide Metric为64bit，而路由表中为32bit，故在将wide metric放入路由表时，需要使用比例因子将metric进行缩小
$RIB\ Metric = (Wide\ Metric / RIB\_scale\_value).$
```purescript
 Router(config-router-af)# metric rib-scale Scale-value
```
##### 命名模式加密认证
SHA2-256 bit
```purescript
Router(config)#  authentication mode hmac-sha-256 PASSWORD
```

--- 
## 路由重分布
IGP 内部网关协议
- 路由重分布是指连接到不同路由域（自治系统）的边界，路由器在他们之间交换和通告路由选择信息的能力。
- 重分布可以是从一种协议到另一种协议，或同一种协议的多个**实例**。
- 重分布总是向外的，执行重分布的路由器不会修改其路由表。
- 路由必须要位于**路由表**中才能被重分布，只通告最优路由

网络中使用多种IP路由协议
1. 多厂商的路由环境
2. 网络合并（同一协议或是不同协议）
3. 从旧的路由协议过渡到新的路由协议
4. 路由策略的需要（可靠性、冗余性、分流模型等）

**度量值——种子度量值**
- 路由器通告与其接口直接相连的链路时，使用的**初始度量值**叫做种子
度量值（也叫做默认度量值）。
- 种子度量值或默认度量值是在重分布配置期间定义的，并在自治系统
内部正常递增（除OSPF E2路由）
- 可使用命令default-metric或在redistribute命令中使用metric指定
种子度量值。

![[Pasted image 20230313155544.png]]
重分布直连不会发hello报文，像被动接口

---
##### 单点重分布
单台设备翻译
1. 单向重分布
2. 双向重分布

##### 多点重分布
多台设备翻译
1. 单向重分布
![[Pasted image 20230313163102.png]]
随后R4开启重分布也不会导入新的路由，一起开启比谁快，始终会产生次优路径
1. 双向重分布


---
##### 实现
**RIP**
```purescript
Router(config)# router rip
Router(config-router)# redistribuete ospf Process_ID metric Metric
```
默认度量值无穷大
**OSPF**
```purescript
Router(confit-router)# redistribute eigrp AS subnets metric-type M
```
默认度量值为20，默认度量类型为2
**EIGRP**
```purescript
Router(confit-router)# redistribute {connected | static} metirc Bandwidth Delay Reliability Load MTU
```
```purescript
Router(confit-router)# redistribute ospf Area metirc Bandwidth Delay Reliability Load MTU
```
外部EIGRP AD=170，默认度量值无穷大 最好用接口值配置

---
## Path control
- 路由匹配工具
	- [[CCNA-Enterprise#Access Control List（控制访问列表）|ACL]]
		 - ACL只能抓取网络号，无法精确匹配到掩码
	- Prefix-list
- 路由控制工具
	- Distribute-list
	- Filter-list
	- Offset-list
	- Route-map （也有匹配功能）
	- Administrative Distance
- 数据控制工具
	- PBR
- 其他工具
	- Passive interface

---
##### Prefix-list
**前缀列表** 最后也会**拒绝所有**
- 前缀列表既能限制前缀的范围，又能限制掩码的范围。
- 前缀列表Permit，将抓取相应的路由；Deny则不抓取。
- 前缀列表包含序列号，从最小的开始匹配，默认序列为5，以5累加。
```purescript
ip prefix-list {List-name [Seq_number]} {deny | permit} Network/Length [ge Ge_value] [le Le_value]
```
参数描述
`ge Ge_value` 要匹配的前缀范围，范围为ge-value到32
`le Le_value` 要匹配的前缀范围，范围为length到le-value
`seq_number` 默认5n
length < ge-value <= le-value <= 32
- 如果只写ge，范围：ge ~ 32
- 如果只写le， 范围：length ～ le

![[Pasted image 20230314131014.png]]
常用
```purescript
ip prefix-list A permit 0.0.0.0/0       \\只匹配默认路由
ip prefix-list A permit 0.0.0.0/0 le 32 \\匹配所有路由
ip prefix-list A permit 0.0.0.0/0 ge 32 \\匹配主机路由
```


---
##### Distribute-list
**分发列表** 控制路由更新
- Distribute-list ——分发列表
- 路由过滤工具，可根据下列因素过滤路由：
	- 入站接口
	- 出站接口
	- 从另一种路由协议重分发



- 对于距离矢量路由协议RIP、EIGRP，in影响自己和别人
![[Pasted image 20230314133941.png]]
- 对于链路状态路由协议，in**只**影响自己，out**禁止**，但能在ASBR重分布使用，过滤5类LSA
![[Pasted image 20230314134211.png]]
```purescript
Router(config-router)# distribute-list { [Access_list_number | Name] | [prefix] | [route-map] } in [Interface_type Interface_number]]
```
```purescript
Router(config-router)# distribute-list { [Access_list_number | Name] | [prefix] | [route-map] } out [Interface_name | routing–process [routing-process parameter]]
```

---
##### Filter-list
在OSPF的**ABR**上过滤**3**类LSA
```purescript
Router(config-router)# area Area_id filter-list prefix Prefix_list_name { in | out }
```

---
##### Offset-list
**偏移列表** 在入站或出站时，增大通过EIGRP或RIP获悉**某一条或多条**路由度量值。

```purescript
Router(config-router)# offset-list {Access–list-number | Name} { in | out } Offset [Interface-type Interface-number]
```

---
##### Route-map
**路由映射表** 用途
- 重分发期间进行路由过滤，OSPF路由出口
- BGP
- PBR（策略路由）
- NAT（网络地址转换）

 Route Map 类似脚本语言，工作就像一个复杂的访问列表：
1. 基于命名的方式配置
2. 匹配条件和设置标准类似脚本语言中的“如果match，那么set”
3. 每一行使用序列号以方便编辑，自上而下**逐条**处理，也支持行插入、删除

- 使用MATCH命令匹配特定的分组或路由，使用SET修改相关属性：
	1. 单条MATCH命令可包含多个属性相同的条件，各条件使用逻辑OR运算。
	2. 多条MATCH命令可包含属性不同的条件，各条件使用逻辑AND运算。若包含的属性相同，会合并成一条。
- Route-map默认动作为permit，默认序列号为10，增加序列号需手动设定。
- 末尾隐含Deny any
```purescript
Router(config)# route-map Name {permit | deny} [seq]
```
match动作
```purescript
match ip address {ACL | prefix Prefix_name}  匹配访问列表或前缀列表
match length                       根据分组的第三层长度进行匹配
match interface                    匹配器下一跳为指定接口之一的路由
match ip next-hop                  匹配器下一跳路由器地址
match metric                       匹配具有指定度量值的路由
match route-type                   匹配指定类型的路由
match community                    匹配BGP共同体
match tag                          根据路由的标记进行匹配
```
set动作
```purescript
set metric        设置路由协议的度量值
set metric-type   设置目标路由协议的度量值类型
set interface     首先检查策略路由，不符合策略后使用路由表进行数据包转发处理
set default interface 先查询路由表，找不到精确匹配的路由条目时，才转发数据包到default配置的接口
set ip next-hop   首先检查策略路由，不符合策略后使用路由表进行数据包转发处理
set ip default next-hop 先查询路由表，在找不到精确匹配的路由条目时，就转发数据包到下一跳IP
set next-hop      指定下一跳的地址，指定BGP的下一跳
set as-path       指定AS路径
set community     指定团体属性
set local-preference 指定本地优先级
set weight        指定权重
set origin        指定起源
set tag           指定Tag
default           关键字优先级低于明细路由
```
打tag防环
![[Pasted image 20230315132837.png]]

---
##### Administrative Distance
管理距离控制路由
OSPF
- 精确
```purescript
Router(config-router)# distance Administrative_distance Ip_src Wildmask Acls
```
- 全局
```purescript
Router(config-router)# distance ospf inter-area Ad1 intra-area Ad2 external Ad3
```
EIGRP
- EIGRP外部路由只能通过全局方式修改管理距离
```purescript
Router(config-router)# distance Administrative_distance Ip_src Wildmask Acls
Router(config-router)# distance eigrp Internal_distance External_distance
```

---
##### 策略路由（PBR）
- 通过策略实现为不同的数据包选择不同的路径。
- 应用到入站方向的数据包，匹配打标记的流量。
- 采用Route-map的配置方法，被匹配的流量可以通过set命令修改。

路由选择判断顺序
1. PBR 强制跳转
2. 路由表
3. PBR 默认跳转
4. 默认路由

**匹配流量**
- 使用扩展ACL匹配流量
```purescript
access-list access-list-number {permit | deny} protocol destination destination-wildcard [operator port]
match ip address {access-list-number | name}
```
- 使用Route-map调用ACL
```purescript
source source-wildcard [operator port]
```

---

使用**Route-map**设置

- 设置直连下一跳地址，无论路由表中是否有到目标地址的路由
```purescript
set ip next-hop ip-address […ip-address]
```
- 设置本地出接口，无论路由表中是否有到目标地址的路由
```purescript
set interface type number […type number]
```
- 当路由表中没有到目标地址的路由时，设置到此直连下一跳地址
```purescript
set ip default next-hop ip-address […ip-address]
```
- 当路由表中没有到目标地址的路由时，设置到此本地出接口
```purescript
set default interface type number […type number]
```

---
策略路由调用和验证
- 在流量进入的接口下调用，匹配数据入方向的流量
```purescript
Router(config-if)# ip policy route-map name
```
- 在全局调用，匹配从路由器本身发出的IP报文（与接口调用不冲突）
```purescript
Router(config)# ip local policy route-map name
```
- 验证：
```purescript
show ip policy / debug ip policy
```

>若下一跳不可达，不执行set动作
继续匹配下一跳router map
在router map最后加上放通其他防止

---
##### Passive interface
被动接口，和重分布直连差不多
默认设为被动接口
```purescript
Router(config-route)# passive-interface default
```
```purescript
Router(config-route)# passive-interface Interface_type Interface_number
```
- EIGRP：在指定接口不向外发送Hello消息，而且通过这个接口不与其他路由器建立邻居关系，不发送其他EIGRP的数据流。
- OSPF：在指定接口不向外发送Hello消息，而且通过这个接口不与其他路由器建立邻居关系，不发送和接收OSPF的数据流。

---
## BGP-1
BGP概述
- Border Gateway Protocol = BGP
- 边界网关路由协议，为路径矢量。主要作用是在AS之间传递路由信息。
- BGP的自治系统通过AS号区分。
- 目前BGP有4个版本：V1、V2、V4、V4＋（即MBGP）

使用BGP的三大理由：
- 大量路由需要承载，IGP只能容纳千条，而BGP可以容纳上万。
- 支撑MPLS/VPN的应用，传递客户VPN路由。
- 策略能力强，可以很好的实现路由决策与数据控制。

企业连接到ISP
连接到两家或是多家ISP，提供链路的可靠性，连接方式如下：
1. 单宿：只连接到一家ISP且没有冗余链路
2. 双宿：只连接到一家ISP，使用两条链路来提供冗余
3. 多宿：连接到多家ISP
4. 双多宿：连接到多家ISP，同时使用两条链路
- 采用多宿或是双多宿的原因：
	1. 提高internet连接的可靠性：一条连接出现故障时，可使用另一条。
	2. 提高连接的性能：前往某些目的地时，可使用更佳的路径

---
##### BGP特征
- BGP使用TCP为传输层协议，TCP端口号**179**。
- BGP路由器之间建立TCP连接，这些路由器称为BGP对等体也叫
BGP邻居（**EBGP**、**IBGP**），AS号不同EBGP（外部），AS号相同IBGP（内部）
- 运行BGP的路由器有一个独立的表（BGP表），路由器将BGP表中
最佳路由提供给路由表。
- 管理距离：EBGP路由为20，IBGP路由为200

表
- BGP邻居表：邻居列表show ip bgp summary
- BGP表：包含了从邻居学习所有路由，以及到达目的网段的多个路径和属性。运行BGP的路由器有一个**独立**的表（BGP表），路由器将BGP表中最佳路由提供给IP路由表。
- 路由表：列出了到达目的网段的最佳路径。
- 管理距离：EBGP路由为20，IBGP路由为200.

AS号
- AS：autonomous system 自治系统，指的是在同一个组织管理下使用
相同策略的设备的集合。
- 不同AS通过AS号区分，AS号取值范围1－65535，其中64512－65535是私有AS号。
- 中国电信163 AS号：4134
- 中国电信CN2 AS号：4809
- 中国联通169 AS号：4837

---
##### BGP的路径矢量特征
- 路径矢量信息中包含一个BGP自治系统号列表
- BGP路由器不接受路径列表中**包含其AS号**的路由更新，是无环路的。
- BGP支持对BGP自治系统路径应用路由策略
- BGP路由器只能将其使用的路由通告给邻接自治系统中的对等体

---

##### BGP报文
![[Pasted image 20230315204831.png]]
![[Pasted image 20230315205012.png]]
`KEEPALIVE` 60s一次，180s死

---
##### BGP的有限状态机
![[Pasted image 20230315210222.png]]
![[Pasted image 20230315210342.png]]
Connect retry timeout=32s，一直在connect和active之间切换
参数不合，进程掉了等才会error发送notification报文


#### IBGP和EBGP
BGP Peer
- 运行BGP的路由器被称为BGP speaker
- BGP对等体也叫BGP邻居，建立基于TCP的关系

EBGP Peer
- EBGP：BGP位于**不同自治系统**的路由器之间，称为EBGP。
- 建立EBGP邻接关系，必须满足三个条件：
	- EBGP之间自制系统号不同
	- neighbor中指定的IP地址要可达
	- 定义邻居建立TCP会话

IBGP Peer
- IBGP：BGP位于同一个自治系统的路由器之间运行，用于同一个AS中
交换BGP信息。
- 建立IBGP邻接关系，满足的条件：
	- 自治系统号相同
	- 定义邻居建立TCP会话
	- IBGP邻居可达（LoopBack）

路由黑洞
![[Pasted image 20230315211847.png]]
解决方法
- BGP重分布到OSPF，但是路由条目太多，所有OSPF路由器都要学习，不能用
- BCD之间都建立IBGP peer，让C也知道域外条目，但不能少任何一个peer关系，原因是水平分割原则
---
##### BGP防环
BGP水平分割原则
![[Pasted image 20230315212735.png]]
IBGP不会把从IBGP学习的路由再告诉给IBGP

---
## BGP-2
##### BGP 同步规则
- BGP路由器不会将从IBGP获悉的路由通告给EBGP邻居，除非该路由是**IGP**中存在的
- CiscoIOS默认关闭BGP同步规则功能

![[Pasted image 20230316130313.png]]
```purescript
Router(config-router)# synchronization
```

##### EBGP和IBGP的区别
- EBGP：外部边界网关协议主要作用是在不同的自治系统间交换路由信息。
IBGP：内部边界网关协议主要作用是向内部路由器提供更多信息。
- EBGP一般情况下都要求EBGP邻居之间存在物理连接。
IBGP不需要IBGP邻居之间有物理连接，只需要逻辑连接即可(IGP通告路由)
- 从EBGP邻居学到的路由通告给IBGP和EBGP；
从IBGP邻居学到的路由，是否通告给自己EBGP邻居，要根据AS内的BGP和IGP路由表是否同步而定。但不会再通告给IBGP邻居（水平分割，防止环路）
- EBGP防止环路通过AS_PATH属性来实现。
- IBGP和EBGP使用的BGP属性不同，例如IBGP可以传递LOCAL_PREF
（本地优先属性），而EBGP不行。

---
#### 配置BGP
进入BGP进程
```purescript
Router(config)# router bgp Autonomous_system
```
- 仅执行此命令并不能在路由器上激活BGP，必须至少执行一个子命令才能在路由器上激活BGP进程。
- 在路由器上**只能配置一个**BGP实例。

指定BGP邻居及激活BGP会话
```purescript
Router(config-router)# bgp router-id Router_id
Router(config-router)# neighbor Neighbor_id remote-as Neighbor_as
```
- 邻居指定的IP地址必须可达
- AS决定了与邻居时EBGP会话还是IBGP
- 对于EBGP（一般用直连 ）和IBGP（一般用loopback口）都需要用该命令指定

---
**指定更新源**
- 当创建BGP邻居时，定义了目的IP地址和出接口定义了源IP地址。
- 源IP地址必须与另一台路由器上相应的neighbor命令指定的地址相同。
```purescript
Router(config-router)# neighbor {Ip_address | Peer_group_name} update-source Interface_type Interface_number
```

**EBGP multihop**
```purescript
Router(config-router)#neighbor {Ip_address | Peer_group_name} ebgp-multihop [ttl]
```
- 建立对等关系时，如果不进行额外配置，EBGP路由器只能使用与外部EBGP路由器直接相连的接口地址。ttl默认为1，直连检测，虽然跳数为1也会检测是否直连，所以loopback口需要设为2，最大255

查看
```purescript
Router# show ip bgp
Router# show ip bgp summary
Router# show ip bgp neighbor
```


指定BGP将通告的网络
```purescript
Router(config-router)#network Network_number mask [Network_mask]
```
- network命令与IGP不同，BGP命令network为通告**哪些网段**（接口ip或者路由表都可以）进BGP，而不是在接口上启用BGP。
- network支持无类前缀，前缀必须与路由表中的条目完全匹配。
	1. 如果不指定mask，则只通告主类网络号，而且仅当主类网络中至少有一个子网出现在全局路由表中，BGP才会将该主类网络作为一条BGP路由通告。
	2. 若指定mask，则仅当全局路由表中有与该网络完全匹配的条目时才被通告出去。

---
关于标记为r的路由，查看没有加入路由表的原因
```purescript
Router# show ip bgp rib-failure
```

---
修改next-hop
- BGP是AS-by-AS的路由协议，而不是router-by-router的路由协议。
- 在BGP中，next-hop并不意味着是下一台路由器，而是到达**下一个AS的IP地址**。
- EBGP中，默认next-hop为发送更新的邻居路由器的IP地址。
- IBGP中，从EBGP传来的next-hop属性在IBGP中**保持不变**的被传递。

传给邻居的下一跳改成自己
```purescript
Router(config-router)# neighbor Neighbor next-hop-self
```

软清
```purescript
Router# clear ip bgp * soft
```
硬清
```purescript
Router# clear ip bgp *
```

---
##### BGP同步
- BGP同步规则意义：BGP路由器不应使用通过IBGP获悉的路由或将其通告给外部邻居，除非该路由是本地的或通过IGP获悉的。
- 禁用同步，则BGP可以使用从IBGP邻居那里获悉的但没有出现在本地路由表中的路由，并将其通告给外部BGP邻居。Cisco IOS默认禁用同步。
- BGP同步规则的目的：为防止一个AS内部（非全互联）出现路由黑洞，即向外部通告了一个本AS不可达的虚假的路由。
- BGP同步规则的问题：若将BGP路由发布到IGP中,那么是IGP路由器要维护数以万计的外部路由，对路由器的资源占用将带来巨大的开销。
- 结论：通常BGP协议的运行需要关闭同步。
- 路由的正常传递：1.同步问题2.下一跳问题

命令
- 禁用同步
```purescript
Router(config-router)# no synchronization
```
- 启用同步
```purescript
Router(config-router)# synchronization
```

---
##### Peer Group
- 将更新策略相同的邻居划分到一个对等体组中，以简化配置。
- 对等体组成员继承对等体组的所有配置选项。
- 更新对于每个对等体组值生成一次，每个成员复制该更新。
```purescript
Router(config-router)# neighbor Peer_group_name peer-group
Router(config-router)# neighbor Ip_address peer-group Peer_group_name
```
如
```purescript
router bgp65100
neighbor internal peer-group
neighbor internal remote-as 65100
neighbor internal update-source Loopback 0
neighbor internal next-hop-self
neighbor internal distribute-list 20 out
neighbor 192.168.24.1 peer-group internal
neighbor 192.168.25.1 peer-group internal
neighbor 192.168.26.1 peer-group internal
```
---
##### BGP身份验证
- BGP支持MD5邻居身份验证。
- 认证都是在TCP建立连接的时候完成的。
- 启用身份验证后，将的TCP连接传输的所有数据等进行验证。
```purescript
Router(config-router)# neighbor {Ip_address | Peer_group_name} password String
```

---
#####  关闭邻居
- 从管理层面暂时关闭某个邻居，而避免删除配置
```purescript
Router(config-router)# neighbor {ip-address |peer-group-name} shutdown
```
- 重新启用
```purescript
Router(config-router)# no neighbor {ip-address |peer-group-name}shutdown
```

---
#### BGP汇总
自动汇总
- 重分布的方式导入，会被汇总
- Network方式导入，不会被汇总
- 默认关闭自动汇总

手动汇总
![[Pasted image 20230316192921.png]]
此时R4学习到4条明细，1条汇总，1条null 0，最好用分发列表取消4条明细

---
##  BGP-3
##### BGP路由汇聚
通告汇总路由和**全部**明细
```purescript
R3(config)# router bgp 100
R3(config-router)# aggregate-address 172.16.0.0 255.255.0.0
```
![[Pasted image 20230316193516.png]]
>Next top 0.0.0.0 就是自己产生的
path 会丢失明细路由的AS，只会有汇总的AS

**只**通告汇总路由
```purescript
R3(config)# router bgp 100
R3(config-router)# aggregate-address 172.16.0.0 255.255.0.0 summary-only
R3(config-router)# aggregate-address 172.16.0.0 255.255.0.0 summary-only as-set
```
>明细路由带上s（抑制），不发给邻居
有as-set的话，path会带上明细路由的AS `{65005,65006} 65123`

通告汇总路由，**抑制部分**明细
```purescript
R3(config)# access-list 10 permit 172.16.10.0 0.0.0.255
R3(config)# access-list 10 permit 172.16.20.0 0.0.0.255
R3(config)# route-map test permit 10
R3(config-route-map)# match ip address 10
R3(config)#router bgp100
R3(config-router)# aggregate-address 172.16.0.0 255.255.0.0 suppress-map route-map test
```
![[Pasted image 20230320135411.png]]
通告汇总路由，**泄露部分**明细
```purescript
R3(config)# access-list 1 permit 172.16.1.0 0.0.0.255
R3(config)#route-map test permit 10
R3(config-route-map)#match ip address 1
R3(config)#router bgp100
R3(config-router)# neighbor 35.35.35.5 unsuppress-map test
R3(config-router)#aggregate-address 172.16.0.0 255.255.0.0 summary-only
```
![[Pasted image 20230316193843.png]]

汇总路由防环机制，告知执行汇总的区域，路由明细来源区域
![[Pasted image 20230316193939.png]]
- R3在执行了路由汇总后导致部分具体路由路径信息丢失。为避免因此引入的环路隐患，R3使用ATOMIC_AGGREGATE和AGGREGATOR属性通知R4在R1处执行了路由汇总。
- 在具体路由稳定的情况下，R1也可以选择使用AS_SET属性通告R1聚合路由所包含的具体路由所经过的全部AS。


aggregate命令
- As-set：让聚合路由继承明细路由的属性，包括：as-path，local_preference，community，origin－code。与advertise-map合用，只继承advertise-map里面匹配的明细路由的属性。
- Summary-only：将聚合路由所包括的所有明细路由都**抑制**掉，被抑制的路由在bgp的转发表里，显示为s，代表suppress的意思。发送更新时，只发送聚合路由。
- Advertise-map：只对advertise-map里面匹配的路由进行**聚合**。当advertise-map里面匹配的明细路由**全部消失**后，即使聚合路由范围内还有其他明细路由，聚合路由也将消失。当与as－set合用时，只继承advertise-map里面匹配的明细路由的属性。
- Suppress-map：将suppress-map里面匹配的路由**抑制**掉，被抑制的路由在bgp的转发表里，显示为s，代表suppress的意思。发送更新时，只发送聚合路由和没有被抑制的明细路由。只能对穿越的路由更新过滤，对自身产生的不起作用。
- Attribute-map和route-map：这两个参数一样，可以将聚合路由的属性清除掉（除了as-path属性），添加自己需要添加的属性。

---
#### 路由反射器
RR 从clients和nonclients收路由更新后路由反射的规则：
- 从 client 收到的更新，反射到 nonclients 和 clients
- 从 EBGP 邻居收到的更新，反射到所有nonclients 和 clients
- 从 nonclient 收到的更新，反射到 clients，**不反射到 nonclient**
- 从 RR 收到的更新，drop

RR配置：建立邻居，指定client
```purescript
RB(config)# router bgp 100
RB(config-router)# neighbor 3.3.3.3 remote-as 100
RB(config-router)# neighbor 3.3.3.3 route-reflector-client
```
Client配置：建立邻居
```purescript
RC(config)# router bgp 100
RC(config-router)# neighbor 2.2.2.2 remote-as 100
```

RR的冗余
![[Pasted image 20230320143517.png]]

---
#### 联盟
- 把一个大的AS分给为若干个子AS，通过不同的AS号区分，
- 对外呈现为一个AS号；
- 子AS之间是EBGP Peer，但不改变next-hop、MED、local-pref等属性；
- 子AS不会影响as-path长度，可能会导致次佳路由。

![[Pasted image 20230320143822.png]]
```purescript
R4(config)# router bgp 65060 
R4(config-router)# bgp confederation identifier 100   //BGP联盟AS为100
R4(config-router)# bgp confederation peers 65050      //BGP联盟内的EBGP邻居AS
R4(config-router)# neighbor 20.0.0.1 remote-as 65050  //指定联盟内部的EBGP邻居
R4(config-router)# neighbor x.x.x.x remote-as 65060   //指定联盟内部的IBGP邻居
```
也可以一个RR（R4）

---
#### 维护BGP
- 重置BGP会话：将新策略应用于所有路由，必须触发一个更新。
- 主要使用2种触发更新的方式：硬重置、软重置。
1. 硬重置
**断开**相应的TCP连接，通过这些会话收到的所有信息都将失效，并从BGP表中删除。断开邻居
```purescript
R# clear ip bgp *
R# clear ip bgp {neighbor-address}
```
2. 软重置
不会重置BGP会话，但会刷新路由，并将整个BGP表发送给指定的邻居。
需要修改策略时，建议使用该命令
```purescript
R# clear ip bgp * soft
R# clear ip bgp {neighbor-address} soft
```

查看
```purescript
R# show ip bgp
R# show ip bgp neighbors {address} routes
R# show ip bgp neighbors {address} advertised-routes
R# debug ip bgp updates
```

---
#### BGP属性
- 公认属性Well-Known
	- 公认强制属性Well-known mandatory
	- 公认自由属性Well-known discretionary
- 可选属性Optional
	- 可选传递的Optional transitive
	- 可选非传递的Optional non-transitive

![[Pasted image 20230320145151.png]]

---
##### 报文
![[Pasted image 20230320154404.png]]

---
##### WEIGHT 权重
- 在路由器**本地**配置，只提供本地路由策略，不会传播给任何BGP邻居。
- 范围：0~65535，越大越优先。
- 路由器本地通告的路径默认权重为32768，从其他BGP邻居学习到的为0。

---
##### LOCAL PREFERENCE 本地优先级
公认自由属性
- 告诉**AS中**的路由器，哪条路径是**离开**AS的首选路径。
- LOCAL PREFERENCE越高路径越优。默认本地优先级为100。
- 只发送给IBGP邻居，而不能传递给EBGP邻居。

---
##### ATOMIC_Aggregate
公认自由属性（原子聚合，汇总）

---
##### AS-path
公认强制属性
- 是前往目标网络的路由经过的自制系统号列表，通告该路由的自治系
统号位于列表末尾。
- 作用：确保无环，通告给EBGP时会加上自己的AS号；通告给IBGP时
不修改AS-path。
- 检查是否包含自己属于的区域、包含就不学习

---
##### Origin
公认强制属性
- 指出了路径信息的源头，有下列3种可能：IGP和EGP是协议
- IGP：用network通告路由时，用i表示
- EGP：路由通过EGP获悉，用e表示
- Incomplete：路由的源头未知或是通过其他方法获悉的，用？表示。例
如重发布

---
##### NEXT_HOP
公认强制属性
- 指出了用于前往目的地的下一跳IP地址，BGP中的下一跳为AS。
- 对EBGP会话来说，NEXT-HOP就是通告该路径的EBGP邻居的接口IP。
- 对IBGP，起源AS内部的路由的NEXT-HOP就是通告该路径的邻居的IP。（如果有设定更新源，则为更新源地址），而从EBGP学到的路由的NEXT-HOP，在IBGP内传递时不变，始终指向的是下一个AS（本AS对端的EBGP邻居接口IP）。

---
##### MED
可选非传递属性（像度量值）
- 用于向外部邻居指出进入AS的首选路径。当**入口**有多个时，自治系统可以使用MED动态的影响其他AS如何选择进入路径。
- MED值**越小越优先**，Cisco定义的MED值默认值是0。
- MED是在AS之间交换。MED发送给EBGP对等体时，这些路由器在AS内传播，不传递给下一个AS
- bgp always-compare-med，比较来自不同自治系统的邻居的路由MED

---
##### COMMUNITY
可选传递属性
- 用于简化路由策略的执行
- 可以将某些路由分配一个特定的COMMUNITY属性，之后就可以基于COMMUNITY值而不是每条路由进行BGP属性的设置了

---
##### ORIGINATOR_ID与CLUSTER_LIST
- 用于防止RR环路的产生
- ORIGINATOR_ID:当RR收到客户或是非客户的路由信息放射给他的其它客户时加上originator-id属性，一般是对端的BGP的router-id 。
- CLUSTER_LIST:当两台RR互为客户时，当一台RR向另外一台RR放射路由时会加上cluster-list属性，一般是自己的cluster id号来填充。如果RR收到路由信息的cluster-list属性与自己的cluster id一致的话，就把此路由信息丢弃，来达到防止环路的目的。

## BGP-4
#### BGP选路
前提：路由下一跳不可达或没有解决同步问题，则不能参与路由选择：
1. 选择**Weight值最高**的路由——思科私有（只影响自己）
2. 选择**Local-Preference较大**的路由（影响AS）
3. 选择network或aggregate或重分布获得的**本地路由**（next-hoop 0.0.0.0）
4. 选择**AS路径较短**的路由
5. 依次选择Origin属性为IGP、EGP和INCOMPLETE类型的路由
6. 选择**MED较小**的路由（AS之间）
7. 优选EBGP而不是IBGP
8. 选择下一跳**IGP度量值较小**的路由
9. 负载均衡，BGP默认不启用负载均衡。若配置负载均衡，则不比较后面的参数（maximum-paths n）
10. 如果都是EBGP路由，则选择先收到的那条 
11. 选择BGP Router ID小的BGP对等体通告的路由
12. 优先选择最短的cluster-list
13. 优先选择邻居IP地址最小的路由(neighbor指定的地址)

补充说明：
- 第3点：本地发起的路由有多种方式，如在BGP进程下用network命令，或将其它路由协议重分布进BGP，或者手工聚合（汇总）。通过network和重分布的优先于手工聚合。
- 第4点：在做聚合路由时，使用as-set后产生的AS-Path列表中{ }里的AS号长度只算一个AS号的长度，在联盟内的AS-Path列表中（）的AS号长度不做计算依据。
- 第9点：等价负载均衡，当前面8条选路原则都无法优选出最优路由时，并且在BGP进程下面配置了maximum-paths，那么将执行负载均衡。
- 第10条，第11条：如果BGP进程下使用bgp bestpath compare-routerid命令，则忽略第10条，进行第11条的比较。

>AS path 修改 (100) 变成 (100, 100)，不建议添加不存在的AS


---
##### 修改weigth
```purescript
Router(config)# route-map Name premit 10
Router(config-route-map)# match ip address ACL
Router(config-route-map)# set weight 20
```
##### 修改BGP默认本地优先级
1. IBGP邻居之间，选择离开本AS的出口。
2. 默认为100 ，越大越优。
3. Local preference是公认自由属性。
```purescript
Router(config-router)# bgp default local-preference value
```
- 此命令更改默认的本地优先级。
- 向IBGP邻居发布的所有路由都将本地优先级设置指定的值。

![[Pasted image 20230321125912.png]]

---
##### 修改BGP的MED属性
1. 当EBGP之间存在多个路径时，使用MED。
2. Cisco的默认设置0，越小越优。
3. 通过network或redistribute命令通告到BGP中的直连路由，
则BGP MED=0
4. 通过network或redistribute命令通告到BGP中的IGP路由，
则BGP MED=IGP Metric
```purescript
Router(config-router)# default-metric number
```
- 此命令更改默认的MED值。
- 通告给EBGP邻居的所有路由都将设置为使用此命令指定的值。

![[Pasted image 20230321125856.png]]

---
##### 负载
```purescript
Router(config-router)# maximum-paths {eibgp | ibgp} Number_of_paths
```
标记>是最优，m是负载，只会告诉邻居最优。

---
#### BGP高级特性
##### BGP路由过滤
用前缀列表来过滤，这个是BGP的标准过滤方法，可以用in和out方向。
```purescript
neighbor 1.1.1.1 prefix-list 1 {in | out}
```
用访问控制列表来过滤，支持扩展访问控制列表。建议用prefix-list来过滤。
```purescript
neighbor 1.1.1.1 distribute-list access-list-number {in | out}
```
用route-map来过滤，一般用在前缀有属性改变的时候。
```purescript
neighbor 1.1.1.1 route-map XX {in | out}
```
用as-path-access-list所定义的正则表达式表示的AS-path来过滤。
```purescript
neighbor 1.1.1.1 filter-list as-path-access-list-number {in | out}
```

---
##### Regexp正则表达式
```purescript
ip as-path access-list acl-number [permit|deny] regexp
```
![[Pasted image 20230321132421.png]]

---
##### 移除私有AS
- Remove private AS：过滤私有的AS号
- To remove private autonomous system numbers in outbound
routing updates
- neighbor {ip-address | peer-group-name} remove-private-as

![[Pasted image 20230321132532.png]]
![[Pasted image 20230321133641.png]]

---
##### 4 Byte AS number
- RFC 4271 defines an AS number as 2-bytes
- Private AS Numbers = 64512 through 65535
- Public AS Numbers = 1 through 64511
39000+ have already been allocated
We will eventually run out of AS numbers
- Need to expand AS size from 2-bytes to 4-bytes
from 65536 to 4294967295
Private AS Numbers = 65536 through 65551

4 Byte AS number的两种格式：
- Asplain—2-byte 和4-byte 都使用十进制来表示（默认）
例如，65526 是一个2-byte AS 号码，234567 是一个4-byte AS 号码。
- Asdot—2-byte 使用十进制表示，4-byte 用点号分隔。
例如，65526 是一个2-byte AS 号码，65,536,005 =1000.5
0000001111101000 :0000000000000101
0000001111101000 = 1000
0000000000000101 = 5
123=0.123
65536=1.0

---
## IPv6
IPv4存在的问题ipv4 32bit 4,294,967,296
- 地址耗尽：1. 私有地址 2. NAT
- 所有行业都是IPv6的潜在用户
- Internet用户快速增长
- Internet路由表增大
- 缺乏真正的端到端模型

IPv6特点32bit -> 128bit
2^128=340,282,366,920,938,463,374,607,432,768,211,456
- 更大的地址空间
- 没有广播，无需NAT
- 无状态自动配置
- 一个接口允许多个地址
- 设置链路本地地址

![[Pasted image 20230321205100.png]]

Qos：维护类流量优先级较高、通讯类其次、最低下载

扩展报头
![[Pasted image 20230321225349.png]]
- 扩展报头只有目标节点查看，其他节点不查看和处理大部分扩展报头
- 要按顺序查看扩展报头的内容
- 使用扩展报头时，报头顺序如下：
	1. IPv6基本报头
	2. 逐跳选项报头：所有路由器都要对其处理
	3. 目标选项报头：使用了路由选择报头
	4. 路由选择报头：列出了一个或多个中间点
	5. 分段报头
	6. 身份验证报头（AH）和封装安全有效负载（ESP）报头
	7. 上层报头：主要为TCP和UDP

---
#### IPv6编址
- 冒号分隔十六进制格式
2001 : 0da8：0207：0000：0000：0000：0000：8207
- 首选格式：无任何化简，就是把IPv6地址完完整整的写出来。
- 压缩表示：
	1. 在有4个十六进制位组成的字段中，可省略前导零。
	2. 在每个地址中，可使用一对冒号来表示任意数量的连续零。

IPv6地址前缀
- IPv6地址前缀可以用来定义路由或子网，默认长度为64。
- 当前缀长度为64时，代表一个网段。
- 例如：
2001:2DB:0:BC::/64 代表网段
2001:2DB:0:BC::/60 代表路由、子网
2001:2DB:0:CD30::/60 可以代表的地址范围：
2001:2DB:0:CD30::/64 到2001:2DB:0:CD3F::/64
超过前缀长度的比特必须为零。如2001:2DB:0:CD3F::/60就是不合法的表示法。

IPv6地址类型
- 单播地址（Unicast Address）
	- 标识一个接口，目的地址为单播地址的报文会被送到被标识的接口
- 组播地址（Multicast Address）
	- 标识多个接口，目的地址为组播地址的报文会被送到被标识的所有接口
- 任播地址（Anycast Address）
	- 标识多个接口，目的为任播地址的报文会被送到最近的一个被标识接口，最近节点是由路由协议来定义的
- IPv6没有定义广播地址


单播地址（Unicast）
- 可聚合全球单播地址（2或3开头）（**公网地址**）
	- 相当于IPv4全局单播地址
	- 由48位的全局路由选择前缀+16位的子网ID+64位的接口ID组成
- 本地链路地址（**本地广播**）
	- 有效范围为本地链路，以`FE80::/10`为前缀，11-64位为0 + 一个64位接口标识。
	- 用于自动地址配置、邻居发现、路由器发现。一般自动生成。
	- 一个链路本地地址只在一条链路中有效，不能被路由。不同链路的链路本地地址是可以重复的。
- 本地唯一地址（**私网地址**）
	- 有效范围为本地站点，以`FC00::/7`为前缀，该地址块又被划分成两个/8的地址块，`FC00::/8`、`FD00::/8`。
	  ![[Pasted image 20230322180624.png]]
	- L位为1表示本地设定，L位为0还未定义。所以地址总是以FD开头。Global ID根据算法随机生成。
	- 本地唯一地址类似于IPv4私有地址，用于内网通信。用于取代之前Site-Local地址。
	- 这种地址在组织内是全局的，但不会在Internet上被路由。

组播地址（Multicast）
- 用来标识一组接口，发送给多播地址的数据流同时传输到多个目的地。
- 范围：`FF00::/8`
- `FF02::1` 表示链路上的所有节点（相当于广播）
- `FF02::2` 表示链路上的所有路由器（主机获取IP地址）
- `FF02::5` OSPFv3 All routers
- `FF02::6` OSPFv3 DR routers
- `FF02::9` RIP routers
- `FF02::A` EIGRP routers

配置和验证IPv6单播地址
- IPv6单播地址的分配方法
   ![[Pasted image 20230322181256.png]]
   `IPv6 Unnumbered` 拷贝，例如将loopback地址拷贝到e口


IPv6编址
- 接口标识符、主机位。
- 接口标识符用于标识链路上的接口，在每条链路上接口ID必须唯一。（一条线上前64位相同）
- 总长度为64位，可根据第二层介质和封装方式自动创建。
- 在以太网中，接口ID基于接口的MAC地址创建的，格式为EUI-64。

EUI-64 插入`FFEE`，第七位变换，加上前面`FE80::`

- 无状态（autoconfig）
	1. 主机发送router Solicitation报文 
	2. 路由器回应Router Advertisement报文（通告前缀信息）
	3. 主机获得前缀及其它参数，通过EUI-64等方法生成
	4. 路由器周期性地向外发送RA报文 /300s 
![[Pasted image 20230302153131.png]]
- 有状态，路由器有地址池

开启ipv6路由单播
```purescript
Router(config)# ipv6 unicast-routing
```
动态ipv6地址需要开启
```purescript
Router(config-int)# ipv6 enable
```
配置地址
```purescript
Router(config-int)# ipv6 address 2035:1:2bc5::87c:0:a/64 eui-64
```



---
#### IPv6 路由协议
- 静态路由
- RIPng
- OSPFv3
- IS-IS
- EIGRP
- MP-BGP4
注：在配置任何IPv6路由协议之前，必须启用IPv6单播路由功能，
使用ipv6 unicast-routing 命令开启（默认未开启）

**静态路由**
```purescript
Router(config)# ipv6 route ipv6-prefix/prefix-length {ipv6-address | interface-type interface-number [ipv6-address]} [administrative-distance] [administrative-multicast-distance] | unicast | multicast][next-hopaddress] [tag tag]
```

##### OSPFv3
- 将IPv6链路本地地址用作源地址，运行在链路而不是子网上
- 使用IPv6链路本地地址来标识OSPFv3邻居
- OSPFv3的组播地址： FF02::5、FF02::6
- 每个接口可以有多个地址和OSPF实例
- 支持使用IPSec进行身份验证
- 使用相同的报文：Hello、DBD、LSR、LSU、LSAck
- 邻居发现机制和邻接关系建立机制相同
- LSA泛洪机制相同
- 支持STUB和NSSA
- 可以支持双栈，IPv4和IPv6一起，但是router-id只能是IPv4地址，如果物理、loopback没有IPv4地址，默认为0.0.0.0

进入IPV6 OSPF路由进程，**单协议栈**
```purescript
router(config)# ipv6 router ospf process-id
```
在接口上激活IPV6 OSPF
```purescript
router(config-if)# ipv6 ospf Process-id area area-id
```
指定接口cost值
```purescript
router(config-if)# ipv6 ospf cost interface-cost
```
将区域指定为末节区域
```purescript
router(config-ipv6-route)# area area-id stub [no-summary]
```
区域边界汇总路由
```purescript
router(config-ipv6-route)# area area-id range ipv6-prefix/prefix-length [cost]
```

进入OSPFv3路由进程，**双协议栈**
```purescript
Router(config)# router ospfv3 process-id
```
在接口上激活OSPFv3 IPV6
```purescript
Router(config-if)# ospfv3 process-id ipv6 area area-id
```
指定接口cost值
```purescript
Router(config-if)# ospfv3 process-id ipv6 cost cost
```
将区域指定为末节区域
```purescript
Router(config-router)# address-family ipv6 unicast
Router(config-router-af)# area area-id {stub|nssa}
```
区域边界汇总路由
```purescript
Router(config-router)# address-family ipv6 unicast
Router(config-router-af)# area area-id range ipv6-prefix/prefix-length [cost]
```

---
##### IPv6 EIGRP
进入EIGRP路由进程，**单进程栈**
```purescript
Router(config)#ipv6 router eigrp autonomous-system-number
```
接口下启用EIGRP
```purescript
Router(config-if)#ipv6 eigrp autonomous-system
```

**IPv6 EIGRP命名模式**，**双进程栈**
进入命名模式EIGRP进程
```purescript
Router(config)# router eigrp name
```
指定IPv6的EIGRP进程号
```purescript
Router(config-router)# address-family ipv6 autonomous-system Autonomous-system
```
进入接口地址簇配置模式
```purescript
Router(config-router-af)#af-interface e0/0
```
关闭e0/0的EIGRP功能
```purescript
Router(config-router-af-interface)#shutdown
```
- EIGRP命名模式下启用IPv6时，默认在所有接口启用。

---
##### IPv6 BGP
进入BGP路由进程
```purescript
Router(config)# router bgp autonomous-system-number
```
建立邻居
```purescript
Router(config-router)#neighbor X:X:X:X::X remote-as autonomous-system-number
```
进入IPv6地址簇，激活邻居
```purescript
Router(config-router)# address-family ipv6 unicast
Router(config-router-af)# neighbor X:X:X:X::X activate
```
通告路由
```purescript
Router(config-router-af)#network X:X:X:X::X/<0-128>
```
查看两表
```purescript
show bgp all summary
router#show ip bgp ipv6 unicast
```

---
## STP
二层转发特征
1. 转发时不用修改数据帧中的信息
2. MAC地址学习是基于**源地址**的学习方式（覆盖）
3. 转发广播帧
4. 泛洪未知单播帧
5. 直接转发已知单播帧

MAC地址表（cam表）
冗余拓扑会产生的问题：
1. 广播风暴
2. 多帧复用
3. MAC地址表不稳定

查看单播、广播数据包
```purescript
show interface count
```

1. 逻辑上打破二层环路
2. 保持冗余链路


BPDU
- 有两种类型的BPDU：
	1. Config BPDU 
	2. TCN BPDU
- BPDU默认每2秒发送一次
![[Pasted image 20230323142513.png|300]]

STP 将特定的端口选为（Blocking state）堵塞（桥就是交换机）
1. 每个广播域选择一个根桥（桥优先级（默认32768），桥MAC地址）
	   - Bridge ID = Bridge Priority + MAC address
	   - 选择最小的Bridge ID为根桥。
 
3. 每个非根桥上选择一个根端口，最低的根路径的端口（最低根桥ID，最低的根路径代价`cost`，最低**发送者桥**ID`brigde-ID(priority,mac)`，最低**发送者桥**端口ID`port-ID`）
4. 每个段选择一个指定端口，同上 
5. 阻塞其他接口

---
##### STP操作
1. **根桥**的选举
- 配置交换机成为根桥，将根据现有情况自动配置最佳优先级
```purescript
Switch(config)#spanning-tree vlan 1 root primary
```
- 配置交换机成为备份根桥
```purescript
Switch(config)#spanning-tree vlan 1 root secondary
```
- 直接配置交换机的优先级(0-61440，4096的倍数，默认32768)
```purescript
Switch(config)#spanning-tree vlan 1 priority priority
```

2. 在所有**非根桥交换机**选择一个到根桥开销最低的接口作为根端口。
   根端口接收BDBU

比较规则
1. 收到BPDU后增加COST，然后比较大小，越小越优。
2. 若COST相同，则比较该接口对端设备(发送者)的BID
3. 若BID相同，则比较该接口对端设备(发送者)的PID
4. 若PID相同，则比较本地接口PID

PID=接口优先级(默认128) + 接口编号


3. 在所有运行生成树的链路选择一个到根桥开销最低的接口作为**指定端口**
   指定端口发送BDBU

![[Pasted image 20230323150205.png]]
直连线路出问题的话从右边开始走
![[Pasted image 20230323150401.png]]


**拓扑变更tcn**
![[Pasted image 20230323150720.png]]
根桥将mac地址表老化时间300s变成15s，加速收敛

**STP“54332”规则**
![[Pasted image 20230323150821.png]]

**生成树协议比较**
![[Pasted image 20230323151123.png]]
Cisco Catalyst 交换机支持：PVST+，RPVST+，MST
默认为PVST+

---
##### 快速生成树协议（802.1W RSTP）
- 802.1D STP能够在大约1分钟之内恢复连接。
- 802.1W STP能够快速的收敛。

![[Pasted image 20230323151346.png]]
原理：
- RSTP会选择一台交换机作为连接到活动拓扑的生成树的根，并为交
换机上的不同端口分配端口角色，在出现故障之后，交换机之间实施
明确的握手协议，完成快速的收敛。

RSTP端口角色
![[Pasted image 20230323151403.png]]
![[Pasted image 20230323151756.png]]

RSTP快速过渡到转发状态
- 边缘端口，各类生成树都可以使用。（接入主机）
- 配置边缘端口使用：spanning-tree portfast 命令。

RSTP PA机制
![[Pasted image 20230323152259.png]]

Downstream RSTP Proposal and Agreement
![[Pasted image 20230323152455.png]]


STP拓扑变更机制
- 802.1D拓扑变更机制
- 原理
1. 根网桥知道网络拓扑发生变更时，设置BPDU的TC标志
2. 此BPDU传输给网络中的所有网桥
3. 网桥接收到TC置位的BPDU后，将桥接表的老化时间300s降低
到转发延迟的秒数。15s

---
##### RPVST+
为每个VLAN运行一个独立的生成树实例，需要通过BID字段来
承载VLAN ID信息，使用扩展系统ID
![[Pasted image 20230323152546.png]]

生成树的配置和验证
- 配置模式
```purescript
Switch(config)# spanning-tree mode rapid-pvst
```
- 指定root / secondary root
```purescript
Switch(config)#spanning-tree vlan 1 priority priority
Switch(config)#spanning-tree vlan 1 root secondary
```
- 指定交换机的优先级
```purescript
Switch(config)#spanning-tree vlan 1 root primary
```
- 查看：
```purescript
show spanning-tree vlan vlan-id
```

---
##### MST-802.1s 多生成树
- MST区域是指一组相互连接，并且具有相同MST配置的网桥。
- MST主要目的是降低与网络的物理拓扑相匹配的生成树实例的总数，进而降低交换机的CPU周期MST区域- VLAN到MST的分组必须在同一个MST区域的所有网桥中保持一致。拥有不同MST配置的网桥或运行802.1D协议的传统网桥则可以看做位于不同的MST区域中。
- MST的配置中包括如下属性：
	1. 包含数字和字母的配置名称
	2. 配置修订号
	3. VLAN映射表

MST 配置参数
- Region Name
- Revision number
- VLAN association table


MST的配置
- 指定模式
```purescript
Switch(config)#spanning-tree mode mst
```
- 配置参数
```purescript
Switch(config)#spanning-tree mst configuration
Switch(config-mst)#name Name
Switch(config-mst)#revision Rev_num
Switch(config-mst)#instance Inst vlan Range
```
- 配置MST的primary 和secondary roots
```purescript
Switch(config)#spanning-tree mst Instance_number root primary|secondary
```
- MST验证
```purescript
show spanning-tree mst instance_number detail
show spanning-tree mst configuration
```

CIST（公共与内部生成树）生成树的计算：
1. 在每个MST域内，MSTP根据VLAN和生成树实例的映射关系，针对不同的VLAN生成不同的生成树实例。
2. MSTP将每个MST域作为单台交换机对待，通过计算，在MST域间生成连接交换网络内所有MST域的一棵生成树。
3. 网络中的设备发送接收BPDU报文，在经过比较配置消息后，在整个网络中选择一个优先级最高的交换机作为CIST的树根。
![[Pasted image 20230323153156.png]]

---
#### STP特性
##### PortFast
能够使得2层接口立即进入转发状态
- 配置
```purescript
Switch(config-if)#spanning-tree portfast
```
- 全局启用
```purescript
Switch(config)#spanning-tree portfast default
```
- 接口禁用
```purescript
Switch(config-if)#no spanning-tree portfast
```

---
##### BPDU Guard 安全
- 能够**限制**在启用PortFast端口**接收**BPDU。防止交换机连接到PortFast端口。
- 启用后若接口收到BPDU，将进入err-disabled状态
- 全局配置
```purescript
Switch(config)#spanning-tree portfast bpduguard default
```
或接口配置
```purescript
Switch(config-if)#spanning-tree bpduguard enable
```
- 全局下配置，只影响portfast特性开启的接口

---
##### BPDU Filter
- 能够**限制**在启用PortFast端口**发送和接收**BPDU。
- 全局启用：当端口**接收**到BPDU时，**不**再处于PortFast状态，过滤特性也会被禁用
```purescript
Switch(config)#spanning-tree portfast bpdufilter default
```
- 接口启用：不发送也不接收任何BPDU数据包，收到BPDU就丢弃，但不会关闭接口
```purescript
Switch(config-if)#spanning-tree bpdufilter enable
```
- BPDU Filter优先级>BPDU Guard优先级，若同时启用两者，则BPDU Filter生效
- 查看：
```purescript
show spanning-tree summary
show spanning-tree interface interface-id detail
```

---
##### Root Guard
能够防止接入端口上的交换机成为根交换机
- 启用根防护的端口**不能成为根端口**，将成为指定端口。
- 当该端口接收到更优的BPDU时，跟防护特性就会使接口进入root-inconsistent的阻塞状态。
- root-inconsistent状态等效于监听状态。当root-inconsistent端口不在接收到更优的BPDU时，它会自动恢复。
- 配置
```purescript
Switch(config-if)#spanning-tree guard root
```
- 查看：
```purescript
show running-config interface interfac-id
show spanning-tree inconsistentports
```

---
##### LOOP Guard
- 避免二层桥接环路的产生，来提高二层网络的稳定性。(主要是防止链路
产生**单向**故障)
![[Pasted image 20230323154207.png]]
- 当SW2的tx出现问题后，SW3过渡到STP状态，将产生环路。
- 开启loop guard，BPDU max-age(20s)之后，Blocking将进入到loopinconsistent状态。
- loop-inconsistent状态的端口重新接收到了BPDU，根据接收到的
BPDU过渡到STP状态，为自动恢复过程。
- 配置
```purescript
Switch(config)#spanning-tree loopguard default
Switch(config-if)#spanning-tree guard loop
```
- 查看
```purescript
show spanning-tree interface interface-id detail
```

---
##### UDLD
- 一个二层协议，与一层机制协同工作。能够检测并禁用单向链路。
- 启用UDLD后，交换机会定期向邻居发送UDLD协议包，并要求定期
收到回应，否则判断为单向链路，并且关闭该端口
- 数据包中包含设备ID，端口ID，邻居设备ID和端口ID信息
- 模式：
- Normal mode：只能检测光口，未接收到UDLD消息时，端口状态为
undetermined状态产生系统日志，但并不影响流量转发
```purescript
Switch(config)# udld enable
Switch(config-if)# udld port
```
- Aggressive mode：检测光口和电口，未接收到UDLD消息时，就会
与邻居重新建立连接关系，连续尝试了8次都失败后，端口就会成为
err-disable状态
```purescript
Switch(config)# udld aggressive
Switch(config-if)# udld port aggressive
```
![[Pasted image 20230323155220.png]]

---
##### Flex
- Flex链路是一种二层的可用性特性，是STP的一种替代解决方案。
- 在关闭了STP的情况下，仍然可以实现基本的链路冗余。
- 可让收敛时间降低到50毫秒以下。

Flex链路
- Flex链路定义了一对主用/备用链路。
- Flex链路是一对接口，可以是switchport接口、port-channel接口。
- 主用链路和备用链路的类型(fast ethernet/gigabit ethernet/ portchannel)不强求一致。
- Flex链路端口上禁用STP，所以STP没有启用时，要确保配置拓扑中没有环路
- 接口只属于一个Flex链路。

- 配置
```purescript
Switch(config-if)# switchport backup interface interface-id
```
- 配置——例
```purescript
Switch(config)# interface f0/1
Switch(config-if)# switchport backup interface f0/2
```
- 查看
```purescript
show interface switchport backup
```

---
## standby
高可用性的组成
- 高可用性是确保整个网络能够快速复原的技术，旨在增强IP网络的
可用性。如何实现网络的快速复原功能。
- 高可用性的组成部分：
	- 冗余性
	- 技术(包括硬件和软件特征)
	- 人员
	- 流程
	- 工具
- 冗余性设计旨在避免单点故障：
	1. 双设备
	2. 双链路
	3. 双WAN服务提供商
	4. 多个数据中心
- 高可用之快速复原
	- 路由协议(OSPF/EIGRP)
	- STP
	- EtherChannel
	- HSRP/VRRP/GLPB

---
##### EtherChannel
为了适应园区网业务的发展、速率的提高，我们可以采用多种方式提高园区网络中的数据传输速度。
1. 使用端口速率更快的端口，如1Gbit/s或10Gbit/s。
2. 增加两边交换机上物理链路的数量
3. EtherChannel是将多个快速以太网端口或吉比特以太网端口分组到一个逻辑通道中
-   on（静态，手动）可以和P主动搭配
-   捆绑接口协议：
    -   PAgP（主动desirable，被动auto）**cosic私有**
    -   LACP（主动active，被动passive）
    -   不能两端接口同时被动，也不能不同协议
- 注意事项：
	- 可以最多将8条物理链路捆绑为一条逻辑的EtherChannel链路。（多余的休眠，活动的down才用多余的）
	- 同一个EtherChannel的所有**接口**要**配置相同**的速率和双工，相同的接口模式，允许的VLAN。
	- 同一条EtherChannel连接的两台**设备**配置也必须**相同**，不能向不同交换机发送流量（除堆叠或虚拟化）
	- 配置EtherChannel接口时，同时影响所有分配了该接口的端口。
	- EtherChannel不能作为SPAN（端口镜像）中的**目的**端口。

二层EtherChannel配置
```purescript
Switch(config)# interface range interface Port - Port
Switch(config-if-range)# channel-protocol {pagp | lacp}
Switch(config-if-range)# channel-group number mode {active | passive | on | desirable | auto}
```


三层EtherChannel配置
```purescript
Switch(config)# interface range interface port - port
Switch(config-if)# no switchport
Switch(config-if)# channel-group number mode {active | passive | on | desirable | auto}
Switch(config)# interface port-channel port-channel-number
Switch(config-if)# no switchport
Switch(config-if)# ip address address mask
```
查看
```purescript
show running-config interface port-channel Num
```

`no switchport` 非二层接口，物理接口会执行 `default interface port` 初始化再加上该命令

接口类型
- 二层接口：access、trunk
- 三层接口：ip地址

负载分担类型：
- src-mac
- dst-mac
- src-dst-mac
- src-ip
- dst-ip
- src-dst-ip
- src-port
- dst-port

```purescript
Switch# show etherchannel load-balance
Switch(config)#port-channel load-balance type
```
---
#### HSRP/VRRP
定义了一组路由器，这组路由器共享虚拟IP地址和虚拟MAC地址，模拟出一台虚拟的路由器。主路由器响应虚拟IP地址的ARP问询，故障后备用路由器响应。

双VRRP
![[Pasted image 20230323191141.png]]

---
#### GLBP
- HSRP和VRRP能够实现网关的快速复原，但对于冗余性组中的备用成员
来说，处于备用模式时，是无法使用上行链路带宽的。
- GLBP可在多台网关之间进行自动故障倒换，可同时使用多台可用网关。
- Cisco私有的解决方案

每个AVF都有不同的虚拟MAC地址，与AVG共用一个虚拟IP地址，AVG收到数据，代替AVF应答上对应的虚拟MAC地址，**轮询机制**

GLBP功能
- GLBP AVG(活跃虚拟网关)：一个GLBP组中只有一台为AVG，其他的为AVG的备用网关，AVG的作用是为GLBP组中的每个成员分配一个虚拟MAC地址。
- GLBP AVF(活跃虚拟转发者)：一个GLBP组中的所有路由器都为AVF，负责转发到该虚拟MAC地址的数据包
- GLBP 通信：GLBP每3s向组播地址224.0.0.102 UDP 3222端口发送Hello数据包。


GLBP特性
- 负载分担
- 多虚拟路由器
- 有效的资源利用

```purescript
Router(config)# interface vlan Vlan_id
Router(config-vlan)# ip address 10.1.7.5
Router(config-vlan)# glbp 7 ip 10.1.7.1
Router(config-vlan)# glbp 7 priority 150
Router(config-vlan)# glbp 7 timers msec 200 msec 700
```

---
#### StackWise-480 堆叠环架构
- 以Catalyst 9300为例，最高支持8台设备组成一个堆叠。支持电源堆叠。
- 采用背板堆叠方式，独立的堆叠端口，专用互连电缆。组成堆叠后统一管理。

![[Pasted image 20230323214358.png]]
一般用在接入层、汇聚层
![[Pasted image 20230323214556.png]]

- 堆叠发现：所有交换机加电且堆叠接口打开后，堆叠发现协议就会使用广播发现堆叠拓扑，并与其他成员分享邻居信息。 
![[Pasted image 20230323214928.png]]
- 堆叠选举：
堆叠**重新引导或初始引导**过程中，需要确定单个Active和Standby角色。
如果所有成员都在选举窗口（120秒）内启动，它们都将参与选举。
Active选举完成后加入的设备没有资格参与Active选举。
除了Active和Standby，剩下的交换机成为Member。
- 选举规则：
最高优先级、最低MAC地址。(优先级存在于ROMMON，而不是NVRAM)
两分钟后，由Active再选举Standby，以减轻同步压力。
当Active出现故障时，Standby转换为Active。
Active不可抢占，但可以先启动设备占领Active。

```purescript
Switch1# switch <number> priority 15
Switch2# switch <number> priority 14
Switch3# switch <number> priority 13
Switch4# switch <number> priority 12
Switch# switch <number> renumber <number>
```
![[Pasted image 20230323220427.png]]

角色状态
![[Pasted image 20230323220446.png]]

以三个交换机堆叠为例：
交换机1：ws-c3750g-12s，交换机2：ws-c3750g-24ts，交换机3：ws-c3750g-48ts
交换机1做为主交换，配置如下：
```purescript
Switch(config)# switch 1 provision ws-c3750g-12s
Switch(config)# switch 1 priority 15
Switch(config)# switch 2 provision ws-c3750g-24ts
Switch(config)# switch 2 priority 14
Switch(config)# sdm prefer desktop
Switch(config)# copy running-config startup-config
```

---
#### 虚拟交换系统——Virtual Switching System
思科VSS、华三IRF、锐捷VSU、华为CSS
虚拟交换系统将两台交换机虚拟组合成单一交换机。
- 中间采用虚拟交换链路（VSL）互连。
- 对外来看只有一台交换机，管理冗余链路如同管理一个单一接口。
- 只能配置主交换机

核心层
![[Pasted image 20230323221351.png|300]]

- 互连交换机通过链路聚合链接到**VSS**的两台交换机。
- VSS利用**MEC技术**在捆绑的逻辑端口上实现冗余和负载均衡。使得下游交换机好像与一台交换机进行互联。
- VSS和下联交换机之间形成了一个**无环**的二层网络结构，不再需要生成树协议，也减少了3层路由邻居，简化了网络的配置和操作。
- 交换机之间可以再加BLD线路，VSL线路断掉，通过BLD关闭备用交换机的业务接口，防止双主机

- 开启VSS时，两台VSS成员设备通过相互协商，
一个成为Active状态，另一个成为Standby状态。
- Active状态设备用于控制整个VSS，Standby状态设备将控制流量通过VSL交由Active统一处理。两台设备同时转发数据层面流量。
- VSL是一条特殊的链路，用于VSS系统中的两台设备间传输控制流量和数据流量。
VSL最多支持八条10GE捆绑，利用Etherchannel技术实现负载和冗余。
其中的控制流量优先级高于数据流量。
- Standby设备使用VSL监控Active设备，检测到Active故障时，Standby设备将把自己转换成Active状态。

Switch1：
```purescript
Switch1(config)# switch virtual domain 100 // 指定交换机1为VSS100区域内的设备
Switch1(config-vs-domain)# switch 1 // 指定VSS区域内该交换机的ID
```
Switch2：
```purescript
Switch2(config)# switch virtual domain 100 // 指定交换机2为VSS100区域内的设备
Switch2(config-vs-domain)# switch 2 // 指定VSS区域内该交换机的ID
```
Switch1/2：
```purescript
Switch(config)# interface port-channel 10 // 启动逻辑接口
Switch(config-if)# switch virtual link 1 // 配置交换ID1使用该逻辑接口
Switch(config)# interface range tenGigabitEthernet 1/1-2 // 进入需要加入逻辑接口的物理接口
Switch(config-if)# channel-group 10 mode on // 物理接口绑定逻辑接口
Switch# platform hardware vsl pfc mode pfc3c // 将PFC模式转换成PFC3C（可选）
Switch# switch convert mode virtual // 转换交换模式为虚拟交换
```

---
##### 组合
![[Pasted image 20230323222825.png]]

---
#### IP SLA
服务水平检测
远端链路或设备故障，本地无法感知。（经过了交换机，只有直连才能检测）
可通过运行动态路由协议来获取拓扑变更。

##### 静态路由+SLA
ping目的地址检测，若不能到达就取消静态路由
![[Pasted image 20230323223030.png]]
```purescript
ip sla 1
  icmp-echo 10.1.12.2 source-ip 10.1.12.1
  frequency 5
ip sla schedule 1 life forever start-time now
track 1 ip sla 1 reachability

ip route 10.10.10.0 255.255.255.0 10.1.12.2 track 1
```
##### VRRP+SLA
主路由器ping目的地址，若不能到达就降低主路由器的优先级，让备用路由器成为主路由器发送
![[Pasted image 20230323223516.png]]
```purescript
ip sla 1
icmp-echo 10.1.12.2 source-ip 10.1.12.1
frequency 5
ip sla schedule 1 life forever start-time now
track 1 ip sla 1 reachability

vrrp 1 ip 192.168.1.254
vrrp 1 track 1 decrement 10
```

验证
```purescript
show ip sla configuration [operation]
show ip sla monitor configuration [operation]
show ip sla statistics [operation-number] [details] command
show ip sla monitor statistics [operation-number] [details]
```

---
#### Syslog
- 思科设备会产生系统日志或系统记录消息，这些消息能够输出到设备控
制台，VTY连接，系统缓冲区，远程日志服务器。
- 如果发送到syslog服务器，消息被发送在UDP端口514
- 系统日志格式：
%FACILTY-SUBFACILITY-SEVERITY-MNEMONIC: message text
%SYS-5-CONFIG_I: Configured from console by console;


---
#### SNMP
由一组网络管理的标准组成，该协议能够支持网络管理系统，用以**监测**连接到网络上的设备是否有任何引起管理上关注的情况。
- SNMP定义为应用层协议，因而它依赖于UDP数据报服务。
- SNMP管理的网络由下列三个关键组件组成：
	- 网络管理系统（NMS，Network-management systems）
	- 被管理的设备（Managed device）
	- 代理者（Agent）
- 网络管理系统从代理收集网络设备信息的方式： 定期轮询、Trap报文(上报更改消息)

![[Pasted image 20230323224703.png]]

- MIB：SNMP报文中用管理变量来描述设备中的管理对象。
- 为唯一标识设备中的管理对象，SNMP用层次结构命名方案来识别管理对象。整个层次结构就像一棵树，树的节点表示管理对象。
- SNMP版本：V1、V2、V3
	1. V1和V2版本以明文的形式发送共同体认证，不能验证消息的来源或加密消息，因此只能用于只读访问。
	1. SNMPv3增加了三个安全级别：noAuthNoPriv：不验证也不加密，authNoPriv：验证发送方但不加密消息，authPriv：验证发送方和加密消息。
- 为保证网络管理信息的安全，代理必须对多个管理站进行本地MIB的访问控制
	- 认证服务 MIB访问限定在授权的管理站范围内，基于团体名认证 Community name
	- 访问策略 对不同的管理站给予不同的访问权限 Read-only Read-Write
- SNMP用Community来定义Agent和Manager间的认证、访问控制和代管关系，提供初步的安全能力。

```purescript
//Set ACL to use SNMP (Optional)
access-list 1 permit 192.168.1.0 0.0.0.255

//Read-only access with this community string
snmp-server community SPOTO1 RO 1
//Read-write access with this community string
snmp-server community SPOTO2 RW 1

//Set SNMP Trap Server IP and community string
snmp-server host IP SPOTO
snmp-server enable traps
```

---
#### SPAN
SPAN技术主要是用来监控交换机上的数据流，可以把交换机上想要被监控端口的数据流COPY或MIRROR一份，发送给连接在监控端口上的流量分析仪，
比如IDS或装了抓包工具的PC
![[Pasted image 20230323225447.png]]
1. 配置本地SPAN:
```purescript
Switch(config)# monitor session 1 source interface f0/10
//设定SPAN的受控端口
Switch(config)# monitor session 1 destination interface f0/20
//设定SPAN的监控端口
```
2. 监测命令：
```purescript
Switch#show monitor session 1
```

---
#### Wireshark
报文过滤
tcp、udp、arp
源目的ip或mac
eth.addr == 00ac.aacc.00a1
ip.addr == 192.168.1.1
ip.src/dst == 192.168.1.1
端口过滤
tcp.srcport/dstport == 8080
逻辑表达式
arp or http
ip.addr == 192.168.1.1 and http
not ip
- 流分析功能
- 因此telnet、FTP等，实际都是不安全的协议

---
#### NetFlow
主要用于酒店
![[Pasted image 20230323225716.png]]
![[Pasted image 20230323225731.png]]
## 交换安全
#### 交换机安全基础
考虑网络安全通常都关注以下几点：
1. 来自企业网络外部的攻击(防火墙)
2. 接入层设备和二层通信安全

![[Pasted image 20230324190031.png]]
核心层不建议实施数据包处理是想要快速转发


二层攻击分类
- MAC攻击
- VLAN攻击
- 欺骗攻击
- 交换机设备上的攻击

---
##### MAC攻击
无效源MAC地址的数据帧向交换机泛洪，消耗完交换机的CAM表空间，从而阻止合法主机的MAC地址生成新条目。去往其他主机的流量会向所有端口泛洪
>发送大量非法源MAC地址的数据帧，使得MAC地址表溢出，没有合法的主机，正常流量未知单播泛洪，被非法获取正常流量

端口安全。MAC地址VLAN访问控制列表。

---
##### 端口安全
- 基于端口建立接入规则
- 接入规则
	- 端口MAC最大个数
	- 端口+MAC
	- 端口+MAC+VLAN
	- 端口+IP
	- 端口+IP+MAC+VLAN

安全违例产生于以下情况：
- 如果一个端口被配置为一个安全端口，当其安全地址的数目已经达到允许的最大个数。
- 如果该端口收到一个源地址不属于端口上的安全地址的包。

当安全违例产生时，你可以选择多种方式来处理违例：
- Protect：当安全地址个数满后，安全端口将**丢弃**未知地址的包。
- Restrict：当安全地址个数满后，安全端口将**丢弃**未知地址的包，同时增加接口违规计数器。
- Shutdown：当违例产生时，将**关闭**端口，并发送一个SNMP **Trap**通知。

```purescript
// 打开端口安全功能
Switch(config-if)# switchport port-security
// 配置最大MAC地址数
Switch(config-if)# switchport port-security maximum 3
// 配置MAC地址静态绑定
Switch(config-if)# switchport port-security mac-address 001a.a900.0001
// 配置MAC地址粘滞，状态接口上所有通过动态学习到的MAC，将被转成sticky mac address，形成安全
// 地址。命令配置后新学习到的MAC地址，也属于sticky。
Switch(config-if)# switchport port-security mac-address sticky
// 配置违例处理方式
Switch(config-if)# switchport port-security violation {protect | restrict | shutdown}
```
```purescript
show port-securtity
show port-securtity interface f0/1
show port-securtity address
```

---
##### VLAN攻击
- VLAN跳转
通过**改变**trunk链路中封装数据包的VLAN ID，攻击设备可以发送或接收不同VLAN中的数据包，而绕过三层安全性机制。
- 公共VLAN设备之间的攻击
即使是公共VLAN中的设备，也需要逐一进行保护，尤其是在为多个客户提供设备的服务提供商网段中尤为如此

![[Pasted image 20230324192246.png]]
DTP 动态trunk协商协议，一边主动一边被动，自动设置trunk
![[Pasted image 20230324203542.png]]


- 加强trunk的配置
- 未使用端口的协商状态
- 未使用端口放入公共VLAN
- 采用VLAN ACL过滤

缓解VLAN跳转攻击
- 将所有未使用的端口设置为**Access端口**，使其无法协商链路聚集协议。
- 将所有未使用的端口设置为**Shutdown状态**，并放入同一个VLAN中。
- 在建立Trunk链路时，将链路聚集协议设置成nonegotiate （关闭DTP）
- 在Trunk链路上配置所需要承载的具体VLAN。
- Native VLAN与任何数据VLAN都不相同。

---
##### VLAN ACL
MAC ACL，地铁方案防环，别的基本上用不到 
```purescript
Switch(config)# mac access-list extended BACKUP-SERVER
Switch(config-ext-mac)# permit any host aaaa.bbbb.cccc
Switch(config)# access-list 100 permit ip 10.1.9.0 0.0.0.255 any
Switch(config)# vlan access-map XYZ 10
Switch(config-map)# match ip address 100
Switch(config-map)# action drop
Switch(config-map)# vlan access-map XYZ 20
Switch(config-map)# match mac address BACKUP-SERVER
Switch(config-map)# action drop
Switch(config-map)# vlan access-map XYZ 30
Switch(config-map)# action forward
Switch(config)# vlan filter XYZ vlan-list 10,20
```

---
##### DHCP欺骗
- DHCP耗竭 
攻击设备可以在一段时间内，消耗完DHCP服务器上得可用地址空间。
- DHCP欺骗
在中间人攻击中，把自己伪装成DHCP服务器

![[Pasted image 20230324210213.png]]


---
##### DHCP监听
![[Pasted image 20230324210226.png]]
将端口变成信任端口，信任端口可以正常接收并转发DHCP Offer报文，默认交换机的端口都是非信任端口，只能够发送DHCP请求.
```purescript
Switch(config)# ip dhcp snooping
Switch(config)# ip dhcp snooping vlan 10
Switch(config-if)# ip dhcp snooping limit rate 10 // dhcp包的转发速率，超过就接口就shutdown
Switch(config-if)# ip dhcp snooping trust // 将端口变成信任端口，信任端口可以正常接收并转发DHCP Offer报文，默认交换机的端口都是非信任端口，只能够发送DHCP请求.
switch# show ip dhcp snooping
```

---
##### ARP欺骗
攻击设备故意为合法主机伪造ARP应答。攻击设备的MAC地址就会成为该合法网络设备所发出的数据帧的二层目的地址（伪装成网关）

缓解：使用动态ARP检测、DHCP侦听、端口安全

如何判断是否存在ARP欺骗
- 网络突然不稳定，时断时续或网速突然很慢
- 使用arp –a，发现网关的MAC地址在变化
- 利用抓包进行报文分析，可以很快的定位ARP攻击源头

手工绑定IP、MAC
- PC上
arp –s ip地址 mac地址
- 网络设备上
arp ip地址 mac地址 arpa
- CISCO：DAI (动态IP环境)

Dynamic ARP inspection
- 通过DHCP Snooping功能将用户**正确的IP与MAC**写入交换机的DHCP Snooping表（不能用别人的MAC）
- 使用DAI功能校验ARP报文的正确性
- 应用场景
	- 用户使用**动态IP地址**，通过DHCP报文来记录
- 缺点
	- DAI功能需通过CPU处理，大量的ARP报文可能导致CPU过高

```purescript
ip dhcp snooping vlan 10
Ip dhcp snooping
ip arp inspection vlan 10
Interface f0/24
ip dhcp snooping trust
ip arp inspection trust
```

---
##### 交换机设备攻击
- CDP修改
通过CDP发送的信息是明文形式且未加密，若攻击者截CDP消息，就可以获悉网络拓扑信息
在所有无使用的端口上禁
用CDP
- SSH修改
Telnet数据包可以以明文的形式查看。SSH可以对数据包进行保护，但版本1中仍然存在安全问题
使用SSH版本2，使用Telnet结合VTY ACL

.

- DNP邻居发现协议
- CDP 默认启用的二层协议，cisco私有
- LLDP 默认禁用状态，与厂商无关的二层协议
```purescript
Switch(config)# no cdp run
或
Switch(config-if)# no cdp enable
switch#show cdp neighbor
Switch(config)#no lldp run
或
Switch(config-if)#no lldp enab
```

- Telnet漏洞
- SSH
```purescript
Switch(config)# enable secret cisco //配置enable密码
Switch(config)# username spoto password spoto //配置用户名和密码
Switch(config)#ip domain-name spoto.net //配置主机名和域名
Switch(config)#crypto key generate rsa general-keys //生成RSA密钥
Switch(config)#line vty 0 15
Switch(config-line)#login local
Switch(config-line)# transport input ssh //在线路上启用SSH传输
```
---
## SDN 软件定义网路
- 要素一：集中化管理（Controller）
![[Pasted image 20230324213129.png]]
- 要素二：转/控分离
![[Pasted image 20230324213145.png]]
- 要素三：可编程
![[Pasted image 20230324213156.png]]


#### SD-ACCESS 软件定义接入
![[Pasted image 20230324213216.png]]
![[Pasted image 20230324213711.png]]

#### SD-WAN 软件定义广域网
![[Pasted image 20230324214321.png]]
![[Pasted image 20230324214341.png]]
`vBond` 负责接入设备，拒绝不合法设备
`vManage` 报表和数据分析，API对接
`vSmart` 下方指令
`WAN Edge` 各个服务器、站点和vSmart之间使用路由协议

![[Pasted image 20230324214738.png]]