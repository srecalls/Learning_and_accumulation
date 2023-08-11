# 国内开发者站

## 项目介绍

[国内开发者站](dev.mi.com) 前端

[仓库地址](https://git.n.xiaomi.com/xiaomi-appstore/appstore-developer-web-fe)
## 技术选型

1. 前端框架选用 `React`

2. router 方案 `React Router`

3. UI 框架选用了 `Ant Design(3.x)`

## 前端技术方案

- todo
## 项目构建

### 脚手架


采用了 `CRA`，定制化**未**通过 `eject` 方式，而是选用[customize-cra](https://github.com/arackaf/customize-cra) 定制。

  
> 已知问题及 Workaround：（css loader支持）https://github.com/arackaf/customize-cra/issues/201

### 项目部署

1. [测试环境部署](https://cloud.mioffice.cn/#/product/deploy-system/task/create?action=create&jobId=4397)

2. [生产环境部署](https://deploy.pt.xiaomi.com/services/65323/task/index)

3. 开发调试
##### 开发环境、测试环境、生产环境
```js
软件开发环境(Software Development Environment，SDE)是指在基本硬件和宿主软件的基础上，为支持系统软件
和应用软件的工程化开发和维护而使用的一组软件，简称SDE。它由软件工具和环境集成机制构成，前者用以支持软件开发
的相关过程、活动和任务，后者为工具集成和软件的开发、维护及管理提供统一的支持。

_项目部署环境一般可分为三种：生产环境，测试环境，开发环境_

开发环境：开发环境时程序猿们专门用于开发的服务器，配置可以比较随意，为了开发调试方便，一般打开全部错误报告和
测试工具，是最基础的环境。开发环境的分支，一般是feature分支。

测试环境：一般是克隆一份生产环境的配置，一个程序在测试环境工作不正常，那么肯定不能把它发布到生产服务器上，是
开发环境到生产环境的过度环境。测试环境的分支一般是develop分支，部署到公司私有的服务器或者局域网服务器上，
主要用于测试是否存在bug，一般会不让用户和其他人看到，并且测试环境会尽量与生产环境相似，一般staging分支。

生产环境： 生产环境是指正式提供对外服务的，一般会关掉错误报告，打开错误日志，是最重要的环境。部署分支一般为
master分支。

三个环境也可以说是系统开发的三个阶段：开发->测试->上线，其中生产环境也就是通产说的真实的环境，最后交给用户
的环境。
```

- 开发工作流切换至 Whistle(前端代理) + SwitchyOmega(浏览器插件)

##### 代理原理
```js
原：



现：

```

- 启动流程

```bash

npm start # 启动工程

w2 start # 需要安装 whistle，具体配置方式可见(whistle官网)[https://wproxy.org/whistle/install.html]

访问：http://onebox.developer.mi.com，可供使用的公共账号: userName: rangaopan@baidu.com password:xiaomi123
```

- whistle 配置

``` bash
## 10.38.160.81 为 stagingb

onebox.developer.mi.com/uiueapi 10.38.160.81

onebox.developer.mi.com/callback 10.38.160.81

onebox.developer.mi.com/sts 10.38.160.81

onebox.developer.mi.com 127.0.0.1:8080
```
### 开发工作流

目前开发者站采用定期发版的方式进行项目的迭代维护，发版流程


> 需求评审 ---> 需求开发 ---> 需求测试 ---> 灰度发布 ---> 全量发布

##### 什么叫灰度测试
```js
简介： 灰度测试是什么意思呢？如果对互联网软件研发行业不太了解的话，可能对这个词还是很陌生的，其实灰度测试就
是指如果软件要在不久的将来推出一个全新的功能，或者做一次比较重大的改版的话，要先进行一个小范围的尝试工作，然
后再慢慢放量，直到这个全新的功能覆盖到所有的系统用户，也就是说在新功能上线的黑白之间有一个灰，所以这种方法也
通常被称为灰度测试。

https://developer.aliyun.com/article/710854#:~:text=%E5%A6%82%E6%9E%9C%E5%AF%B9%E4%BA%92%E8%81%94%E7%BD%91%E8%BD%AF%E4%BB%B6,%E8%A2%AB%E7%A7%B0%E4%B8%BA%E7%81%B0%E5%BA%A6%E6%B5%8B%E8%AF%95%E3%80%82
```

##### 开发流程
```js
1.先拉取master分支代码
2.基于master分支 另开 feat/需求 分支 进行需求的开发
3.开发完毕进行提测前的CodeReview
4.CodeReview完毕将代码合并入staging分支
5.部署到测试环境
6.测试环境测试完毕，将staging分支合并如release分支 （release分支一般命名为'release/2023/07/31' ）
7.部署生产环境
8.进行灰度测试
9.测试完毕进行全量发布
10.测试通过，将release分支合并（git rebase）进入master分支
```

##### commit类型
```
commit 的类型：

- feat: 新功能、新特性
- fix: 修改 bug
- perf: 更改代码，以提高性能（在不影响代码内部行为的前提下，对程序性能进行优化）
- refactor: 代码重构（重构，在不影响代码内部行为、功能下的代码修改）
- docs: 文档修改
- style: 代码格式修改, 注意不是 css 修改（例如分号修改）
- test: 测试用例新增、修改
- build: 影响项目构建或依赖项修改
- revert: 恢复上一次提交
- ci: 持续集成相关文件修改
- chore: 其他修改（不在上述类型中的修改）
- release: 发布新版本
- workflow: 工作流相关文件修改
```




为此，前端开发也制定了对应的工作流，下面举例说明，例：2021/11/01 将要发布某个版本

1. 从 `master` 分支 checkout 对应 release/2021/11/01 分支，此分支为最终提测分支

> 采用 `/` 分割的好处是很多 git 软件会根据 / 将分支归类，比较方便管理

2. 开发需求X，从 `master` 分支 checkout `feat/X` 开发完成后`merge`进入`release/2021/11/01`

3. 版本发布

1. 定义版本号：修改 `package.json` 的 `version` 字段，例如：`version: 0.9.6-0`

> 版本号采用语义化版本号即：major.minor.patch-build 的形式

2. 运行``npm run prerelease`` 则会自动增加 `build` 号，方便测试反馈 bug 的定位跟踪

3. 提测 ---> 2 ---> 3

4. 测试完成后，打上 release tag（运行 ``npm run release``）

5. 部署发布

6. 待功能稳定，MR 进入 Master 并清理 release 分支



### TODO

1. 采用 react-error-boundary 优雅的处理页面异常

2. 统一封装 request 对 response code 的处理逻辑

3. 应用/游戏代码同构

4. 对于上传文件/图片的 URL 统一封装处理，目前部分全路径，部分 Hash 返回

5. 面包屑导航关于 namespace 问题的处理

6. 统一 history.push 以及路由字面量的管理


##### 无关内容（自己写的）
自己注释用 **五级标题（#####）** 表示


```js

```