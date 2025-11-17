https://juejin.cn/post/7134314981515853831#heading-5

平常写React都是通过create-react-app、umi、next.js等框架初始化项目，用这些工具的好处就是上手快、不用自己配置，缺点是不了解webpack、babel、typescript等库的使用和配置，不清楚React项目是怎样运行的，最后可能导致自己都搭不起来项目。

  

# 基础搭建项目

1. ## 初始化项目
    

```undefined
npm init
```

项目就可以初始化成功了。此时项目只有一个package.json文件，结构如下

```JSON
{
  "name": "myreact",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  }
}
```

2. ## 安装react、react-dom
    

```undefined
npm install react react-dom
```

`react`： react是 React 库的核心包。它提供了用于创建组件、处理虚拟 DOM、状态管理、生命周期等功能。通过使用react包，可以构建功能丰富、可复用和高性能的用户界面。

`react-dom`： react-dom 是用于与浏览器 DOM 进行交互的 React 的包装器。它提供了用于将 React 组件渲染到实际的 DOM 中的方法，以及处理事件、更新组件等功能。react-dom使得在 Web 应用中使用 React 变得简单且高效。

3. ## 新建src目录，添加App.js与index.js
    

配置如下

index.js

```JavaScript
import React from 'react'
// 这行代码导入了 React 模块
// 它是用于构建 React 应用程序的核心库。它提供了用于创建组件、处理虚拟 DOM 等功能。

class App extends React.PureCompoent {
    render() {
        return (
            <div>App Component</div>
        )
    }
    // 这是 App 组件的 render 方法，它负责渲染组件的内容。
    // 在这个例子中，它返回一个包含字符串 "App Component" 的 <div> 元素。
    // render() 方法是 React 提供的。它是 React 组件类的一个生命周期方法，用于定义组件的渲染逻辑。
    // 在 React 中，每当组件需要更新自己的输出时，都会调用 render() 方法。该方法是必需的，并且应该返回一个 React 元素，用于描述组件的输出内容。
    // App 组件中的 render 方法可以被视为重写。
    // 当一个类组件继承自 React.PureComponent 或 React.Component
    // 并且在该类中定义了一个名为 render 的方法时，它就会重写继承自父类的默认 render 方法。
}
// 这是一个类组件的定义，名为 App。它继承自 React 的 PureComponent 类。
// 意味着该组件会在 props 或 state 发生变化时进行浅比较，以决定是否重新渲染组件。这有助于优化性能。

export default App
```

App.js

```JavaScript
import React from 'react'
// 这行代码导入了 React 模块，用于构建 React 应用程序的核心库。
import { createRoot } from 'react-dom/client'
// 这行代码从 react-dom/client 模块中导入了 createRoot 方法。
// createRoot 方法是 React 18 新引入的 API，用于启动 React 应用的根节点。
impot App from './App.js'

const root = createRoot(document.getElementById('id'))
// 这行代码使用 createRoot 方法创建了一个根节点，并将其赋值给名为 root 的常量。
// createRoot 方法接收一个 DOM 元素作为参数，用于标识要将 React 应用挂载到哪个 DOM 节点上。
root.render(<App />)
// 这行代码使用 root 对象的 render 方法将 <App /> 元素渲染到之前创建的根节点上。
// <App /> 是 JSX 语法，表示将 App 组件作为一个元素进行渲染
```

4. ## 安装babel
    
      babel是javascript编辑器，作用如下：
    
    1. 负责把ES6、ES7等高版本js编译成低版本js，供浏览器运行。
        
    2. 负责把react语法（jsx）编译成js。
        
    

