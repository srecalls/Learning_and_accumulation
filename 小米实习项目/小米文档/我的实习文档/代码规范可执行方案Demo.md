## 问题分析

（由于早期没有统一的代码基本规范或开发人员没有相关代码规范方案或未严格遵守[前端代码规范方案](https://xiaomi.f.mioffice.cn/wiki/wikk4HWbcQ4AgYHzXlq7Zn9Pvcc#wGebzm)严格执行的原因 ，导致在【开发者站】及【国内开发者运营后台】项目编译运行过程中出现大量Eslint Warnning警告
![[代码规范可执行方案Demo.png]]
  

![[代码规范可执行方案Demo-1.png]]![[代码规范可执行方案Demo-2.png]]

- 可能会导致**后续开发过程**中编写的代码**无法直观**从终端中看到代码错误规范的编写，从而**选择性忽视错误规范的代码**
    （comment：不按照规范编写会有什么问题？或者说为什么需要统一的规范？）

- 且部分错误规范的代码无法轻易从Code Review中获取，**例如在函数花括号前未增加空格等易在CR忽略的问题**
    （comment： 规范有两种，一种是格式规范，比如缩进有几个空格；还有一种是代码规范，比如useEffect的依赖数组缺少依赖项
这两种规范各自的作用、风险大小都不完全相同）

![[代码规范可执行方案Demo-3.png]]
- 上类问题一方面会导致开发人员对于交付的代码存在忽略与轻视，降低代码质量的同时可能会造成项目无法正常交付的问题
    
- 统一的代码规范有助于项目代码理解、修改和扩展、减少潜在bug的发生，减少项目的错误崩溃
    

## 需要解决的问题

主要问题：减少项目运行过程中的Eslint Warning，

扩展性：按照方案执行之后是否易拓展（比如目前的代码缩减是2个空格，改成4个空格后方案是否依然有效）

影响度：现有方案进行代码规范之后是否会影响现有项目的运行，是否会导致bug的增多

执行难度：是否需要消耗大量时间与资源去执行此方案，对于未规范的代码应该如何处理，对于以后的代码应该做何处理

  

## 解决手段

对于以前的代码，当开发人员根据需求对此前文件进行改动的时候，根据现有的规范要求进行代码规范的重构，逐步减少此前代码的不规范问题，同时能够让测试与产品人员进行需求范围内的测试与验收。

对于以后开发的代码，按照代码规范进行编写，并通过下列技术进行检查与评估。

## 技术实现

> ESLint
> 
> - (ES -> ECMAScript)
>     
> - Lint -> Lint 是静态代码分析工具的计算机科学术语，用于标记编程错误、错误、样式错误和可疑结构。(**Lint** is the computer science term for a static code analysis tool used to flag programming errors, bugs, stylistic errors and suspicious constructs)
>     

1. ### 统一的代码规范方案
    

  

目前的项目代码规范：无明确项目代码规范方案，根据项目.eslintrc.js，结合extends内核心规则以及rules内自己配置的相关规则，进行代码开发，且部分项目的.eslintrc内的规则存在差异，不能实现统一。

目标项目代码规范：严格针对前端代码规范方案制定Vue项目与React项目对应的代码规范方案，根据制定好的代码规范，配置与代码规范相对应的Eslint文件，实现每个项目代码规范的统一。

  

2. ### 编写代码时自动格式化成规范代码
    

作用：利用eslint 进行 规则代码的配置，prettier

`--fix`

此项指示 ESLint 尝试修复尽可能多的问题。这些修复是对实际文件本身进行的，只有剩余的未修复的问题才会被输出。

- **参数类型**：不支持参数。
    

不是所有的问题都可以用此项来修复，在这些情况下，此项不起作用：

1. 当代码通过 pipe 传递给 ESLint 时会抛出错误。
    
2. 此项对使用处理器的代码没有影响，除非处理器选择了允许自动修复。
    

如果你想从 `stdin`（标准输入，std means standard, in means input) 中修正代码，或者想在不实际写入文件的情况下进行修正，请使用 `[--fix-dry-run](https://zh-hans.eslint.org/docs/latest/use/command-line-interface#--fix-dry-run)` 项。

```TypeScript
Fixing problems://修正问题
  --fix                          Automatically fix problems//自动修复问题
  --fix-dry-run                  Automatically fix problems without saving the changes to the file system//自动修复问题而不保存对文件系统的更改
```

`--fix` 示例

```Shell
npx eslint --fix file.js
```

  

方案一、仅利用Eslint去配置格式化代码

在VsCode的设置(setting.json)中进行如下配置

```JSON
 //关闭VSCode在Save时候自动格式化，因为VSCode自带的格式化和ESlint规范并不兼容
 "editor.formatOnSave": false,
 //代码保存时，自动执行ESlint格式化代码
 "editor.codeActionsOnSave": {
   "source.fixAll.eslint": true,
 },
 // 配置 ESLint 检查的文件类型
 //"eslint.validate": ["javascript","vue","html"]
```

存在问题：部分风格检查无法实现

目前【开发者站】与【国内开发运营后台】Eslint文件存在的已知的配置问题如： （无法通过Eslint的fix进行修复）

- 单行长度不得超过100，超过需要换行。（风格检测）
    

