## 1.初始化webpack项目

### (1).项目初始化命令

csharp

复制代码

```
npm init
```

### (2).安装webpack 项目依赖包


```js
npm i webpack webpack-cli -D
```

### (3).配置打包的命令


```js
    scripts: {
        "build": "webpack --config webpack.config.js"
    }

```

### (4).配置基础的webpack(需要在根目录新建webpack.config.js)

```js
const path = require('path')
module.exports = {
    entry: './src/index.js', // 配置打包入口文件
    output: { // 配置输出路径
        path: path.resolve(__dirname, 'dist'),
        filename: "name.[hash].js"
    }
}

```
[[6.TCP的拥塞控制机制]]
### (5).引入webpack-html-plugin

```js
const path = require('path')
const htmlwebpackPlugin = require('html-webpack-plugin')
module.exports = {
   entry: './src/index.js', // 配置打包入口文件
   output: { // 配置输出路径
     //  __dirname: 找到当前文件所在的绝对路径
     //  dist: 打包后的文件路径
     path: path.resolve(__dirname, 'dist'),
     filename: "name.[hash].js"
   },
   mode: 'development', // 开发模式
   plugins: [
     // 配置默认的index.html, 打包后的js自动引入到index.html文件中
     new htmlwebpackPlugin({
       template: './public/index.html',
     })
   ]
}
```
![[webpack从0到1搭建vue项目.png]]
### (6).配置解析css, 安装css-loader、style-loader

css

复制代码

```js
npm install --save-dev css-loader style-loader
```

配置css-loader、style-loader

```js
module.exports = {
  module: {
    rules: [
      {
        // 正则匹配css文件
        test: /.css$/,
         // loader的解析顺序是倒叙, 先使用css-loader解析css，
         在使用style-loader解析
        use: [ 'style-loader', 'css-loader'],
      }
    ]
  }
}
```

### (7).配置解析less， 安装 less less-loader



```js
npm i less less-loader -D
```

配置less的rules

```js
rules: [
    {
      test: /\.less$/,
      use: [{
          loader: "style-loader"
      }, {
          loader: "css-loader"
      }, {
          loader: "less-loader"
      }]
    }
]
```

### (8).分析css 安装 mini-css-extract-plugin



```
缘由：由于style-loader的作用是将css动态添加style标签的方式添加在当前页面的Html中，在正式的项目中是不适用的，故需要将css进行项目拆分
```



```
npm i mini-css-extract-plugin -D
```

webpack.config.js配置css分离

```js
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
// rules配置修改如下
module: {
      rules: [
        {
          // 正则匹配css文件
          test: /\.css$/,
          // loader的解析顺序是倒叙, 先使用css-loader解析css，在使用style-loader解析
          // style-loader 会将css在html页面中创建style标签
          use: [{
            loader: MiniCssExtractPlugin.loader,
            options: {
              publicPath: '../'
            }
          }, 'css-loader' ]
        },
        {
          test: /\.less$/,
          use: [{
              loader: "style-loader" // creates style nodes from JS strings
          }, {
              loader: "css-loader" // translates CSS into CommonJS
          }, {
              loader: "less-loader" // compiles Less to CSS
          }]
        }
      ]
    },
    //增加plugin配置
    plugins: [
      // 配置默认的index.html, 打包后的js自动引入到index.html文件中
      new htmlwebpackPlugin({
        template: './public/index.html',
      }),
      new MiniCssExtractPlugin({
        filename: 'css/index.css' // 配置打包生成的目录
      })
    ]
```

### (9).配置图片打包



   ```
   npm i url-loader file-loader -D
   ```

webpack.config.js图片打包配置



```js
rules: [
    {
      test: /\.(png|jpg|gif)$/,
      use: [
        {
          test: /\.(png|jpg|gif)$/,
          use: [
            {
              loader: 'url-loader',
              options: {
                // 限制图片大小，小于8K转换成base64 大于8k的部分则不转换
                limit: 8 * 1024, 
                name: '[name].[ext]',
                publicPath: '../images/', // 设置发布的目录
                outputPath: "images/"
              }
            }
          ]
        }
      ]
    }
]
```

