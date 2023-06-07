# [Js(v8)](https://labfiles.acmcoder.com/ojhtml/index.html#/?id=jsv8)

## [语言docker镜像版本](https://labfiles.acmcoder.com/ojhtml/index.html#/?id=%e8%af%ad%e8%a8%80docker%e9%95%9c%e5%83%8f%e7%89%88%e6%9c%ac-12)

```
v8:20170827
```

## [输入API](https://labfiles.acmcoder.com/ojhtml/index.html#/?id=%e8%be%93%e5%85%a5api)

### [读取一行输入](https://labfiles.acmcoder.com/ojhtml/index.html#/?id=%e8%af%bb%e5%8f%96%e4%b8%80%e8%a1%8c%e8%be%93%e5%85%a5)

> read_line()，函数别名： readline()、readLine()

> 将读取至多1024个字符，当还未达到1024个时如果遇到回车或结束符，提前结束。

> 读取多行最简单的办法是while((line = read_line()) != '')。

> 或者使用下一个API。

### [读取n个字符](https://labfiles.acmcoder.com/ojhtml/index.html#/?id=%e8%af%bb%e5%8f%96n%e4%b8%aa%e5%ad%97%e7%ac%a6)

> gets(n)

> 将读取至多n个字符，当还未达到n个时如果遇到回车或结束符，会提前结束。

> 回车符可能会包含在返回值中。

### [读取一个（长）整数](https://labfiles.acmcoder.com/ojhtml/index.html#/?id=%e8%af%bb%e5%8f%96%e4%b8%80%e4%b8%aa%ef%bc%88%e9%95%bf%ef%bc%89%e6%95%b4%e6%95%b0)

> readInt()

### [读取一个浮点型](https://labfiles.acmcoder.com/ojhtml/index.html#/?id=%e8%af%bb%e5%8f%96%e4%b8%80%e4%b8%aa%e6%b5%ae%e7%82%b9%e5%9e%8b)

> readDouble()

## [输出API](https://labfiles.acmcoder.com/ojhtml/index.html#/?id=%e8%be%93%e5%87%baapi)

### [不加回车的输出](https://labfiles.acmcoder.com/ojhtml/index.html#/?id=%e4%b8%8d%e5%8a%a0%e5%9b%9e%e8%bd%a6%e7%9a%84%e8%be%93%e5%87%ba)

> printsth(sth, ...)

> 往控制台输出sth，当有多个参数时，空格分隔；最后不加回车。

### [带回车的输出](https://labfiles.acmcoder.com/ojhtml/index.html#/?id=%e5%b8%a6%e5%9b%9e%e8%bd%a6%e7%9a%84%e8%be%93%e5%87%ba)

> console.log(sth, ...)、print(sth, ...)

> 往控制台输出sth，当有多个参数时，空格分隔；最后加回车。

## [示例代码1](https://labfiles.acmcoder.com/ojhtml/index.html#/?id=%e7%a4%ba%e4%be%8b%e4%bb%a3%e7%a0%811)

```
var a, b;
var solveMeFirst = (a,b) => a+b;
while((a=readInt())!=null && (b=readInt())!=null){
  let c = solveMeFirst(a, b);
  console.log(c);
}
```

## [示例代码2](https://labfiles.acmcoder.com/ojhtml/index.html#/?id=%e7%a4%ba%e4%be%8b%e4%bb%a3%e7%a0%812)

```
var line;
var solveMeFirst = (a,b) => a+b;
while((line = read_line()) != ''){
  let arr = line.split(' ');
  let a = parseInt(arr[0]);
  let b = parseInt(arr[1]);
  let c = solveMeFirst(a, b);
  console.log(c);
}
```