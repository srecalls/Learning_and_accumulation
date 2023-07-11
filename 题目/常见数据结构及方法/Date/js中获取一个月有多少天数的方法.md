## js获取一个月有多少天
### 方法一
new Date()第3个参数默认为1，就是每个月的1号，把它设置为0时， new Date()会返回上一个月的最后一天，然后通过getDate()方法得到天数
```js
function getMonthDay(year, month) {
  let days = new Date(year, month + 1, 0).getDate()
  return days
}
```

### 方法二
可以把每月的天数写在数组中，再判断时闰年还是平年确定2月分的天数
```js
function getDays(year, month) {
   let days = [31,28,31,30,31,30,31,31,30,31,30,31] 
  if ( (year % 4 ===0) && (year % 100 !==0 || year % 400 ===0) ) {
        days[1] = 29
  }
　　return days[month]
}
```


## js快速获取一个月的总天数
在js中通过设置日期对象的月份参数为0,能够返回当前月份总共天数

在计算2月总天数时，不需要判断当前年份是润年还是平年，就能准确的获取2月份的总天数
```js
<script>
    let date = new Date(2020, 2, 0)
    console.log(date.getDate())
</script>
```