### (10).配置清除打包目录，防止打包产物有残留


```
npm i clean-webpack-plugin -D
```

webpack.config.js增加clean-webpack-plugin 配置项

```js
const { cleanWebpackPlugin } = require("clean-webpack-plugin");
plugins: [
      new cleanWebpackPlugin()
]

```

### (11).配置babel, 增加js语法的兼容性



```
npm i babel-loader @babel/core @babel/preset-env -D
```

babel在config文件的配置


```js
rules: [
    {
      test: /\.js$/,
      exclude: /(node_modules|bower_components)/,
      use: {
        loader: 'babel-loader',
        options: {
          presets: ['@babel/preset-env']
        }
      }
    }
]
```

### (12).配置开发服务器(前端可以在开发的时候，保存就会自动刷新当前页面)

css

复制代码

```js
    npm i webpack-dev-server -D
```

package.json新增dev命令


```js
 "scripts": {
    "build": "webpack --config webpack.config.js",
    "dev": "webpack-dev-server --config webpack.config.js"
  },
```

webpack.config.js

```js
    devServer: {
      port: 3000, // 前端启动端口
      open: true, // 启动自动打开浏览器
    },
```

#### (13).生产环境和开发环境分离

less

复制代码

```js
    //webpack-merge主要用于拆分文件后,合并基础配置以及开发或者生产环境的配置
    npm i webpack-merge -D

```

将webpack.config.js 拆分成

![[webpack从0到1搭建vue项目-1.png]]

|文件名|释义|
|---|---|
|webpack.base.js|webpack基础性配置|
|webpack.dev.js|开发环境专属配置|
|webpack.pro.js|生产环境专属配置|

增加package.json运行命令,修改了文件命令位置

```js
"scripts": {
    "build": "webpack --config config/webpack.pro.js",
    "dev": "webpack-dev-server --config config/webpack.dev.js"
  },
```

### (14).提取公共模块

config/webpack.base.js增加配置

```js
optimization: {
  splitChunks: {
    chunks: 'async',
    minSize: 20000,
    minRemainingSize: 0,
    minChunks: 1,
    maxAsyncRequests: 30, //按需加载时的最大并行请求数
    maxInitialRequests: 30, //入口点的最大并行请求数
    enforceSizeThreshold: 50000,
    cacheGroups: {
      defaultVendors: {
        test: /[\\/]node_modules[\\/]/,
        priority: -10,
        reuseExistingChunk: true,
      },
      default: {
        minChunks: 2,
        priority: -20,
        reuseExistingChunk: true,
      },
    }
  }
}
```

## 2.进入vue配置

#### (1).添加vue (由于我配置的是vue3.0与2.0, 配置略微有些差异)

css

复制代码

```
npm i vue -S
```

在src目录下新建main.js 、App.vue文件 ![[webpack从0到1搭建vue项目-2.png]]
![[webpack从0到1搭建vue项目-3.png]]
index.html 修改如下 ![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d776fdad0ae54b4c9b82e75ae0c3e76e~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)
#### (2).添加 vue编译插件



```
npm i vue-loader vue-template-compiler -S
```

webpack.base.js添加vue文件编译loader配置


```js
const { VueLoaderPlugin } = require('vue-loader')

rules: [
    {
      test: /\.vue/,
      use: 'vue-loader'
    }
]
plugins: [
    new VueLoaderPlugin()
]
```

总结: 以上就是最基础的webpack配置从0到1配置Vue的全部过程了,实际上如果相对了解webpack的基础知识的时候，在去看当前配置信息时，则是相对简单的，如果没有webpack相对会吃力，不过做了这个，心里确实会很舒畅的，把自己想要输出的内容都做完了

  

作者：crazyu  
链接：https://juejin.cn/post/7090479661389447199  
来源：稀土掘金  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。