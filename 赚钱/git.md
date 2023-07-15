### 1. git常用指令

1. git init：初始化
2. git clone xx：克隆
3. git remote add origin xx：连接远程仓库
4. git branch newBranch：创建新分支
5. git checkout newBranch：切换分支
6. git checkout -b newBranch oldBranch：基于当前分支创建并切换到新分支，如果有写oldBranch则是基于oldBranch分支创建
7. git add xx：工作区添加到暂存区
8. git commit -m 'xx'：暂存区添加到本地版本库
9. git push origin xx：推送到远程仓库
10. git pull origin xx：从远程仓库拉取，相当于git fetch + git merge
11. git status：查看工作区状态
12. git log：查看提交记录
13. git reset --(soft、mixed、hard) head：回退版本
14. git revert xx：撤销指定版本的修改
15. git stash：暂存
16. git stash list：查看暂存表
17. git stash pop stash@{x}：删除暂存并拿回来

### 2. git merge和git rebase的区别

git merge会有一个合并的提交节点，git rebase则是直线的提交纪录，git merge可以用在主分支的合并，便于代码的追踪和管理，git rebase可以用在两个不是主分支的分支合并，这样提交纪录更简洁清晰。

### 3. git reset和git revert的区别

git reset是回退到某个版本，而git revert是撤销某个版本