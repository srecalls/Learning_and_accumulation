# 前言

相信在现在这个时间节点（2023年），没有哪位前端开发者还会对 TypeScript 的大名感到陌生。

TypeScript 是由微软开发的一款开源的编程语言，是 JavaScript 的超集。TypeScript 在 JavaScript 的基础上扩展了类型的语法和语义，让 JavaScript 代码达到了静态类型语言级别的类型安全，之前只能在运行时发现的类型不安全的问题，现在能在编译期间进行检查了。

细心地你可能已经发现问题了，【在编译期间检查】意味着 TypeScript 最终仍然需要编译成为 JavaScript 语言。事实就是，现在的主流客户端并不支持直接运行 TypeScript 语言，因此在通常的生产环境下，开发者编写的 TypeScript 代码需要通过某些编译工具转化为 JavaScript 代码。

1. # 背景
    

**小米开发者站是一个通过 React 开发的单页面应用，开发语言是 JavaScript ，目前已经在线上稳定运行了五年时间。但是随着网站功能的持续迭代，前端项目工程的复杂度日益提升。与此同时，随着团队人力的持续增加与更替，如何保持项目的可维护性、提高团队间协同开发的效率、确保代码质量等一系列问题都日益变得尖锐起来**

comment：这句话太长了，拆解下

在此背景下，小米开发者站前端团队决定使在项目中引入 TypeScript 来解决上面提到的一系列问题。TypeScript 作为 JavaScript 的超集，支持与 JavaScript 共同工作，JavaScript 项目可以渐进式地逐步迁移到 TypeScript

**TypeScript 的引入方式非常简单：**
comment：
```js
庄梦秋10月27日 14:30

那难点是啥？这么简单的事情，为啥你要拿出来大讲特讲

10月27日 14:32

@庄梦秋 我再改改。一开始写的时候没想好重点，写得很流水账。文章其实主要就是对比了一下Babel和tsc

嗯，最好先想清楚这个文章你想讲的是什么事情
```

1. 安装 TypeScript：通过 `npm install typescript` 在项目添加 TypeScript。当然，为了 TypeScript 更好地工作，根据项目的不同你可能还需要补充一些其他的类型声明模块，比如`@types/react`
    
2. 配置 `tsconfig.json`：`tsconfig.json`文件表示了一个 TypeScript 项目的根目录，用于配置 TypeScript 自带工具如何处理 TypeScript 代码
    
3. 编译 TypeScript：如论是在开发调试阶段，还是最终生产阶段，我们都希望自己的代码可以运行在真实客户端环境中（比如浏览器），因此，我们需要将 TypeScript 编译成为 JavaScript。然而我们应该使用什么工具？如何完成 TypeScript 的编译呢
    

  

2. # 常见的 TypeScript 编译方式
    [[webpack和vite的区别]]

1. ## tsc
    

tsc 是 tyepscript compiler 的缩写，它是 TypeScript 自带的编译工具（安装typescript就可以获得）

你可以通过在终端执行以下命令将目标文件编译为JS文件：

```Bash
tsc target.ts
# 执行后你将会得到一个 target.js 文件
```

你也可以直接执行 `tsc` 命令，tsc 会自动寻找 `tsconfig.json` 配置文件，并根据对应配置对你的项目进行编译

  

**tsc** **编译流程包含了5个阶段：**

- 扫描器：TypeScript 源码经过扫描器扫描之后变成一系列 Token
    
- 解析器：解析 token，得到一棵抽象语法树（AST）
    
- 绑定器：在 AST 语法树各个节点上生成一系列标记（Symbol），这些标记指向相关联其它节点
    
- 检查器：扫描 AST，进行类型检查，收集错误
    
- 发射器：根据 AST 生成最终的 JavaScript 代码
    

  

这5个阶段可以表示成下图：

暂时无法在飞书文档外展示此内容

![[TypeScript编译工具选择：开发者站前端项目实践.png]]

1. ### **扫描器：**
    

通常语言编译分为三个主要步骤：词法分析(token流) -> 抽象语法树(AST) -> 编译生成新的代码

扫描器的作用就是对原代码字符串进行分词，将原代码字符串解析为词法单元（token）

举个例子：

```JavaScript
let a = 1;

// 上述代码字符串经过词法分析后，会被解析为如下几个词法单元：

[
    'let',  // 变量声明关键词
    'a',  // 变量名
    ':',  // 类型声明
    'number',   // 整数类型
    '=',  // 赋值
    '1',  // 整数值
    ';'  // 句尾
]
```

2. ### **解析器**
    

解析器在上一步生成的token流的基础上，进一步生成抽象语法树（AST）。AST 以树状的形式记录代码的语法语义，树上的每个节点都表示源代码中对应的代码语句

