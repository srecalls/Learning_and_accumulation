# 拼多多-前端实习一二三面+hr面(已offer)

写在前面：  
多多面试官都很好，会引导我写题。写得慢的也很耐心在等我。

### 一面

一面面试官侧重知识广度（因人而异，主要看面试官）  
1h 左右，面试当场面试官跟我说过了。第二天收到二面邀请。

```js
- 写题：  
    实现 sum(2)(3)(4)，输出结果为参数乘积 2*3*4=24  
    追问是否可以进一步用函数柯里化形式改写
```
- 判断输入输出
    
```js
    function a(i){
    let value=0;
     function b(){
      value+=i;// 当前作用域没有 value，向上级作用域查找
      console.log(value)
      const msg = `Current value is ${value}`
      return function c(){
        console.log(msg);
      }
    }
    return b;
    }
    //-----------------
    let lon = a(1);
    let log = lon(); // 1
    lon(); // 2
    lon(); // 3
    log(); // Current value is 1
    
```
    做完问我这道题考了什么
    
    [[1.对闭包的理解]]
- 问答环节  
```
    很全面地考察知识广度，不算难。  
    大概 1min 一个问题，问了几十个。应接不暇那种  
    html css js promise 计网 基本都问了（有空补上）  
    说几个印象深刻的
    1. `<meta>` 标签的作用
    2. `position:relative` 是相对于谁定位的
```
- 反问  
    反问环节开始前，面试官主动给我解释了我刚才答错的部分。

### 二面

二面面试官侧重知识深度，每个知识点都会深挖。  
1h 左右，过了不到一周收到三面邀请。

- 项目  
    细节等等，不具体说了。因人而异
- 写题  
    实现一个 debounce 函数，除了满足防抖功能以外，当函数触发次数达到 n 次时，也会执行。  
    写完面试官说思路是正确的，然后一点一点引导我一起改细节，同时追问了很多问题。  
    （根据我说的来进一步提问，面试体验超好）
    ```js
    function debounce(fn, dalay, time) {
	    let timer = null
	    let times = 0
	    return function () {
		    if (timer) {
			    cleatTimeout(timer)
		    }
		    if (times === time) {
			    fn.apply(this, arguments)
			    cleatTimeout(timer)
		    }
		    timer = setTimeout(() => {
			    fn.apply(this, arguments)
		    }, delay)
	    }
	}
```
- 问答  
    说几个印象深刻的  
    1）如何判断一个对象是 promise 对象  
    [[判断对象是否为 Promise 对象]]
    2）a++ 和 ++a 的区别，分别的使用场景  
    3）如何判断一个对象是空对象  
    [[21.如何判断一个对象是空对象]]
    [[数组和伪数组的区别，为什么要设置成伪数组,如何判断是否为伪数组]]
    [[3.判断数组的方式有哪些]]
    4）类数组对象转成数组的方式
    - `Array.from(args)`
    - `Array.prototype.slice.call(args)` 追问 splice 可不可以
    - `[...args]`
    - 追问其他方法，map可以吗，怎么实现？ `Array.prototype.map.call(item=>item)`
[[JavaScript常用数组操作方法，包含ES6方法]]
### 三面

25min  
三面面试官很和蔼，开始就告诉我“聊一聊”，大概 20-30min。  
三面面试官侧重学习能力、逻辑能力等综合素质。

- 高考为什么选择南理工？（直接给我整蒙了hhh），为什么选这个专业
- 什么时候去 LeetCode 实习的，为什么去做这段实习，什么样的机会下选择了这家公司。
- 什么时候决定往前端方向发展
- 有没有团队，是自己学习吗？自己怎么学的
- 项目难点，技术细节，怎么解决的
- 项目技术选型的考虑
- 对我用到的库有没有去了解底层是怎么实现的
- 解释 immutable.js 的实现原理
- base 地点的考虑
- 互联网公司的工作节奏
- 如果你的底子比其他人有一些差距，你会怎么做？
- 反问

### hr 面 4月19日

30min

- 项目难点，项目遇到问题怎么解决的
- 你最挫败的经历
- 是否接收互联网工作强度
- 对 base 地的考虑
- 个人、家庭相关问题
- 实习期望的薪资

hr 说 2-3周给 offer

---

5月5日 收到 offer 邮件

  
  
作者：努力冲大厂的驴驴不要害怕不要放弃  
链接：[https://www.nowcoder.com/discuss/353159557444739072](https://www.nowcoder.com/discuss/353159557444739072)  
来源：牛客网