难度：<font color ="lightgreen">简单</font>

**(适用于搭配，而非最佳搭配)**

小扣在秋日市集选择了一家早餐摊位，一维整型数组 `staple` 中记录了每种主食的价格，一维整型数组 `drinks` 中记录了每种饮料的价格。小扣的计划选择一份主食和一款饮料，且花费不超过 `x` 元。请返回小扣共有多少种购买方案。

注意：答案需要以 `1e9 + 7 (1000000007)` 为底取模，如：计算初始结果为：`1000000008`，请返回 `1`

**示例 1：**

	输入：`staple = [10,20,5], drinks = [5,5,2], x = 15`
	输出：`6`

	解释：小扣有 6 种购买方案，所选主食与所选饮料在数组中对应的下标分别是： 第 1 种方案：staple[0] + drinks[0] = 10 + 5 = 15； 第 2 种方案：staple[0] + drinks[1] = 10 + 5 = 15； 第 3 种方案：staple[0] + drinks[2] = 10 + 2 = 12； 第 4 种方案：staple[2] + drinks[0] = 5 + 5 = 10； 第 5 种方案：staple[2] + drinks[1] = 5 + 5 = 10； 第 6 种方案：staple[2] + drinks[2] = 5 + 2 = 7。

**示例 2：**

	输入：`staple = [2,1,1], drinks = [8,9,5,1], x = 9`
	输出：`8`
	解释：小扣有 8 种购买方案，所选主食与所选饮料在数组中对应的下标分别是： 第 1 种方案：staple[0] + drinks[2] = 2 + 5 = 7； 第 2 种方案：staple[0] + drinks[3] = 2 + 1 = 3； 第 3 种方案：staple[1] + drinks[0] = 1 + 8 = 9； 第 4 种方案：staple[1] + drinks[2] = 1 + 5 = 6； 第 5 种方案：staple[1] + drinks[3] = 1 + 1 = 2； 第 6 种方案：staple[2] + drinks[0] = 1 + 8 = 9； 第 7 种方案：staple[2] + drinks[2] = 1 + 5 = 6； 第 8 种方案：staple[2] + drinks[3] = 1 + 1 = 2；

**提示：**

- `1 <= staple.length <= 10^5`
- `1 <= drinks.length <= 10^5`
- `1 <= staple[i],drinks[i] <= 10^5`
- `1 <= x <= 2*10^5`

## 官方答案


解题思路
计数排序可参考文章
根据其他语言的代码，可以看出，此题的价格为整数类型
此题中食物的价格和饮料的价格只有在 x 的范围内符合，所以此题的数据有特定的范围

因此可以使用计数排数的思路进行排序
首先创建长度为 x + 1 的数组，填充 0
然后遍历食物数组 staple ，将**价格转为 arr 数组的 key**，在 **arr 中对应的元素值上 +1 即 arr[staple[i]] ++**
接着**遍历 arr 数组**，让它的**每个元素都等于它前面的元素加上它自身，即 arr[i] += arr[i - 1]**

以上操作的目的是，当我拥有一个饮料的价格，当我需要去**查询符合条件的食物的价格有几种时**，我只需**计算出食物价格的最大值 y = x - drinks[i]** ，然后用 **y 去 arr 中查询，得到的值就是符合条件的食物价格的个数**
然后遍历饮料数组，根据每个饮料的价格，按照以上的查询方式获取**符合条件的食物价格的个数**，并将查询到的个数叠加即可


```js
/**
 * @param {number[]} staple
 * @param {number[]} drinks
 * @param {number} x
 * @return {number}
 */
 // 根据 java 版本代码，可知价格都为整数
 // 用计数排序的思路解此题
var breakfastNumber = function(staple, drinks, x) {
    // 查询数组的长度
    const arrLength = x + 1
    // 查询数组
    const arr = new Array(arrLength).fill(0)
    const stapleLength = staple.length
    const drinksLength = drinks.length
    let result = 0
    // 遍历食物价格，将 x 范围内的食物的价格作为 arr 的下标，然后 arr 中对应的值 +1
    for(let i = 0; i < stapleLength; i ++){
        if(staple[i] <= x){
            arr[staple[i]] ++
        }
    }
    // 将 arr 数组中，当前值都加上前一个元素的值，这样使用任意的 key 查找，都可以查找到前面所有元素值的和
    for(let j = 1; j < arrLength; j ++){
        arr[j] += arr[j - 1]
    }
    // 遍历饮料价格，将 x 减饮料的价格，则得到的就是食物的最大价格
    // 用食物的最大价格去查 arr，可以得到当前饮料能组合的食物的个数
    for(let j = 0; j < drinksLength; j ++){
        if(drinks[j] <= x){
            result += arr[x - drinks[j]]
        }
    }
    return result % 1000000007
};
```

时间108ms击败 100.00%使用 JavaScript 的用户

内存56.90mb击败 100.00%使用 JavaScript 的用户