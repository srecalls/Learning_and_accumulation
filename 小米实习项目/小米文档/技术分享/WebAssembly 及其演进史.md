## Web 的一点点历史

- 先看一张复古的图
    
![[WebAssembly 及其演进史.png]]

- 早些年网页基本都是静态的，为了在浏览器上写点动画，Brendan Eich于1995年花费10天时间为Netscape开发出JavaScript，刚开始的名字叫 Mocha，后来改名叫 LiveScript ，语言从Lisp借鉴了“函数作为一等功能”的理念，从 Self 语言借鉴了基于原型的继承，语法上抄了些 Java，主要是为了蹭热度好宣传，名字也改成了 JavaScript（如果非要说相关，也就是变量和 API 都是驼峰命名）
    
- 开发的主要目的也是希望在浏览器端执行一些简单的任务，比如动画，所以本身设计的很简单，是一门脚本语言（毕竟只有10天，还要什么自行车）
    
- 2004年4月1号，谷歌推出了 Gmail，利用我们目前已经习以为常的 Ajax 技术，第一次人们感受到网页可以像一个本地应用一样，但当年的浏览器还是IE统治的年代，JS 作为一门解释执行的脚本语言，性能依然较弱
    
- 2008年，谷歌推出了 Chrome 浏览器，最重要的是随他一起发布的 V8 引擎，通过 JIT 显著提升了 JS 的性能
    
- 2009年，Nodejs 出现，JavaScript 开始越来越重要，Atwood's Law: Any application that can be written in JavaScript, will eventually be written in JavaScript.
    
- 后来的故事大家基本就都知道了，前端还是越来越重要，人们对 JS 的诉求，期待也越来越越高，比如**速度**
    

  

## JS、JIT 和性能

- JS 是解释执行的，众所周知，解释执行的语言通常性能不如编译执行的语言
    
- 如今的JS 之所以快，因为引擎加入了 JIT 的能力，通常 JIT（Just-In-Time） 的三阶段
    
    - warm阶段（解释执行的代码被执行多次）： 将解释执行的代码发送给JIT（Just-In-Time）引擎，并创建出编译为机器码的执行代码，但此处并不进行替换；
        
    - hot阶段（解释执行的代码被执行得十分频繁）： 解释执行代码被替换为warm阶段的机器码执行代码；
        
    - very hot阶段：将解释执行的代码发送给优化编译器（Optimising Compiler），创建和编译出更高效的机器码的执行代码并进行替换
        
- 以下面代码为例
    

```Assembly
function test(value) {
    // some logic
}

const arr = [0, 'hello']
for (let i = 0; i < arr.length; i++) {
    test(arr[i])
}
```

- 由于数组arr中存在两种数据类型（Number/String），当我们多次执行相关代码时，`test`函数会被JIT（Just-In-Time）引擎创建并编译出两个不同类型的机器码执行代码版本，并且使用不同的表单元进行引用。当然，由于机器码执行代码的创建和编译是存在代价的，因此不同的JIT（Just-In-Time）引擎会有不同的优化策略。
    
- 如果部分代码执行得异乎频繁，那么自然的这部分解释执行的代码会被发送给优化编译器（Optimising Compiler）进行更高程度的优化，从而创建并编译出相比warm阶段更高效的机器码执行代码版本。与此同时，在创建这些高度优化的机器码执行代码期间，编译器将会严格限制执行代码的适用类型（比如仅适用于Number/String或某些特定类型参数），并且在每次调用执行前都会进行参数类型的检查，如果匹配则会使用这些高度优化的机器码执行代码，否则将会回退到warm阶段生成的机器码执行代码或是直接解释执行
    
