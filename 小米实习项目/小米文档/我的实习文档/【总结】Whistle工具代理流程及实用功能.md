1. ## Whistle安装
    

打开Visual Studio Code工具，打开终端输入下面指令实现安装

```Bash
npm  i -g whistle
```

  

安装完成后，在终端输入根据下面指令启动工具

```Bash
w2 start
# 或者 whistle start
```

![[【总结】Whistle工具代理流程及实用功能.png]]

  

此句话表明在`127.0.0.1:8899`端口开启了whistle服务器

Tip：可以通过`w2 help`或者`whistle help`来获取更多操帮助信息

  

2. ## Whistle的基本使用
    

### 2.1 前置条件

为了使用Whistle服务器进行代理，需要对浏览器进行代理指向Whistle服务器地址`127.0.0.1:8899`（此处输入根据在终端中显示的服务器为准），为了方便进行代理切换，使用浏览器插件 `Proxy SwitchyOmega`进行切换。

![[【总结】Whistle工具代理流程及实用功能-1.png]]

  

此处以Chrome浏览器为准，展示下载链接：`[Proxy SwitchyOmega](https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif)`

  

下载完毕后，进入`Proxy SwitchyOmega`插件`选项`进行配置。

![[【总结】Whistle工具代理流程及实用功能-2.png]]

进入配置页面，进入`情景模式`进行代理服务器的配置，此处将代理服务器设置为Whistle服务器地址`127.0.0.1:8899`（此处输入根据在终端中显示的服务器为准）以完成前置条件配置。

![[【总结】Whistle工具代理流程及实用功能-3.png]]

配置完毕后，通过选择插件`proxy`（此处以对应情景模式名称为准）选项即可通过Whistle服务器进行代理。

  

### 2.2使用流程

通过点击**终端链接**，或在手动在浏览器输入`127.0.0.1:8899`（此处输入根据在终端中显示的服务器为准），以进入Whistle服务器进行配置。

此处以百度搜索（www.baidu.com)以进行示范，`127.0.0.1:8084`为此次演示开启的目标服务器。

![[【总结】Whistle工具代理流程及实用功能-5.png]]


点击左侧导航栏`Rules`模块，进入规则的配置。

  

此处在规则中输入如下规则即可完成配置。

```undefined
www.baidu.com 127.0.0.1:8084
```

  

配置完毕后，在搜索栏输入`www.baidu.com`即可进行代理转发。
![[【总结】Whistle工具代理流程及实用功能-6.png]]

## 3. 工作原理

### 3.1 原理图
![[【总结】Whistle工具代理流程及实用功能-7.png]]
### 3.2 代理流程图

注意：此处Whistle代理规则中对应的IP地址即为目标服务器IP地址，而浏览器发起请求时图中对应的”已知IP“地址为原服务器的IP地址。

  

暂时无法在飞书文档外展示此内容

- 1.浏览器输入URL发起请求
    
- 2.判断是否开启服务器代理，若开启服务器代理则进入代理流程
    
- 3.Whistle代理服务器对浏览器发起的请求进行拦截（此处可进行抓包操作）
    
- 4.Whistle代理服务器根据配置的规则进行拦截后请求的转发
    

  

## 4.使用Whistle配置进行Mock开发（实用🌟）

### 4.1 前提须知

此处以【国内开发者站运营后台】项目为例子

此处使用`fetch`来进行`get`方法的网络请求，并封装`get`方法

```JavaScript
#！ common/fetch.js

const commonUrl = '/doc-api'; // 请求的url
const get = (url, params = {}) => {
  const urlWithParams = patchparams(url, params);

  return new Promise((resolve, reject) => {
    fetch(commonUrl + urlWithParams)
      .then((res) => res.json())
      .then((resJson) => {
        const { code } = resJson;
        if (+code === 0) {
          resolve(resJson);
        } else {
          errorHandle(resJson, reject);
        }
      })
      .catch(catchHandle);
  });
};
```

  

### 4.1 未使用Whistle配置进行Mock开发

Mock地址：https://mock.presstime.cn/mock/64d5efbbf27131eed445852f/inclusion-management/mission

在`apis/inclusion-management/js`中封装请求而不进行Whistle配置。

```JavaScript
#！ apis/inclusion-management/js
import { get, post } from 'common/fetch';

export const getMissionList = (params) => get('/mission', params);
```

**未配置时的Whistle的Rules规则**

```Shell
http://onebox.appadmin.pt.xiaomi.com/doc-api/ 10.38.160.81
onebox.appadmin.pt.xiaomi.com 127.0.0.1:8084
```
![[【总结】Whistle工具代理流程及实用功能-8.png]]

此时无法通过直接编写获取Mock数据。

  

