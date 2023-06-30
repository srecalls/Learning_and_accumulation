JavaScript数组和C数组有以下几点区别：

1. 动态大小：JavaScript数组的大小可以动态增长或缩小，而C数组的大小是固定的，一旦定义后就无法改变。

2. 数据类型：JavaScript数组可以存储不同类型的数据，包括基本类型、对象和函数等，而C数组中只能存储同一种数据类型的元素。

3. 内存管理：JavaScript数组的内存管理是由JavaScript引擎自动处理的，程序员不需要手动分配或释放内存，而C数组需要程序员手动分配和释放内存。

4. 操作方法：JavaScript数组提供了一系列内置的方法，用于在数组中添加、删除或修改元素，例如`push()`、`pop()`、`splice()`等，而C数组没有这些内置方法，程序员需要手动编写代码实现这些操作。

5. 索引方式：JavaScript数组的索引是基于字符串的，即可以使用数字索引，也可以使用字符串索引，例如`arr[0]`和`arr['0']`都可以访问到数组的第一个元素。而C数组的索引是基于数字的，只能使用整数索引来访问数组的元素。

需要注意的是，JavaScript中的数组实际上是一种特殊的对象类型，它通过索引来访问和操作其中的元素。因此，JavaScript数组与C数组在实现方式上有很大的不同。

## 例子
下面是一个使用JavaScript数组和C数组实现相同功能的例子，以便更好地理解它们之间的区别：

JavaScript数组实现：

```javascript
// 创建一个空数组
let arr = [];

// 向数组中添加元素
arr.push(1);
arr.push('hello');
arr.push({name: 'John', age: 30});

// 访问数组中的元素
console.log(arr[0]); // 1
console.log(arr[1]); // 'hello'
console.log(arr[2]); // {name: 'John', age: 30}

// 使用for循环遍历数组
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}
```

C数组实现：

```c
#include <stdio.h>

int main() {
  // 创建一个整型数组
  int arr[3];

  // 向数组中添加元素
  arr[0] = 1;
  arr[1] = 2;
  arr[2] = 3;

  // 访问数组中的元素
  printf("%d\n", arr[0]); // 1
  printf("%d\n", arr[1]); // 2
  printf("%d\n", arr[2]); // 3

  // 使用for循环遍历数组
  for (int i = 0; i < 3; i++) {
    printf("%d\n", arr[i]);
  }

  return 0;
}
```

在上述代码中，我们首先使用JavaScript数组和C数组分别创建了一个空数组和一个整型数组，并向数组中添加了若干个元素。然后，我们使用不同的语法方式来访问数组中的元素，并使用for循环遍历了数组中的所有元素。

需要注意的是，JavaScript数组中的元素可以是任意类型的数据，包括基本类型、对象和函数等，而C数组中的元素必须是同一种数据类型。此外，JavaScript数组的长度可以动态增长或缩小，而C数组的长度是固定的，一旦定义后就无法改变。