1. CommonJS 模块输出的是一个值的拷贝，ESM输出的是值的引用。
2. CommonJS 模块是运行时加载，ESM是编译时输出接口。
3. CommonJS 模块的require()是同步加载模块，ESM的import命令是异步加载，有一个独立的模块依赖的解析阶段。

ESM的import存在提升，且变量像const的 是只读的。

#### CommonJS 模块输出的是值的拷贝,ESM输出的是值的引用

CommonJS一旦输出一个值，模块内部的变化就影响不到这个值  
ESM是动态引用，并且不会缓存值，模块里面的变量绑定其所在的模块


```jsx
//commonjs

// lib.js
var counter = 3;
function incCounter() {
  counter++;
}
module.exports = {
  counter: counter,
  incCounter: incCounter,
};
// main.js
var mod = require('./lib');

console.log(mod.counter);  // 3
mod.incCounter();
console.log(mod.counter); // 3
//----------------------------------------------------
//ESM
// lib.js
export let counter = 3;
export function incCounter() {
  counter++;
}

// main.js
import { counter, incCounter } from './lib';
console.log(counter); // 3
incCounter();
console.log(counter); // 4
//-------------------------------------

//ESM只是一个“符号连接”，这个变量是只读的，对它进行重新赋值会报错。类似于 const 的特性
counter=1 // TypeError
```  

#### CommonJS 模块是运行时加载，ESM是编译时输出接口

CommonJS 加载的是一个对象（即module.exports属性），该对象只有在脚本运行完才会生成。而 ESM不是对象，它的对外接口只是一种静态定义，在代码静态解析阶段就会生成。

```jsx
// ESM的import命令具有提升效果，会提升到整个模块的头
foo();
import { foo } from 'my_module';
//以上代码不会报错，因为import命令是编译阶段执行的，在代码运行之前。
```

#### Commonjs模块加载ESM模块

CommonJS 的require()命令不能加载 ES6 模块，会报错，只能使用import()这个方法加载。
```dart
(async () => {
  await import('./my-app.mjs');
})();
```

require()不支持 ES6 模块的一个原因是，它是同步加载，而 ES6 模块内部可以使用顶层await命令，导致无法被同步加载。

#### ESM模块加载Commonjs模块

只能整体加载，不能只加载单一的输出项

```jsx
// 正确
import packageMain from 'commonjs-package';

// 报错
import { method } from 'commonjs-package';
```
  
因为 ES6 模块需要支持静态代码分析，而 CommonJS 模块的输出接口是module.exports，是一个对象，无法被静态分析，所以只能整体加载