forEach专门用来循环数组，可以直接取到元素，同时也可以取到index值
存在局限性，不能continue跳过或者break终止循环，没有返回值，不能return


终止foreach循环 ： **运用抛出异常（try catch）可以终止foreach循环** 
for of是ES6新引入的特性。修复了ES5中for in的不足
允许遍历 Arrays（数组）、Strings（字符串）、Maps（映射）、Sets（集合）等可迭代的数据结构
for of 支持return

for in 和 for of可以return 或者 break 跳出
# 错误用法1：使用break(会报错)
```js
var array = ["第一","第二","第三","第四"];
        
// 直接就报错了
array.forEach(function(item,index){
    if (item == "第三") {
        break;
    }
    alert(item);
});
```
![[JS跳出Array.prototype.forEach循环.png]]


# 错误用法2：使用return fasle （只是终止本次循环）

相当于for 循环中的continue
```js
var array = ["第一","第二","第三","第四"];
        
// 会遍历数组所有元素，只是执行跳过"第三"，return false下面的代码不再执行而已
array.forEach(function(item,index){
    if (item == "第三") {
        return false;
    }
    console.log(item);// "第一" "第二" "第四"
});
console.log("以下代码")// 以下代码
```
![[JS跳出Array.prototype.forEach循环-1.png]]


# 正确用法：运用抛出异常（try catch）
```js
try {
    var array = ["第一","第二","第三","第四"];
    
    // 执行到第3次，结束循环
    array.forEach(function(item,index){
        if (item == "第三") {
            throw new Error("第三");
        }
        console.log(item);// 第一 第二
    });
} catch(e) {
    if(e.message!="第三") throw e;
};
// 下面的代码不影响继续执行
console.log("下方代码");//下方代码
```
![[JS跳出Array.prototype.forEach循环-2.png]]