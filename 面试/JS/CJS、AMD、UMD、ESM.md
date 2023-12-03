JavaScript模块规范：CommonJS (CJS)、Asynchronous Module Definition (AMD)、Universal Module Definition (UMD)和ECMAScript Modules (ESM)。
### CJS

CJS（**CommonJs**） 适用于后端 Node。

Node 与 Javascript 最开始是没有`模块`这个概念的。相反，模块概念在 java 和 php 等却存在。为了方便对代码开发和管理，Node 首先提出了 CJS 模块规范。它采用同步加载模块的方式。通过`require`来引入模块，使用`module.exports`和`exports`来导出模块。这种规范适用于服务器端开发，在浏览器中使用时可能会遇到性能问题，因为同步加载可能会阻塞页面渲染。

```js
// util.js 
module.exports = function dosomething(data) {
    // todo
}

// main.js
const dosomething = require('./util.js')
```
### AMD
 /eɪˈsɪŋ.krə.nəs/
AMD（**asynchronous module definition**） 异步模块定义 适用于前端。

CommonJs 主要适用于服务器 Node，浏览器 Javascript 那时还没有 ESM。而开发人员也想实现浏览器代码模块化开发，随之诞生了 AMD。

AMD 使用 **requirejs** 库来实现，它采用异步加载模块的方式，适用于浏览器环境。通过`define`来定义模块，使用`require`来异步加载模块。这种规范在处理大量模块时能够更好地优化性能，但写起来可能会稍显繁琐。

AMD是异步加载模块的，也可以通过`回调`处理异步。

```js
// dep1.js
define(['jquery', 'util'], function (jquery, util) { 
    var dosomething = function() {};
    return {
        dosomething: dosomething
    }
});

// dep2.js
define(['dep1'], function (dep1) { 
    // dep1.dosomething();
});
// require 也可以直接用来替换define。
// require(['dep1'], function (dep1) { 
//   dep1.dosomething();
// });
```

**require 多用于解决循环依赖中，在运行时加载文件。**


### UMD

UMD（**Universal Module Definition**）通用模块定义 适用于任何环境下使用。

与 CJS、AMD 不同，UMD是一种通用的模块规范，旨在在不同环境下都能正常工作，包括CommonJS、AMD等。它能够兼容各种模块加载方式，使得你的代码可以同时运行在不同的平台上。

> 很多小伙伴为避免问题，在打包时都会把打包模式改成 umd。并且在 ESM 不能使用的情况下也会选择 UMD。

```js
// webpack.config.js
output: {
  ...
  // 将你的 library 暴露为所有的模块定义下都可运行的方式
  libraryTarget: 'umd',
}

// rollup.config.js
output: {
  ...
  // 将你的 library 暴露为所有的模块定义下都可运行的方式
  format: "umd",
}

```

### ESM

ESM（**ES Module**）这是 `Javascript` 提出的实现一个标准模块系统的方案。

ESM 是官方规定的 JavaScript 模块规范，从 ES6（ES2015）开始引入。它采用`import`和`export`语法来导入和导出模块，与现代浏览器和 Node.js 兼容。

```js
// util.js
export const dosomething () {
    // todo
}；

// main.js
const { dosomething } = import('./util.js')
```

ESM 是近些年来常用的敲代码方式。

另，ESMScript 的出现，也使得在 script 中可以直接引用 ESM 文件。

```js
<script src="./main.js" type="module"></script>
```

设置`type=module` ，会将加载的文件视为模块文件，识别模块的`import`语句并加载。

- ESM 可以替代 CJS 与 AMD，并且兼备 UMD 任何环境都可使用的特性。
- 自身的静态化特点，在编译时加载，使得页面加载速度快。
- 真正意义上做到了按需使用。使用 import 并不会直接执行模块，而是生成一个动态的只读引用，等到真的需要用到时，才会到模块里面去读取。
- 可以在 html 中直接使用，如下：

```js
<script type="module"> 
    import { dosomething } from './util.js'; 
    dosomething(); 
</script>
```

因为 ESM 独有的特性，目前 Rollup 与 Vite 已经在dev与打包中使用。

### 结语

选择适合的模块规范取决于你的项目和环境。如果你的项目主要在 Node.js 环境中运行，那么 CommonJS 是一个很好的选择。如果你的项目在浏览器环境中运行且需要异步加载模块，那么 AMD 可能更适合（目前已经很多团队放弃了）。而如果你希望代码可以同时在不同的环境中运行，UMD 是一个通用的解决方案。如果你在现代浏览器和 Node.js 中运行，并且想要利用静态分析的优势，那么 ESM 可能是最好的选择。

现在都是使用打包工具如webpack、vite、rollup等打包成你想要的JavaScript模块规范，多是 UMD。
