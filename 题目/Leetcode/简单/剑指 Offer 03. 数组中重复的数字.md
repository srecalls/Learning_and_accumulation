难度：<font color ="lightgreen">简单</font>
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。



示例 1：

	输入：
	[2, 3, 1, 0, 2, 5, 3]
	输出：2 或 3 

限制：

`2 <= n <= 100000`


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 我的提交
### version1
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var findRepeatNumber = function(nums) {
    let hash = {}
    for (let item of nums) {
        hash[item] = (hash[item] || 0 ) + 1
    }
    for (let [key, value] of Object.entries(hash)) {
        if (value > 1) return key
    }
};
```
执行用时：144 ms, 在所有 JavaScript 提交中击败了18.47%的用户
内存消耗：73.2 MB, 在所有 JavaScript 提交中击败了5.04%的用户

### version2
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var findRepeatNumber = function(nums) {
    let hash = {}
    for (let item of nums) {
        hash[item] = (hash[item] || 0 ) + 1
    }
    for (let key in hash ) {
        if (hash.hasOwnProperty(key)) {
            const value = hash[key]
            if (value > 1) return key
        }
    }
};
```
执行用时：112 ms, 在所有 JavaScript 提交中击败了18.78%的用户
内存消耗：60 MB, 在所有 JavaScript 提交中击败了5.04%的用户

### version3
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var findRepeatNumber = function(nums) {
    let hash = {}
    for (let item of nums) {
        if (hash[item] !== undefined) {
            return item
        }
        hash[item] = 1
    }
};
```
执行用时：64 ms, 在所有 JavaScript 提交中击败了90.33%的用户
内存消耗：48.5 MB, 在所有 JavaScript 提交中击败了50.79%的用户

### version 4
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var findRepeatNumber = function(nums) {
    nums = nums.sort();
    for(let i=0; i<nums.length-1; i++) {
        if(nums[i] == nums[i+1]) return nums[i];
    }
};
```
执行用时：60 ms, 在所有 JavaScript 提交中击败了95.81%的用户
内存消耗：47 MB, 在所有 JavaScript 提交中击败了61.63%的用户

## 官方答案
```js
var findRepeatNumber = function(nums) {
    let map = new Map();
    for(let i of nums){
        if(map.has(i)) return i;
        map.set(i, 1);
    }
    return null;
};
```
执行用时：92 ms, 在所有 JavaScript 提交中击败了24.38%的用户
内存消耗：58.7 MB, 在所有 JavaScript 提交中击败了5.04%的用户