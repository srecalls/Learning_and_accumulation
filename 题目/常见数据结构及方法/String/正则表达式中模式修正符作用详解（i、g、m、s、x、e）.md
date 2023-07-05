正则表达式中常用的模式修正符有i、g、m、s、x、e等。它们之间可以组合搭配使用。

它们的作用如下：

##  修正符: **i** 不区分大小写的匹配;  
  
         //如:"/abc/i"可以与abc或aBC或ABc等匹配;

## 修正符：**g**表示全局匹配

  
    //修正符:m 将字符串视为多行,不管是那行都能匹配;  
  
       例://模式为:$mode="/abc/m";  
         //要匹配的字符串为:$str="bcefg5e\nabcdfe"  
             //注意其中\n,换行了;abc换到了下一行;  
         //$str和$mode仍可以匹配,修正符m使得多行也可匹配;
           
## 修正符:**s** 将字符串视为单行,换行符作为普通字符;  
  
       例://模式为:$mode="/pr.y/";  
           //要匹配字符串为:$str="pr\ny";  
           //两者不可匹配; . 是除了换行以外的字符可匹配;  
           //修改下模式为:$mode="/pr.y/s";  
               //其中修正符s将\n视为普通字符,即不是换行;  
           //最后两者可以匹配;  
## 修正符:**x** 将模式中的空白忽略;  
## 修正符:**A** 强制从目标字符串开头匹配;  
  
         例://$mode="/abc/A";  
           //可以与$str="abcsdfi"匹配,  
           //不可以与$str2="sdsdabc"匹配;  
           //因为$str2不是以abc开头;  
## 修正符:**D** 如果使用$限制结尾字符,则不允许结尾有换行;  
  
         例://模式为:$mode="/abc$/";  
           //可以与最后有换行的$str="adshabc\n"匹配;  
           //元子符$会忽略最后的换行\n;  
           //如果模式为:$mode="/abc/D",  
           //则不能与$str="adshabc\n"匹配,  
           //修正符D限制其不可有换行;必需以abc结尾;  
           
## 修正符:**U** 只匹配最近的一个字符串;不重复匹配;  
  
	 例:  
		 如模式为:  
		$mode="/a.*c/";  
		$str="abcabbbcabbbbbc" ;  
		preg_match($mode,$str,$content);  
		echo $content[0]; //输出:abcabbbcabbbbbc;  

		//如果$mode="/a.*c/";变成$mode="/a.*c/U";  
		 // 则只匹配最近一个字符串,输出:abc;  
  
## 修正符:**e** 配合函数` preg_replace() `使用,  
           可以把匹配来的字符串当作正则表达式执行;

## 例子
### m的作用详解：
示例代码
```js
<html>
<body>
<textarea id="aid" cols="55" rows="10"></textarea> <input type="button" onClick="fun()" value="check" />
<div id="myid">    
</div>
</html> 
<script>
/*
测试数据：
bd76 
dfsdf 
sdfsdfs 
dffs 
b76dsf 
sdfsdf
*/

function fun(){
    var reg = /^b./gm; //匹配到两个结果{bd,b7}
    //var reg = /^b./g;//匹配得到一个结果{bd}
    //var reg = /^b./m;//匹配得到一个结果{bd}
    var str = document.all("aid").value;
    var rs=str.match(reg); 
    for(var i=0; i<rs.length; i++){
        document.all("myid").innerHTML += "第"+i+"个元素："+rs[i] + "<br/>";
    }
}
</script>
```


### 参数g的用法  
  
表达式加上参数g之后，表明可以进行全局匹配，注意这里“可以”的含义。我们详细叙述：  
  
1）对于表达式对象的exec方法，不加入g，则只返回第一个匹配，无论执行多少次均是如此，如果加入g，则第一次执行也返回第一个匹配，再执行返回第二个匹配，依次类推。例如  

	var regx=/user\d/;  
	var str=“user18dsdfuser2dsfsd”;  
	var rs=regx.exec(str);//此时rs的值为{user1}  
	var rs2=regx.exec(str);//此时rs的值依然为{user1}  
	如果regx=/user\d/g；则rs的值为{user1}，rs2的值为{user2}  
	
