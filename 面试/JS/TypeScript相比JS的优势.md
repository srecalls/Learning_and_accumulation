[[TypeScript介绍]]
TypeScript 是 JS 的超集，JS有的TypeScript都有，是Type和JavaScipt的结合，在JS的基础上为 JS 添加了类型系统。

从编程语言的动静来区分，TypeScript属于静态类型的编程语言，JS属于动态类型的编程语言。静态类型是编译期做类型检查，动态类型是执行期做类型检查。代码编译和代码执行的顺序本身是1编译2执行。  
  

对于JS来说：需要等到代码真正去执行的时候才能发现错误(晚)。

对于TS来说：在代码编译的时候(代码执行前)就可以发现措误(早)。

并且，配合VSCode等开发工具，TS可以提前到在编写代码的同时就发现代码中的错误，减少找Bug、改Bug时间。相比JS，开发体验更友好，增加开发了开发的幸福度。  
  

**TypeScript相比JS的优势:**

1.更早(写代码的同时)发现错误，减少找Bug、改Bug时间，提升开发效率。

2.程序中任何位置的代码都有代码提示，随时随地的安全感，增强了开发体验。

3.强大的类型系统提升了代码的可维护性，使得重构代码更加容易。

4.支持最新的ECMAScript语法，优先体验最新的语法，让你走在前端技术的最前沿。

5.TS类型推断机制，不需要在代码中的每个地方都显示标注类型，让你在享受优势的同时，尽量降低了成本。除此之外，Vue 3源码使用TS重写、Angular默认支持TS、React与TS完美配合，TypeScript已成为大中型前端项目的首先编程语言。




**TypeScript 和 JavaScript 的区别：**

-   TypeScript 被称为面向对象的编程语言，而 JavaScript 是一种基于原型的语言。
-   TypeScript 具有称为静态类型的功能，但 JavaScript 不支持此功能。
-   TypeScript 支持接口，但 JavaScript 不支持。

**使用 TypeScript 优于 JavaScript 的优势**

-   TypeScript 总是在开发时（预编译）指出编译错误。因此，不太可能出现运行时错误，而 JavaScript 是一种解释型语言。
-   TypeScript 支持静态/强类型。这意味着可以在编译时检查类型的正确性。此功能在 JavaScript 中不可用。
-   TypeScript 只不过是 JavaScript 和一些附加功能，即 ES6 功能。您的目标浏览器可能不支持它，但 TypeScript 编译器也可以将**.ts**文件编译成 ES3、ES4 和 ES5。

  
  
