### 1. assets和static的区别

assets和static两个文件夹都是用来存放静态资源文件的，放在assets中的文件在打包的时候会被webpack解析处理，小图片可以使用url-loader压缩成base64，大图片使用image-webpack-loader压缩，而放在static里的静态资源文件不会被webpack处理；assets使用相对路径，static使用绝对路径。

### 2. loader和plugin的区别

loader可以直译为“加载器”，webpack本身只能打包js文件，针对于css，图片等文件格式没法打包，因此就需要到loader；loader虽然扩展了webpack，但它只专注于转化文件这个领域，完成压缩，打包，语言翻译，loader仅仅是为了打包。

plugin跟loader一样也是扩展webpack的功能，但是plugin不仅只局限在打包上，它的功能要更加丰富，可以打包优化和压缩，重新定义环境变量；它在webpack运行的生命周期中会广播出许多事件，plugin可以监听这些事件，在合适的时机通过webpack提供的API改变输出结果；loader是运行在打包之前（loader为模块加载时的预处理文件），plugin是在整个编译期都起作用的。loader是在module.rules中配置的。plugin是在plugins中单独配置的。

常见的loader：

1. babel-loader：将ES6代码转化为ES5；
2. vue-loader：将vue文件编译成js文件；
3. css-loader：解析css；
4. style-loader：将css注入到HTML文档中；
5. less-loader/sass-loader：将less/sass文件编译成css文件；
6. url-loader：压缩小图片成base64；
7. image-webpack-loader：压缩大图片，需要配合file-loader才能使用；
8. postcss-loader：

常见的plugin：

1. CleanWebpackPlugin：重新打包的时候，自动帮你删除dist文件；
2. HtmlWebpackPlugin：以一个html文件为模板，生成一个html文件，并将打包后的js代码注入；
3. HotModuleReplacementPlugin：热更新；
4. uglifyjs-webpack-plugin：压缩js；

### 3. vite为什么启动比webpack快

1. webpack是先将所有文件打包后再启动服务器，vite是直接启动服务器，然后按需编译依赖文件，也就是请求哪个模块再对哪个模块进行实时编译；
2. webpack是使用js编写的，vite是使用go编写的，js是解释型语言，go是编译型语言；
3. 热更新：webpack的热更新是重新将该模块的所有依赖重新编译，vite只需要重新请求该模块。

### 4. webpack中hash，chunkhash，contenthash有什么区别

1. hash：所有文件hash值相同，一个改动则所有文件hash值改变；
2. chunkhash：根据入口文件进行依赖文件解析，构建对应的chunk，生成对应的哈希值；
3. contenthash：js代码中引入css文件，如果改了js代码css文件也会跟着变，这个时候就需要contenthash来解决。

### 5. package.json与package-lock.json的区别

package.json记录了你下载了哪些包，以及这些包大版本号，package-lock.json记录的更为详细，会有包的具体版本号，以及你下载的包的依赖包（package.json只记录了你下载的包，下载的包的依赖包不会记录），当你执行npm install的时候它会读取package.json中所有的包，并与node_modules中安装的依赖进行对比，存在的话就根据package-lock.json检查更新，没有则通过package-lock.json获取相应的版本号，接着看一下这个版本号与package.json里是否兼容，兼容就安装，不兼容就按照package.json里的安装，并更新package.lock.json。

### 6. webpack的打包流程

1. 解析配置文件

   配置文件一般是webpack.config.js，根据配置生成一个compiler对象；

2. 读取入口文件

   从入口文件开始，读取这些文件及其依赖的模块，得到他们的依赖关系；

3. 解析模块依赖

   根据上一步得到的依赖关系递归的去解析它们，直到所有依赖都被解析完毕；

4. 加载模块

   使用相应的loader处理解析完的文件，把它们转化为webpack可以处理的格式；

5. 转换代码

   对加载模块进行一系列的转换操作，比如压缩、合并、优化等；

6. 输出文件

   将文件合成一个或多个bundle，并输出到指定的目录。

