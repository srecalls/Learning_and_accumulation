## # vue : 无法加载文件 D:\nodejs\node_global\vue.ps1，因为在此系统上禁止运行脚本。
在vscode新建vue项目 **vue init webpack vue_app** 时报错

vue : 无法加载文件 D:\nodejs\node_global\vue.ps1，因为在此系统上禁止运行脚本。

![[Pasted image 20230326155436.png]]

PowerShell的执行政策阻止了该操作。

运行`Get-ExecutionPolicy`查看发现执行策略为受限状态：

  ![[Pasted image 20230326155446.png]]



运行`Set-ExecutionPolicy -Scope CurrentUser`，**再输入`RemoteSigned`即可
![[Pasted image 20230326155454.png]]
  
