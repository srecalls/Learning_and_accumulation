appstore-ui

# 背景

我们团队最近技术栈升级到了vue3，但是还没有一套文档清晰可实时预览的移动端组件库可以使用，目前有很多团队都在做组件库，也有很多团队也都升级到了vue3，但是作为系统级应用的开发者，对适配的要求比较高，所以，很多组件很难拿过来直接用，所以我们就打算自己做一套。

# 快速开始

组件库文档：https://appstore-ui.market.pt.xiaomi.com/docs/

预览站点：https://appstore-ui.market.pt.xiaomi.com/#/

## 使用

https://appstore-ui.market.pt.xiaomi.com/docs/

## 贡献

https://appstore-ui.market.pt.xiaomi.com/docs/contribution.html

# 思路

作为组件库这样的工程，其实是一个比较大的工程，需要做的工作很多，不是拿一个脚手架贡献点组件，然后打包发布npm那么简单。

做之前考虑的也比较多。但保持一个目标不变就是正确的，我们希望团队中使用这个工程的人可以快速的上手，所以要保证：

- 文档清晰
- 可实时预览

对于业务方，要保证：

- 可按需引入和全量引入
- 组件可靠
- 尽量轻量

对于贡献者，要：

- 统一风格和规范
- 快速进入逻辑的开发
- 减少维护的工作量

暂时无法在文档外展示此内容

# 如何搭建

在做一个组件库之前，准备工作其实很多，要列好方向，首先列一个大的方向，然后从大的方向里列出具体的点，就像实现一个产品一样，从具体的点里再筛选出一部分来，完成一个mvp版本。

首先第一步就是考虑用户是谁，要做成什么样的产品拿出来用，所以根据这样的需求列出要实现的功能，就不难了。

根据功能划分，将组件库分为以下几大模块：

1. 构建、发布
2. 组件设计和实现
3. 文档系统
4. 预览系统
5. 自动化测试
6. 协作规范

## 构建

### 构建工具

构建方案：vite （https://vitejs.dev/guide/）

为什么用vite？https://cn.vitejs.dev/guide/why.html

1. 开发效率高，冷启动和热更新都快
2. 内置rollup，适合打包库文件

vite是一种新型前端构建工具，能够显著提升前端开发体验。由两部分构成：

