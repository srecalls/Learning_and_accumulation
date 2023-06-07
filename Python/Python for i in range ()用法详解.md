**for i in range ()作用：**

range()是一个函数， for i in range () 就是给i赋值：

比如 for i in range （1，3）：

就是把1,2依次赋值给i

range () 函数的使用是这样的:

range(start, stop[, step])，分别是起始、终止和步长

range（3）即：从0到3，不包含3，即0,1,2  
```PYTHON
for i in range(3):
	print(i)
# 0
# 1
# 2
```



range(1,3) 即：从1到3，不包含3，即1,2
```PYTHON
for i in range(1,3):
	print(i)
	
# 1
# 2

```
range（1,3,2）即：从1到3，每次增加2，因为1+2=3，所以输出只有1

第三个数字2是代表步长。如果不设置，就是默认步长为1

```PYTHON
for i in range(1,3,2):
	print(i)


# 1

```

如果改成range(1,5,2)，就会输出1和3
```PYTHON
for i in range(1,5,2):
 print(i)

 
# 1
# 3

```
For i in range(100)

则读取normMat[i,:]样本的编号为：0-99，共100个