1. ## 需求背景


TS优势：随着前端开发的不断发展，TypeScript 作为JavaScript 的超集，具有静态类型检查、更好的代码可维护性和可扩展性等优势，逐渐成为主流的前端开发语言。

JS劣势：随着项目的不断演进和规模的扩大，JS的动态性和灵活性可能会导致一些问题。例如，由于缺乏静态类型检查，开发人员在编写代码时容易出现类型错误，这可能导致在运行时出现潜在的错误。此外，当项目变得复杂时，缺乏明确的类型定义和模块化可能导致代码难以理解、维护和扩展。

为了解决这些问题，团队决定将现有的JS项目迁移为TS项目。

2. ## 设计考虑
    

稳定性：由于当前项目规模较大，在迁移过程中，由于需要对原有正常JavaSript文件进行修改会影响项目的稳定性，从而导致项目无法正常运行。

兼容性：一些第三方库可能没有提供类型定义文件，或者使用了不兼容的模式和语法。在迁移过程中，需要评估这些库的替代方案或者手动编写类型定义文件，以确保整个项目的顺利迁移和正常运行。

影响率：由于项目基于JavaScript语言进行编写，将项目进行TypeScript语言迁移可能对开发人员造成开发困难，影响开发效率，同时由于需要对修改后的项目文件进行测试，可能导致测试成本的上升。

3. ## 技术方案
    

### **混合迁移策略（☑️）**

**混合迁移**策略：对开发过程中遇到的JS文件进行逐个迁移

#### 工具选型

- Typescript
    

-- JavaScript的超集，添加了静态类型和其他一些特性

- @types/node
    

-- TypeScript类型声明文件库，用于提供Node.js核心模块的类型定义

- @types/react & @types/react-dom
    

-- TypeScript类型声明文件库，用于提供React和ReactDOM库的类型定义

- @types/jest
    

-- TypeScript类型声明文件库，用于提供Jest测试框架的类型定义

#### 流程图

![[未命名-7.png]]

#### 方案实现

1. 将TypeScript添加进现有CRA项目
    

```Bash
npm install --save typescript @types/node @types/react @types/react-dom @types/jest
或者
yarn add typescript @types/node @types/react @types/react-dom @types/jest
```