babel详细使用请看[文档](https://link.juejin.cn/?target=https%3A%2F%2Fbabeljs.io%2Fdocs%2Fen%2F)。执行命令：

```undefined
npm install @babel/core @babel/cli @babel/preset-env @babel/preset-react --save-dev
```

1. `@babel/core`： @babel/core是 Babel 的核心模块，它提供了 Babel 的核心功能，包括代码解析、转换和生成。
    
2. `@babel/cli`： @babel/cli是 Babel 的命令行工具。它允许你在终端中使用 Babel，通过命令行对文件或文件夹进行代码转换。
    
3. `@babel/preset-env`： @babel/preset-env 是 Babel 的预设之一，用于根据目标环境自动确定需要转换的语法特性和插件。它根据配置的目标环境，将代码转换为兼容该环境的版本。
    
4. `@babel/preset-react`： @babel/preset-react 是 Babel 的预设之一，用于转换 React 的特定语法和 JSX 表达式。它将 JSX 转换为普通的 JavaScript 代码，以便在浏览器中运行。
    

  

5. ## 配置babel
    

根目录下添加.babelrc文件

配置如下

.babelrc

```JSON
{
    "presets": ["@babel/preset-env", "@babel/preset-react"]
}
```

这段代码是用于配置 Babel 的转换规则，它定义了 Babel 要使用的预设（presets）。

1. `"presets": ["@babel/preset-env", "@babel/preset-react"]`： 这行代码指定了 Babel 的预设。预设是一组 Babel 插件的集合，用于转换特定的语法和功能。
    
    1. `@babel/preset-env` 是 Babel 的预设之一，用于根据目标环境自动确定需要转换的语法特性和插件。
        
    2. `@babel/preset-react` 是 Babel 的预设之一，用于转换 React 的特定语法和 JSX 表达式。
        
2. 通过将这两个预设添加到 `"presets"` 数组中，Babel 将根据配置的目标环境和 React 的使用情况，自动应用相应的转换规则和插件。
    
3. 例如，`@babel/preset-env` 可以将最新的 JavaScript 语法转换为目标环境支持的旧版本语法，以确保代码在各种浏览器和环境中正常运行。而 `@babel/preset-react` 可以将 JSX 语法转换为普通的 JavaScript 代码，以便在浏览器中运行。
    
4. 通过在 Babel 的配置文件（例如 `.babelrc`）中添加这段代码，你告诉 Babel 在转换过程中要使用这两个预设，以便正确处理代码中的语法和功能。
    

6. ## 安装Webpack
    

集成webpack。webpack是一个现代JavaScript应用程序的静态模块打包器，现代前端应用很多都是用webpack打包，webpack详细使用请看[文档](https://link.juejin.cn?target=https%3A%2F%2Fwebpack.js.org%2Fconcepts%2F)。webpack-dev-server用来搭建一个本地服务，可以热加载前端项目，详细请看[文档](https://link.juejin.cn?target=https%3A%2F%2Fwebpack.js.org%2Fconfiguration%2Fdev-server%2F)。

```Bash
npm i webpack webpack-dev-server webpack-cli --save-dev
```

1. `webpack`： webpack是一个现代的 JavaScript 模块打包工具。它可以将多个模块和资源文件打包成一个或多个最终的静态资源文件，以便在浏览器中加载和使用。Webpack 提供了丰富的功能和配置选项，包括代码分割、模块解析、代码压缩等，以帮助开发者更高效地构建复杂的 Web 应用程序。
    
2. `webpack-dev-server`： webpack-dev-server是一个用于开发环境的轻量级服务器，它与 Webpack 集成得很好。它提供了一个本地开发服务器，可以实时监视文件的变化，并自动重新编译和刷新浏览器。它还支持热模块替换（Hot Module Replacement，HMR），可以在不刷新整个页面的情况下更新模块。
    
3. `webpack-cli`： webpack-cli是 Webpack 的命令行接口工具。它提供了一组命令，用于在终端中与 Webpack 进行交互，例如执行打包、启动开发服务器、创建配置文件等。通过使用webpack-cli，你可以通过命令行更方便地执行 Webpack 相关的任务。
    

  

除此之外，webpack集成babel还需要babel-loader，加载html文件还需要插件html-webpack-plugin

```Bash
npm i babel-loader html-webpack-plugin --save-dev
```

1. `babel-loader`： babel-loader是 Webpack 的一个加载器（loader），用于在 Webpack 构建过程中将 ES6+ 代码转换为向后兼容的 JavaScript 代码。它会通过 Babel 解析和转换 JavaScript 模块，使其能够在旧版浏览器或其他环境中运行。通过配置babel-loader，你可以在 Webpack 构建中集成 Babel，并确保你的代码在目标环境中正常运行。
    
2. `html-webpack-plugin`： html-webpack-plugin是一个 Webpack 插件，用于自动生成 HTML 文件，并将打包后的 JavaScript 和 CSS 文件自动注入到生成的 HTML 文件中。它简化了在 Webpack 构建中手动创建 HTML 文件的过程，同时可以根据配置生成带有 hash 值的文件名、压缩 HTML 文件等。通过使用html-webpack-plugin，你可以方便地生成与打包后的文件相关联的 HTML 文件，以便在浏览器中正确加载和展示你的应用程序。
    

安装完成后添加webpack配置。在根目录下新建webpack.config.js文件

```JavaScript
const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-hteml')
// 大多数情况下，Webpack 的配置文件是在 Node.js 环境中执行的，而 Node.js 目前仍然更常用于使用 CommonJS 格式的模块系统。
// 因此，通常你会看到在 Webpack 配置文件中使用 require 来引入模块，而不是使用 import
moudule.export = {
  // 入口文件, Webpack从这里开始构建依赖图
  entry: {
    main: './src/index.js'
  },
  output: {
    path: path.resolve(__dirname, 'dist'),
    // 出口路径
    fileName: 'bundle.js'
    // 打包后的文件名称
  },
  // webpack只能处型js和json文件。加载别的文件需要Loader处型，module就是配置Loader的地方
  module: {
    rules: [
      {
        test: '/\.js$/',
        use: 'babel-loader',
        exclude: /node_module/
      }
    ]
  },
// webpack加html文件需要htmL-webpack-pLugin插件处理
// 启动vebpack-dev-server的时候，会把打包好的js文件、css文件、htmL文件放在内存里
  plugins: [
    new HtmlWebpackPlugin({
      template: './public/index.html'
    })
  ],
  mode: 'development'
}
```

  

7. ## 配置打包脚本
    

在package.json里配置打包脚本：

```SQL
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack"
  },
```

然后执行命令：

```Plain
npm run build
```

项目开始打包，生成bundle.js、index.html文件，结构如下：

index.html

```Bash
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
<script defer src="bundle.js"></script></head>
<body>
  <div id="root"></div>
</body>
</html>
```

至此webpack简易版配置已经完成。接下来配置热加载功能，

8. ## 下载webpack-dev-server
    

```SQL
npm i webpack-dev-server --save-dev
```

在package.json添加脚本：

```SQL
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack"
    "start": "webpack server --open --port 8080"
  },
```

- `webpack`：指示运行Webpack命令。
    
- `server`：指示运行Webpack开发服务器。
    
- `--open`：这是一个可选参数，表示在启动开发服务器后自动在浏览器中打开网页。当你希望在启动服务器后自动打开浏览器时，可以使用此参数。
    
- `--port 8080`：这也是一个可选参数，用于指定开发服务器监听的端口号。在这个例子中，设置为8080端口。如果没有指定该参数，默认端口号是8080。
    

  

运行

```SQL
npm run start
```

项目在3000端口启动，启动后会自动打开浏览器窗口。热加载配置完成，文件修改保存后浏览器直接展示出来。

到此react项目简化版搭建完成。后续继续集成其他工具库即可。

# 使用TS

9. ## 安装ts
    

安装typescript、ts-loader。typescript是ts编辑器，把ts代码编译成js，详细请看[文档](https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2F)。ts-loader是让webpack识别.ts/.tsx文件，调用编译器编译，详细看[文档](https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fts-loader)。

```SQL
npm i typescript ts-loader --save-dev
```

1. `typescript`：TypeScript是一种开源的编程语言，它是JavaScript的超集，添加了静态类型检查和更多的语言特性。通过安装`typescript`包，你可以在项目中使用TypeScript编写代码。
    
2. `ts-loader`：`ts-loader`是Webpack的一个加载器（loader），用于在构建过程中将TypeScript代码编译为JavaScript代码。它可以与Webpack一起使用，将TypeScript文件转换为可在浏览器中运行的JavaScript文件。
    

安装react、react-dom类型库：

```undefined
npm i @types/react @types/react-dom --save-dev
```

1. `@types/react`：React是一个流行的JavaScript库，用于构建用户界面。`@types/react`是React的类型声明文件，它提供了React库的类型定义，让你在使用TypeScript编写React应用时能够获得类型检查和自动完成等功能。
    
2. `@types/react-dom`：`@types/react-dom`是React DOM库的类型声明文件，它提供了React DOM库的类型定义。React DOM是用于在浏览器中渲染React组件的库。
    

10. ## 添加ts配置文件
    

执行命令初始化配置文件

```undefined
npx tsc --init
```

ts配置文件详细请看[文档](https://link.juejin.cn/?target=https%3A%2F%2Fwww.tslang.cn%2Fdocs%2Fhandbook%2Ftsconfig-json.html)。在根目录下添加tsconfig.json：

```SQL
{
  "compilerOptions": {
    "target": "es5",                                  /* Set the JavaScript language version for emitted JavaScript and include compatible library declarations. */
    "lib": ["es6", "dom"],                                        /* Specify a set of bundled library declaration files that describe the target runtime environment. */
    "jsx": "react",                                /* Specify what JSX code is generated. */
    "module": "esnext",                                /* Specify what module code is generated. */
    "moduleResolution": "node",                     /* Specify how TypeScript looks up a file from a given module specifier. */
    "allowJs": true,                                  /* Allow JavaScript files to be a part of your program. Use the 'checkJS' option to get errors from these files. */
    "sourceMap": true,                                /* Create source map files for emitted JavaScript files. */
    "importHelpers": true,                            /* Allow importing helper functions from tslib once per project, instead of including them per-file. */
    "allowSyntheticDefaultImports": true,             /* Allow 'import x from y' when a module doesn't have a default export. */
    "strict": true,                                      /* Enable all strict type-checking options. */
    "skipLibCheck": true                                 /* Skip type checking all .d.ts files. */
  },
  "include": ["src"]
}
```

  

1. `"target"`：设置生成的JavaScript代码的目标版本。在这个例子中，目标版本设置为"es5"，意味着生成的JavaScript代码将符合ECMAScript 5标准。
    
2. `"lib"`：指定一组捆绑的库声明文件，描述目标运行时环境。在这个例子中，指定了"es6"和"dom"库，表示项目中可以使用ECMAScript 6和DOM相关的类型和功能。
    
3. `"jsx"`：指定生成的JSX代码的类型。在这个例子中，设置为"react"，表示生成的JSX代码将与React一起使用。
    
4. `"module"`：指定生成的模块代码的类型。在这个例子中，设置为"esnext"，表示生成的模块代码将采用ECMAScript的下一代模块系统。
    
5. `"moduleResolution"`：指定TypeScript如何根据给定的模块规范符解析文件。在这个例子中，设置为"node"，表示使用Node.js的模块解析策略。
    
6. `"allowJs"`：允许将JavaScript文件作为项目的一部分。设置为`true`，表示允许在项目中引入和编译JavaScript文件，并通过设置`checkJS`选项来检查这些文件中的错误。
    
7. `"sourceMap"`：为生成的JavaScript文件创建源映射文件。源映射文件可以用于在调试过程中将编译后的JavaScript代码映射回原始源代码。
    
8. `"allowSyntheticDefaultImports"`：允许在模块没有默认导出时使用`import x from y`语法。设置为`true`，表示允许使用这种语法来导入模块。
    
9. `"strict"`：启用所有严格的类型检查选项。设置为`true`，表示开启所有严格的类型检查，提高代码的类型安全性和可靠性。
    
10. `"skipLibCheck"`：跳过对所有`.d.ts`文件的类型检查。设置为`true`，表示在类型检查过程中跳过所有`.d.ts`文件，这可以提高编译速度，但也可能导致一些类型相关的错误不被检测到。
    
11. `"importHelpers"`：当设置为true时，TypeScript编译器会从tslib中导入帮助函数（helper functions）。帮助函数是一些用于支持编译后的JavaScript代码的辅助函数，例如__extends、__assign、__awaiter等。通过从tslib中导入这些帮助函数，可以减少生成的JavaScript代码的重复，提高代码的可维护性和可读性
    

11. ## 修改Webpack配置
    

修改webpack配置：

```JavaScript
const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  // 入口文件, Webpack从这里开始构建依赖图
  entry: {
    main: './src/index'
  },
  output: {
    path: path.resolve(__dirname, 'dist'),
    // 出口路径
    filename: 'bundle.js'
    // 打包后的文件名称
  },
  // webpack只能处型js和json文件。加载别的文件需要Loader处型，module就是配置Loader的地方
  module: {
    rules: [
      {
        test: /\.j|tsx$/,
        use: 'ts-loader',
        exclude: /node_modules/
      }
    ]
  },
  //增加扩展选型，让webpack可以识别.ts/tsx文件
  resolve: {
    extensions: ['.ts', '.tsx', '.js']
  },
// webpack加html文件需要htmL-webpack-pLugin插件处理
// 启动vebpack-dev-server的时候，会把打包好的js文件、css文件、htmL文件放在内存里
  plugins: [
    new HtmlWebpackPlugin({
      template: './public/index.html'
    })
  ],
  mode: 'development'
}
```

12. ## 修改.js后缀改为.ts/tsx后缀
    

启动项目，正常运行。ts集成成功。

  

  

# 路由

13. ## 安装路由
    

项目中路由是必不可少的。本节简单介绍路由如何使用，详细使用请看[文档](https://link.juejin.cn/?target=https%3A%2F%2Freactrouter.com%2Fdocs%2Fen%2Fv6)。

```SQL
npm install react-router-dom@6
```

`react-router-dom` 是 React Router 库的一部分，它是一个用于在 React 应用中实现路由功能的包。通过使用 `react-router-dom`，你可以在 React 应用中实现客户端端路由，使用户在不同的 URL 上导航和浏览不同的页面。

具体来说，`react-router-dom` 提供了一组 React 组件，用于定义路由配置、渲染正确的组件，并与浏览器的 URL 进行交互。

以下是 `react-router-dom` 的一些主要功能和作用：

1. 路由定义和配置：`react-router-dom` 提供了 `BrowserRouter` 和 `HashRouter` 组件，用于定义和配置路由规则。你可以在这些组件中定义不同的路由和对应的组件。
    
2. 路由匹配和渲染：`react-router-dom` 提供了 `Route` 组件，用于匹配当前 URL 和路由配置，并渲染对应的组件。你可以通过 `exact` 属性控制精确匹配，也可以使用动态路由参数进行模式匹配。
    
3. 嵌套路由：`react-router-dom` 支持嵌套路由，允许你在应用中创建层次结构的路由。这样你可以定义多个级别的路由，并根据需要嵌套渲染对应的组件。
    
4. 路由导航和跳转：`react-router-dom` 提供了 `Link` 和 `NavLink` 组件，用于创建导航链接。这些链接可以响应用户的点击操作，并通过 URL 跳转到对应的路由。
    
5. 路由参数和查询参数：`react-router-dom` 允许你通过路由参数和查询参数传递数据。你可以在路由配置中定义参数，并在组件中访问和使用这些参数。
    
6. 路由守卫和权限控制：`react-router-dom` 提供了 `Route` 组件的 `render` 和 `component` 属性，允许你根据条件渲染组件。这可以用于实现路由守卫和权限控制逻辑，限制用户访问某些页面。
    

14. ## 修改index.tsx文件
    

使用BrowserRouter标签包裹跟标签

```TypeScript
import React from 'react'
import { createRoot } from 'react-dom/client'
import App from './App'
import { BrowserRouter } from 'react-router-dom'

const root = createRoot(document.getElementById('root') as any)
root.render(
    <BrowserRouter>
      <App></App>
    </BrowserRouter>
)
```

15. ## 使用路由
    

使用路由。新建Home.tsx、About.tsx组件如下