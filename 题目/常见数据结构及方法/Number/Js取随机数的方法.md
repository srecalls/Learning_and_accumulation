js 获取随机数方法如下：

1.Math.random()表示 结果为0-1间的一个随机数(包括0,不包括1) ；

　　返回指定范围的随机数(m-n之间)的公式

	　　Math.random()*(n-m)+m;

	　　Math.random()*10+5; //返回5-15之间的随机数

2.Math.ceil(n) 返回大于等于n的整数

	　　用Math.ceil(Math.random()*10);时，主要获取1到10的随机整数，取0的几率极小。

3、Math.round(n); 返回n四舍五入后整数的值。　　

	　　用Math.round(Math.random());可均衡获取0到1的随机整数。  
	　　用Math.round(Math.random()*10);时，可基本均衡获取0到10的随机整数，其中获取最小值0和最大值10的几率少一半。

4、Math.floor(n); 返回小于等于n的最大整数。

	　　用Math.floor(Math.random()*10);时，可均衡获取0到9的随机整数。

5、基于时间，亦可以产生随机数
```js
var now=new Date();
var number = now.getSeconds(); //这将产生一个基于目前时间的0到59的整数。

var now=new Date();
var number = now.getSeconds()%43; //这将产生一个基于目前时间的0到42的整数。
```

参考来源：http://www.studyofnet.com/news/181.html

js 获取随机颜色


```js html css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<style type="text/css">
    #box{width: 100px;height: 100px;margin: 20px auto;background-color: #c66;}
</style>
<body>
    <div id="box" onclick="getColor();">box1</div>
    <script type="text/javascript">
    var x,y,z;
    var oBox=document.getElementById('box');
    function getColor(box){
        x=Math.round(Math.random()*255);
        y=Math.round(Math.random()*255);
        z=Math.round(Math.random()*255);
        oBox.style.backgroundColor='rgb('+x+','+y+','+z+')';
    }
    </script>
</body>
</html>
```