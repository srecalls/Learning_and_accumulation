2021-08-20 22:45研发工程师

关注

# 小米 / 前端 / 一面+二面 / 许愿OC

## 小米

> 许愿OC,十年老米粉了，给了就签

### 小米一面8.13

> **面试情况：**挺好
> 
> **面试时长：**40分钟
> 
> **面试官态度**: ★★★★★
> 
> **面试感受：**挺好的，小哥哥很和蔼


1. 自我介绍
2. 为什么会选择前端呐？
3. JS和Java、python，你觉得你对前端更感兴趣哪个点？
4. 你觉得前端哪些地方需要抠细节呐？
[[你觉得前端哪些地方需要抠细节]]

**八股**

- CSS+HTML
    
## 1. H5新特性
        
        （补充：增强表单、Canvas、SVG、地理位置、拖放API、WebWorker、WebStorage、WebSocket）
        
## 2. 说说localStorage和SessionStorage应用
        [[蛋老师cookie、localStorage 和 sessionStorage的区别及应用实例]]
        [[localStorage和sessionStorage的应用场景]]
        [[1.浏览器本地存储方式及使用场景]]
## 1. localStorage什么情况下会被清空？如何手动清空
        
        （忘了，尴尬）
        
        - 保存数据：localStorage.setItem(key,value);
        - 读取数据：localStorage.getItem(key);
        - 删除单个数据：localStorage.removeItem(key);
        - 删除所有数据：localStorage.clear();
        - 得到某个索引的key：localStorage.key(index);

	[[localStorage什么情况下会被清空？]]
	[[localStorage什么情况下会被清空？如何手动清空]]
    1.  SessionStorage什么情况下会被清空？如何手动清空

        > SessionStorage：用于临时保存同一窗口(或标签页)的数据，在关闭窗口或标签页之后将会删除这些数据。    
        (关闭当前页面数据的销毁与否有两种情况：①如果它的页面中没有其他的超链接，或者没有打开，那么关闭当前页面，数据就会被销毁。②而如果通过当前这个页面，打开了其他的页面，那么只有当这些页面都关闭了，数据才会销毁。)
        
## 1. 块级元素和行内元素区别
        [[块级元素和行内元素的区别]]
##1. img是块状元素还是行内元素
	[[img是块状元素还是行内元素]]
        （尴尬，这个也忘了，img是行内块元素）

## 1. 定位position
        [[position有哪些属性]]
        [[position的属性有哪些,区别是什么]]
## 1. 了解fixed吗

        （回答的不太好
        - static，默认值。处于文档流的位置。
        - inherit，从父元素继承 position 属性的值。
        - fixed，生成绝对定位的元素。可定位于**相对于浏览器窗口**的指定坐标。但当祖先元素具有transform属性且不为none时，就会**相对于祖先元素**指定坐标，而不是浏览器窗口。
        - absolute，**相对于距该元素最近的已定位的祖先元素**进行定位。
        - relative，**相对于该元素在文档中的初始位置进行定位**。


## 1. 了解sticky吗
        
## 10. 默认定位是什么定位
        
## 11. CSS画三角形
        [[1.实现一个三角形]]
## 12. flex实现左上角元素移动到左下角
        
## 13. flex-shrink
        [[flex：1 完整写法]]
## 14. align-item和align-content区别
        [[flex布局常见父项属性]]
        [[flex布局子项常见属性]]
- **JS**
## 1. let和var
	[[var、let、const的使用及区别，什么是暂时性死区？]]

## 1. 原型链
        
    3. map和forEach区别
        
        （map有返回值（返回一个新数组，原数组不变），forEach返回undefined）
        
        （讲错了，讲了forEach不可以终止，其实他们都不能终止）
        
    4. 那你说说那些其他遍历方法可以终止
        
        （some和every）
        
## 5. 检测一个空对象
        [[21.如何判断一个对象是空对象]]
        （for in、Json.stringtyfy与''比较、Object.keys）
        
- ## HTTP
    
## 1. 状态码
        [[HTTP状态码]]
## 2. 同源策略
        [[说一下什么是同源策略]]
        （为什么要同源没回答好）
        [[为什么需要同源策略]]
