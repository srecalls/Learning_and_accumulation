![[Pasted image 20230316212351.png]]

## flex-direction
### 主轴与侧轴
![[Pasted image 20230316212716.png]]

### 属性值
![[Pasted image 20230316212739.png]]
![[Pasted image 20230316212827.png]]

## justify-content 设置主轴上的子元素排列方式
![[Pasted image 20230316213056.png]]

## flex-wrap设置子元素是否换行
![[Pasted image 20230316213447.png]]
![[Pasted image 20230316213509.png]]




## align-content 设置侧轴上的子元素排列方式（多行）
![[Pasted image 20230316214139.png]]

### center
![[Pasted image 20230316214251.png]]

### space-between
![[Pasted image 20230316214354.png]]

### space-around
![[Pasted image 20230316214424.png]]


## align-items设置侧轴上的子元素排列方式（单行）
![[Pasted image 20230316213817.png]]

### 居中
![[Pasted image 20230316213944.png]]a

### 拉伸
![[Pasted image 20230316213839.png]]


## flex-flow
![[Pasted image 20230316215305.png]]
![[Pasted image 20230316215319.png]]


## align-content和align-items区别
![[Pasted image 20230316215126.png]]

- align-items 适用于单行情况下，只有上对齐、下对齐、居中和拉伸
- align-content适应于换行(多行)的情况下( 单行情况下无效)，可以设置上对齐、下对齐、居中、拉伸以及平均分配剩余空间等属性值。
- 总结就是单行找 align-items 多行找 align-content