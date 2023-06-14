是的，JavaScript 中有栈（stack）和队列（queue）这两种数据结构。

栈（stack）是一种后进先出（Last-In-First-Out，LIFO）的数据结构，类似于一个弹夹。在 JavaScript 中，可以使用数组来模拟栈的行为。例如，可以使用数组的 push() 方法向栈顶添加元素，使用 pop() 方法从栈顶删除元素。

以下是一个使用数组实现栈的示例代码：

```
const stack = []

stack.push(1) // 添加元素到栈顶
stack.push(2)
stack.push(3)

const top = stack.pop() // 从栈顶删除元素
console.log(top) // 3
```

队列（queue）是一种先进先出（First-In-First-Out，FIFO）的数据结构，类似于排队。在 JavaScript 中，可以使用数组来模拟队列的行为。例如，可以使用数组的 push() 方法向队列尾部添加元素，使用 shift() 方法从队列头部删除元素。

以下是一个使用数组实现队列的示例代码：

```
const queue = []

queue.push(1) // 添加元素到队列尾部
queue.push(2)
queue.push(3)

const head = queue.shift() // 从队列头部删除元素
console.log(head) // 1
```

需要注意的是，JavaScript 中的数组是一种动态的数据结构，可以根据需要动态改变大小。因此，使用数组来实现栈和队列的操作比较方便和高效。