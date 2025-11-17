

![[使用 Gitlab-CI‘CD 自动化部署 (转载).png]]

## **介绍**

CI/CD 是一种通过在应用开发阶段引入自动化来频繁向目标用户（测试、客户等）交付应用的方法。CI/CD 的核心概念是持续集成、持续交付和持续部署。作为一个面向开发和运营团队的解决方案，CI/CD 主要针对在集成新代码时所引发的问题（“[集成地狱](https://www.solutionsiq.com/agile-glossary/integration-hell/)”）。

具体而言，CI/CD 可让持续自动化和持续监控贯穿于应用的整个生命周期（从集成和测试阶段，到交付和部署）。这些关联的事务通常被统称为“CI/CD pipeline”，由开发和运维团队以敏捷方式协同支持。

- 持续集成 Continuous Integration (CI)

CI 属于开发人员的自动化流程，意味着代码的新更改会随着提交或定期构建、测试并合并到某个公共的位置或分支。强调开发人员提交了新代码之后，立刻进行构建、（单元）测试。根据测试结果，我们可以确定新代码和原有代码能否正确地集成在一起。可以解决在一次开发中有太多应用分支，从而导致相互冲突的问题。

![](https://xiaomi.f.mioffice.cn/space/api/box/stream/download/asynccode/?code=NTBjMDQzZGRmOTNkNzI4YzhiMjU3OTViNTgzYjFiNzlfTDFyTnJSNHYwdHpoemRZVmZpUkRzMW4zdmV2UFdIMkNfVG9rZW46Ym94azRyVnVnUjZ6YWVlZGlGb1haYnpmMmVkXzE3MDE0MTE4MzY6MTcwMTQxNTQzNl9WNA)

- 持续交付 Continuous Delivery (CD)

CD 意味着代码的变更随着新的提交或者定期构建、测试。持续交付在持续集成的基础上，将集成后的代码部署到更贴近真实运行环境的「类生产环境」中。比如，我们完成单元测试后，可以把代码部署到连接数据库的 Staging 环境中更多的测试。如果代码没有问题，可以继续手动部署到生产环境中。
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-1.png]]

- 持续部署

持续部署则是在持续交付的基础上，把部署到生产环境的过程自动化。
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-2.png]]
所谓的**持续**，就是说每完成一个完整的部分，就向下个环节交付，发现问题可以马上调整。使得问题不会放大到其他部分和后面的环节。总之，CI/CD 是一个流程，用于实现应用开发中的高度持续自动化和持续监控。

到这里我们可以看到自动化集成部署带给我们的好处

## **自动化集成部署带来的好处**

1. 可提高开发效率和我们和测试之间的协调

**Before**

如果按照传统的流程，在项目上线前的测试阶段，前端同学修复bug之后，要手动把代码部署之后。才能通知测试同学在测试环境进行测试。

这会造成几个问题：本身手动部署服务的工作是比较繁琐的，占用了开发时间。同时开发-测试之间的环节的耦合问题，则会增加团队沟通成本。

**After**

通过 CI/CD，前端开发在提交代码之后就不用管了，CI 流程会自动部署到测试或集成环境的服务器。很大程度上节约了开发的时间。

同时，因为开发和测试人员可以在 Gitlab 中看到 pipeline 界面,，测试同学能够随时把握代码部署的情况，同时还可以通过交互界面手动启动 pipeline，自己去部署测试，从而节约和开发之间的沟通时间。

2. 更流程化标准化地管理开发部署流程
3. 运行环境统一，避免了一些因开发环境差异而导致的结果不同或无法运行
4. 持续集成、持续交付、持续部署可以早发现早解决在开发过程中新旧代码的集成问题，从而可以最大限度避免这个问题

## **概念**

1. Pipeline & Job

Pipeline 是 Gitlab 根据项目的 .gitlab-ci.yml 文件执行的流程，由多个节点（stage）组成，每一个节点都是一个任务（Job）。

