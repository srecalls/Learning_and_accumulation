难度：<font color ="lightgreen">简单</font>
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 官网答案
### 1.迭代
#### 思路
![[Pasted image 20230721043300.png]]
#### 代码
```js
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    const prehead = new ListNode(-1) // 哨兵节点
    let prev = prehead
    while(l1 && l2) {
        if (l1.val <= l2.val) {
            prev.next = l1
            l1 = l1.next
        } else {
            prev.next = l2
            l2 = l2.next
        }
        prev = prev.next
    }
    // 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
    prev.next = l1 === null ? l2 : l1
    return prehead.next
};
```
#### 复杂度
![[Pasted image 20230721043413.png]]


### 2.递归
#### 思路
![[Pasted image 20230721043343.png]]
#### 代码
```js
var mergeTwoLists = function(l1, l2) {
    if (l1 === null) {
        return l2;
    } else if (l2 === null) {
        return l1;
    } else if (l1.val < l2.val) {
        l1.next = mergeTwoLists(l1.next, l2);
        return l1;
    } else {
        l2.next = mergeTwoLists(l1, l2.next);
        return l2;
    }
};
```
#### 复杂度
![[Pasted image 20230721043404.png]]

## 步骤图
#### 1.
创建prehead头用于记录头部位置
![[Pasted image 20230721042634.png]]
#### 2.
创建prev指针用于移动连接
![[Pasted image 20230721042644.png]]
#### 3.
l1元素与l2元素进行比较
![[Pasted image 20230721042700.png]]
#### 4.
根据题目选择出较小的元素
![[Pasted image 20230721042710.png]]
#### 5.
让prev指向l1进行连接
![[Pasted image 20230721042721.png]]
#### 6.
链接完毕，l1移动到下一个元素
![[Pasted image 20230721042729.png]]
#### 7.
prev移动到下一个元素用于判断链接
![[Pasted image 20230721042737.png]]
#### 8.
开启下一轮比较
![[Pasted image 20230721042743.png]]
中间步骤省略
#### 9.
最后一个元素进行比较
![[Pasted image 20230721043108.png]]
#### 10.
l1移动到null
![[Pasted image 20230721043129.png]]

#### 11.
prev后移
![[Pasted image 20230721043208.png]]

#### 12.
prev链接到最后一个l2完成链接
![[Pasted image 20230721043241.png]]
