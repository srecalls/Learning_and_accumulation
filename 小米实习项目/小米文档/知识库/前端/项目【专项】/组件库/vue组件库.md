vue组件库

> 📃 背景：

> 以前贡献组件的问题是：每次写完组件，需要自己创建组件，创建demo，创建文档，手动添加路由，手动修改文档的sidebar，手动改changelog内容，修复某个bug的时候，经常会忘记某个步骤。。。并且版本更新没有原则

> 项目地址：https://git.n.xiaomi.com/appstore-frontend/appstore-ui

> 目标：文档方便查看+可预览+支持按需引入+团队协作规范

# 一、成熟组件库优劣分析

## Dev-ui

优点：

1. 通过命令，生成组件模板，包括入口文件、css文件，主要逻辑文件
2. 通过命令，去修改组件引入文件（避免多人同时修改一个文件，合并代码时，有冲突）
3. 通过命令，生成文档中sidebar的部分？？？？这部分还没有实现
4. 通过命令，给组件生成demo文档，这个devui没有实现，但是我以前做过

缺点：

1. 文档和组件分离，不方便维护，最好都放到同一个目录下
2. demo文档里完成了文档和预览逻辑，一方面开发不方便，另一方面，使用的这个方式适合PC端框架，预览模式不能单独抽离出来
3. 样式没有做隔离，没有统一的css规范

汲取优点后的方案：

1. 通过命令，输入组件名，生成组件模板，包括入口文件、css文件，主要逻辑文件、文档模板、demo目录、demo的引入逻辑，均维护在当前组件目录下
2. 通过命令，去修改组件引入文件
3. 预览站点使用iframe内嵌

# 二、架构设计

## 工程搭建

存疑：构建结果：

一个包构建为多个模块支持按需加载 + 1个版本号 VS 构建多个包 + 多个版本号

个人觉得前者好。

1. 构建工具：vite（内置rollup）
2. 包管理工具：lerna ！！！！！？？？？？？？？
3. 框架：vue3+typescript+tsx+less
4. 代码格式化：eslint
5. 提交格式化：husky+lint-staged
6. changelog自动化：conventional-changelog-cli
7. 版本自动化：standard-version

## 组件实现

1. css使用bem规范：B(block)__E(element)--M(modify)
2. css变量单独维护，方便后期主题配置
3. 组件目录：
    1. ComponentA
        1. src
            1. Component.tsx 逻辑实现
            2. Types.ts 类型定义
            3. index.less 样式控制
            4. var.less 变量控制
        2. index.ts 入口文件
        3. README.md 文档说明
        4. demo
            1. index.vue

## 预览

1. 预览站点，监听文件改动，自动生成路由，引入demo文件；
2. 以iframe方式内嵌于文档中
    1. 本地开发模式，可以直接预览localhost下的站点
    2. 生产模式，改为线上预览地址
    3. 进度

- [x] 完成文档路由变动，预览站点路由变动
- [ ] 预览站点路由切换，文档路由切换

## 文档（vitepress vs vuepress）

1. vitepress生成文档，文档更新快、layout可以自己配置
2. changelog自动化

目前的问题：

文档和组件如果想要不分离，需要做一些处理：

组件和文档分离的解决方案： （担心后期不好扩展，而且本地开发）

