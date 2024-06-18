[![头像](https://uploadfiles.nowcoder.com/images/20240601/891985434_1717230407224/FECD76F09C4EFFA7102ECDBC1795FB3B?x-oss-process=image%2Fresize%2Cw_72%2Ch_72%2Cm_mfit)](https://www.nowcoder.com/users/891985434)

[Ku1s](https://www.nowcoder.com/users/891985434)[![](https://static.nowcoder.com/fe/file/site/www-web/prod/1.0.341/imageAssets/310869668470a4bb981d.png)](https://www.nowcoder.com/users/891985434)

06-14 09:32已编辑合肥工业大学宣城校区 计算机类发布于安徽

关注



我单方面开摄像头，时长 60mins

1. 自我介绍
    
2. 拷打项目: 项目介绍，后端接口，登陆验证，路由拦截，表单验证
    
3. 如何实现一个Promise？ 口述了很久，后面讲到了实现all和race他说可以了
    [[6.Promise.all和Promise.race的区别和使用场景]]
    [[手写Promise.all]]
    
1. CSS 文字溢出怎么实现？
    
5. 水平垂直居中有哪些方法？
    
6. flex:1  是哪些属性构成的？
    
7. 回流和重绘
    
8. JS 类型有哪些？
    
9. 如何判断是否为 Array？ instanceof
    
    - instanceof 原理？
    - 还有什么判断方法？ Object.prototype.toString
10. 字符串常用方法，增删改查？ 一开始把和数组的搞混了,后来让我说数组的
    
11. 数组常用方法？ 答了pop push shift unshift splice slice 还有 includes find
    
    - splice 用法
    - slice 用法
12. 数组轮询的常用方法？ for of forEach
    
    1. map方法可以遍历数组吗？
    2. map 和 forEach 的区别？
    3. map是否会改变原数组？ 这里没答好
13. 求两个数组的交集？
    
    ```js
    arr1 = [1,2,3,4,5]
    arr2 = [3,4,5,6,7]
    
    const set = new Set(...arr1)
    const res = arr2.filter(item => set.has(item))
    ```
    
14. == 和 === 的区别? == 的使用场景
    
15. 浅拷贝和深拷贝的区别? 说两个浅拷贝的方法? 深拷贝怎么实现?
    
16. 异步输出问题:
    
    ```js
    setTimeout(() => console.log(0))
    
    new Promise((resolve) => {
      console.log(1)
      resolve(2)
      console.log(3)
    }).then((o) => console.log(o))
    
    new Promise((resolve) => {
      console.log(4)
      resolve(5)
    })
      .then((o) => console.log(o))
      .then(() => console.log(6))
    
    // 1  3  4  2  5  0
    ```
    
17. React 常用 hooks
    
18. 用 git 吗? 平时的项目都是几个分支?
    
19. 反问:
    
    1. 对我的评价和学习建议: 说我总体不错, 可以涉猎得广一点,向AI这种
        

总结:

总体体验不错, 面试官虽然没开摄像头但是很和善, 从CSS溢出开始我一直在共享屏幕, 边敲边回答, 有啥不太对的地方他也会提示, 问的也不难, 可惜最后反问说到他们可能会找有实习经历可以直接去干活的, 我说大概懂了

[#前端#](https://www.nowcoder.com/creation/subject/3bf5855355554c05a65af8b25cd105b3)[#面经#](https://www.nowcoder.com/creation/subject/928d551be73f40db82c0ed83286c8783)[#蔚来#](https://www.nowcoder.com/creation/subject/e938a07ddcb5471aa50dda2970b6808e)