![[Pasted image 20230306133826.png]]
![[Pasted image 20230302194143.png]]
![[Pasted image 20230302201452.png]]


# 2. 暂时性死区
let、const与var的另一个重要的区别，let、const声明的变量不会在作用域中被提升。ES6新增的let、const关键字声明的变量会产生块级作用域，如果变量在当前作用域中被创建出来，由于此时还未完成语法绑定，所以是不能被访问的，如果访问就会抛出错误ReferenceError。因此，在这运行流程进入作用域创建变量，到变量可以被访问之间的这一段时间，就称之为暂时
性死区

## 面试题
![[Pasted image 20230306134112.png]]
![[Pasted image 20230306134331.png]]