如下使用根节点 stages 关键字定义本次 Pipeline 的任务节点：

```
stages:
    - install # 安装依赖
    - build   # 构建 
    - deploy  # 发布 
```

2. Runner

Runner 是 CI 任务的运行器，对项目执行 Pipeline 的应用程序，分为 Specific 和 Shared Runner

![[使用 Gitlab-CI‘CD 自动化部署 (转载)-3.png]]

- Shared Runner 是 Gitlab 平台提供的免费使用的 runner 程序，由 Google 云平台提供支持，每个开发团队有十几个。对于公共开源项目是免费使用的，如果是私人项目则每月有2000分钟的CI时间上限
- Specific Runner 是我们自定义的，在自己选择的机器上运行的 runner 程序，提供了一个 gitlab-runner 的命令行软件，在对应机器安装后运行 gitlab-runner-register，使用 token 进行注册，就可以在自己的机器远程运行 pipeline 了

区别：

1. Shared Runner 是所有项目都可以使用的，而 Specific Runner 只能针对特定项目运行
2. Shared Runner 默认基于 docker 运行，没有提前装配执行 pipeline 运行环境，例如 node java等。而 Specific Runner 可以自由选择平台，也可以是各种机器 Linux / Windows 等，并且在上面装配需要的运行环境，当然也可以选择 Docker/K8s
3. 当然使用 Shared Runner 可以在 pipeline 中引入目标 Docker 基础镜像当做运行环境来运行对应的任务

默认镜像：cr.d.xiaomi.net/build-service/gitlab-runner-default:latest

也可以引入其他或者自己构建的基础镜像
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-4.png]]
## **运行机制**
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-5.png]]
1. 在项目根目录下配置 .gitlab-ci.yml 文件，gitlab 会在代码提交后检查是否有 .gitlab-ci.yml （默认）文件，如果有就会执行脚本

2. CI 运行基于 gitlab-runner，在物理机或docker上运行，通过 token 将对应进程的 runner 和 git 进行链接，也可使用公司共享 runner。GitLab 共享运行器将在同一个运行器上执行不同项目的代码。

3. CI 所有流程都是可视化的，每个流程节点的状态可以再Gitlab中看到，包括执行成功或失败以及其运行细节输出。因为它执行像多节管道一样，所以我们通常叫它 pipeline
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-6.png]]
4. 不同的 commit 所触发的 CI 流程互相隔离，即每次推送都会有独立的任务进行，即便使用 --amend 提交代码
5. pipeline 可由 commit 被动触发，也可以手动进行触发

## **YML 及其基本语法**

1. #### **yml 执行文件**
    

CI 流程运行控制取决于 .gitlab-ci.yml，这是默认的配置
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-7.png]]
当然也可以在 gitlab 后台进行目标文件的配置
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-8.png]]
甚至可以使用路径来指定其他公开或有权限项目执行脚本来进行合并 yml
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-9.png]]
2. #### **语法**
    

接下来我们来了解一下 YML 基本语法规则，YML 比 JSON 更为简洁

基本规则：

- 大小写敏感
- 使用缩进表示层级关系
- 缩进时不允许使用Tab键，只允许使用空格
- 缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
- JSON 一样，也是由对象、数组、以及数组对象嵌套组成
- 字符串不需要添加双引号或者单引号，当然添加也可以
- yml还有着比JSON更为丰富的功能，比如用”&"符号和"<<:*”符号可以实现的片段导入的功能，以及gitlab-ci提供的include关键字和extend关键字等提供的结构编排功能。

YML 对象：

```
animal:
    name: dog
    age: 1
```

相当于 JSON 对象：

```
{
    animal: {
       name: 'dog',
        age: 1
    }
}
```

YML 数组：

```
colors:
    - red
    - black
```

相当于 JSON 数组：

```
{ colors: ['red', 'black'] }
```

也可以进行数组对象嵌套：