需要自己写一个`fetch`请求来获取Mock地址的数据（繁杂）

```JavaScript
  
  const getMissionList = useCallback(() => new Promise((resolve) => {
    fetch('https://mock.presstime.cn/mock/64d5efbbf27131eed445852f/inclusion-management/mission')
      .then((res) => res.json())
      .then((resJson) => {
        if (resJson.code === 0) {
          resolve(resJson);
        }
      });
  }), []);
  
   useEffect(() => {
    getMissionList()
      .then((res) => {
        // 处理请求
        }
      });
  }, []);
```

  

### 4.2 Whistle配置进行Mock开发

对配置Whistle的Rules规则进行配置

注意：项目封装的fetch请求使用的是http协议，mock地址使用的是https协议，编写规则是需要注意，记得加上对应的协议。

```Bash
onebox.appadmin.pt.xiaomi.com/doc-api/ 10.38.160.81
# 新增规则
http://onebox.appadmin.pt.xiaomi.com/doc-api/mission https://mock.presstime.cn/mock/64d5efbbf27131eed445852f/inclusion-management/mission
onebox.appadmin.pt.xiaomi.com 127.0.0.1:8084
```

此时直接在`apis/文件.js`直接封装请求，即可获取Mock地址数据

```JavaScript
import { getMissionList } from '@/apis/inclusion-management';

  useEffect(() => {
    getMissionList()
      .then((res) => {
        // 处理请求
        }
      });
  }, []);
```
![[【总结】Whistle工具代理流程及实用功能-9.png]]当服务端接口写好之后，就可以直接对apis文件内容进行修改了。

比如服务端接口地址为`/task`

```JavaScript
#！ apis/inclusion-management/js
import { get, post } from 'common/fetch';

// 原：export const getMissionList = (params) => get('/mission', params);
// 直接修改即可
export const getMissionList = (params) => get('/task', params);
```

## 5.抓包流程

通过**代理****流程图**可知，进过Whistle服务器的请求都会被拦截下来，因此可以查看到对应的请求包。

### 5.1 前置条件（获取HTTPS请求包）

注意：whistle 只支持抓http 的请求包，如果要抓 https，需要安装证书，这样才能解开 https 请求包

此处以`Macos`与`Android`为准

#### 5.1.1 Macos

1. 首先在Whistle服务器上方工具栏的`HTTPS`选项中根据图中选项进行配置（勾选`Capture TUNNEL CONNECTS`），获取证书的二维码。
    
![[【总结】Whistle工具代理流程及实用功能-10.png]]
2. 下载证书
    
![[【总结】Whistle工具代理流程及实用功能-11.png]]

3. 双击证书以进行配置
    

![[【总结】Whistle工具代理流程及实用功能-12.png]]

4. 信任该证书以完成配置
    
![[【总结】Whistle工具代理流程及实用功能-13.png]]

1. 扫描二维码进行证书的安装
    

![[【总结】Whistle工具代理流程及实用功能-14.png]]

  

### 5.2 电脑端

点击左侧导航栏`Network`模块，进入拦截请求的展示页面。

![[【总结】Whistle工具代理流程及实用功能-15.png]]

可以通过在上方工具栏`Setting`进行展示配置。

  

此处展示**过滤功能**。

在`Include Filter`进行配置，过滤出`host`为`www.baidu.com`的网络请求
![[【总结】Whistle工具代理流程及实用功能-16.png]]

  

其于过滤规则

1. `m:pattern`：pattern为字符串或正则表达式，匹配请求方法包含该字符串(不区分大小写)或匹配该正则的请求
    
2. `i:ip`：ip表示客户端ip或正则表达式，匹配客户端ip包含该字符串(不区分大小写)或匹配该正则的请求
    
3. `h:header`：header表示请求头rawData的某部分字符或正则表达式，匹配请求头包含该字符串(不区分大小写)或匹配该正则的请求
    
4. `H:host`：host表示Network里面的host字段，为请求的域名加端口，匹配请求host字段包含该字符串(不区分大小写)或匹配该正则的请求
    
5. `其它`：正则或普通字符串，匹配请求URL包含该字符串(不区分大小写)或匹配该正则的请求
    

  

### 5.3 移动端

1. 将电脑、手机连在同一个局域网下 (连同一个 wifi )，点击 whistle 界面右上角的 `Online`。
    
![[【总结】Whistle工具代理流程及实用功能-17.png]]

  

2. 配置自己手机的代理地址为online中的ip地址即可，就能在桌面端监测抓包手机上的应用
![[【总结】Whistle工具代理流程及实用功能-18.png]]

3. 查看手机IP地址，通过上述过滤功能以更直观查看抓包效果。
    
![[【总结】Whistle工具代理流程及实用功能-19.png]]