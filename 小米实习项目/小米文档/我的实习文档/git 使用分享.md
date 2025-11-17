1. ## git分区
    

一、git有三个分区，分别为：

- **工作区**
    
- **暂存区（stage或叫index）**
    
- **版本库**
    

暂时无法在飞书文档外展示此内容

`git status`

可以用来查看工作区和暂存区的状态，该命令**经常使用**；每执行一条指令后，都可以使用该命令**查看**工作区和暂存区的**状态**；**红色**表示对文件的更改还没提交到暂存区；**绿色**表示已提交到暂存区；
![[git 使用分享.png]]
## 2.工作区-->暂存区

`git add <file>`

可以将**工作区**中的文件提交到**暂存区**：

![[git 使用分享-1.png]]

如图中：原先1.txt和2.txt都在工作区，处于未跟踪（untruck）的状态。在使用`git add 1.txt`后，就成功将1.txt提交到了暂存区。还可以使用`git add .`命令将**所有**工作区未跟踪状态的文件都提交到暂存区（**不推荐，**最好手动输入要提交的更改文件，添加了什么文件要自己心中有数，也是一个对改动过的代码再检查的过程）。

## 3.暂存区-->版本库

1.`git commit -m '注释'`

git commit将暂存区中的文件提交到版本库，**一定要添加注释，否则不让提交**：
![[git 使用分享-2.png]]
**commit的注释规范非常重要！**详细参考[Git commit 规范 V1.0](https://xiaomi.f.mioffice.cn/docs/dock42OhsL48XWsrKUWNGN8JNZd)

尽量要参照commit规范来写注释，在注释比较多有多行的情况下，可以这样来分行：

在git commit -m后面先只打一个引号`"`，然后输入内容并可以使用回车进行换行，在多行注释写完后在最后一行的后面补全第二个引号`"`。
![[git 使用分享-3.png]]
注释较多的情况下也可以直接使用`git commit` 回车，此时会弹出默认的文本编辑界面，一般为vim编辑器（[vim使用教程](https://www.runoob.com/linux/linux-vim.html)），ubantu系统为nano编辑器([nano使用教程](https://cloud.tencent.com/developer/article/1935086))。可以在里面输入多行注释。结束后vim通过`:wq`保存并退出。nano按`ctrl+x`保存退出。
![[git 使用分享-4.png]]
如何改变git默认唤起的编辑器？

可以通过以下两种方式（以 nano 改 vim 为例）：

- 设置环境变量 你可以设置 `GIT_EDITOR` 环境变量来改变 Git 默认使用的编辑器。在终端中输入以下命令： `export GIT_EDITOR=vim` 如果你想将这个设置永久保存下来，可以将这个命令添加到你的 shell 配置文件中（例如 `~/.bashrc` 或 `~/.zshrc`）。
    
- 修改 Git 配置文件 你也可以通过修改 Git 配置文件来改变默认编辑器。可以使用以下命令打开 Git 配置文件： `git config --global core.editor "vim"`
    

  

## 4.修改提交信息

### (1)修改最近一次提交信息

`git commit --amend` :

如果写错了提交消息,可以通过：`git commit --amend` 来修改**上一次(最近的一次)**的提交信息：（`amend`是修复的意思）。同样是通过vim或nano界面进行注释编辑。

Git log查看到最近的一次提交是“rebase咯”
![[git 使用分享-5.png]]
用git commit --amend进入vim或nano界面进行注释编辑
![[git 使用分享-6.png]]
保存后git log可以看到最近的一次commit被修改为了新的备注信息：可以看到两次commit id是不同的。amend操作并不是简单的在原来的上面修改，而是创建了一个**新**commit替换了原来需要修正的commit。
![[git 使用分享-7.png]]
在注释较短的时候也可以用`git commit --amend -m "注释"` 。

  

  

### (2)修改特定某次/多次提交信息

需要用到功能强大的`git rebase -i`

在交互式模式下，你可以指定要重写的提交范围，然后 git 会打开一个文本编辑器，让你对这些提交进行编辑。你可以对每个提交进行操作，比如修改提交信息、合并提交、删除提交等等。

关于`git merge`和`git rebase`和`git cherry-pick`的区别：

`git merge`

将两个分支的更改合并成一个新的提交，并将其添加到**当前**分支的历史记录中。这个新的提交有两个父提交，分别是当前分支和要合并的分支。这种方式会保留原来的提交历史，但可能会产生一些不必要的合并提交。

![[git 使用分享-8.png]]

`git rebase`变基

**将要合并的分支的更改“重演”在当前分支上，然后将当前分支指向这些新的提交。**这种方式会使提交历史变得更加线性，因为它会将要合并的分支的更改“插入”到当前分支的提交历史中。
![[git 使用分享-9.png]]
使用 rebase 方法形成的提交历史是**完全线性**的，同时相比 merge 方法少了一次 merge 提交，看上去更加整洁。

  

`git rebase` 的交互模式：

`git rebase`命令有标准和交互两种模式，在命令后添加 `-i`或 `--interactive` 选项即可使用交互模式。

在 rebase 的标准模式下，当前工作分支的提交会被直接应用到传入分支的顶端；而在交互模式下，则允许我们在重新应用之前通过编辑器以及特定的命令规则对这些提交进行**合并**、**重新排序**及**删除**等**重写操作**。

交互模式会打开vim或nano编辑器，交互模式可用命令：

|   |   |
|---|---|
|**命令（简写，全写）**|**作用**|
|**p, pick**|使用提交|
|**r, reword**|使用提交，但修改提交说明|
|**e, edit**|使用提交，进入 shell 以便进行提交修补|
|**s, squash**|使用提交，但融合到前一个提交|
|f, fixup|类似于 "squash"，但丢弃提交说明日志|
|x, exec|使用 shell 运行命令（此行剩余部分）|
|b, break|在此处停止（使用 'git rebase --continue' 继续变基）|
|**d, drop**|**删除提交。被删除的提交中的代码将不会出现在重写后的分支中**|

对命令的使用可以参照：[Git rebase 的一个小case:](https://xiaomi.f.mioffice.cn/docx/doxk4ckraBQkaQbURgq7StRounh)

`git cherry-pick`

择优挑选:"cherry-pick" 这个词源于英语中的一个习语，意思是选择最好的部分或最有利的部分。

在git 中，cherry-pick 操作就是选择一个或多个提交，将它们应用到当前所在的分支上，而不是将整个分支合并过来。即：需要另一个分支的所有代码变动，那么就采用合并（`git merge`）。若只需要部分代码变动（某几个提交），这时可以采用cherry-pick。 和 rebase 操作正好相反，会以当前的分支为基础，然后将 commit 一个个的拿过来应用。形成的 commit 记录和rebase一样也是串行的。

  

#### 合并提交信息

方法一：git rebase -i HEAD~n

要将commit id为6ab0a和c5cba的两次commit进行合并
![[git 使用分享-10.png]]
![[git 使用分享-11.png]]

![[git 使用分享-12.png]]
![[git 使用分享-13.png]]
方法二：

在本地分支使用git merge --squash，再提交到远程仓库
![[git 使用分享-14.png]]
使用

`git merge --squash feature`
![[git 使用分享-15.png]]
方法三：可以在gitlab的merge request界面勾选Squash commits，可以将多个commits合并，在Squash commit message中可以编辑合并后的commit信息。merge默认会添加分支中的所有commits message和一条merge message，勾选squash后只会添加一条commit message和一条merge message。
![[git 使用分享-16.png]]

  

## 5.工作区<--暂存区

简单来说，就是将`git status`指令显示出来的文件，从**绿色**变为**红色**，大概有如下三种方法：

(1)`git rm --cached <file>`
![[git 使用分享-17.png]]
(2)`git restore --staged <file>`
![[git 使用分享-18.png]]
（3）`git reset HEAD <file>`
![[git 使用分享-19.png]]

## 6.日志git log

git log有很多可用的后缀选项，可以使log看起来更清晰：

|   |   |
|---|---|
|选项|作用|
|`-p`|显示提交的补丁（具体更改内容）|
|**`--oneline`**|以简洁的一行格式显示提交信息|
|**`--all`**|显示分支、标签和其他引用的历史记录中的所有提交|
|**`--graph`**|以图形化方式显示分支和合并历史|
|**`--decorate`**|显示分支和标签指向的提交|
|**`--author=<作者>`**|只显示特定作者的提交|
|**`--since=<时间>`**|只显示指定时间之后的提交|
|`--until=<时间>`|只显示指定时间之前的提交|
|`--grep=<模式>`|只显示包含指定模式的提交消息|
|`--no-merges`|不显示合并提交|
|`--stat`|显示简略统计信息，包括修改的文件和行数|
|`--abbrev-commit`|使用短提交哈希值|
|`--pretty=<格式>`|使用自定义的提交信息显示格式|

一个小case：使用后缀选项让log可视性更好：`git log --all --decorate --oneline --graph`

(也可以使用例如tig和git graph,gitlens等vscode插件来进行更好看的图形化显示)
![[git 使用分享-20.png]]
如果不想每次都打这么长的命令，可以使用git的alias命令（用于创建自定义的 Git 命令别名）来简化命令：

`git config --global alias.lg git log --all --decorate --oneline --graph`

这样之后输入git lg就可以使用这行代码的快捷命令。[Git Aliases的使用](https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases)

  

  

## 7.有关“撤销”的操作

### (1)工作区中的撤销

`git restore -- <file>`撤销工作区中对文件的操作，包括新增、修改、删除等
![[git 使用分享-21.png]]

### (2)commit版本回退

分两种情况：

- 已经add,commit,尚未push
    

**`git reset`** `--mixed|--soft|--hard` (默认值就是--mixed)

上面常见三种类型

`--mixed`

会保留源码,只是将git commit和index 信息回退到了某个版本。

git reset 默认是 --mixed 模式

git reset --mixed 等价于 git reset

`--soft`

保留源码,只回退到commit 信息到某个版本.不涉及index的回退,如果还需要提交,直接commit即可。

`--hard`

源码也会回退到某个版本,commit和index 都回回退到某个版本.(注意,这种方式是改变本地代码仓库源码)

- 已经push
    

**`git revert`** `-- <commit ID>`

git revert用一个**新提交**来消除一个历史提交所做的任何修改。revert 之后本地代码会回滚到指定的历史版本,这时再 git push 就可以把线上的代码更新。(这里不会像reset造成冲突的问题)

revert 使用,需要先找到你想回滚版本唯一的commit标识代码

git revert是用一次新的commit来回滚之前的commit，git reset是直接删除指定的commit

看似达到的效果是一样的,其实完全不同：

第一:

reset 是在正常的commit历史中,删除了指定的commit,这时 HEAD 是向后移动了,而 revert 是在正常的commit历史中再commit一次,只不过是反向提交,他的 HEAD 是一直向前的。如果已经push到线上代码库, reset 删除指定commit以后，git push可能导致一大堆冲突。但是revert 并不会。

第二:

如果在日后现有分支和历史分支需要合并的时候,reset 恢复部分的代码依然会出现在历史分支里。但是revert 方向提交的commit 并不会出现在历史分支里.

  

## 8.git分支问题

有关git分支的常见操作有：git branch（创建）,git checkout（创建，切换）,git switch（创建，切换）

**`git switch`****和****`git checkout`****的区别？**

在进行分支切换的情况下，这两个命令的作用是相同的。不同点在于，`switch`仅仅用于切换，而`checkout`是一个很复合的命令，可以完成很多事情，比如git checkout `<file> 可以将 <file>`文件恢复到最近一次提交的状态。因此在某些少见的特殊情况下（比如文件名和分支名重复），使用git checkout可能出现混乱。切换分支推荐使用git switch。

git switch -c(作用等同 git checkout -b)

`git switch -c <branch> --track <remote>/<branch>`(新建并跟踪远程分支)

  

**`git branch -d`****和****`git branch -D`****的区别？**

**`git branch -d <branch>`**和 **`git branch -D <branch>`**都是用来删除分支的命令，但是它们之间有一些区别。 **`git branch -d <branch>`**：这个命令会删除指定的分支，但是如果该要删除的分支还没有被合并到当前分支，那么删除操作会失败，因为这样会导致未合并的修改丢失。如果要强制删除该分支，可以使用 `-D` 选项。 **`git branch -D <branch>`**：这个命令会强制删除指定的分支，即使该分支还没有被合并到当前分支。使用这个命令要小心，因为它会永久删除分支上的所有提交，包括未合并的提交，这些提交可能会丢失。

## 9.vscode中git可视化操作

vscode的侧边栏：源代码管理中，可以用可视化方法操作git

git add和git commit
![[git 使用分享-22.png]]
git push和git pull:同步更改
![[git 使用分享-23.png]]
  

## git学习链接

**git****练习sandbox**： [learn git branching](https://learngitbranching.js.org/?locale=zh_CN&NODEMO=) 试试闯关levels

git官方参考书：[Pro Git 中文版（第二版）](https://www.progit.cn/)