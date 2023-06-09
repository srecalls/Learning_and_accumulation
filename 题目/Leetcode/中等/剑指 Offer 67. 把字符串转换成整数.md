难度：<font color ="orange">中等</font>
写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。

 

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：

假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 \[$−2^{31}$,  $2^{31}$ − 1]。如果数值超过这个范围，请返回  INT_MAX (  $2^{31}$ − 1) 或 INT_MIN (−  $2^{31}$) 。

示例 1:

	输入: "42"
	输出: 42
示例 2:

输入: "   -42"
	输出: -42
	解释: 第一个非空白字符为 '-', 它是一个负号。
	     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
示例 3:

	输入: "4193 with words"
	输出: 4193
	解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
示例 4:
	
	输入: "words and 987"
	输出: 0
	解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
	     因此无法执行有效的转换。
示例 5:

	输入: "-91283472332"
	输出: -2147483648
	解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
	     因此返回 INT_MIN (−231) 。
 

注意：本题与主站 8 题相同：https://leetcode-cn.com/problems/string-to-integer-atoi/

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof

	1.^ :匹配输入字符串的开始位置， 除非在方括号表达式中使用，
	当该符号在方括号表达式中使用时， 表示不接受该方括号表达式中的字符集合。
	要匹配 ^ 字符本身， 请使用\ ^ 。
	2.?:匹配前面的子表达式零次或一次， 或指明一个非贪婪限定符。 要匹配 ? 字符， 请使用\ ? 。
	3.|:指明两项之间的一个选择。 要匹配 | ，请使用\ | 。
	4.+: 匹配前面的子表达式一次或多次。 要匹配 + 字符， 请使用\ +


```JS
var strToInt = function(str) {
   str = str.trim(); //trim() 方法用于删除字符串的头尾空格,不会改变原始字符串。

    //正则表达式
    var pattern=/^(\-|\+)?[0-9]+/;
    var tmp=pattern.exec(str);   
    if(tmp){
        var num=Number(tmp[0]);  //tmp是个类数组，第一位是匹配到的字符串
        if (num < Math.pow(-2,31)){
            return Math.pow(-2,31)
        }
        if (num >=Math.pow(2,31)){
            return Math.pow(2,31)-1;
        }
        return num;
    }
    return 0;
};
```



## 我的提交 （未通过）
```js
/**
 * @param {string} str
 * @return {number}
 */
var strToInt = function(str) {
    console.log(str)
    if (str.trim().charAt(0) == '-' && parseInt(str) < -2147483647) {
        return -2147483648
    }
    if (str !== '0' && parseInt(str) >= 2147483647) {
        return 2147483647
    }
    if (str.trim().length > 1  && str.trim().charAt(2) == ' ') {
        return 0
    }
    if (str.includes('+') && str.includes("-")) return 0
    if (str.trim().charAt(0) == '+') {
        if(str.trim().length == 1) {
            return 0
        }
        str = str.trim().slice(1)
        if (!isNaN(parseInt(str))) return parseInt(str)
        else return 0
    }
    if (str.trim().charAt(0) !== '' && isNaN(str.trim().charAt(0)) || str.trim().length == 0) {
        return 0
    }
    if (str.trim().length == 1 && str.trim().charAt(0) == '-') {
        return 0
    }
    let judge = 0
    for(let i = 0; i < str.length; i++) {
        console.log(str[i] - 0)
        if (!isNaN(str[i] - 0)) {
            judge = 1
        }
    }
    if (judge == 1) {
        parseInt(str)
    }
    if (judge == 0) {
        return 0
    }
    return parseInt(str)
};
```