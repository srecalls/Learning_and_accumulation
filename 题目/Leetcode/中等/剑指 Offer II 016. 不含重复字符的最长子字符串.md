难度：<font color ="orange">中等</font>
给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长连续子字符串** 的长度。

示例 1:

	输入: s = "abcabcbb"
	输出: 3 
	解释: 因为无重复字符的最长子字符串是 "abc"，所以其长度为 3。
	
示例 2:

	输入: s = "bbbbb"
	输出: 1
	解释: 因为无重复字符的最长子字符串是 "b"，所以其长度为 1。
	
示例 3:

	输入: s = "pwwkew"
	输出: 3
	解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
	     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
  
示例 4:

	输入: s = ""
	输出: 0
 

提示：
	
	0 <= s.length <= 5 * 10^4
	s 由英文字母、数字、符号和空格组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/wtcaE1


## 面试题解
```js
// 计算给定字符串中最长的无重复字符的子串长度
var lengthOfLongestSubstring = function(s) {
    let map = new Map(); // 用 Map 存储字符和它们的索引
    let i = -1; // i 为滑动窗口的左边界
    let res = 0; // res 记录最长的无重复字符的子串长度
    let n = s.length; // 字符串的长度
    for (let j = 0; j < n; j++) { // j 为滑动窗口的右边界
        if (map.has(s[j])) { // 如果当前字符在 Map 中已经存在
            i = Math.max(i, map.get(s[j])); // 移动左边界，确保左边界不会向右移动
        }
		// abbac*bcad*
		// abba
        res = Math.max(res, j - i); // 更新最长的无重复字符的子串长度
        map.set(s[j], j); // 将字符和它的索引存入 Map 中
    }
    return res; // 返回最长的无重复字符的子串长度
};
```

	执行用时：72 ms, 在所有 JavaScript 提交中击败了95.13%的用户
	内存消耗：44.2 MB, 在所有 JavaScript 提交中击败了70.35%的用户
	通过测试用例：987 / 987
