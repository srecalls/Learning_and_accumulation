当设计一个简单的 Loader 时，我们可以以将输入的代码转换为大写形式为例。下面是一个基本的示例：

  

```Java
// uppercase-loader.js
module.exports = function(source) {
  // 将输入的代码转换为大写形式
  const transformedCode = source.toUpperCase();
  return transformedCode;
};
```

在这个简单的 Loader 示例中，我们将输入的代码通过 `toUpperCase()` 方法转换为大写形式，并将转换后的代码作为结果返回。

当你完成了 Loader 的编写，你可以将其作为一个独立的模块发布到 npm 上，或将其直接放置在你的项目中，并在 Webpack 配置文件中进行配置：

```Java
// webpack.config.js

module.exports = {
  // ...
  module: {
    rules: [
      {
        test: /\.js$/, // 匹配需要使用 Loader 处理的文件
        use: [
          {
            loader: 'uppercase-loader', // 使用你的 Loader
          },
        ],
      },
    ],
  },
};
```

  

在上述的 Webpack 配置中，我们使用了 `uppercase-loader` 来处理以 `.js` 结尾的文件。当 Webpack 执行构建时，它会自动应用我们编写的 Loader，将输入的代码转换为大写形式。

请注意，这只是一个非常简单的示例，用于说明 Loader 的基本原理。实际上，Loader 的设计和实现可能会更加复杂，根据你的需求和场景来决定。你可以根据自己的具体需求来设计更复杂和功能丰富的 Loader。

  

.js文件会作为函数参数传入进去uppercase-loader吗？

是的，Webpack 在使用 Loader 时会将匹配到的文件的内容作为参数传递给 Loader 函数。在上述的示例中，`.js` 文件的内容会作为 `source` 参数传入 `uppercase-loader` 函数。

在 Loader 函数中，你可以通过 `source` 参数来获取输入文件的内容，并对其进行处理。在示例中，我们使用 `source.toUpperCase()` 将输入的代码转换为大写形式。

需要注意的是，Loader 函数需要遵循一定的约定，以便与 Webpack 进行正确的交互。通常，Loader 函数应该是一个 JavaScript 模块，使用 CommonJS 或 ES 模块的语法导出一个函数。这个函数接受输入内容作为参数，并返回处理后的结果。

当你在编写 Loader 时，可以根据需要定义和使用更多的参数，以灵活地处理输入内容。例如，你可以在 Loader 配置中指定一些自定义的选项，并将这些选项作为参数传递给 Loader 函数。这样可以使 Loader 更加可配置和可定制。

总之，Webpack 会将匹配到的文件内容作为参数传递给 Loader 函数，你可以在 Loader 函数中获取并处理这些内容。