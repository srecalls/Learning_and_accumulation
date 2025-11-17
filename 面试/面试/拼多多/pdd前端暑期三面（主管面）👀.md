# -13 pdd前端暑期三面（主管面）

0. 自我介绍  
1. 为什么学前端  
2. 看输出（中间好像还有一部分，但是忘记了）  
```  js
console.log(typeof A);  
console.log(typeof B);  
function A(){};  
var B = function(){} // 然后var改成let会怎样  
  
const obj = {};  
function C(){  
    return obj;  
}  
console.log(new C()===obj);// 答了true，然后问为什么这里是true，回答了构造函数如果返回值是引用类型则直接返回，如果是基本类型或没有显式返回，则返回创建的实例对象  
console.log(C()===obj);  // true
```  
[[手写new操作符]]
3. 获取页面所有标签的名字，以数组形式返回，且返回的数组不包含重复的名字（真是救了大命，前两天刚好看到过类似的面试题自己写了一下，本来对dom的api不是很熟悉）  
[[20.常见的DOM操作有哪些]]
[[常见的DOM操作有哪些]]
[[常见的DOM元素属性]]
![[pdd前端暑期三面（主管面）.png]]
```js

```
4. 手写promise.all（然后问了一下我代码里为什么用Object.prototype.toString.call来判断promise对象）  

反问：咱们三面就做这几道题就结束了吗？  
答：是的，因为是招实习生嘛（全程唯一一次笑），所有项目经历也没什么好问的。（leader就是不一样）  
  
leader特别年轻，虽然全程不苟言笑，但语气都很好。然后看得出他特别忙，给了题后就一直皱眉头看手机。  
  
希望能收到hr面![](https://uploadfiles.nowcoder.com/images/20220815/318889480_1660553876118/CAEB30813C5D910A6FBAAC41F8914E38)

![](https://static.nowcoder.com/fe/file/oss/icon_job.png)

  
  
作者：啊咧嗑嘶  
链接：[https://www.nowcoder.com/feed/main/detail/13e45c8e2f2947b0ba156cc98d114c60?sourceSSR=search](https://www.nowcoder.com/feed/main/detail/13e45c8e2f2947b0ba156cc98d114c60?sourceSSR=search)  
来源：牛客网