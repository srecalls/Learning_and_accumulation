在Python中，可以使用列表（List）来实现数组。以下是一些常见的Python数组操作：
### 1. 声明数组：

```python

array = [1, 2, 3, 4, 5]

```

### 2. 访问数组元素：

```python

print(array[0]) # 输出1

print(array[-1]) # 输出5，-1表示倒数第一个元素

```

### 3. 修改数组元素：

```python

array[0] = 0

print(array) # 输出[0, 2, 3, 4, 5]

```

### 4. 数组切片：
左闭右开
```python

print(array[1:3]) # 输出[2, 3]，从下标1开始，到下标3之前（不包括下标3）

print(array[:3]) # 输出[0, 2, 3]，从下标0开始，到下标3之前（不包括下标3）

print(array[3:]) # 输出[4, 5]，从下标3开始，到数组末尾

```

### 5. 数组拼接：

```python

array1 = [1, 2, 3]

array2 = [4, 5, 6]

array3 = array1 + array2

print(array3) # 输出[1, 2, 3, 4, 5, 6]

```

### 6. 数组长度：

```python

print(len(array)) # 输出5

```

### 7. 数组迭代：

```python

for x in array:

print(x)

```

输出结果为：

```

2

3

4

5

```

### 8. 数组排序：

```python

array.sort()

print(array) # 输出[0, 2, 3, 4, 5]

```

### 9. 查找数组元素：

```python

if 3 in array:

print("3 is in the array.")

```

输出结果为：

```

3 is in the array.

```

### 10. 删除数组元素：

```python

del array[0]

print(array) # 输出[2, 3, 4, 5]

```

以上是一些常见的Python数组操作。需要注意的是，列表是可变的，也就是说，可以在程序运行过程中添加、删除或修改元素。这使得列表成为在Python中处理数组的方便工具。