- 一个开发服务器，它基于 [原生 ES 模块](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) 提供了 [丰富的内建功能](https://cn.vitejs.dev/guide/features.html)，如速度快到惊人的 [模块热更新（HMR）](https://cn.vitejs.dev/guide/features.html#hot-module-replacement)。
- 一套构建指令，它使用 [Rollup](https://rollupjs.org/) 打包你的代码，并且它是预配置的，可输出用于生产环境的高度优化过的静态资源。

vite还比较新，但是也出来1年多了，有很多团队都在用，没有选择vue-cli这种现成的脚手架是因为本身也是使用webpack配置的

当前影响我们开发效率的一个重要因素就是随着项目规模的增加，无论是本地开发还是构建打包的时间都会增加。尤其是改bug的时候，这种时间就会被凸显出来，而vite就是解决这样的问题的。

而且rollup的tree-shaking做的要比webpack好

### 框架

方案：vue3 + Typescript

这点毋庸置疑，因为我们要支持的就是vue3项目，而为了更好的支持Typescript，我们采用jsx的方式去实现组件，而不是SFC的方式。

问：组件书写采用tsx的方式，而不是SFC的形式

答：虽然一定程度上未使用vue3对template静态标记带来的性能优化，但是作为工具类库，正确严谨更重要，使用tsx的好处：（https://juejin.cn/post/6911175470255964174）

1. Typescript原生支持JSX，对于SFC组件，TS 是不知道这个组件的 Props 应该接收什么的，而TS的优势是：

- 开发时的自动提示
- 编译时的 TS 校验，让你尽早发现问题
- 编译组件生成你的组件定义（对于类库开发尤其重要）

2. 更好的使用js的方法，而不是使用指令

### 目录设计

作为一个lib工程，最关键的就是目录设计，一方面方便贡献，另一方面方便打包。

大体分为三部分：

1. 组件
2. 文档
3. 预览

组件部分，比较好的方式就是和组件相关的都在这个组件目录，包括：

1. 组件实现
2. 类型定义
3. demo
4. 文档
5. 测试用例

目前因为vitepress有规定好的文档目录，所以组件的文档没有和组件在同一目录下。

#### 组件目录

Component

│ ├── __tests__

│ │ └── Component.spec.js 测试用例 // 具体的名字可以更方便的对组件进行单元测试

│ ├── demo

│ │ └── index.vue demo演示

│ ├── index.ts 入口文件

│ └── src

│ ├── Component.tsx 逻辑实现

│ ├── Types.ts 类型定义

│ ├── index.less 样式控制

│ └── var.less 变量控制

├── config.ts 组件配置信息

为了团队规范和协作，所以这部分内容会自动生成。这里参考了最近掘金和B站都比较热的开源组件库dev-ui的做法

导出组件的时候用两种导出方式， export {}和exprot default的方式

#### 文档目录

这部分一般使用的文档系统都会有规定好的目录形式，统一放到docs目录下。

### 工程规范工具

1. 版本管理 standard-version
2. 代码格式管理 eslint
3. commit管理 husky+lint-staged （@mi/commition）
4. changelog自动生成 standard-version

### 预处理器以及css规范，适配方案

按照使用习惯，选择less

#### CSS规范

确定好css命名规范，BEM，对于组件库来说很重要，因为css如果命令没有处理好的话就会引发样式问题，还有最终打包体积的问题

思考？

1. 如何比较好的去应用bem，而不是人为去约束
2. 如何更方便的给dom添加css

借鉴了vant的做法，创建namespace的方式：B(block)__E(element)--M(modify)

```
const [name, bem] = createNamespace('tabs'); // 每个组件有为一个block
 <div class={bem('bar-wrap')}></div> // bar-wrap 为element，会自动转换为 .mi-tabs__bar-wrap
 <div class={bem('bar', { fixed })}></div>  // fixed为modify，会自动转换为 .mi-tabs__bar--fixed
```

#### 适配方案

~~rem+vw+媒体查询~~

1. ~~媒体查询界定不同设备宽度设置不同样式，即不同宽度设备下根节点的font-size变动，使用vw为单位进行变化~~
2. ~~书写使用px为单位~~
3. ~~插件进行px到rem的转换~~
4. ~~特殊设备引用方特殊处理~~

以上方案不适用于我们，因项目中已经设置了root的font-size，如果适配方案不一致的话会有冲突

所以最终方案是使用pxTovw

### 构建方案

#### 组件导出

组件其实就是插件，所以在导出的时候要为每个组件添加install方法。

#### 构建

vite内置了rollup，可以配置输出为lib的库文件

引用方按需加载，输出方就要输出多个文件，用哪个文件最终哪个文件就会被打包。

所以在打包的时候要以两种方式打包，这样引用方就可以根据需要选择引入方式

1. 全量构建
2. 单独构建：遍历组件目录

引用方使用babel-plugin-import，所以对输出文件的名称要小写

#### 构建兼容

0.0.30版本前支持的浏览器

![](https://xiaomi.f.mioffice.cn/space/api/box/stream/download/asynccode/?code=NGU0NGJmNzE5NTU5Yzc3MmQ5YWY5MTU3MGJlYTY1OGZfSDZQM1UxcWIyTDAwb0ZLMXBKZGdjZTlvcjdVcmdMRTNfVG9rZW46Ym94azRaamxQWkNYaVdrU1JxWmlSZFVjTFNkXzE3MDE0MDg5MzA6MTcwMTQxMjUzMF9WNA)

之后支持改为es2015 相当于chrome 58

### 发布

最终发布的文件是lib目录下的文件，需要配置packgage.json中的files为lib

使用 standard-version做版本控制，发布时会自动生成CHANGELOG

执行npm run publish即可

### 部署

文档和预览站点需要部署到云平台上。

#### 部署MICE

1. 融合云创建应用

https://cloud.mioffice.cn/#/product/container/app/detail?cluster=c4&namespace=cl75322&appid=10510

#### 接入CICD

配置job

1. prepare 安装依赖
2. build 打包

合入master分支时自动触发build

1. build预览包
2. build文档包（vitepress未暴露outDir）
3. 整理build后目录

#### 申请域名

向运维提jira，申请文档访问域名

#### 静态服务配置

构建完成后，启动线上静态文件的服务，配置访问路径

构建完成后目录：

```
public
├── demo
│   ├── assets
│   └── index.html
├── docs
│   ├── assets
│   ├── contribution.html
│   ├── index.html
│   └── logo.svg
└── favicon.ico
```

文档和预览站点均在public目录下

使用express起静态服务：

1. 默认访问的是预览
2. 访问/docs即可访问文档

遇到问题：

demo配置history路由，如何访问正常

## 自动化测试工具

jest @vue/test-utils

这个比较容易，使用业界通用方案即可，@vue/test-utils也支持了tsx语法的组件

对于UI组件，需要测试是否正常渲染，改动是否有影响，jest提供了快照的功能，可以记录组件渲染后的dom结果

需要处理的：

模拟touch事件

模拟滚动事件

## 文档系统

文档系统的组成：

1. 分组明确的目录结构
2. 容易操作的demo演示
3. 对应的代码演示
4. 使用说明

3，4两点需要开发人员去维护

1，2两点则需要在选择文档系统的时候做设计

### 如何选择文档系统

vitepress 轻量的文档库，使用vite构建，文档更新快、layout可以自己配置。

有很多文档系统可以选择，docz、storybook、vuepress，最终选择 vitepress是因为基于vite，热更新快，而且轻量，可配置，可以自己扩展一些组件。

缺点是还不是很成熟，可以参考的东西比较少，所以花了些时间，而且觉得这种目录设计不太合理，文档和组件分离。

### 开发人员如何产出文档？

组件的文档产出问题：手动输出文档容易出错而且耗费精力

理想情况是：根据组件添加的注释自动生成文档

vue2中可以使用的工具，vue-styleguidist，但是需要配置webpack

vue3中可以使用vueuse，但是只支持SFC的写法，jsx还不支持

## 预览系统

### 方案选择：iframe

移动端组件库的预览一般都是通过iframe内嵌文档的方式展示的，而PC端组件库的预览一般是demo和代码块都展示在文档里，预览demo的时候就可以找到对应的代码展开。

猜想：移动端的组件有一些触摸效果，而且视觉上就是一个手机上展示不同的效果（比如一些动画），所以用iframe更合适。

### 实现iframe内嵌文档

vitepress很好的是可以自己扩展组件，所以把他的主题拷贝一份就可以直接修改布局，在layout右侧添加了一个RightDemo的组件：

1. 内嵌iframe
2. 监听文档路由变化，iframe的src指向不同组件的地址
3. 区分开发和编译两种环境，iframe的指向不同域名，方便本地实时预览组件
4. 监听组件内部路由变化，更新文档路由 （未完成）

这样的好处是我们不需要在文档中去引入demo，处理demo，书写文档的时候就纯粹的去写markdown就可以

而且vitepress很方便的是，我们可以像正常开发一个vue项目一样去使用它。

我们可以在vite.config.js里注入我们要使用的全局变量

```
vite: defineConfig({
    define: {
      DOC__GLOBAL: {
        mode: process.env.mode, // 可以在此处定义一些全局变量
      },
    },
 }),
```

它也内置了一些常用的全局变量，比如import.meta.env.MODE 可以获取当前的mode是development还是production。

vitepress的上手成本比较低，熟悉vue就可以快速的上手。

### 预览效果输出

这个很容易，因为我们本身就是一个项目，开发了很多组件，组件输出了demo，所以只要用路由把这些demo关联起来就可以。总结下来需要做的就以下两点

1. 路由设计
2. 预览站点首页展示所有组件demo的索引

路由文件容易冲突，所以自动生成。

为了更好的将代码示例和demo效果联系起来，同时为了方便写demo，所以需要开发一些组件来控制整个预览站点的样式

1. DemoBlock组件
2. ListItem组件

## 协作规范

> 背景：

> 以前贡献组件的问题是：每次写完组件，需要自己创建组件，创建demo，创建文档，手动添加路由，手动修改文档的sidebar，手动改changelog内容，修复某个bug的时候，经常会忘记某个步骤。。。并且版本更新没有原则

最小维护成本方案

目标：不依靠文档规范贡献者的行为，同时提升创建组件的速度。

方案：

1. 自动创建符合规范的目录和模板
2. 自动创建容易产生冲突的文件，减少MergeRquest时解决冲突的时间

## 组件设计和实现

原则：先设计，再实现。

建议：

1. 先写文档
2. 定义类型
3. 实现组件