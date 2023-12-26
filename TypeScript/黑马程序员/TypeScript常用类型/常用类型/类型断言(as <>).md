#  类型断言
**作用：当类型太宽泛的时候，使用类型断言指定更加具体的类型**
**例子：getElementByid方法返回值类型是HTMLElement，该类型只包含所有公共的属性或方法，不包含a标签特有的href等属性**

类型断言两种用法
```ts
1. as关键字
const aLink = document.getElementById('link') as HTMLAnchorElement
2. 使用<>语法
const aLink = <HTMLAnchorElement>document.getElementById('id')
```

如何知道某种类型
```ts
console.dir()查看DOM元素，然后查看原型__proto__
```



![[Pasted image 20230327014046.png]]
![[Pasted image 20230327014228.png]]
# 使用类型断言 as <>
![[Pasted image 20230327014338.png]]
![[Pasted image 20230327014841.png]]

如何知道是什么类型的呢
打开浏览器，输入console.dir($0)
$0表示当前选择的元素
然后打开对象翻到最底下
![[Pasted image 20230327014702.png]]
![[Pasted image 20230327014814.png]]