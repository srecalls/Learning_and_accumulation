Git Commit Message 书写指南

1. 分支命名规范

> 我们为什么需要分支规范，好的分支规范有助于工具生成 change log，便于后续追踪代码仓库的演进过程

1. 功能分支： feat/username-module
2. bugfix 分支：fix/username-module
3. 代码重构分支：refactor/username-module
4. 文档相关：doc/username-module

2. commit message 提交建议

良好的 commit message 向他人传递刚刚好（不模糊、不冗余）的信息和细节，从而减少他人理解代码的心智负担，保证代码仓库的良性增长。

如下是 linux 内核的一个 commit，可以看到 commit 的信息（远）超过了代码改动本身，对于多人合作的项目，commit 信息可以向别人传递某处修改的前因后果，提供上下文，或者一些不为人知的细节，让他人更好的理解代码。当然我们并非要求所有的 commit message 都这样书写，当代码（或者代码中的注释）已经可以说明问题的时候，可以写的更加简短。

建议：

1. bugfix 描述bug为何引入，以及修复的逻辑
2. 对于需求，补充对应的产品文档、技术文档、接口文档
![[Git Commit Message 书写指南.png]]

下面是一段我们自己仓库的提交记录，也遵循了如上原则，由于此次提交有特例，但代码本身不足够描述这个特例，特在提交记录中备注说明，所以是一个好的提交记录。
![[Git Commit Message 书写指南-1.png]]
如下记录虽然只有一行，仍然是一个好的提交记录，因为这一句话结合代码已经把事情描述的足够清晰
![[Git Commit Message 书写指南-2.png]]
3. 原则上要求一次功能分支一个commit，在mr提交之前，git rebase -i origin/master；或者也可以通过 gitlab 自带的功能``squash commits when merge request is accepted`` 合并
![[Git Commit Message 书写指南-3.png]]
参考：[【写好 CL 描述】](https://jimmysong.io/eng-practices/docs/review/developer/cl-descriptions/)

Git 操作：[Git 飞行指南](https://github.com/k88hudson/git-flight-rules/blob/master/README_zh-CN.md)