```
a:
    b:
        - c
d: e
```

相当于 JSON：

```
{
    a: ['c'],
    d: 'e'
}
```

3. #### **高级语法**
    

- ##### **片段复用**
    

**试思考**：如果有一段配置片段会被很多Job使用，那么如果重复写入片段，则会使我们的YML文件变得过分冗长。

而如果能把这段提前进行定义，并根据别名进行导入，就能让YML文件简洁很多了。

YML的语法天然提供了这个功能:

- 使用 **&**符号可以定义一个片段的别名
- 使用 **<<**符号和 ***** 符号可以将别名对应的YML片段导入
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-10.png]]
- 还提供了extend关键字，它的功能和YML的片段导入的功能是一样的， 不过可读性更好一些
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-11.png]]
- ##### **模块化功能**
    

试思考，如果我们配置脚本很长的话，我们一定要把它写在.gitlab-ci.yml这单独一个文件里吗？

能否将它分成多个yml文件，然后把其他YML文件导入到入口YML文件(.gitlab-ci.yml)中呢。

gitlab-ci提供的include关键字便可实现这个功能, 它可以用来导入外部的YML文件。

例如我们有如下的YML结构

├── .gitlab-ci.h5.yml

├── .gitlab-ci.dev.yml

├── .gitlab-ci.wx.yml

└── .gitlab-ci.yml

那么在.gitlab-ci.yml中这么写，就可以对它们做合并
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-12.png]]
4. #### **CI Lint**
    

CI 页面提供了 yml 语法校验工具，可以静态检查语法错误
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-13.png]]
5. #### 关键字
    

关键字作为保留字，不能被用于 job 名称
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-14.png]]
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-15.png]]

![[使用 Gitlab-CI‘CD 自动化部署 (转载)-16.png]]
6. #### 比较常用的关键字
    

- variables
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-17.png]]
CI 也有自己的环境变量预设：https://docs.gitlab.com/ee/ci/variables/predefined_variables.html
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-18.png]]
敏感信息可以通过 gitlab 来进行配置
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-20.png]]
也可以在手动运行流水线的时候临时配置
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-21.png]]
- image & services

可以定义当前运行阶段所使用的docker镜像

- stage

定义当前 job 所处阶段，同一个 stage 可包含多个 job
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-22.png]]
- script

定义 job 运行的的命令脚本

- before_script 和 after_script
- 它可能会覆盖全局定义的 before_script 和 after_script
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-23.png]]
- when

定义任务何时运行：

![[使用 Gitlab-CI‘CD 自动化部署 (转载)-24.png]]

manual 和 allow_failure 结合来看

`allow_failure`可以用于当你想设置一个job失败的之后并不影响后续的CI组件的时候。失败的jobs不会影响到commit状态。

当开启了允许job失败，所有的intents和purposes里的pipeline都是成功/绿色，但是也会有一个"CI build passed with warnings"信息显示在merge request或commit或job page。这被允许失败的作业使用，但是如果失败表示其他地方应采取其他（手动）步骤

- 手动操作指令是不自动执行的特殊类型的job；它们必须要人为启动。手动操作指令可以从pipeline，build，environment和deployment视图中启动。

![[使用 Gitlab-CI‘CD 自动化部署 (转载)-25.png]]

- 手动操作指令默认是不阻塞的，即开始 pipeline 会跳过手动任务，如上图。即可选的手动操作指令默认设置`allow_failure:true`。
- 当 pipeline 被阻塞时，即使是 pipeline 是成功状态也不会继续进行。被阻塞的pipelines也有一个特殊的状态，叫`manual`。
- 如果你想要手动操作指令产生阻塞，首先需要当前 job 添加`allow_failure:false`。
- 可选动作的状态不影响整个pipeline的状态。
- 手动操作指令被认为是写操作，所以当前用户触发操作时，必须拥有操作保护分支的权限。换句话说，为了触发一个手动操作指令到pipeline中正在运行的指定分支，当前用户必须拥有推送到这分支的权限。

