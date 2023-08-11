- **通常情况下，服务器分以下几种部署、运行环境：**

> staging：用于开发功能时给 RD 测试用，代码、数据库都是测试环境的。  
> preview：用于代码部署到生产环境前的测试，代码是准生产版本，数据库是生产环境的。  
> production：生产环境，代码、数据库都是生产环境的。

- **为了配合以上环境，git代码库一般会有以下分支：**

> staging分支：用于staging环境的部署  
> master分支：git默认的分支，提供最新、稳定的代码  
> preview分支：用于preview环境的部署  
> production分支：用于production环境的部署

以上分支将会永久留存在git代码库中，但是在开发、bugfix的过程中，还会用到如下几种分支：

> dev分支：以dev_xxx命名，xxx表示对某种功能的简单描述  
> feature分支：以feature_xxx命名，xxx表示对子功能的简单描述  
> bugfix分支：以bugfix_xxx命名，xxx表示对bug的简单描述，修复常规bug时会用到  
> hotfix分支：以hotfix_xxx命名，xxx表示对bug的简单描述，修复紧急bug时会用到

![[开发过程中的git分支管理.png]]

各个分支的生命周期

- 由于公司实际开发中只有staging环境与production环境，故去掉preview分支，各个分支详细如下：

### master分支：

默认存在的分支，保持最新、稳定的代码  
从以下分支合并：dev、bugfix、hotfix

### preview分支：

预生产环境的分支  
从以下分支合并：master

### release分支：

生产环境的分支  
从以下分支合并：preview

### dev分支：

开发环境的分支  
派生自以下分支：master  
从以下分支合并：feature  
合入以下分支：master

### staging分支：

测试环境的分支  
从以下分支合并：feature

### feature分支：

开发者开发各自功能的分支  
派生自以下分支：dev  
合入以下分支：staging、dev

### bugfix分支：

用来解决常规bug的分支  
派生自以下分支：master  
合入以下分支：staging、master

### hotfix分支：

用来解决紧急bug  
派生自以下分支：release  
合入以下分支：staging、preview、release

  
  
作者：任无名F  
链接：https://www.jianshu.com/p/f96f4c8ce80c  
来源：简书  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。