拉取代码

	git pull '仓库地址'
	
查看状态

	git status

提交到本地缓存区

	git add .

提交本地仓库

	git commit -m '修改描述'

提交到远程仓库

	git push ' 仓库地址’ master
	
创建分支

	git branch -b XXX
	
合并分支

	git merge ' 合并分支的名字 '

合并完后要再次push到远程仓库


第一次要拉取代码git pull，然后写完代码要上传，上传前要看状态git status
要提交到本地缓存区 git add . ，再提交到本地的git仓库 git commit -m ”“，
要把它提交到远程仓库 git push ” “ master，然后就可以用git pull来拉取代码了。
怎么创建分支 git branch -b xxx ，给不同的开发者用，开发完后要合并分支，
git merge ”“，然后在push到仓库里