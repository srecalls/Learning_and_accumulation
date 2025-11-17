## 项目相关工具（当前阶段）

背景与原因：

- 旨在前端团队项目的规范自动化生成与自动化补齐
- 增加代码可读性，后来人接入成本更低
- 商店前端从代码规范到git commit到部署，有统一标准与流程
- 为商店前端项目定制化脚手架做准备

#### 代码规范

- eslint+prettier公用规范（平台无关性） 【待开发】
    - 后续会扩展开发vue+ts 、react+ts 独立规范
- git commit flow 规范（@mi/commition[git hooks + lint-staged + commition标准校验]） 【已完成】
- 编辑器配置文件.editorconfig等 【开发中】

#### CI继承规范

`流程交互式`添加自动化ci/cd配置模版

- .apollo.yml 模版生成配置[文档]【待开发】
- .gitlab-ci.yml 模版生成配置【待开发】

#### 架构规范（详细文档整理中）

- 目录架构生成CLI （对应不同应用场景与技术栈）[目前在整理中台+react17]
    - 中台、C端
    - Vue3、React17
- 自动化配置及环境变量定义，例如（development，staging/preview，production，test区分等）

## 中台项目脚手架（后期规划）

#### 脚手架流程

- 运行@mi/appstore-front-cli `npx appstore-front-cli`
- 选择vue或者react项目 【后续如果统一中台技术框架则没有改步骤】
- 官方cli执行`vue3-cli` 或`react-cli`
- 代码规范生成eslint+prettier、lint-staged、.editorconfig等等文件生成
- 目录与中台自定义方案生成，（目录、router、数据管理、service、config（环境变量）、npm scripts）模版化生成
- 询问gitlab地址，并初始化git init
- 安装git commit流程规范
- 选择自动化部署平台`融合云`与`MICE` ；并开始询问式模版初始化
- 完成

#### 方案：官方CLI + 自研规范CLI

vue2/3

Vue CLI + ElementUI + Typerscript + AppstoreFrontCLI

React17

CreateReactApp CLI + Ant + Typerscript + AppstoreFrontCLI