- 计算机行业有一句经典的话叫：“没有银弹”，JIT 也不是万能的，可以发现，上面的过程每一步都有代价，比如说上面的数组，类型不同，如果这个数组类型不确定且长度不固定，那引擎可能会认为这段代码永远无法 warm，那性能基本接近于解释执行，例如这篇文章[JIT-less V8](https://v8.dev/blog/jitless)
    

## WASM 的前任们

- 在混合应用、NodeJS 中遇到性能问题，大家会怎么做？
    
    - 看 Chrome 的 performance ，对代码做性能优化
        
    - 写个 Native 模块，部分性能敏感给让 Native 代码做
        
    - 恭喜你，你跟发明 WASM 一帮人一样聪明
        
- asm.js
    
    - 简单来说，就是限制 JS 的动态性，“面向 JIT“编程，提高代码的 JIT 友好度，从而提升性能，有上古编程经验的人可能还记得”[循环展开大法](https://en.wikipedia.org/wiki/Loop_unrolling#:~:text=Loop%20unrolling%2C%20also%20known%20as,known%20as%20space%E2%80%93time%20tradeoff.)“
        
    - http://asmjs.org/faq.html
        
- NaCI（Native Client）
    
![[WebAssembly 及其演进史-1.png]]
- PNaCI（Portable Native Client）
    
- 详细的可见：[NaCl and PNaCl](https://developer.chrome.com/docs/native-client/nacl-and-pnacl)
    
- 但总体来说，用 Native 开发成本是高的、但是 asm.js 的局限性又很大，有没有什么办法两全其美？
    
    - 软件工程领域还有另一句话：“计算机科学领域的任何问题都可以通过增加一个间接的中间层来解决”，这个时候业界的大牛和浏览器的头牌（Chrome，Firefox，Edge）就站出来了，搞了一套新的标准（抽象），也就是今天我们熟知的 Web Assembly
        
    - 当然这里还有个很重要的点就是LLVM的出现，感兴趣可以了解下 [llvm/文章/LLVM编译器框架介绍.md](https://github.com/0voice/kernel_new_features/blob/main/llvm/%E6%96%87%E7%AB%A0/LLVM%E7%BC%96%E8%AF%91%E5%99%A8%E6%A1%86%E6%9E%B6%E4%BB%8B%E7%BB%8D.md)
        

## 闲话少叙、书接上文

- 先说说 ASM，下面是一段经典的 Hello World 代码
    
![[WebAssembly 及其演进史-2.png]]
- 那么它对应的（部分）汇编代码如下，文件共计 128 行
    
![[WebAssembly 及其演进史-3.png]]
- `[Web Assembly](https://webassembly.github.io/spec/core/intro/introduction.html)` 其实也是一样，我们可以来看看对应的形式（部分），文件共计 781 行
    
![[WebAssembly 及其演进史-4.png]]
- 是不是可以手写 WASM 并编译呢？
    
    - 当然可以，我们先来看一段 WASM 的文本源码
        
    
    ```Assembly
    (module
      (func $add (param $lhs i32) (param $rhs i32) (result i32)
        local.get $lhs
        local.get $rhs
        i32.add)
      (export "add" (func $add))
    )
    ```
    
- 如何理解语法
    
    - [S 表达式](https://zh.wikipedia.org/wiki/S-%E8%A1%A8%E8%BE%BE%E5%BC%8F)，学过 Lisp 的懂得都懂
        
        - 想象有一颗树
            
        - 每个节点由"()"包围
            
        - 括号的第一个标签告诉你节点的类型，后面的是属性或者子节点
            
    - 堆栈虚拟机
        
        - 大家学算法的时候都知道“逆波兰表达式”，堆栈虚拟机的一大优势就是易于实现，例如安卓的 Java 虚拟机就也是基于堆栈的
            
- 方便探索的工具
    
    - 编译工具：https://github.com/webassembly/wabt
        
    - 在线编译器：https://webassembly.github.io/wabt/demo/wat2wasm/
        
- 与 JavaScript 交互-WASM 的载入与执行
    

```JavaScript
 const importObj = {};
      WebAssembly.instantiateStreaming(fetch("add.wasm"), importObj)
      .then(result => {
        console.log('add 1 and 2 using wasm function =', result.instance.exports.add(1,2))
      })
```

- 与 JavaScript 交互-核心 API
    
    - 首先 `WebAssembly` 是 JS 加载 WASM 的构造函数
        
    - 我们可以打印一下，不难发现示例还有其他属性
        
    
  ![[WebAssembly 及其演进史-5.png]]
    - `WebAssembly.Module` 构造一个 ES 模块
        
    - `WebAssembly.Instance` 构造模块的实例
        
    - 用来管理内存的 API
        
        - `WebAssembly.Memory` 用来创建一块 WASM 的内存
            
            - 无类型的、连续的、字节数组
                
            - 内存模型：
                
                - 线性内存
                    
                - 安全沙盒
                    
                - 内存分配以页为单位，一页 64k
                    
        - `WebAssembly.Table` 另一种形式的内存空间，区别于 `WebAssembly.Memory` 的是它
            
            - 带类型的**引用数组**
                
            - 目前仅仅支持存储“函数引用”，为什么？
                
                - 函数引用是静态数据
                    
                - 安全性，例如：通过引用地址绕开访问控制，越界访问非法内存
                    
                - 移植性，现代计算机的内存概念往往是被抽象的并不是真正意义的物理地址，所以跨机器可能会有差异
                    
    - 此外是一些工具 API，就不一一介绍了
![[WebAssembly 及其演进史-6.png]]

## WASM 一些其他的补充

- 破除迷信：越低级的语言越快
    
    - 这句话基本上都有一个限定条件：“在同样的操作下”，但这句话是最容易被忽视的
        
    - 在如今的条件下，优秀的架构往往能够解决很多性能问题，同样糟糕的设计也会带来很多性能问题
        
    - 比如这篇文章：[2023.04 Wasm 入坑记](https://xiaomi.f.mioffice.cn/wiki/wikk4VQ90Ax93rzOBTR3kSCT3Ed) 表现得_更快的语言却有更慢的性能，原因是因为内存拷贝_
        
    - 再比如：[语言性能对比](https://programming-language-benchmarks.vercel.app/java-vs-javascript)
        
- 2023年，像上面那样写 WASM 的代码，那效率也太低了，比如一个上面一个简单的 Hello World 要接近 800 行，所幸围绕 WASM 的生态已经越来越完善
    
- 例如上面的 C 代码就是通过 [emscripten](https://emscripten.org/docs/getting_started/downloads.html) 工具编译为 WASM 的
    
- 另外 Rust 这门语言近些年来异军突起，尤其是在 WASM 方面，工具链是最容易配置的，只需要：`cargo install wasm-pack` 就可以完成安装和配置
    
- rust 是一门值得投入的语言，作为现代语言，后发的Rust本身有很多现代特性，是一门即可用于系统编程，也可用于应用开发的语言且与 web 生态结合较为紧密
    
    - 例如：[Linus Torvalds：Rust 将被合并到 Linux 6.1 主线](https://www.oschina.net/news/212066/linus-rust-will-go-into-linux-6-1)
        
    - 成熟的wasm的工具链，可以方便的在传统的 Web 页面中用于混入 Native 代码
        
    - [TAURI](https://tauri.app/) 可用于桌面开发
        
    - Web 开发的前端框架，比如：[YEW](https://play.yew.rs/)
        
- 近些年前端的很多工具链也由向 Rust 迁移的趋势
    
- 我不是很喜欢它，但建议大家可以跟进一下
    

  

## 业务落地

- 可以一起讨论并实践
    

  

## 过程中的一些参考资料

- https://00f.net/2023/01/04/webassembly-benchmark-2023/
    
- https://www.cncf.io/wp-content/uploads/2023/09/The-State-of-WebAssembly-2023.pdf
    
- https://blog.scottlogic.com/2023/10/18/the-state-of-webassembly-2023.html
    
- https://www.runtime.news/why-2023-is-a-key-year-for-webassembly-a-promising-cloud-technology/
    
- https://graffersid.com/webassembly-vs-javascript/
    
- https://blog.logrocket.com/top-rust-web-frameworks/
    
- https://dev.to/dboatengx/history-of-javascript-how-it-all-began-92a
    
- https://www.wired.com/2014/04/gmail-ten/
    
- https://v8.dev/blog/jitless
    
- https://web.dev/articles/what-is-webassembly?hl=zh-cn
    
- https://en.wikipedia.org/wiki/WebAssembly
    
- https://github.com/0voice/kernel_new_features/blob/main/llvm/%E6%96%87%E7%AB%A0/LLVM%E7%BC%96%E8%AF%91%E5%99%A8%E6%A1%86%E6%9E%B6%E4%BB%8B%E7%BB%8D.md