![[代码规范可执行方案Demo-4.png]]

- 依赖循环 （质量检测）
    

![[代码规范可执行方案Demo-5.png]]
> 
![[代码规范可执行方案Demo-6.png]]
> 
![[代码规范可执行方案Demo-7.png]]

- 已声明，但是未读取其值 （质量检测）
    

> ![[代码规范可执行方案Demo-8.png]]
- 未采用驼峰命名 （风格检测）
    

> ![[代码规范可执行方案Demo-9.png]]
  

- 期望此表达式之前没有换行符（风格检测）
    

> ![[代码规范可执行方案Demo-10.png]]

  

方案二、利用Eslint和prettier插件配置

> 目前eslint的配置只提供了部分风格修复，但是这导致有部分的代码依然没有实现风格修复。

- **ESLint主要负责: 质量检查(例如使用了某个变量却忘记了定义)、风格检查**
    
- **Prettier主要负责: 风格检查, 没有质量检查**
    

> 全局下载：包安装在Node安装目录下的node_modules文件夹中
> 
> 本地下载：包安装在指定项目的node_modules文件夹下（修改项目文件）

1. 在全局下载`eslint-config-prettier`，使用该插件关掉与Prettier产生冲突的ESlint格式相关配置
    

```undefined
npm i eslint-config-prettier -g
```

2. 通过ESlint来自动保存,就要把Prettier的修复通过ESlint来体现, 就需要`eslint-plugin-prettier`配置（全局下载）
    

```Plain
npm i eslint-plugin-prettier -g
```

3. 在`.eslintrc.js`中进行配置
    

```Java
module.exports = {
    "env": {
        "browser": true,
        "es2021": true
    },
    "extends": [
        "eslint:recommended",
        "plugin:react/recommended",
        'plugin:prettier/recommended' // 进行配置，一定要放在最后用于覆盖之前的规则
    ]
}
```

4. 在根目录新建`.prettierrc.json`，根据代码规范对`prettier`进行配置
    

```undefined
// 这里需要根据制定的项目代码格式进行配置。
```

5. 在`gitignore`进行配置，忽略`.prettierrc.json`的提交
    

```Bash
# misc
.prettierrc.json
```

这一步后可以在代码编写进行保存后，对代码进行风格修复和一部分的质量修复。

```JSON
    // 继承，顾名思义，继承其他配置的规则
    "extends": [
        "plugin:react/recommended",
        "airbnb"
    ]
```

这里只能进行一部分质量修复是因为prettier只针对风格问题进行修复（代码格式），不针对质量问题代码进行修复，而依靠目前继承的规则只能完成部分质量修复。

3. ### 提交时检测规范代码
    

方案:Husky + git hooks

1. 全局下载安装Husky
    

```undefined
npm install Husky -g
```

2. **启动Husky**
comment：启动的作用是什么，为什么不能直接用，要启动
comment：Husky是一个工具，它允许我们轻松地处理Git Hooks 并在提交代码时运行我们想要的脚本。

```undefined
Husky install
```

3. 添加 `commit` 时的 `hook` （`npx eslint --ext .js --ext .jsx src` 会在执行到该 hook 时运行）
    

```Bash
## 针对目前【开发者站】与【国内开发者站运营后台】
## ESLint默认只会检查.js后缀的文件，如果还有其它后缀我们需要使用--ext来指定
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

npx husky add .husky/pre-commit "npx eslint -fix --ext .js --ext .jsx src"
```

4. 在`gitignore`进行配置，忽略`.husky`的提交
    

```Bash
# misc
.husky
```

如果不进行配置上述方案会针对所有文件夹进行检查，接下来要实现对目标文件夹进行Eslint检测

方案一、利用`lint-staged`插件

1. 全局下载`lint-staged`
    
2. 配置`.lintstagedrc.js`文件
    

```Java
// .lintstagedrc.js
module.exports = {
  "src/**/*.{js, jsx}": [
    "eslint --fix",
    "git add"
  ]
}
```

3. 这里就要修改`husky`了，让他执行`lint-staged`指令执行`lint-staged`
    

```Bash
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

lint-staged
```

4. 记得这里也要在`.gitignore`文件里配置忽略`.lintstagedrc.js`
    

```Bash
# misc
.husky
.prettierrc.json
.lintstagedrc.js
```

方案二、采用`.eslintignore`对目标文件夹进行扫描

```undefined
src/*
!src/pages/xxx
```

5. 针对报错的质量问题代码进行逐个修改
    

4. ### 提交完毕检测规范代码（CR）
    

Code Review对提交完的代码进行检查

这里可以在CI/CD再针对提交的代码进行检测

## 潜在问题

1. `node`版本切换之后全局下载的包需要重新下载
    
2. 如何制定`react`和`vue`项目的代码规范（投票选出最多的吗）
    
3. 如何监控项目内开发人员严格按照方案的进行。
    
4. 对pretter再进行一下配置，会有人忘记save，就不能格式化。
    

  

  

  

Eslint -> 规范代码 -> 提升代码质量 -> 不按照代码规范来也可以通过

为规范项目代码，提升代码质量，本方案对目前项目采用Eslint工具进行代码进行规范检测存在的“不符合规范的项目代码亦可通过检测”问题而针对开发过程、提交过程