[https://dewfall123.github.io/vitepress-for-component/guide/config.html](https://dewfall123.github.io/vitepress-for-component/guide/config.html)

- [ ] changelog自动生成到docs目录下
- [ ] 公共文档的书写
- [ ] 文档自动化生成

---vuese 不支持tsx

---vue-styleguidist 需要配置webpack，并且只支持vue2 https://vue-styleguidist.github.io/docs/GettingStarted.html

## 测试

方案：jest + @vue/test-utils

测试用例的书写建议：

1. UI测试，是否按照预期渲染，即是否渲染了正确的dom结构
2. 属性变更，是否正常表现到具体的元素上
3. 业务逻辑触发是否正确，方法调用，传参、以及调用次数是否正确（容易产生错误的地方是否多次执行？？）

## 适配方案

~~rem+vw+媒体查询~~

1. ~~媒体查询界定不同设备宽度设置不同样式，即不同宽度设备下根节点的font-size变动，使用vw为单位进行变化~~
2. ~~书写使用px为单位~~
3. ~~插件进行px到rem的转换~~
4. ~~特殊设备引用方特殊处理~~

以上方案不适用于我们，因项目中已经设置了root的font-size，如果适配方案不一致的话会有冲突

所以最终方案是使用pxTovw

# 三、进展

- [x] 组件初始化：组件自动生成、路由自动生成，导出文件自动生成、sidebar自动生成
- [ ] jsx自动提取关键信息生成文档
- [ ] 预览站点路由切换，文档路由切换
- [x] 自动化测试
- [ ] 
    
    ## 工程搭建
    
    - [x] vite+typescript+tsx+eslint+husky
        - [x] 添加组件做测试
    - [x] 目录结构设计
- [ ] 添加组件
    - [x] bem方法封装2021年10月8日 18:00
    - [x] Swipe组件2021年10月8日 14:00
    - [x] Tab组件2021年10月8日 18:00
    - [x] 敲2021年10月8日 20:00定适配方案
    - [x] 添加Icon组件
    - [ ] 组件文档完善2021年10月9日 20:00
- [x] changelog自动化处理，是否自动化去除冗余commit
- [ ] 组件发布打包
    - [x] 构建分析可视化2021年10月9日 18:00
    - [ ] 寻找优化空间
    - [x] 版本自动化处理、测试
    - [x] 组件目录结构设计
- [ ] 引入文档vitepress
    - [x] 文档结构搭建完成
    - [ ] 文档自动化
- [ ]  预览处理
    - [x] 完成索引目录页面展示、跳转2021年10月8日 14:00
    - [x] 根据组件目录，自动生成路由
    - [x] 将预览部分嵌入文档内部
    - [ ] 预览站点单独发布，可单独预览
- [x] 引用devui的命令，自动生成组件，并做调整
    - [x] 通过命令，输入组件名，生成组件模板，包括入口文件、css文件，主要逻辑文件、文档模板、demo目录、demo的引入逻辑
    - [x] 通过命令，去修改组件引入文件
- [ ] 主题定制探索
- [x] 测试处理

# 四：组件库引入方式

1. 支持按需引入
    1. 按需引入全局注册
    2. 按需引入局部注册
2. 支持全局引入
    1. 全局引入全局注册 import appstoreUI from 'appstore-ui' app.use(appstoreUI)

# 五、相关资料

1. 文档组织结构：[https://github.com/jrainlau/vue-donut/tree/mobile](https://github.com/jrainlau/vue-donut/tree/mobile) [https://segmentfault.com/a/1190000009660650](https://segmentfault.com/a/1190000009660650)
2. Dev-ui：https://gitee.com/rainydaydy/vue-devui 主站：https://juejin.cn/user/712139267650141/posts
3. 文档预览参考：https://juejin.cn/post/7005355551928352776
4. vite官方：https://cn.vitejs.dev/guide/features.html
5. jsx语法参考：https://github.com/vuejs/jsx-next
6. lerna最佳实践：https://github.com/LittleBreak/lerna-best-practices https://juejin.cn/post/6844903568751722509
7. vuepress VS vitepress https://cloud.tencent.com/developer/article/1741239
8. 工程化版本控制：https://jelly.jd.com/article/5f51aa34da524a0147e9529d
9. 组件库文档工具优劣对比 https://segmentfault.com/a/1190000039931429

背景

1. 逻辑和UI耦合严重，无法复用
2. 有相似交互和样式的部分无法立刻找到demo查看，需要去查逻辑
3. 每次新的业务需求都需要重新开发组件
4. 组件是否可以复用需要去熟悉具体的代码
5. 原来的组件没有做样式隔离，相同类名不断覆盖，非常不利于后续维护

# 对象：产品+运营+设计

目的：其他业务组知道前端都做了哪些事

我们做了一个组件库，组件库中目前包含了这么多组件