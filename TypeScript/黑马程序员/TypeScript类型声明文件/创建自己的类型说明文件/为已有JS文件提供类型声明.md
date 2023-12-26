# 为已有JS文件提供类型声明
```ts

关键："导入js文件的时候，ts会自动加载与.js同名的.d.ts文件，来提供类型声明"

1. 使用declare关键字"(注意，是在.d.ts文件中使用)"
作用：用于类型声明，为其他地方（比如.js文件）已存在的变量，来声明类型。而不是创建一个新的变量。
对于只能在TS使用的，比如type、interface就不用加declare关键字
对于在TS和JS都能用的，比如let，function，就需要使用declare关键字，用于指定的此处用于类型声明


对于纯粹的 JavaScript 文件，您可以使用 `.d.ts` 文件添加类型声明，而无需使用 `import` 和 `export` 关键字。`.d.ts` 文件的主要目的是为 JavaScript 代码提供类型检查和类型推断的支持，而不是用于模块化导入和导出。
```

如果您有一个 JavaScript 文件，并希望为其添加类型，可以使用 `.d.ts` 文件（TypeScript 声明文件）来为该 JavaScript 文件提供类型定义。下面是一个示例，展示了如何使用 `.d.ts` 文件为 JavaScript 文件添加类型。

假设您有一个 JavaScript 文件 `math.js`，其中包含一个函数 `add`，用于将两个数字相加：

```javascript
// math.js

function add(a, b) {
  return a + b;
}
```

现在，您可以创建一个名为 `math.d.ts` 的 `.d.ts` 文件，用于为 `math.js` 文件添加类型定义：

```typescript
// math.d.ts

declare function add(a: number, b: number): number;
```

在上述示例中，我们使用 `declare` 关键字创建一个函数声明，与 `math.js` 文件中的 `add` 函数对应。

在声明中，我们指定了函数的参数类型和返回类型，将其定义为接受两个 `number` 类型的参数，并返回一个 `number` 类型的值。

通过创建这样的 `.d.ts` 文件，您为 `math.js` 文件提供了类型定义。现在，当在 TypeScript 项目中使用 `math.js` 文件时，TypeScript 编译器将使用 `.d.ts` 文件中的类型信息来检查和推断代码，提供类型安全性和智能提示。
![[Pasted image 20230328050249.png]]
![[Pasted image 20230328050708.png]]
![[Pasted image 20230328050724.png]]
![[Pasted image 20230328050849.png]]
![[Pasted image 20230328050945.png]]