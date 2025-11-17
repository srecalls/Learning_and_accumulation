Git log中有A～F共6个commit记录:

![[Git rebase 的一个小case.png]]

接下来我们将要执行的操作是：

- 将 B、C 合并为一个新的提交 ，并仅保留原提交 C 的提交信息（pick,squash或fixup）
    
- 删除提交 D (drop)
    
- 将提交 E 移动到提交 F 之后并重新命名（即修改提交信息）为提交 G（pick,reword）
    

  

以A的commit id为rebase的基底：
![[Git rebase 的一个小case-1.png]]
fixup/squash C（fixup会忽略掉C的commit message。squash则会保留C的commit message，后续还会弹出编辑器界面来编辑此次合并的commit message，可在BC中选择）
![[Git rebase 的一个小case-2.png]]
执行完成保存后，再次git log查看，C已经和B合并，并沿用了commit message:B。
![[Git rebase 的一个小case-3.png]]
使用drop删除C：

![[Git rebase 的一个小case-4.png]]
保存后git log中不再有C的commit记录。
![[Git rebase 的一个小case-5.png]]
将commit E移动到commit F之后，并重新命名为G：

![[Git rebase 的一个小case-6.png]]
![[Git rebase 的一个小case-7.png]]