原因：由于B端JS项目是由通过`CRA`工具而非直接使用`Webpack`进行构建，无法直接借助`ts-loader`或`babel-loader`对TypeScript文件进行转换。因此结合`create-react-app`文档内步骤对项目进行TypeScript添加，采用`tsc`进行对TypeScript编译转换。（[Adding TypeScript](https://create-react-app.dev/docs/adding-typescript/)）

  

2. 初始化TypeScript配置


- `tsconfig.json`是Typescript项目的配置文件，用于配置Typescript
- `tsconfig.json`配置文件可以通过 `npx tsc --init` 生成


原因：TypeScript是在JavaScript语法的基础上新增了一些特性，新增的特性导致不符合JavaScript的语法了， 但是Web浏览器和Node.js只认识JavaScript语法， 因此就需要把TypeScript语法 转换为JavaScript语法。

`TypeScript Compiler`，简称`tsc`

作用：将TypeScript语法转换为JavaScript语法

  

3. 修改`jsconfig.json`为`path.tsconfig.json`
    

```Bash
Error: You have both a tsconfig.json and a jsconfig.json. If you are using TypeScript please remove your jsconfig.json file.
```

原因：如果不对`jsconfig.json`进行调整会出现以上报错。

`jsconfig.json`源于 TypeScript 的配置文件[tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html)。相当于`tsconfig.json`的`allowJs`属性设置为`true`

  

字段含义`：path.tsconfig.json`仅用于命名，无意义，此处考虑到不同项目中`jsconfig`配置之间可能存在差异，因此通过在`tsconfig.json`配置文件中利用`extends`字段对原有配置进行继承。

`extends`允许当前的 `tsconfig.json` 文件继承另一个配置文件的设置，以便重用共享的配置选项。

  

4. TypeSript配置
    

```JSON
{
  "extends": "./path.tsconfig.json",
  // 编译选项
  "compilerOptions": {
    // 生成代码的语言版本：将我们写的 TS 代码编译成哪个版本的 JS 代码
    // 命令行： tsc --target es5 11-测试TS配置文件.ts
    "target": "es5",
    // 指定要包含在编译中的 library
    "lib": ["dom", "dom.iterable", "esnext"],
    // 允许 ts 编译器编译 js 文件
    "allowJs": true,
    // 跳过类型声明文件的类型检查
    "skipLibCheck": true,
    // es 模块 互操作，屏蔽 ESModule 和 CommonJS 之间的差异
    "esModuleInterop": true,
    // 允许通过 import x from 'y' 即使模块没有显式指定 default 导出
    "allowSyntheticDefaultImports": true,
    // 开启严格模式
    "strict": true,
    // 对文件名称强制区分大小写
    "forceConsistentCasingInFileNames": true,
    // 为 switch 语句启用错误报告
    "noFallthroughCasesInSwitch": true,
    // 生成代码的模块化标准
    "module": "esnext",
    // 模块解析（查找）策略
    "moduleResolution": "node",
    // 允许导入扩展名为.json的模块
    "resolveJsonModule": true,
    // 是否将没有 import/export 的文件视为旧（全局而非模块化）脚本文件
    "isolatedModules": true,
    // 编译时不生成任何文件（只进行类型检查）
    "noEmit": true,
    // 指定将 JSX 编译成什么形式
    "jsx": "react-jsx"
  },
  // 指定允许 ts 处理的目录
  "include": ["src"]
}
```

配置：根据目前B端已有TypeScript项目`tsconfig.json`文件与TypeScript官方文档默认配置[TypeScript配置](https://www.typescriptlang.org/zh/play?#handbook-0)进行配置。

  

5. 修改文件后缀
    

React 组件对应的文件后缀，修改为：`.tsx`

工具函数对应的文件后缀，修改为：`.ts` 或者为其添加类型声明文件 `.d.ts`

6. 文件迁移改造
    

对修改后的JavaScript文件进行TypeScript迁移

- 类型判断：旧的JavaScript代码可能依赖于隐式类型推断，而没有显式指定类型，需要进行添加明确的类型注解。
    
- 模块：JavaScript和TypeScript在模块系统上存在一些差异。在迁移过程中，可能需要将旧的模块系统（如CommonJS）转换为TypeScript支持的模块系统（如ES Modules）
    
- 第三方库兼容：迁移到TypeScript时，某些第三方库可能不兼容或存在一些问题。这可能需要寻找替代的库、修复或调整使用方式。
    

#### 迁移模式

- 增量代码：新的功能用 TS
    
- 存量代码：已实现的功能，可以继续保持 JS 文件，慢慢修改为 TS 即可
    

  

#### 问题处理

1. 稳定性
    

迁移过程稳定：混合迁移策略允许选择性地将JavaScript文件逐个迁移到TypeScript。**这种逐个迁移的方式可以降低整个项目在迁移过程中的不稳定性**，因为只有迁移的部分代码受到影响，而其他部分仍然保持原样。

2. 兼容性:
    

绝大部分第三方库的类型声明文件有两种存在形式

- 库自带类型声明文件
    

这种情况下，正常导入该库，**TS** **就会自动加载库自己的类型声明文件**，以提供该库的类型声明。

- 由 DefinitelyTyped 提供
    
    - DefinitelyTyped 是一个 github 仓库，用来提供高质量 TypeScript 类型声明
        

解决方案：

- 针对库自带类型声明文件，无需处理正常导入即可。
    
- 针对需要由DefinitelyTyped提供的声明文件。
    
    - 可以通过 npm/yarn 来下载该仓库提供的 TS 类型声明包，这些包的名称格式为:@types/*
        
    - 在实际项目开发时，如果使用的第三方库没有自带的声明文件，VSCode 会给出明确的提示
        
    - 当安装 @types/* 类型声明包后，TS 会自动加载该类声明包，以提供该库的类型声明
        
- 针对既不属于库自带类型声明文件也无法在DefinitelyTyped上找到的TS类型声明包，考虑自行对工具包进行TS类型声明文件对编写。
    

3. 影响率：
    

学习曲线平稳：逐个迁移JavaScript文件的方式可以使开发人员逐步熟悉TypeScript，而无需一次性全面转变。**这种渐进学习的方式有助于降低学习曲线和减少由于项目文件全面迁移对开发人员的造成的开发难度。**

测试复杂度小：由于是逐个将JavaScript文件进行迁移，在对迁移的单元模块进行测试的时候，仅需关注被迁移的文件是否出现问题，而不必同时考虑整个项目的测试。**这种逐个迁移的方式可以减少测试的范围和复杂度。**

  

#### 方案缺陷

混合代码风格：在混合迁移过程中，项目中可能存在不一致的代码风格，即部分文件是基于JS的松散语法和约定，而另一部分是基于TS的严格类型和语法要求，**可能导致代码库的一致性和可维护性的问题。**

迁移耗时：逐个迁移文件需要一定的时间和工作量，对于大型项目而言，**可能会导致迁移过程的延迟和开发周期的延长。**

#### 方案总体项目文件调整

1. `package.json`文件修改
    

```undefined
"dependencies": {
    ...其他依赖
     "typescript": ???,
    "@types/jest": ???,
    "@types/node": ???,
    "@types/react": ???,
    "@types/react-dom": ???,
    // ??? 表示 项目node版本下对应的工具版本
    ...
```

2. `jsconfig.json`文件重命名为`path.tsconfig.json`
    
3. 新增`tsconfig.json`文件，并进行以下配置
    

```JSON
{
  "extends": "./path.tsconfig.json",
  "compilerOptions": {
    "target": "es5",
    "lib": [
      "dom",
      "dom.iterable",
      "esnext"
    ],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": [
    "src"
  ]
}
```

4. 生成一个`react typescript`项目时，在src目录下会生成一个`react-app-env.d.ts`类型声明文件
    

```undefined
/// <reference types="react-scripts" />
```

- **三斜线引用告诉编译器在编译过程中要引入的额外的文件。**三斜线指令是包含单个`XML`标签的单行注释。 **注释的内容会做为编译器指令使用**。
    
- 三斜线指令中有两种`types` 和 `path` 两种不同的属性，它们的区别是：`types` 用于声明对另一个库的依赖，而 `path` 用于声明对另一个文件的依赖。上面`react-app-env.d.ts`依赖react-scripts库的类型声明文件，`react-scripts`下的`package.json`中`types`指定了`TypeScript`的入口文件。
    
- 当项目编译时将会根据`tsconfig.json`中`include`指定的目录去找代码所需要的类型声明文件，而`react-app-env.d.ts`会告诉编译器含有哪些类型声明，里面含有一些常用的类型声明，比如`react、react-dom`的一些`API`类型声明，图片、样式模块类型声明等等。
    

当引入的包没有相应的类型声明时就需要在`react-app-env.d.ts`或者在`src`目录下另外定义一个`.d.ts`文件中加上该模块的类型声明。

  

  

## tsc or webpack+babel-loader or webpack + ts-loader的选择

介绍：目前主流的ts编译方案有2种，分别是官方tsc编译、babel+ts插件编译

对于ts官方模式来说，ts编译器就是tsc（安装typescript就可以获得），而编译器所需的配置就是tsconfig.json配置文件形式或其他形式。ts源代码经过tsc的编译（Compile），就可以生成js代码，在tsc编译的过程中，需要编译配置来确定一些编译过程中要处理的内容。

  

babel-loader是webpack和babel（由@babel/core和一堆预置集preset、插件plugins组合）的桥梁。

### babel作用

1. babel进行解析、转换、生成
    
2. babel 本身不具有任何转化功能，它把转化的功能都分解到一个个 plugin 里面。因此当不配置任何插件时，经过 babel 的代码和输入是相同的。
    

> 插件总共分为两种：

- 当我们添加 语法插件 之后，在解析这一步就使得 babel 能够解析更多的语法。(顺带一提，babel 内部使用的解析类库叫做 babylon，并非 babel 自行开发)
    
- 当我们添加 转译插件 之后，在转换这一步把源码转换并输出。这也是我们使用 babel 最本质的需求。
    

因为babel的插件处理的力度很细，我们代码的语法、语义内容规范有很多，如果我们要处理这些语法，可能需要配置一大堆的插件，所以babel提出，将一堆插件组合成一个preset（预置插件包），只需要引入一个插件组合包，就能处理代码的各种语法、语义。

将ts编译为js的两种方式（tsc、babel），但仅仅是简单将一个index.ts编译为index.js