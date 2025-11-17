## 背景

@mi/commiton无法适配低版本Node.js

  

## 问题

1. ## **项目Node版本较低**
    

当前部分B端项目Node版本较低，导致一些工具无法适配。**开发者站**生产环境Node.js版本为**12.10.0**，**国内开发者站运营后台**Node.js版本为**10.16.3**

  

2. ## **项目工具无法适配**
    

### **Lint-staged**

`lint-staged`是一个用于在 Git 提交之前对暂存文件进行代码检查和格式化的工具。它的作用是通过配置预定义的规则，自动地在每次提交前对指定的文件进行检查和修复，以确保代码的质量和一致性。

  

1. 当前@mi/commition工具中所用lint-staged**默认**为**最新版本**。
    

```Go
  const packages = ['commitizen', 'cz-conventional-changelog', 'conventional-changelog', 'lint-staged'];
```

详见[@mi/commitlint源代码整理](https://xiaomi.f.mioffice.cn/docx/doxk4lz8VB3IZQuFt74YUBNQXag)

基于lint-staged工具库release日志统计。https://github.com/lint-staged/lint-staged/releaseslint-staged

工具与node版本匹配关系如下

```SQL
      15: '>=18.12.0',
      14: '>=16.14.0 <18.12.0',
      13: '>=14.13.1 <16.14.0',（其中13.3.0版本无法适配该区间Node，归于14版本类）
      12: '>=12.20.0 <14.13.1',
      10: '>=10.13.0 <12.20.0',
```

从而导致lint-staged与低版本Node项目出现**适配问题**.

  

### Commitlint

`Commitlint`是一个用于规范化提交消息格式的工具。它通过定义和强制执行提交消息规范，帮助团队维持一致的提交风格，提高代码仓库的可读性和可维护性。

  

其中项目使用到了commitlint中的cli与config-conventional两个工具包，**默认**为**最新版本**。

```SQL
    packages.push('@commitlint/cli');
    packages.push('@commitlint/config-conventional');
```

`@commitlint/cli` 是 Commitlint 的命令行工具，它提供了用于验证提交消息的命令行接口。你可以使用该工具来执行提交消息的验证、自定义规则和配置文件等操作。通过集成到 Git Hook 或其他自动化流程中，可以实现提交消息的规范化验证。

`@commitlint/config-conventional` 是 Commitlint 提供的一个预定义配置包，用于规范化提交消息格式的常用配置。它基于 Conventional Commits 规范，提供了一套符合该规范的默认配置项。

基于commitlint工具库release日志统计。https://github.com/conventional-changelog/commitlint/releases

commitlint工具与node版本匹配关系如下

```JavaScript
      17: ">=14.0.0",
      13: ">=12.0.0 <14.0.0",
      12: ">=4.0.0 <12.0.0"
```

从而导致commitlint与低版本Node项目出现**适配问题**.

  

### Commitizen（严重）

`Commitizen`是一个用于帮助团队规范化提交消息的工具。它提供了一个交互式的命令行界面，引导开发者生成符合规范的提交消息，以确保提交消息的一致性和可读性。

  

未能在Commitizen官方release文档中发现Node版本匹配问题。https://github.com/commitizen/cz-cli/releases

但在下载过程中发现存在以下问题。

![[@mi-commition适配问题阐述.png]]

1. commitizen安装需要依赖cz-conventional-changelog工具
    

`cz-conventional-changelog` 是 Commitizen 的一个插件，它用于生成符合 Conventional Changelog 规范的提交消息。

  

2. cz-conventional-changelog安装需要依赖`commitlint/load`
    

`commitlint/load` 是 Commitlint 的一个函数，用于加载和解析 Commitlint 的配置文件。

此时安装版本"commitlint": "^12.1.4",排除commitlint引发的兼容问题。

![[@mi-commition适配问题阐述-1.png]]

  

注意：此处@commitlint/load，采用>6.1.1进行安装最新版本。
![[@mi-commition适配问题阐述-2.png]]

![[@mi-commition适配问题阐述-3.png]]
使用Typescript原因：`@commitlint/load` 模块使用Typescript在实现时使用了 TypeScript，主要是为了提供类型定义和类型检查的功能。

  

3. 最新版本@commitlint/load会导致typescript^5.2.2的安装。从而引发下列问题。
    
![[@mi-commition适配问题阐述-4.png]]
问题原因：低版本Node无法运行TypeScript5.1

https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-1.html
![[@mi-commition适配问题阐述-5.png]]
  

当采用commitizen@3以及cz-conventional-config@2时，typescript不会出现安装。但仍然会出现上述问题。

猜测typescript较新，作者维护commitizen时未考虑typescript适配情况。

  

当此处主动修改为typescript@4版本时任出现以下问题
![[@mi-commition适配问题阐述-6.png]]
TypeError: flat is not a function"

出现该问题原因：

```JavaScript
如果您看到错误消息 "TypeError: flat is not a function"，可能意味着：
方法不受支持，或者
方法在对象上不存在。
方法不受支持
Array.prototype.flat() 方法在 ES10 中添加，并在 V8 v6.9 中实现（一些浏览器和 Node.js 使用的引擎）。因此，可能是因为您使用的浏览器版本（或 Node.js 版本）未实现/不支持该方法。
```

https://www.designcise.com/web/tutorial/how-to-fix-flat-is-not-a-function-javascript-error

## 结论

适配失败：无法通过直接修改@mi/commition工具包中工具的版本进行低版本Node的适配。

  

  

## 解决方法

项目Node版本提升：有上述问题可知，出现问题的原因是基于低版本Node.js版本不支持导致。因此考虑升级项目Node版本已解决问题。https://www.cnblogs.com/strick/p/16617169.html

经尝试：在node版本为14.18.0时未出现以上问题，且工具可正常导入使用
![[@mi-commition适配问题阐述-7.png]]