- only 和 except
    - `only`定义哪些分支和标签的git项目将会被job执行
    - `except`定义哪些分支和标签的git项目将不会被job执行

- `only`和`except`在一个job配置中同时存在，则以`only`为准，跳过`except`
- `only`和`except`可以使用正则表达式
- `only`和`except`允许使用特殊的关键字：`branches`，`tags`和`triggers`
- `only`和`except`允许使用指定仓库地址但不是forks的仓库

```
only:
    - master
    - /.+test$/
except:
    - dev
```

使用 triggers 可以实现使用 API 触发运行，比如可应用在飞书机器人通过飞书对话框的交互执行部署

![[使用 Gitlab-CI‘CD 自动化部署 (转载)-26.png]]


![[使用 Gitlab-CI‘CD 自动化部署 (转载)-27.png]]

- environment

```
environment:
    name: development
    url: https://www.baidu.com
    on_stop: stop-preview
```

用于设置部署完成的地址，在 pipeline 结束后可以在 `运维 -> 环境` 中看到入口

![[使用 Gitlab-CI‘CD 自动化部署 (转载)-28.png]]

- 关闭环境

![[使用 Gitlab-CI‘CD 自动化部署 (转载)-29.png]]

```
deploy-dev:
    environment:
        name: development
        url: https://www.baidu.com
        on_stop: stop-dev
stop-dev:
    environment:
        name: development
        action: stop
```

- cache
- artifacts
- dependencies

7. #### cache 和 artifacts
    

区别：

1. cache 不一定命中，aritfacts 一定命中
2. cache 可以在不同的 pipeline 中共享，artifacts 在不同的 job 中共享
3. artifacts 可作为 job 产物在 gitlab 中提供下载和浏览
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-30.png]]
![[使用 Gitlab-CI‘CD 自动化部署 (转载)-31.png]]

**cache**

cache 的设计用来保存编译或者重建后的资源依赖或者库，比如 node_modules，来加速下次的编译构建的 pipeline。

**cache: key**

可使用 key 来标记不同的 cache，默认为 defalut

**cache: policy**

1. pull-push：在默认情况下，如果有 cache 的配置，那么每个 job 会在开始执行前将对应路径的文件下载下来，并在任务结束前重新上传，不管文件是否有变化都会如此操作。这个默认的配置是 `cache:policy` 中的 `pull-push` 策略。
2. pull：但是如果我们已经知道，某个 job 只是使用的其他 job 改变的文件，自身并无改变对应路径的文件，那么就不需要进行文件上传操作，采用`pull` 策略即可。
3. push：反过来，某个 job 不依赖于其他 job 改变的文件，自身改变的文件被其他 job 所依赖，那么就不需要在 job 开始前进行文件下载操作，采用`push` 策略。这样减少了不必要的操作，在一定程度上节约了时间。

```
cache:
    key: $CI_COMMIT_REF_SLUG
    policy: pull-push
    path: node_modules/
```

禁用 cache：cache: {}

**artifacts**

在不同的 stage/job 中共享档案，配合 dependencies 属性使用

```
stages:
    - install
    - build

install:
    stage: install
    artifacts:
        name: packages
        untracked: true
        expire_in: 10 mins
        when: on_success
        paths:
          - node_modules
```

untracked: 缓存对应 path 中没有被 git 跟踪的文件

when: 在何时上传 artifacts，on_success 、 on_failure 、 always

expire_in: 缓存时间，到期自动清除

- '3 mins 4 sec'
- '2 hrs 20 min'
- '2h20min'
- '6 mos 1 day'
- '47 yrs 6 mos and 4d'
- '3 weeks and 2 days'

dependencies：用来在 job 之间传递 artifacts

```
build:
    stage: build
    dependencies: install 
# 或者 
    dependencies: 
        - install
        - others
```

## 实践
