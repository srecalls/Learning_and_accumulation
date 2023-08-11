

## [](https://git.n.xiaomi.com/xiaomi-appstore/dev.mi.com-cms-fe#start)start

npm install npm start

## [](https://git.n.xiaomi.com/xiaomi-appstore/dev.mi.com-cms-fe#online)online

npm run build

## [](https://git.n.xiaomi.com/xiaomi-appstore/dev.mi.com-cms-fe#%E5%9B%BD%E5%86%85%E5%BC%80%E5%8F%91%E8%80%85%E7%AB%99%E5%90%8E%E5%8F%B0)国内开发者站后台

## [](https://git.n.xiaomi.com/xiaomi-appstore/dev.mi.com-cms-fe#%E6%8A%80%E6%9C%AF%E9%80%89%E5%9E%8B)技术选型

1. cra + react-app-rewired + customize-cra + braft-editor
2. 前端框架选用 `React`
3. router 方案 `React Router`
4. UI 框架选用了 `Ant Design(3.x)`
5. 打包`webpack`

### [](https://git.n.xiaomi.com/xiaomi-appstore/dev.mi.com-cms-fe#commit%E6%8F%90%E4%BA%A4)commit提交

npm run commit / git cz

### [](https://git.n.xiaomi.com/xiaomi-appstore/dev.mi.com-cms-fe#%E9%A1%B9%E7%9B%AE%E9%83%A8%E7%BD%B2)项目部署

1. [测试环境部署](https://cloud.mioffice.cn/#/product/deploy-system/task/create?action=create&jobId=3757)
2. [生产环境部署](https://cloud.mioffice.cn/#/product/deploy-system/task/create?action=create&jobId=3799)
3. [Preview 环境](https://cloud.mioffice.cn/#/product/deploy-system/task/create?action=create&jobId=3791)
4. 开发环境启动
    1. 安装 [whistle](https://wproxy.org/whistle/)
    2. 使用 chrome 的 SwitchyOmega 插件代理本地请求，具体过程参考 whistle 的文档
    3. 代理配置如下

```
# 开发环境，ip(10.38.160.81) 地址为服务端的 ip
# onebox.appadmin.pt.xiaomi.com/doc-api 10.38.160.81
# onebox.appadmin.pt.xiaomi.com 127.0.0.1:8080

# preview 环境
# 两台机器 10.132.35.52 10.132.35.53
preview.appadmin.pt.xiaomi.com/doc-api/ 10.132.35.53
preview.appadmin.pt.xiaomi.com 127.0.0.1:8080
```

### [](https://git.n.xiaomi.com/xiaomi-appstore/dev.mi.com-cms-fe#%E5%BC%80%E5%8F%91%E5%B7%A5%E4%BD%9C%E6%B5%81)开发工作流

目前开发者cms后台采用不定期发版的方式（每周一、四有已测试需求则发版）进行项目的迭代维护，发版流程

> 需求评审 ---> 需求开发 ---> 需求测试 ---> 全量发布

为此，前端开发也制定了对应的工作流，下面举例说明，例：2020/05/20 将要发布某个版本

1. `dev-test` 分支，为最终提测、发布分支
    
2. 开发需求`mode-function`，从 `master` 分支 checkout `wurong-mode-function` 开发完成后`merge`进入`dev-test`
    
3. 版本发布：在`dev-test` 分支
    
    1. 定义版本号：修改 `package.json` 的 `version` 字段，例如：`version: 0.9.6-0`
    
    > 版本号采用语义化版本号即：major.minor.patch-build 的形式
    
    2. `npm run commit` 调起标准commit，运行`npm run prerelease` 则会自动增加 `build` 号，方便测试反馈 bug 的定位跟踪
    3. 提测 ---> 2 ---> 3
    4. 向 `master` 发起 `Merge Request` （`dev-test`分支）
    5. 在`master`分支运行 `npm run release`
    6. 部署发布