AST 树状结构的好处是方便我们对代码语句进行修改：我们对源代码的编辑无需基于代码字符串，而是只需要对AST树进行操作即可

在上文力道的例子中，代码会被进一步解析为如下的AST结构：

![[TypeScript编译工具选择：开发者站前端项目实践-1.png]]

3. ### **绑定器**
    

绑定器的作用是为AST中的节点添加依赖关系，为后续的类型检查提供依据

在一个 TypeScript 项目中，类型的声明可能来源与代码的任何一个地方，很多时候还伴随着不同模块之间的引用。反映在 AST 上，这些类型声明分散在 AST 的不同分叉、不同节点中。绑定器的作用正是在 AST 中创建标记（Symbol），通过这些标记将 AST 中不同节点关联起来

有了这些标记，AST 的树形结构进一步变成了一个互相关联的网状类型系统，我们可以很方便的找到任意节点所关联的所有类型信息，接下来就可以进行类型检查了

4. ### **检查器**
    

检查器的工作非常简单，就是遍历扫描 AST 树，校验AST上各个节点的语法与类型声明是否匹配，如果不匹配，则会抛出错误

5. ### **发射器**
    

发射器可以理解为一个反向执行的解析器+扫描器，它的作用是根据 AST 反向生成代码字符串，不过此时生成的目标语言是 JavaScript。在经过检查器的类型检查之后，如果检查通过，tsc 会通过发射器生成最终的 JavaScript 代码。但是，这一步对 tsc 来说是可选的，你可以通过配置 `noEmit: true`，让 tsc 只进行代码检查而不输出 JavaScript 代码。

  

2. ## Babel
    

Babel 是一个工具链，诞生之初是为了用于将采用ECMAScript 2015+ 语法编写的代码转换为向后兼容的 JavaScript 语法，以便能够兼容旧版本的浏览器或其他环境。但是得益于 Babel 强大的插件系统，Babel 也可以用与编译各种 JavaScript 的方言，比如 JSX，当然，也包括 TypeScript。

  

**Babel 的编译流程主要包含了3个阶段：**

- 解析（parse）：将 TypeScript 源码解析为 AST
    
- 转化（transform）：对 AST 进行加工，生成新的 AST
    
- 生成（generate）：根据最终的 AST 生成 JavaScript 代码
    

  

这3个阶段可以表示成下图：

![[TypeScript编译工具选择：开发者站前端项目实践-2.png]]

1. ### 解析阶段
    

在解析阶段，Babel 通过 `@babel/parser` 这个包将源代码解析为 AST。类比到 tsc，Babel 的解析阶段可以等同于 tsc 的扫描+解析两个阶段合并。事实上，在Babel 的 parse 阶段，依然包含了分词（生成 token）和语法分析（生成 AST）两个步骤，只是 Babel 的解析器 `@babel/parser` 将这两个步骤合并执行了

在这一阶段，我们还可以通过添加插件来使 Babel 支持各种不同的语法。不过对于 TypeScript，我们不需要额外的插件，因为`@babel/parser`已经支持了 TypeScript 语法

2. ### 转化阶段
    

在转化阶段，Babel 通过 `@babel/traverse` 这个包对 AST 进行遍历，并对 AST 中每个需要修改的节点进行修改，最终形成一颗新的 AST

Babel 提供了强大的插件功能。在转化阶段，通过引入对应的 Babel 插件，可以告诉 Babel 需要对当前的 AST 进行那些修改，这正是我们使用 Babel 时最本质的需求。如果我们想要编译 TypeScript 代码，我们可以通过引入 `@babel/plugin-transform-typescript` 插件，将 AST 中与 TypeScript 语法相关的节点进行改造

3. ### 生成阶段
    

在生成阶段，Babel 的工作可以类比上文提到的 tsc 中的发射器

在这一阶段，Babel 通过 `@babel/generator` 这个包，根据上一阶段经过转化后最终生成的 AST ，进一步生成为我们需要的 JavaScript 代码字符串。至此，我们就通过 Babel 完成了将 TypeScript 编译为 JavaScript 的全部步骤

  

3. # 在 Webpack 工程中编译 TypeScript
    

在现代的前端项目工程中，我们往往使用模块化的方式进行开发，与之对应的，我们往往需要一个打包工具来将所有的模块组合起来，Webpack 正是其中非常流行的一种，也是开发者站前端项目中所使用的打包工具

Webpack 可以根据一个或多个入口文件，分析所有依赖的模块，并打包生成我们期望的目标产物。这些模块可能包含各种各样的资源，包括 JavaScript文件、CSS文件、图片资源等等。当然，如果你使用了 TypeScript 进行开发，你项目中的 TypeScript 文件也将是 Webpack 需要处理的模块中的一种