通过这个例子说明：对于exec方法，表达式加入了g，并不是说执行exec方法就可以返回所有的匹配，而是说加入了g之后，我可以通过某种方式得到所有的匹配，这里的“方式”对于exec而言，就是依次执行这个方法即可。  
  
2）对于表达式对象的test方法，加入g于不加上g没有什么区别。  
  
3）对于String对象的match方法，不加入g，也只是返回第一个匹配，一直执行match方法也总是返回第一个匹配，加入g，则一次返回所有的匹配（注意这与表达式对象的exec方法不同，对于exec而言，表达式即使加上了g，也不会一次返回所有的匹配）。例如：  

	var regx=/user\d/;  
	var str=“user1sdfsffuser2dfsdf”;  
	var rs=str.match(regx);//此时rs的值为{user1}  
	var rs2=str.match(regx);//此时rs的值依然为{user1}  
	如果regx=/user\d/g，则rs的值为{user1,user2}，rs2的值也为{user1,user2}  
	  
4）对于String对象的replace方法，表达式不加入g，则只替换第一个匹配，如果加入g，则替换所有匹配。（开头的三道测试题能很好的说明这一点）  
  
5）对于String对象的split方法，加上g与不加g是一样的，即：  

	var sep=/user\d/;  
	var array=“user1dfsfuser2dfsf”.split(sep);  
	则array的值为{dfsf, dfsf}  
	此时sep=/user\d/g，返回值是一样的。  
  
6）对于String对象的search方法，加不加g也是一样的。



### 附加参数m的用法  
  
附加参数m，表明可以进行多行匹配，但是这个只有当使用^和$模式时才会起作用，在其他的模式中，加不加入m都可以进行多行匹配（其实说多行的字符串也是一个普通字符串），我们举例说明这一点  
  
1）使用^的例子  

	var regx=/^b./g;  
	var str=“bd76 dfsdf  
	sdfsdfs dffs  
	b76dsf sdfsdf”;  
	var rs=str.match(regx);  

此时加入g和不加入g，都只返回第一个匹配{bd}，如果regx=/^b./gm，则返回所有的匹配{bd,b7}，注意如果regx=/^b./m，则也只返回第一个匹配。所以，加入m表明可以进行多行匹配，加入g表明可以进行全局匹配，综合到一起就是可以进行多行全局匹配  
  
2）使用其他模式的例子，例如  

	var regx=/user\d/;  
	var str=“sdfsfsdfsdf  
	sdfsuser3 dffs  
	b76dsf user6”;  
	var rs=str.match(regx);  

此时不加参数g，则返回{user3}，加入参数g返回{user3,user6}，加不加入m对此没有影响。  
  
3）因此对于m我们要清楚它的使用，记住它只对^和$模式起作用，在这两种模式中，m的作用为：如果不加入m，则只能在第一行进行匹配，如果加入m则可以在所有的行进行匹配。我们再看一个^的例子  

	var regx=/^b./;  
	var str=“ret76 dfsdf  
	bjfsdfs dffs  
	b76dsf sdfsdf”;  
	var rs=str.match(regx);
	  
此时rs的值为null，如果加入g，rs的值仍然为null，如果加入m，则rs的值为{bj}（也就是说，在第一行没有找到匹配，因为有参数m，所以可以继续去下面的行去找是否有匹配），如果m和g都加上，则返回{bj,b7}（只加m不加g说明，可以去多行进行匹配，但是找到一个匹配后就返回，加入g表明将多行中所有的匹配返回，当然对于match方法是如此，对于exec呢，则需要执行多次才能依次返回）  
  
总结3：在HTML的textarea输入域中，按一个Enter键，对应的控制字符为“\r\n”，即“回车换行”，而不是“\n\r”，即“换行回车”，我们看一个前面我们举过的例子： 

	var regx=/a\r\nbc/;  
	var str=“a  
	bc”;  
	var rs=regx.exec(str);  

结果：匹配成功，rs的值为：{ }，如果表达式为/a\n\rbc/，则不会被匹配，因此在一般的编辑器中一个”Enter”键代表着“回车换行”，而非“换行回车”，至少在textarea域中是这样的。