## 3. 跨域解决方案
        [[（1）CORS]]
        [[（2）JSONP]]
- 项目
    
    1. 接触过webpack相关的吗
        
    2. 双绑原理
        
## 3. v-if和v-show
        [[v-if和v-show的区别？]]
## 4. v-if怎么实现的？
        [[11.v-if、v-show、v-html的原理]]
## 5. display:none和visibility:hidden区别
        [[8.display：none与visibility：hidden的区别]]
        （按照我的理解，display:none是不会被继承的，否则子元素可以改为display:block之后就能显示。反之visibility:hidden可以继承，子元素也可以通过改变visibility:visible显示）
        
## 6. vue组件传值/通讯
        [[组件通信]]
## 7. 用过vuex
        
## 8. 说说vuex的api
        [[6.Vuex有哪些属性？]]
## 9. 说说vuex的action和mutation
[[2.Vuex中action和mutation的区别]]
## 10. vue-router了解吗
        [[2.路由的hash和history模式的区别]]
## 11. 路由原理了解吗
        [[vue路由原理]]
- 手撕
    
    - 将数组中所有id变为code，所有title变为name
        
        ```js
        const list = [{
            id: 'a',
            title: 'A'
        }, {
            id: 'b',
            title: 'B',
            children: [{
                id: 'c',
                title: 'C'
            }, {
                id: 'd',
                title: 'D'
            }]
        }]
        ```
        **通过数组方法map（）修改属性名。**
```js

```

- 反问
    
    1. Q：技术栈
    2. A：React
    3. Q：业务
    4. A：OA系统、小米商城客服

### 小米二面

> **面试情况：**挺好
> 
> **面试时长：**30分钟
> 
> **面试官态度**: ★★★★★
> 
> **面试感受：**挺好的，八股文的天堂，有点小帅的小哥哥

**开场**

1. 为什么选择前端
2. 本科/研究生学习过哪些计算机课程（C语言、电工电子算吗？哈哈哈）
3. 怎么学习前端
4. 看过哪些书？（http）

**八股**

- **JS**
    
    - 观察者模式
	
    - ## JS异步编程
      [[async&await介绍]]
      [[9.async&await的优势]]
      [[7.对async&await的理解]]
    - ## promise原理
      [[⭐Promise基本概念]]
    - ## 箭头函数和普通函数
      [[4.箭头函数与普通函数的区别]]
      [[箭头函数和普通函数的区别]]
    - ## 跨域及原理
      [[（1）CORS]]
      [[（2）JSONP]]
    - ## 说说V8引擎和垃圾回收
      [[1.V8的垃圾回收机制是怎么样的]]
	[[1.浏览器的垃圾回收机制]]
	[[JS垃圾回收机制]]
- ## CSS
    
    - position：relative和absolute定位原点
      [[position的属性有哪些,区别是什么]]
    - ## 三角形
      [[1.实现一个三角形]]
    - ## rgba透明度，opacity透明度 
      [[说一下rgba透明度，opacity透明度]]
    - ## 说说BFC
      [[什么是BFC]]
- HTTP
    
    ## 1. 说说http发展史
    ## 2. 说说e-tag和if-modified
       [[1.对浏览器缓存的理解 （强缓存、协商缓存）]]
    ## 3. 说说CSRF
       [[3.什么是CSRF攻击]]
- ## 工程
    
    ## - vue初始化过程
      [[说一下vue初始化过程]]
    ## - webpack打包原理
      [[webpack的构建流程]]
- 手撕
    - 斐波那契数列
[[斐波那契数列]]
- 反问
    
    1. Q：技术栈
    2. A：React

[#小米面试#](https://www.nowcoder.com/creation/subject/9dcda820ab914feba29e5054528ada3c)[#小米#](https://www.nowcoder.com/enterprise/147/discussion)[#前端工程师#](https://www.nowcoder.com/creation/subject/9b7382be5f92428ab65557ddf5c5d188)[#面经#](https://www.nowcoder.com/creation/subject/928d551be73f40db82c0ed83286c8783)