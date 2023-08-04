难度：<font color ="lightgreen">简单</font>
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
**示例 1：**

	输入：head = [1,3,2]
	输出：[2,3,1]

**限制：**

`0 <= 链表长度 <= 10000`


## 我的提交
### version1
```js
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {number[]}
 */
var reversePrint = function(head) {
    let prev = null
    let res = []
    while(head) {
        let next = head.next
        head.next = prev
        prev = head
        head = next
    }
    while(prev) {
        res.push(prev.val)
        prev = prev.next
    }
    return res
};
```

时间72ms击败 52.71%使用 JavaScript 的用户

内存41.85mb击败 72.58%使用 JavaScript 的用户

### version2
```js
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {number[]}
 */
var reversePrint = function(head) {
    let res = []
    while(head) {
        res.push(head.val)
        head = head.next
    }
    return res.reverse()
};
```

时间68ms击败 71.86%使用 JavaScript 的用户

内存42.04mb击败 43.37%使用 JavaScript 的用户