Webpack 默认只支持 JavaScript 类型的模块，为了能够处理其他不同类型的模块，Webpack 使用了一种叫做 loader 的机制。Webpack 在运行时，通过各种不同的 loader 来对不同的模块进行解析，开发者可以通过自己实现不同的 loader 来扩展 Webpack 的能力。为了能在使用 Webpack 的前端工程中使用 TypeScript，我们就需要使用对应的 loader 来处理 TypeScript 代码

Webpack 的工作模式可以简化为下图：

![[TypeScript编译工具选择：开发者站前端项目实践-3.png]]

  

1. ### ts-loader
    

ts-loader 是一个专门用来处理 TypeScript 代码的 Webpack Loader，在 ts-loader 内部，实际上是通过调用 tsc 来实现 TypeScript 的编译的。因此，要使 ts-loader 正常工作，我们还需要保证当前项目组已经安装了 tsc。

ts-loader 的工作流程可以简化成下图：

![[TypeScript编译工具选择：开发者站前端项目实践-4.png]]

可以看到，首先 ts-loader 内部通过调用 `typescript` 提供的 tsc 将 TypeScript 代码编译为 JavaScript 代码。在这一阶段里发生的事情，其实和上文中介绍 tsc 的章节中描述的一模一样，TypeScript 源码经过：扫描 -> 解析 -> 绑定 -> 检查 -> 发射 等一系列阶段，最终转化为 JavaScript 代码

被编译的后的 JavaScript 模块后续会继续进入Webpack 的其他处理流程，比如最常见的一个场景就是，通过 babel-loader 将 JavaScript 代码进一步编译为支持 ES5 的代码。

这个过程存在一个问题，那就是我们同一段 TypeScript 代码需要经过两次编译，一次是将 TypeScript 转化为 JavaScript，一次是对 JavaScript 进行处理（这是绝大部分使用 Webpack 的项目中都会包含的场景，我们要将工程中一个个 JavaScript 模块编译为最终的打包产物，不可避免地需要对 JavaScript 进行各种处理）。如果项目特别大，TypeScript 模块特别多的时候，两次编译所浪费的时间也会变得特别漫长

  

2. ### babel-loader
    

那么有没有一种方式，可以一步到位，直接将 TypeScript 代码编译为我们最终需要的 JavaScript 代码呢？

在上文中我们已经介绍了使用 babel 对一份 TypeScript 进行编译的过程：Babel 天生就是用来对 JavaScript 代码进行各种处理操作的；Babel 通过强大的插件系统，可以任意扩展和修改 Babel 对源代码的编译行为，其中就包括通过 TypeScript 相关的插件实现对 TypeScript 的编译

对于一个 Webpack 项目来说，Babel 提供了 babel-loader 来方便开发者在 Webpack 中使用 Babel 的各种编译功能

babel-loader的工作流程可以简化成下图：

![[TypeScript编译工具选择：开发者站前端项目实践-5.png]]

  

4. # 最终的方案
    

看到这里，我们已经发现，无论是 ts-loader 还是 babel-loader，本质上还是使用了 tsc 和 Babel 的能力，那么在我们的项目中到底应该使用 tsc 还是 Babel 呢

1. ## Babel vs tsc
    

我们从4个角度来对比一下 Babel 和 tsc 在实际使用中的不同：

1. ### 类型检查
    

如果细心的话，在本文第2节的对比中我们其实可以发现，tsc 编译时有【绑定】和【检查】这两个环节，而使用 Babel 编译时好像并没有这两个步骤。还记得这两个环节是干什么的么？是的，这两个环节的目的就是为了执行 TypeScript 的类型检查。

TypeScript 作为一个强类型语言，那 Babel 是如何处理 TypeScript 中的类型的呢？答案是：Babel 直接忽略它。

tsc 的类型检查需要在绑定阶段，拿到整个工程的类型信息，并将工程中散落各处的类型信息互相关联起来。

而 Babel 是基于单个文件编译的，在编译一个文件时，不会去关联其他文件的信息，所以做不到和 tsc 一样的类型检查。在一个 Webpack 工程中，这种解析每个文件的依赖、获取全局模块信息的工作，正好是 Webpack 所擅长的，Babel 只负责将 Webpack 传给自己的源码一个一个地进行编译即可。

2. ### 编译速度
    

那 Babel 是怎么编译 TypeScript 的呢？首先，在解析阶段，Babel 能够正常地将 TypeScript 代码转化为 AST，只不过，在处理 AST 时，Babel 会直接把类型信息去掉，毕竟 JavaScript 本来就是一门弱类型语言，类型的声明的存在与否并不影响本身的 JavaScript 逻辑

