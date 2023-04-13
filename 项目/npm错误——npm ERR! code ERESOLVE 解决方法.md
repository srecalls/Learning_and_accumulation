```SHELL
npm ERR! code ERESOLVE
npm ERR! ERESOLVE unable to resolve dependency tree
npm ERR!
npm ERR! While resolving: vuecli3@0.1.0
npm ERR! Found: vue@2.7.5
npm ERR! node_modules/vue
npm ERR!   vue@"^2.6.10" from the root project
npm ERR!
npm ERR! Could not resolve dependency:
npm ERR! peer vue@"^3.0.0" from vant@3.5.2
npm ERR! node_modules/vant
npm ERR!   vant@"*" from the root project
npm ERR! Fix the upstream dependency conflict, or retry
npm ERR! this command with --force, or --legacy-peer-deps
npm ERR! to accept an incorrect (and potentially broken) dependency resolution.
npm ERR!
npm ERR! See C:\Users\l\AppData\Local\npm-cache\eresolve-report.txt for a full report.
```

在安装组件的时候出现以上问题，npm版本问题报错

解决方法：

在命令后面加上
``` 
--legacy-peer-deps
```
![[Pasted image 20230329120158.png]]



