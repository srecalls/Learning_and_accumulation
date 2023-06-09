难度：<font color ="lightgreen">简单</font>
在字符串` s`  中找出第一个只出现一次的字符。如果没有，返回一个单空格。` s `只包含小写字母。

示例 1:

	输入：s = "abaccdeff"
	输出：'b'
示例 2:

	输入：s = "" 
	输出：' '
 

限制：

	0 <= s 的长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof


## 我的提交
### version 01
```js
/**
 * @param {string} s
 * @return {character}
 */

var firstUniqChar = function(s) {
    let hash = []
    for (let item of s) {
        hash[item] = (hash[item] || 0) + 1 
    }
    for  (let item in hash) {
        if (hash[item] == 1) {
            return item
        }
    }
    return ' '
};
```

### version 02
可以使用字符串的 `indexOf()` 方法和 `lastIndexOf()` 方法来查找字符在字符串中第一次出现和最后一次出现的位置，然后使用数组的 `slice()` 方法来提取字符串中的子串，最后判断子串中是否只包含一个字符即可。
```js
function findFirstUniqueChar(str) {
  for (let i = 0; i < str.length; i++) {
    const char = str[i];
    const firstIndex = str.indexOf(char);
    const lastIndex = str.lastIndexOf(char);
    if (firstIndex === lastIndex) { // 只出现一次
      return char;
    }
  }
  return null; // 没有找到
}
```