因此，由于省略了 tsc 中的【绑定】和【检查】这两个步骤，Babel 对 TypeScript 的编译过程变得异常简洁和高效，编译速度远高于 tsc

这种效率提升在开发阶段显得尤为重要。设想一下，在开发过程中，我们想要快速地验证一些想法，当我们修改了代码之后，我们希望 Webpack 可以立即将我们的修改热更新到浏览器上。你知道自己修改只是临时的，但你只是想在这一点上进行快实验，遗憾的是 TypeScript 要求你在任意时候确保所有代码是类型安全的，你不得不为你的任意修改而时刻小心翼翼

3. ### 与 Webpack 配合使用
    

在一个主流的 Webpack 工程中，Babel 还有一个更大的优势，那就是：你的项目里大概率早已经使用了 Babel。babel-loader 是 Webpack 生态里最主流的 JavaScript 编译器，无论是对旧版本浏览器进行 JavaScript 语法的兼容性处理，还是编译各种 JavaScript 方言（比如JSX、 Vue 的单文件组件等等），你都或多或少已经在使用 babel-loader 了 以这次开发者站项目从 JavaScript 迁移 TypeScript 为例，只需要在项目中现有的 Babel 配置文件里，添加一个配置：`"presets": ["@babel/preset-typescript"]`，即可实现现有打包流程对 TypeScript 的支持。`@babel/preset-typescript`是 TypeScript 和 Babel 团队官方合作维护的，一套支持 TypeScript 的 Babel 插件和配置的合集

使用 babel-loader 避免了在 Webpack 中将 Babel 和 tsc 两个编译器组合使用带来的效率问题。使用 ts-loader 时，编译的流程往往是 `TypeScript > tsc > JavaScript > Babel > JavaScript (again)` 。为了提升效率，ts-loader 推荐结合 `[fork-ts-checker-webpack-plugin](https://github.com/TypeStrong/fork-ts-checker-webpack-plugin)`、`[happypack](https://github.com/amireh/happypack)` 等工具一起使用。而使用 Babel ，你将告别这一切复杂繁琐的配置，并且你的编译流程被简化成了`TypeScript > Babel > JavaScript`，Webpack 打包效率获得极大提升

4. ### 语法支持
    

对各种 ES 语法标准的支持本来就是 Babel 的看家本领。尽管 TypeScript 也处于持续的迭代中，其最新版本默认支持同时期的大部分 ES 特性，但是 TypeScript 不支持还在草案阶段的特性。Babel 的 preset-env 支持所有标准特性，还可以通过各种[插件](https://babeljs.io/docs/plugins-list)来支持更多还未进入标准的特性

但是，也有一部分的 TypeScript 语法在 Babel 编译时可能存在问题，比如：

> - **[命名空间](https://www.typescriptlang.org/docs/handbook/namespaces.html)****：**命名空间语法已经[过时了](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/docs/rules/no-namespace.md)，本身在 TypeScript 中已经不再被推荐使用，可以使用标准的 ES6 模块语法代替（`import` / `export`）。因为 Babel 一次处理一个文件，因此那些需要关联其他模块的语法功能 Babel 无法处理，你可以在 TypeScript 配置中开启 `[isolatedModules](https://www.typescriptlang.org/tsconfig#isolatedModules)` 选项，让 TypeScript 为这些情况提供告警
>     
> - **[尖括号类型断言](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions)****：**使用尖括号的类型断言写法在某些时候可能会和其他语法混淆（比如JSX），你需要留意[额外的配置](https://babeljs.io/docs/babel-preset-typescript#istsx)，或者可以使用`a as TypeB`写法代替
>     

  

2. ## Babel for transpiling，tsc for types
    

综上，使用 Babel 编译 TypeScript 代码相比 tsc 有诸多优势： 编译速度更快；在 Webpack 中的使用更简洁、效率更高；支持更多的语法特性。在前端工程中，如果有一个编译器，可以胜任所有的 JavaScript（包括 TypeScript） 代码编译工作，那么为什么还要使用多个呢？Babel 正是这样一个编译器，因此它也成为了开发者站项目最终的选择

至于类型检查的工作，我们可以继续交给 tsc 来完成，我们只需要在准备好后（开发完成，最终打包时）再检查类型错误。至于开发阶段的类型提示，可以交给 IDE 工具或者是其他 LINT 工具来解决。这些工具的类型检查功能是怎么实现的呢？是的，其实它们背后依然是都 tsc 在工作

至此，开发者站找到了它最佳的 TypeScript 实践方式：使用 Babel 进行编译，使用 tsc 进行类型检查。相信这也是适用于绝大多数现有的使用 Webpack 的、希望从 JS 迁移至 TS 的其它前端项目的最优方案