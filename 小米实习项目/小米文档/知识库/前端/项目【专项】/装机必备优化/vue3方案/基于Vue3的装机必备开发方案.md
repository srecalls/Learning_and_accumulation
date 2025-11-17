

[装机必备- PRD](https://xiaomi.f.mioffice.cn/docs/dock4W06QNpWC7TrFlc9cX5IjWe)

## 技术文档

### 服务端

[装机必备接口文档](https://xiaomi.f.mioffice.cn/docs/dock4PkttaZa8g3VpusLs0z6uc2)

### 基础架构搭建

- #### 项目基础架构搭建
    
    - 脚手架vue-cli
    - css预处理器： Less
    - 代码检测：Eslint + Prettier （Lint on save）

![](https://xiaomi.f.mioffice.cn/space/api/box/stream/download/asynccode/?code=YmY4YTZjNGI2M2ExNzc4YTZiMmJmNjMzYzk1MmU4Y2Zfdzg1ZnRzb0JFMTg0bkdtTzJEc2YwdkN4bEtQZ1VKZVZfVG9rZW46Ym94azR0YlpkbjZjemxmUXhTQkZabjZMTlpjXzE3MDE0MDg3Nzg6MTcwMTQxMjM3OF9WNA)

- 多页面配置
- 环境变量配置

根据开发/生产环境不同，加载对应的环境变量文件，控制变量切。初步设定分为.env.development，.env.preview，.env.production三个环境变量文件，每个文件中设置参数：

```
VUE_APP_DEPLOY_ENV: development、preview、production //发布环境，区分打点参数
VUE_APP_API_HOST: 'https://app.market.xiaomi.com/apm/' // 接口域名
VUE_APP_LINK_HOST: 'https://app.market.xiaomi.com/hd/apm-h5-cdn/' // 页面域名
VUE_APP_PROJECT_NAME：'appstore_mobile' // 项目名称，onetrack打点使用
```

- 文件架构：

- #### 重点模块
    
    - 异步组件加载: 各页面按需加载，不增加同步组件
    - base功能模块

（一个基本原则：可以独立的模块全部独立文件管理，减少逻辑耦合问题以及减小base模块大小，不利于阅读维护）

- request：

所有请求统一文件管理，封装出一个基础的service请求类，每个页面基于该类做扩展，每个请求都独立封装成一个类管理，进行私有属性处理

> 是否继续使用客户端代理？

> 背景：隐私监管要求，需要使用客户端请求，做了对应处理，同时客户端请求介入了miLink

> 问题：不好调试

> 结论：暂时保留已有逻辑，之后考虑重构问题

- 全局事件：Vue2支持全局eBus，Vue3取消了$on,$off,$once
    - 监听页面可见性变化：以注册监听回调方法的方式实现，参考listenVisibleChange
    - 网络变化，// 同上方式，实现一个方法
    - setRecordParams：打点参数设置

- 懒加载：vue-cooler-lazyload插件,基于vue2开发，需要改造
- 按钮状态变化, buttonHandler入口

vuex进行状态管理，主要原因：一个app可能会在页面中多个位置存在，为了保证状态一致性，需要进行状态统一管理，管理方式可以采用h5的方案

- 注册app状态变化回调：REG_APP_STATUS
- 检查当前app状态：CHECK_APPS
- 安装处理：on_install

- 数据存储处理: 数据更新？
- 多语言：i18 done
- 全局变量：ajaxData保持不变、其它封装起来 done
- 深色模式处理：具体查看z-inject-darkmode.js

### 装机必备页面

- banner
- applist
- 吸底全部安装

### 打点：

打点方案暂时与appstore-h5方案保持一致？

STAT_PV: pv/uv上报，不变

曝光： 使用vue-cooler-exposure插件，addAfterRecordCallback中处理曝光数据等

点击：singleRecord

页面浏览时长：不可见到可见变化监听

actionRecord

createReqQuery

??

// TODO :按事件类型分文件管理

### 性能监控

webvitals

performance封装：resource navigate

## 问题

1、是否需要适配K81、J18系统?

> img：cover处理

> 复用现在样式

2、上线后链接：是否需要客户端处理？redirectUrl？ 待确认 部署新路径

## 接口文档

[装机必备接口文档](https://xiaomi.f.mioffice.cn/docs/dock4PkttaZa8g3VpusLs0z6uc2)

## 开发记录

### 接口联调

- [ ] 装机必备确认给服务端上传中高端机型，跟服务端确认参数字段
- [ ] 接口参数网络字段都要报：ajaxData.netStatus ajaxData.network
- [ ] 机型名称需要服务端转换后传给前端
- [ ] 模块标题需要区分主标题和副标题，主标题加粗

### 前端

- [ ] icon加载低质图片 非wifi环境校验
- [ ] appendAd2App 这个方法的逻辑需要了解清楚
- [ ] 不展示动态icon
- [ ] formatApp时添加了打点，这部分需要移到对应文件处理，不能放在formatApp

```
//deeplink: 点击[打开]优先跳转deeplink链接
  if(elem.ext_deeplink){   
    //兼容详情页
    elem.extraParams =  elem.extraParams || {};
    elem.extraParams.ext_deeplink = elem.ext_deeplink;
    //打点
    elem.reportParams.ext_apm_clickType = 'OPEN_DEEP_LINK';
  }
```

- [ ] 链接中设置setTimeout=1000，若前端没有调用load.stop（具体是啥待确定），客户端会认为页面记载失败，展示网络异常那个页面
- [ ] darkmode模式问题
- [ ] 埋点数据整理
- [ ] 多语言翻译
- [ ] 页面可见性以及网络状态检查
- [ ] appstatus
    - [ ] 在installCb中，有一个window.scrollStop处理，不知道干啥的
    - [ ] 更新已安装app列表逻辑待验证

### 上线前检查项：

- [ ] 语言切换
- [ ] 深色模式:
- [ ] 特殊机型是配：
    - [x] j18 已去掉
    - [x] k81 已去掉入口
- [ ] wifi和非wifi模式
- [ ] 广告打点校验

装机必备线上地址：

https://app.market.xiaomi.com/hd/apm-h5-cdn/cdn-essential-firstV2.html?urlKey=essential-first&lo=CN&customization=ct&cpuArchitecture=arm64-v8a%2Carmeabi-v7a%2Carmeabi&clientConfigVersion=0&resolution=1080*2116&mac=e9cd4e92728879b725ba8dc65a8685c2&network=wifi&loadingViewTimeout=10000&miuiBigVersionCode=11&model=MI+MAX+3&androidId=a86d318209285135db357b552b090018&deviceType=0&miuiBigVersionName=V125&clientId=e9cd4e92728879b725ba8dc65a8685c2&supportPatchVer=0%2C1%2C2&os=V12.5.0.1.QEDCNXM&marketVersion=4002184&densityScaleFactor=2.75&webResVersion=1328&installDay=0&launchDay=0&co=CN&romLevel=24%2C15%2C12&la=zh&androidVersion=10&pageConfigVersion=18474801&newUser=true&sdk=29&ro=ct&device=nitrogen&oaId=eaec7cab9e91d686&activedTimeInterval=13046

## 往期文档

### 装机必备页面功能说明

[首次装机必备（CDN）--待逐步完善](https://xiaomi.f.mioffice.cn/docs/dock4HRq3k5QBORR3TjIQE632eh)