## 1.如果想要获取整个网页文档中h1标签的个数，可以通过（）

- [ ] A. var hele=document.getElementByTagName('h1');  alert(hele.length);
- [x] B. var hele=document.getElementsByTagName('h1');  alert(hele.length);
- [ ] C. var hele=getElementsByTagName('h1');  alert(hele.length);
- [ ] D. var hele=getElementByTagName('h1');  alert(hele.length);

官方解析：如果想要获取整个文档中h1标签的个数，可以使用 **document.getElementsByTagName('h1')** ，
B选项正确，A选项错误；
注意 **getElementsByTagName()** 是**DOM节点**的方法，如**若获取的是整个文档的h1标签**，需要使用document节点，CD选项均错误。


没有getElementByTagName，只有getElementsByTagName
有getElement ById


## 4.下面结果为真的表达式是：（）

- [ ] A.null instanceof Object
- [ ] B.null === undefined
- [x] C.null == undefined
- [ ] D.NaN == NaN


参考答案：答案是C。  null和undefined是不同的，但它们都表示“值的空缺”，判断相等运算符“\==”认为两者是相等的（要使用严格相等运算符“\=\==”来区分它们）。

1.instanceof运算符希望左操作数是一个对象，右操作数表示对象的类（初始化对象的构造函数）。如果左侧的对象是右侧对象的实例，返回true，否则返回false。

例如：计算o instanceof f  
首先计算f.prototype，然后在原型链中查找o，找到返回true
2.\=\==严格相等运算符：首先计算其操作数的值，然后比较这两个值，比较过程中没有任何类型转换

3.\==相等运算符：如果两个操作数不是同一类型，那么会尝试进行一些类型转换，然后进行比较

（1）尽管null和undefined是不同的，但它们都表示“值的空缺”，两者往往可以互换，因此\==运算符认为两者是相等的
（2）NaN表示非数字值，特殊之处：它和任何值都不相等，包括自身。判断NaN的方法：x!=x返回true
[[6.instanceof 操作符的实现原理及实现]]


## 5.执行以下程序，输出结果为（）
```js
function Father(age){
    this.age = age
}
function Son(age){
    Father.call(this);
}
Son.prototype = Father.prototype;
Father.prototype.getAge = function(){console.log(40);}
Son.prototype.getAge = function(){console.log(18);}
var father = new Father(40);
var son = new Son(18);
son.getAge();
father.getAge();
```


- [x] A.18 18
- [ ] B.40 40
- [ ] C.18 40
- [ ] D.18 undefined

官方解析：

本题属于ES5继承中的共享原型，由于Son和Father的原型对象指向同一对象，这样就导致了不管是修改Father原型对象还是Son原型对象的属性或方法，另一个的原型对象也会跟着修改。由于getAge()方法均定义在原型对象，后定义的getAge()方法会覆盖先定义的getAge()，所以最终输出结果均是18，A选项正确。

```js
function Father(age) { //此时Father.prototype = { constructor： function Father(){}}
    this.age = age
}
function Son(age) { //此时Son.prototype = { constructor： function Son(){}}
    Father.call(this);
}

Son.prototype = Father.prototype;
//此时Son.prototype = { constructor： function Father(){}}   
//此时Father.prototype = { constructor： function Father(){}}
//现在，Son和Father的prototype指向同一个对象，也就是指向堆里的同一个地址


Father.prototype.getAge = function () { console.log(40) },//堆里加一个getAge属性
//此时：
// Father.prototype = {
//     constructor： function Father(){}
//     getAge: function(){console.log(40);}
// }
//特别注意，因为Son和Father的prototype指向同一个对象（堆里同一个地址），所以
// Son.prototype = {
//     constructor： function Father(){}
//     getAge: function(){console.log(40);}
// }

Son.prototype.getAge = function () { console.log(18) };
//此时：
// Son.prototype = {
//     constructor： function Father(){}
//     getAge: function(){console.log(18);}
// }
//因为Son和Father的prototype指向同一个对象（堆里同一个地址），所以
// Father.prototype = {
//     constructor： function Father(){}
//     getAge: function(){console.log(18);}
// }


var father = new Father(40); // father = { age: 40 } 
var son = new Son(18); //如果构造函数Son里没有Father.call(this);  那么此时 son = {}
//但是，构造函数Son里有Father.call(this);  然后 son = { age: undefined } (暂时不太明白这是为什么)

//以上结束后father = { age: 40 } 
//以上结束后son = { age: undefined } 


father.getAge(); //father里只有一个age,没有getAge方法，去原型Father.prototype里找， 执行函数console.log(18)
son.getAge();//son里只有一个age,没有getAge方法，去原型Son.prototype里找， 执行函数console.log(18)

//本题跟传入的age没有关系，因为getAge方法里没有任何对age的处理，只是执行一个console.log()
```

  

如果把题目改成如下形式，就必须知道Father.call(this);的作用才能答对了

![[Python/网络安全/photo/JavaScript题目.png]]


## 2.以下哪个选项的描述是错误的
- [ ] A. iframe是用来在网页中插入第三方页面，早期的页面使用iframe主要是用于导航栏这种很多页面都相同的部分，这样在切换页面的时候避免重复下载
- [ ] B. iframe的创建比一般的DOM元素慢了1-2个数量级
- [ ] C. iframe标签会阻塞页面的的加载
- [x] D. iframe本质是动态语言的Incude机制和利用ajax动态填充内容


ifreme本身不是动态语言，样式和js需要额外导入。其加载完成之后才会加载window的onload事件

### 1、创建比一般的 DOM 元素慢了 1-2 个数量级

iframe 的创建比其它包括 scripts 和 css 的 DOM 元素的创建慢了 1-2 个数量级，使用 iframe 的页面一般不会包含太多 iframe，所以创建 DOM 节点所花费的时间不会占很大的比重。但带来一些其它的问题：onload 事件以及连接池（connection pool）

### 2、阻塞页面加载

及时触发 window 的 onload 事件是非常重要的。onload 事件触发使浏览器的 “忙” 指示器停止，告诉用户当前网页已经加载完毕。当 onload 事件加载延迟后，它给用户的感觉就是这个网页非常慢。

window 的 onload 事件需要在所有 iframe 加载完毕后（包含里面的元素）才会触发。在 Safari 和 Chrome 里，通过 JavaScript 动态设置 iframe 的 SRC 可以避免这种阻塞情况

### 3、唯一的连接池

浏览器只能开少量的连接到 web 服务器。比较老的浏览器，包含 Internet Explorer 6 & 7 和 Firefox 2，只能对一个域名（hostname）同时打开两个连接。这个数量的限制在新版本的浏览器中有所提高。Safari 3+ 和 Opera 9+ 可同时对一个域名打开 4 个连接，Chrome 1+, IE 8 以及 Firefox 3 可以同时打开 6 个

绝大部分浏览器，主页面和其中的 iframe 是共享这些连接的。这意味着 iframe 在加载资源时可能用光了所有的可用连接，从而阻塞了主页面资源的加载。如果 iframe 中的内容比主页面的内容更重要，这当然是很好的。但通常情况下，iframe 里的内容是没有主页面的内容重要的。这时 iframe 中用光了可用的连接就是不值得的了。一种解决办法是，在主页面上重要的元素加载完毕后，再动态设置 iframe 的 SRC。

### 4、不利于 SEO

搜索引擎的检索程序无法解读 iframe。另外，iframe 本身不是动态语言，样式和脚本都需要额外导入。综上，iframe 应谨慎使用。

### iframe用法
`<iframe>` 是 HTML 中的一个标签，用于在当前网页中嵌入另一个网页或文档。可以将 `<iframe>` 看作是一个窗口，它显示了另一个网页或文档。以下是一些 `<iframe>` 的用法：

1. 嵌入另一个网页

```html
<iframe src="http://www.example.com"></iframe>
```

上述代码将在当前网页中嵌入 `http://www.example.com` 网页。可以使用 `src` 属性指定要嵌入的网页的 URL。

2. 嵌入一个 HTML 文档

```html
<iframe srcdoc="<html><body><h1>Hello, World!</h1></body></html>"></iframe>
```

上述代码将在当前网页中嵌入一个包含 `<h1>Hello, World!</h1>` 的 HTML 文档。可以使用 `srcdoc` 属性指定要嵌入的 HTML 文档。请注意，`srcdoc` 属性仅在支持的浏览器中可用。

3. 指定 `<iframe>` 的大小

```html
<iframe src="http://www.example.com" width="500" height="300"></iframe>
```

上述代码将在当前网页中嵌入 `http://www.example.com` 网页，并将 `<iframe>` 的宽度设置为 500 像素，高度设置为 300 像素。可以使用 `width` 和 `height` 属性指定 `<iframe>` 的大小。

4. 指定 `<iframe>` 的样式和类名

```html
<iframe src="http://www.example.com" style="border: 1px solid black;" class="my-iframe"></iframe>
```

上述代码将在当前网页中嵌入 `http://www.example.com` 网页，并将 `<iframe>` 的边框样式设置为 1 像素的黑色实线，并将 `<iframe>` 的类名设置为 `my-iframe`。可以使用 `style` 和 `class` 属性指定 `<iframe>` 的样式和类名。

5. 嵌入一个 PDF 文件

```html
<iframe src="example.pdf" width="500" height="300"></iframe>
```

上述代码将在当前网页中嵌入 `example.pdf` 文件，并将 `<iframe>` 的宽度设置为 500 像素，高度设置为 300 像素。可以使用 `src` 属性指定要嵌入的 PDF 文件的 URL。请注意，浏览器必须支持 PDF 文件的嵌入才能正确显示文件内容。

总之，`<iframe>` 标签可用于在当前网页中嵌入另一个网页、文档或 PDF 文件等内容，并可以通过属性指定其大小、样式和类名等。


## 4.以下哪个语句打印出来的结果是false？

- [x] A.alert(3\==true)
- [ ] B.alert(2\=="2")
- [ ] C.alert(null == undefined)
- [ ] D.alert(isNaN("true"))

A、
1 == true   // 布尔值会转成number true即为1 所以结果是true
2 == true   // 布尔值会转成number true即为1 所以结果是false  
3 == true   // 布尔值会转成number true即为1 所以结果是false  
1 == false  // 布尔值会转成number false即为0 所以结果是false  
0 == false  // 布尔值会转成number false即为0 所以结果是true

B、数字字符串2会转换成数字2在和数字2进行比较 。  
== js会优先选择将字符串转成数字==  

C、Javascript规范中提到， 要比较相等性之前，不能将null和undefined转换成其他任何值，并且规定null和undefined是相等的。
null和undefined都代表着无效的值。

D、
isNaN() 函数用于检查其参数是否是非数字值。
如果参数值为 NaN 或字符串、对象、undefined等非数字值则返回 true, 否则返回 false。

![[Python/网络安全/photo/JavaScript题目-1.png]]


## 3.执行以下程序，要求当用户点击按钮1秒后禁用按钮，以下选项的做法，不符合要求的是（）

```html
<button>点击</button>
<script>

    var btn = document.querySelector('button');

</script>
```

- [ ] A
```js
btn.onclick = function(){
	var that = this;
	setTimeout(function(){
		that.disabled = true;
	},1000)
}
```

- [x] B
```js
btn.onclick = function(){
	setTimeout(function(){
		this.disabled = true;
	},1000)
}
```

- [ ] C
```js
btn.onclick = function(){
	setTimeout(()=>{
		this.disabled = true;
	},1000)
}
```

- [ ] D.
```js
btn.onclick = function(){
	setTimeout(function(){
		this.disabled = true;
	}.bind(this),1000)
}
```

官方解析：B选项，在定时器中，this指向window对象，而不是btn对象。而在定时器的同级作用域，this指代btn对象，ACD选项均是在定时器函数中使用该btn对象。


## 2.与其他 IEEE 754 表示浮点数的编程语言一样，JavaScript 的 number 存在精度问题，比如 0.2 + 0.4 的结果是 0.6000000000000001。以下选项中，能得到 0.6 的是？

- [ ] A.parseFloat(0.2 + 0.4)
- [ ] B.parseFloat((0.2 + 0.4).toFixed(1))
- [ ] C.Math.round(0.2 + 0.4)
- [ ] D.parseFloat((0.2 + 0.6).toPrecision(1))

- parseFloat 解析一个字符串，并返回一个浮点数
- toFixed 把数字转换为字符串，结果的小数点后有指定位数的数字
- Math.round 把一个数字舍入为最接近的整数
- toPrecision 把数字格式化为指定的长度
  
![[Python/网络安全/photo/JavaScript题目-2.png]]


## 3.以下代码执行后， num 的值是？
```js
var foo=function(x,y){
    return x-y;
}
function foo(x,y){
    return x+y;
}
var num=foo(1,2);
```

- [x] A.-1
- [ ] B.3
- [ ] C.1
- [ ] D.2

**引出重要知识点**

函数提升优先级高于变量提升，且不会被变量声明覆盖，但会被变量赋值覆盖

```js
function foo(x,y){return x+y;}//函数声明优先于变量提升
var foo;
foo=function(x,y){return x-y;}//变量赋值覆盖了函数声明
var num=foo(1,2);
```


在 JavaScript 中，函数声明的优先级比变量声明的优先级高，这被称为函数提升（Function Hoisting）。

这意味着，在函数声明之前就可以调用该函数，因为函数声明会被提升到当前作用域的顶部。例如：

```javascript
foo(); // 调用函数 foo，不会报错

function foo() {
  console.log("Hello, world!");
}
```

上述代码中，函数 `foo()` 被声明在调用它之前，但是调用 `foo()` 不会报错，因为函数声明被提升到了作用域的顶部。

相比之下，变量声明会被提升，但是变量的赋值不会被提升。例如：

```javascript
console.log(x); // 输出 undefined
var x = 10;
```

上述代码中，变量 `x` 被声明在调用 `console.log(x)` 之前，但是输出结果为 `undefined`，因为变量赋值不会被提升，只有变量声明会被提升。

需要注意的是，函数表达式不会被提升，只有函数声明会被提升。例如：

```javascript
foo(); // 报错，foo is not a function

var foo = function() {
  console.log("Hello, world!");
};
```

上述代码中，变量 `foo` 被提升了，但是它是一个函数表达式，不是函数声明，因此在调用 `foo()` 时会报错。

总之，在 JavaScript 中，函数声明的优先级比变量声明的优先级高，函数声明会被提升到当前作用域的顶部，而变量声明也会被提升，但是变量赋值不会被提升，函数表达式不会被提升。


## 4.下面有关JavaScript内部对象的描述，正确的有？

- [x] A.History 对象包含用户（在浏览器窗口中）访问过的 URL
- [x] B.Location 对象包含有关当前 URL 的信息
- [x] C.Window 对象表示浏览器中打开的窗口
- [x] D.Navigator 对象包含有关浏览器的信息

答案：abcd 
Navagator：提供**有关浏览器的信息**
Window：Window对象处于对象层次的**最顶层**，它提供了处理Navagator窗口的方法和属性 
Location：提供了与**当前打开的URL一起工作的方法和属性**，是一个静态的对象 
History：提供了与**历史清单**有关的信息 
Document：包含与文档元素一起工作的对象，它将这些元素封装起来供编程人员使用


## 5.以下哪些事件会在页面加载完成（onload）之前触发？

- [x]  A.readystatechange
- [ ]  B.pageshow
- [ ]  C.beforeunload
- [x]  D.DOMContentLoaded



onload页面加载完成时触发，onpageshow页面显示时触发，onbeforeunload页面跳转前触发。

1. A. readystatechange document有readyState属性来描述document的loading状态，readyState的改变会触发readystatechange事件.
    - loading 文档仍然在加载
    - interactive 文档结束加载并且被解析，但是像图片，样式，frame之类的子资源仍在加载
    - complete 文档和子资源已经结束加载，该状态表明将要触发load事件。

因此readystatechange在onload之前触发。

1. B.onpageshow onpageshow 事件在用户浏览网页时触发。 onpageshow 事件类似于 onload 事件，onload 事件在页面第一次加载时触发， onpageshow 事件在每次加载页面时触发，即 onload 事件在页面从浏览器缓存中读取时不触发。
    
2. C. beforeunload 当浏览器窗口，文档或其资源将要卸载时，会触发beforeunload事件。这个文档是依然可见的，并且这个事件在这一刻是可以取消的. 如果处理函数为Event对象的returnValue属性赋值非空字符串，浏览器会弹出一个对话框，来询问用户是否确定要离开当前页面（如下示例）。有些浏览器会将返回的字符串展示在弹框里，但有些其他浏览器只展示它们自定义的信息。没有赋值时，该事件不做任何响应。
    
3. D.DOMContentLoaded 当初始的 HTML 文档被完全加载和解析完成之后，DOMContentLoaded 事件被触发，而无需等待样式表、图像和子框架的完成加载。 另一个不同的事件 load 应该仅用于**检测一个完全加载的页面**。因此DOMContentLoaded是HTML完全加载和解析完成之后发生的，发生时间点要早于load，选D。 在使用 DOMContentLoaded 更加合适的情况下使用 load 是一个令人难以置信的流行的错误，所以要谨慎。 注意：DOMContentLoaded 事件必须等待其所属script之前的样式表加载解析完成才会触发。
    
## 2.在标准的 JavaScript 中， Ajax 异步执行调用基于下面哪一个机制才能实现？
- [ ] A.Event和callback
- [ ] B.多线程操作
- [ ] C.多CPU核
- [ ] D.Deferral和promise

**JavaScript**是**单线程**的，**浏览器**实现了**异步**的操作，整个js程序是**事件驱动**的，每个事件都会绑定相应的**回调函数，**

## 3.问以下JS代码输出的结果是什么？
```Js
let obj = {
  num1: 117
}
let res = obj;
obj.child = obj = { num2: 935 };
var x = y = res.child.num2;
console.log(obj.child);
console.log(res.num1);
console.log(y);
```

- [ ] A.117、117、undefined
- [ ] B.117、117、935
- [x] C.undefined、117、935
- [ ] D.undefined、117、undefined

```Js
let obj = {
  num1: 117
}
let res = obj;
obj.child = obj = { num2: 935 };
console.log(obj)
console.log(obj.child)
console.log(res)
var x = y = res.child.num2;
console.log(obj.child);
console.log(res.num1);
console.log(y);
```

![[Python/网络安全/photo/JavaScript题目-3.png]]

官方解析：

在对obj赋值的那一行语句可以看到应该拆分成两个表达式，前者的含义是计算obj.child，并暂存了当前的obj，之后才被赋值。而后者是改变了obj的指向覆盖了原本的变量obj，它的值是{num2：935}，所以找不到child这个属性故为undefined。这里的res代表的就是原本的变量obj，因此可以访问到num1和child。至于y在这里是会被认为是全局变量。


let obj = { num1: 117 } 

>     把obj放在栈里，把 { num1:117} 放在堆里，让obj指向堆里的 { num1:117 }     

    let res = obj;

> 把res放在栈里，把res也指向堆里的 { num1:117 }     

![[Python/网络安全/photo/JavaScript题目-4.png]]
    obj.child  =  obj  =  { num2: 935 };
重点：赋值操作先定义变量(从左到右)，再进行赋值（从右到左）        
定义变量    obj.child，给堆里的{ num1:117 }加一个child属性，得{num1:117，child:undefined}      
定义变量    obj,之前在栈里的obj  

![[Python/网络安全/photo/JavaScript题目-5.png]]

赋值    obj = { num2: 935 }，把{ num2: 935 }放在堆里，把栈里的obj指向堆里的{ num2: 935 }   


![[Python/网络安全/photo/JavaScript题目-6.png]]  



赋值    obj.child = obj，把堆里的 {num1:117，child:undefined} 的child指向  {num2: 935}       

![[Python/网络安全/photo/JavaScript题目-7.png]]         


从最后一张图可看出此时：     
> 
>         obj = { num2: 935 }     
> 
>         res = { num1: 117，child：{ num2: 935 }  }


## 4.执行完如下程序后，所有能被访问到的变量包括（）

```js
var a = 1;
b = 2;
eval('var c = 3');
delete a;
delete b;
delete c;
```

- [ ] A.a、b、c
- [ ] B.a、c
- [x] C.a
- [ ] D.c

官方解析：

在eval中使用var声明的全局变量可以被delete删除，所以变量c能删除成功，除此之外，在其他情况下，使用var声明的全局变量或者局部变量一般是不能被delete删除的，所以变量a无法被删除，仍然可以访问到，而未使用var声明的全局变量可以使用delete进行删除，所以无法访问到b。综上，只有变量a未被成功删除，可以访问得到，故正确答案为C选项。



 **delete()** delete 操作符用于删除对象的某个属性  
 var, let以及const创建的不可设置的属性不能被delete操作删除  
 **不可配置属性configurable**  
 当且仅当该属性的 configurable 为 true 时，该属性描述符才能够被改变，同时该属性也能从对应的对象上被删除。默认值为true

- ES6以后除了全局对象以外还维护了一个变量名列表，专门用来存储var,let,const声明的变量,并且约定了该列表里面的变量不能被delete删除，所以a变量无法被删除。
- 尽管var a =1;b =2 都是全局变量，都可以通过全局对象访问到。但b不是var声明的，可被delete删除,因此访问不了
- eval中声明var变量是唯一一个被添加到变量名列表同时也可以被delete删除的特例，所以删除变量c有效。

## 1.如果不给cookie设置过期时间会怎么样？
- [ ] A.立刻过期
- [ ] B.永不过期
- [ ] C.cookie 无法设置
- [x] D.在浏览器会话结束时过期

cookie的有效时间默认为-1，如果不进行设置的话，就会默认在浏览器会话关闭时结束。
可以通过setMaxAge()方法设置cookie的生命期。
立刻删除该浏览器上指定的cookie

## 2.执行下列程序，输出结果为（）
```js
var a = 1;
function fn(){
    var a = 2;
    function a(){console.log(3);}
    return a;
    function a(){console.log(4);}
}
var b = fn();
console.log(b);
```

- [ ] A.1
- [x] B.2
- [ ] C.f a(){console.log(3);}
- [ ] D.f a(){console.log(4);}

官方解析：

输出的b值为函数fn内的变量a，在函数fn内部，由于存在变量提升和函数提升，且函数提升会在变量提升之前，因此变量a会先被赋值为函数f a(){console.log(3);}，之后被重新赋值为函数f a(){console.log(4);}，最后被赋值为2，所以b值为2，B选项正确。


## 4.执行以下代码，输出结果为（）
```js
function test(a){
    a=a+10;
}
var a=10;
test(a);
console.log(a);
```

- [x] A.10
- [ ] B.20
- [ ] C.抛出异常
- [ ] D.undefined

官方解析：变量a为number类型，属于基本数据类型，基本数据类型在传参时，通过拷贝值进行传递。因此，在函数内部修改形参时，不会对实参产生影响，故输出a的值为10，A选项正确。


## 5.对于代码 var a = 10.42; 取出 a 的整数部分，以下代码哪些是正确的？

- [x] A.parseInt(a);
- [x] B.Math.floor(a);
- [ ] C.Math.ceil(a);
- [ ] D.a.split('.')[0];

A. parseInt转换为整数，默认为10进制，结果为10
B. floor向下取整，结果为10 
C. ceil向上取整，结果为11
D. split操作数必需为正则或字符串，结果为TypeError

  
  
## 5.以下关于Histroy对象的属性或方法描述正确的是（）

- [x] A.back回到浏览器载入历史URL地址列表的当前URL的前一个URL
- [ ] B.go表示刷新当前页面
- [ ] C.length保存历史URL地址列表的长度信息
- [x] D.forward转到浏览器载入历史URL地址列表的当前URL的下一个URL。


- length 返回浏览器历史列表中的URL数量。**所以C中表述的长度信息是错误的。**
- back() 加载 history列表中的**前一个URL**。
- forward() 加载  history  列表中的**下一个URL**。
- go()  加载history列表中的**某个具体页面**。**所以B的表述刷新当前页面是错误的。**
![[Python/网络安全/photo/JavaScript题目-8.png]]

  
## 1.下面有关 JavaScript 常见事件的触发情况，描述错误的是？
- [ ] A.onmousedown：某个鼠标按键被按下
- [ ] B.onkeypress：某个键盘的键被按下或按住
- [x] C.onblur：元素获得焦点
- [ ] D.onchange：用户改变域的内容

### 鼠标事件
![[React/Photo/JavaScript题目.png]]

onmousemove、onmouseover、onmouseout、onmouseenter、onmouseleave都是JavaScript中的事件，它们都与鼠标的移动和位置有关，但它们之间有一些区别。

1. onmousemove事件在鼠标在元素上移动时触发，无论鼠标是否进入或离开元素。
2. onmouseover事件在鼠标进入元素时触发。
3. onmouseout事件在鼠标离开元素时触发。
4. onmouseenter事件在鼠标进入元素时触发，与onmouseover事件类似，但不会冒泡。
5. onmouseleave事件在鼠标离开元素时触发，与onmouseout事件类似，但不会冒泡。

因此，onmouseenter和onmouseleave与onmouseover和onmouseout的区别主要在于它们是否冒泡。当鼠标进入或离开元素时，onmouseenter和onmouseleave事件不会冒泡到父元素或其他元素，而onmouseover和onmouseout事件会冒泡到父元素或其他元素。

### 键盘事件
![[React/Photo/JavaScript题目-2.png]]


### 焦点事件
![[React/Photo/JavaScript题目-3.png]]


### 触摸事件
![[React/Photo/JavaScript题目-4.png]]

### 滚轮事件
![[React/Photo/JavaScript题目-5.png]]

### 提交事件
![[React/Photo/JavaScript题目-6.png]]

### 更改表单元素Select触发事件
![[React/Photo/JavaScript题目-7.png]]



## 2.以下哪一项不属于浏览器Response Headers字段：

- [x] A.Referer
- [ ] B.Connection
- [ ] C.Content-Type
- [ ] D.Server

答案：a 

  解析：
  说一说常见的请求头和相应头都有什么呢？ 

###   1)请求(客户端->服务端`[request]`)
  

      GET(请求的方式)
    /newcoder/hello.html(请求的目标资源) HTTP/1.1(请求采用的协议和版本号)
      Accept: */*(客户端能接收的资源类型)
      Accept-Language: en-us(客户端接收的语言类型)
      Connection: Keep-Alive(维护客户端和服务端的连接关系)
      Host: localhost:8080(连接的目标主机和端口号)
      Referer: http://localhost/links.asp(告诉服务器我来自于哪里)
      User-Agent: Mozilla/4.0(客户端版本号的名字)
      Accept-Encoding: gzip, deflate(客户端能接收的压缩数据的类型)
      If-Modified-Since: Tue, 11 Jul 2000 18:23:51 GMT(缓存时间) 
      Cookie(客户端暂存服务端的信息)
       Date: Tue, 11 Jul 2000 18:23:51 GMT(客户端请求服务端的时间)  

  
   ### 2)响应(服务端->客户端`[response]`)

	HTTP/1.1(响应采用的协议和版本号) 200(状态码) OK(描述信息)
	Location:http://www.baidu.com(服务端需要客户端访问的页面路径) 
	Server:apache
	tomcat(服务端的Web服务端名)
	Content-Encoding:
	gzip(服务端能够发送压缩编码类型) 
	Content-Length: 80(服务端发送的压缩数据的长度) 
	Content-Language: zh-cn(服务端发送的语言类型) 
	Content-Type: text/html; charset=GB2312(服务端发送的类型及采用的编码方式)
	Last-Modified:Tue, 11 Jul 2000 18:23:51 GMT(服务端对该资源最后修改的时间)
	Refresh: url=http://www.it315.org(服务端要求客户端1秒钟后，刷新，然后访问指定的页面路径)
	Content-Disposition: attachment;
	filename=aaa.zip(服务端要求客户端以下载文件的方式打开该文件)
	Transfer-Encoding:
	chunked(分块传递数据到客户端）  
	Set-Cookie:SS=Q0=5Lb_nQ;
	path=/search(服务端发送到客户端的暂存数据)
	Expires:-1//3种(服务端禁止客户端缓存页面数据)
	Cache-Control:
	no-***(服务端禁止客户端缓存页面数据)  
	Pragma: no-***(服务端禁止客户端缓存页面数据) 
	Connection: close(1.0)/(1.1)Keep-Alive(维护客户端和服务端的连接关系)  
	Date: Tue, 11 Jul 2000 18:23:51 GMT(服务端响应客户端的时间)   

    在服务器响应客户端的时候，带上Access-Control-Allow-Origin头信息，解决跨域的一种方法。

## 3.执行以下程序，下列选项中，说法错误的是（）
```js
class Phone{
  constructor(brand){
    this.brand = brand;
}
  call(){}...①
}
function playGame(){console.log("我可以打游戏")};
function photo(){console.log("我可以拍照")};
console.log(typeof Phone);...②
var p = new Phone('华为');
console.log(p.brand);...③
```

- [ ] A.①式的call方法是定义在类Phone的prototype对象上
- [x] B.②式输出结果为Object
- [ ] C.③式输出结果为华为
- [ ] D.若想一次性给类添加playGame和photo两个实例方法，可以使用Object.assign(Phone.prototype,{playGame,photo})

官方解析：

**类的所有实例方法均定义在类的原型对象**上，因此，在**类内定义的实例方法和在类的原型对象上定义方法是等价的**，call()是实例方法，故A选项说法正确，不符合题意；类的本质是函数，实际上，**ES6中的类可以视为ES5中构造函数的另一种写法**，所以②式的输出结果为function而不是Object，B选项说法错误，符合题意；p为类的实例对象，该对象有一个属性brand，属性值为华为，C选项说法正确，不符合题意；Object.assign(target, source)可将source源对象所有可枚举的属性（或方法）分配给target对象，所以可以使用Object.assign(Phone.prototype,{playGame,photo})为类一次性添加playGame和photo两个实例方法，D选项说法正确，不符合题意。


## 5.如何阻止IE和各大浏览器默认行为（      ）
- [ ] A.window.event.cancelBubble = true;
- [x] B.window.event.returnValue = false;
- [ ] C.event.stopPropagation();
- [x] D.event.preventDefault();

阻止默认事件：
e.preventDefault()
e.returnValue = false  (IE)

阻止冒泡：
e.stopPropagation()
e.cancelBubble = true (IE)



## 5.NOSCRIPT标签是做什么用的？

- [ ] A.制止脚本的运行
- [ ] B.防止区域脚本被js修改<br>(例如aDiv.innerHTML = 'something' 将会不起作用)
- [x] C.用来定义在脚本未被执行时的替代内容
- [ ] D.NOSCRIPT 标签并不存在

```Js
noscript 元素用来定义在脚本未被执行时的替代内容（文本）。  

<body>  
...
  ...

  <script type="text/javascript">
    <!--
    document.write("Hello World!")
    //-->
  </script><noscript>Your browser does not support JavaScript!</noscript>...
  ...
</body> 
```


定义：NOSCRIPT标签用来定义在脚本未被执行时的替代内容。

作用：**可以用在检测浏览器是否支持脚本，若不支持脚本则可以显示NOSCRIPT标签里的innerText**

noscript元素的内容得以显示的两种情况：

**1.浏览器不支持脚本  
2.浏览器支持脚本，但脚本被禁用**  


## 3.请问以下JS代码的输出结果会是什么
```js
var a = 'w' 
let obj = {
  a: 'o',
  print: function() {
    console.log(this.a)
  },
  print2: () => {
    console.log(this.a)
  }
}
let p = obj.print
let p2 = obj.print2
obj.print()
obj.print2()
p()
p2()
```
- [ ] A.o、 undefined、 undefined、undefined
- [ ] B.o、 w、 undefined、 undefined
- [ ] C.o、 w、 w、 undefined
- [x] D.o、 w、 w、 w

第一个函数执行时this是执行obj所以值为obj里面a变量的值即o，其余函数的this都指向了window，由于变量a是用var声明的，所以window下面有这个变量，那么就输出了w。

## 4.请问以下JS代码的输出顺序是？
```js
let date = new Date()
setTimeout(() => {
    console.log('1')
}, 2000)
setTimeout('console.log(2)',1000);
setTimeout(function() {
  console.log('3')
}, 1500);
while((new Date() - date) < 3000) {}
```
- [ ] A. 报错
- [x] B. 3秒以后同时输出2 3 1
- [ ] C. 1秒后输出2，1.5秒后输出3，2秒后输出1
- [ ] D. 4秒后输出2，4.5秒后输出3，5秒后输出1
官方解析：

需要明确一点的是setTimeout可以将字符串当成代码执行，类比eval函数。前3秒后在执行while函数，setTimeout函数虽然在各自对应时间后插入了队列，但是由于属于宏任务所以暂时还没有执行，直到while微任务完成，才按顺序输出。

## 5.下面关注this对象的理解正确的是 ()
- [x] A.非箭头函数，在不改变this指向的前提下，this总是指向函数的直接调用者
- [x] B.如果有new关键字，this指向new出来的那个对象
- [ ] C.this总是指向函数的非间接调用者
- [x] D.IE中attachEvent中的this总是指向全局对象Window

1、**在不改变this指向的前提下**，this总是指向函数的直接调用者。（对）

2、非间接调用者就是直接调用者，但是说：this总是指向函数的直接调用者就是错的，**因为要有前提this的指向不能改变**

例如：    fn.call(obj)   fn是非间接调用者即直接调用者，但是this指向的是obj

## 1.执行以下程序，下列说法中，正确的是（）
```js
var arr = new Array(3); ...①
arr[0] = 1;
arr.b  = 0;
console.log(arr.length); ...② // 3

arr.forEach(value=>{
	console.log(value); ...③ // 1
})

for(var i in arr){
	console.log(arr[i]); ...④ // 1 0
}
for(var i of arr){
	console.log(i);  // 1 undefined undefiend
}

console.log(arr)
```
![[React/Photo/JavaScript题目-8.png]]

- [x] A.①式创建一个长度为3的数组
- [ ] B.②式输出结果为4
- [ ] C.③式输出结果为1 0
- [ ] D.④式输出结果为1

上面的代码展示了JavaScript中数组和对象的一些特性以及不同的迭代方式。下面我将详细解释为什么`for...of` 和 `for...in` 结果会不同：

在JavaScript中，数组是特殊的对象，你可以为其添加属性，就像你在上面的代码中为数组`arr`添加了属性`b`。然而，这些属性不会被计入数组的长度（`length`），并且它们也不会被标准的数组迭代方法（如`forEach`或`for...of`）遍历。

1. `for...in`循环：这个循环会遍历所有可枚举的属性，包括数组的索引和你添加的所有额外的属性。因此，它首先打印数组元素`arr[0]`的值（`1`），然后打印你添加的属性`arr.b`的值（`0`）。这就是为什么在`for...in`循环中你会看到两个输出：`1`和`0`。

2. `for...of`循环：这个循环会遍历所有的数组元素，但不包括你添加的属性。它仅仅迭代数组的元素，而不考虑这些元素是否已经被定义。因此，对于数组`arr`，它迭代了三次，第一次打印了`arr[0]`的值（`1`），然后因为`arr[1]`和`arr[2]`并未被定义，所以它们的值为`undefined`。这就是为什么在`for...of`循环中你会看到输出：`1 undefined undefined`。

所以，`for...in`和`for...of`之间的主要区别在于他们遍历的内容。`for...in`遍历对象的所有可枚举属性，包括原型链上的属性（如果没有用`hasOwnProperty`过滤），而`for...of`则专门用来遍历可迭代对象的元素，如数组、Map、Set等。

官方解析：

A选项，当new Array()括号内只有一个参数时，该参数表示数组的长度，A正确；B选项，数组的长度仍为3，这是**因为arr.b = 0;实际上是为变量arr赋予属性b，该属性不是数组元素，所以arr.length值不变**，仍为3；C选项，**forEach函数只遍历数组元素，由于arr数组的数组元素只有1，因此输出结果为1**；D选项，**for...in...会遍历数组以及数组的可枚举属性，因此输出结果为1 0**

```js

var arr = new Array(3); ...①    //结果是【empty ，empty ，empty  】
arr[0] = 1;                                //结果是【1，empty ，empty 】
arr.b  = 0;                                //结果是【1，empty ，empty ，b:0】 
                                                //**通过点操作符（.）添加的****属性和length属性处于同一层级，不会影响length的值**。

console.log(arr.length); ...②    //结果是3

arr.forEach(value=>{
	console.log(value); ...③   //结果是1 ，因为此时遍历的是【1，empty ，empty ，b:0】 
})                                              //**通过点操作符（.）添加的属性可以用for...in...循环遍历，但不能用foreach循环遍历。**
  
for(var i in arr){
  console.log(arr[i]); ...④    //结果是1，0 ，因为此时遍历的是【1，empty ，empty ，b:0】
}                                             //**通过点操作符（.）添加的属性可以用for...in...循环遍历**
                                             //for in既能遍历数组，也能遍历对象；
                                             //for in遍历数组时i是下标，遍历对象时i是对象的key，
                                            //对于数组来说arr[i]是1，对于键值对来说arr[i]是0

```


## 2.下面代码获取 input 节点的正确方法是( )  
```js
<form class="file" name="upload">
<input id="file" name="file" class="file"/>
</form>
```

- [ ] A.document.querySelectorAll('file')[0]
- [ ] B.document.getElementById('file')[0]
- [ ] C.document.getElementByTagName('file')[0]
- [x] D.document.getElementById('file')

如果忽略D选项的标点符号错误，那么正确答案确实是D

A: querySelectorAll **接收一个选择器做参数**，正确用法：
document.querySelectorAll(".file")[1];

B: **会返回undefined，因为getElementById 只返回符合id的那一个节点，而不是一个列表不能使用下标**，正确写法
document.getElementById("file");

C: file 根本不是一个tag，会出错, 正确用法：
document.getElementsByTagName("input")[0];


D: 仔细看选项 包裹file的引号，仔细看发现根本不是个引号，更正后：
document.getElementsByClassName("file")[1];


## .以上代码输出结果为（      ）
```js
var str1=new RegExp("e");
document.write(str1.exec("hello"));
```

- [x] A.e
- [ ] B.null
- [ ] C.1
- [ ] D.其他几项都不对

如果匹配成功，exec() 方法返回一个数组，并更新正则表达式对象的属性。返回的数组将完全匹配成功的文本作为第一项，将正则括号里匹配成功的作为数组填充到后面。

如果匹配失败，exec() 方法返回 [null](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/null)。

> [https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec)


	var str1=new RegExp("e");  
	str1.exec("hello")  
	["e", index: 1, input: "hello", groups: undefined]  

	var str1=new RegExp("l");  
	str1.exec("hello")  
	["l", index: 2, input: "hello", groups: undefined]
为什么不是显示数组？


因为document.write是接收字符串参数的方法，隐性调用性toString()后的数据

## 5.已知arr = `[1,2,NaN,1,4,2,NaN]`，现为输出arr的不重复元素（重复元素只输出一次），则下列程序中的①处，可以作为判断条件的是（）
```js
var newArr = [];
for(var i = 0 ;i<arr.length;i++){
  if(①){
    newArr.push(arr[i]);
  }
}
console.log(newArr);
```

- [ ] A.newArr.indexOf(arr[i]) == -1
- [ ] B.!newArr.indexOf(arr[i]) == -1
- [ ] C.newArr.includes(arr[i])
- [ ] D.!newArr.includes(arr[i])

官方解析：**indexOf()方法与includes()方法的一个重要区别在于indexOf()并不能判断数组的NaN元素**，换句话说，**不管数组arr是否有NaN元素，arr.indexOf(NaN)返回值都是-1**，所以AB选项不能对NaN进行去重，不符合题意；如果newArr数组不含有arr数组的某个元素，就应该把该元素添加到newArr数组中，如果含有，则不能添加，这样才能达到去重的目的，即newArr.includes(arr[i])返回值为false时，就应该执行if内的语句，所以应该使用“!”对条件取反，D选项符合题意，C选项不符合题意。


### NaN 相关：
```js
NaN == NaN // false  
NaN === NaN // false  
  
// indexOf方法无法识别数组的NaN成员  
[NaN].indexOf(NaN) // -1  
  
// 向 Set 数据结构中加入值时认为NaN等于自身  
let set = new Set();  
set.add(NaN);  
set.add(NaN);  
console.log(set); // Set {NaN}  
  
// Object.is()方法认为NaN等于NaN  
Object.is(NaN, NaN) // true  
+0 === -0 //true  
Object.is(+0, -0) // false  
  
// ES7中新增的数组实例方法，includes()方法认为NaN等于自身  
[1, 2, NaN].includes(NaN) // true
```

### 区别
```js
 indexOf()判断是否相等使用的是严格相等运算符 === ,所以
 [NaN].indexOf(NaN)值为-1。     
  
   includes()判断是否相等使用的是sameValueZero判断算法,所以
 [NaN].includes(NaN)值为true。

  js中的相等比较算法有以下四种：  
 
  
   1.        The Abstract Equality Comparison Algorithm (==)              
  
   2.        The Strict Equality Comparison Algorithm (===)                 
  
   3.        SameValue (Object.is())                (附：这里NaN和NaN相等，0和-0不相等)  
  
   4.        SameValueZero (暂未提供API)     (附：这里NaN和NaN相等，0和-0和+0都是相等的)   

   最常见的就是第一种和第二种，大家应该都知道了（==只比较值，不比较值的类型；===既比较值，又比较值的类型）  
  
   下面我们主要说第三种和第四种。  
  
   SameValue (Object.is())    
      
Object.is(NaN,NaN);  //true
Object.is(0,-0);     //false
Object.is(0,+0);     //true
Object.is(+0,-0);    //false
   
 1）我们知道NaN==NaN是false，NaN===NaN也是false，  但是SameValue算法里，NaN和NaN是相等的。   
  
   2）SameValue算法里0默认是+0，同时 0 和 -0 是不相等的（+0和-0也不相等）。
 
   SameValueZero (暂未提供API)   
  
   SameValueZero算法和SameValue算法的区别在于对0的处理（认为0、+0以及-0三者是相等的），其他的和SameValue一样（例如NaN和NaN是相等的）  
  
 
例一： 
[NaN].includes(NaN);  //true 
[0].includes(-0);  //true 
[0].includes(+0);  //true  


例二：
const a = new Set();
a.add(0);
a.add(NaN);
 
a.has(-0);  //true
a.has(+0);  //true
a.has(NaN); //true

```

  ## 3.请问以下两次检测对象constructor是否拥有属性名1的结果分别是什么？
  ```js
1 in Object(1.0).constructor
Number[1] = 123;
1 in Object(1.0).constructor
  ```
- [ ] A.false、false
- [ ] B.false、true
- [ ] C.true、true
- [ ] D.true、false
  
实际上Object（1.0）就是将数字“1.0”封装成它对应的包装类的一个对象实例比如Number（1.0），所以目的是为了检测1是否在Number上。一开始1并不在Number原型链上所以返回false，直到添加了“`Number[1]`”这个下标属性之后才让1处于Number的原型链上，也因此返回了true。


-  constructor 是构造函数属性。它是谁的属性？它**是原型属性 prototype 所指向的那个对象的属性**。
- Object(1.0).constructor 的原型是 Number 对象。  
    
- Number 对象本身可作为构造函数，所以 Object(1.0).constructor 就是 Number 对象本身。

1. 在浏览器控制可以看到 Object(1.0).constructor 的原型上的 constructor 属性指向的构造函数即 Number 对象 最初没有 属性 1 ；  
  
![[JavaScript题目-9.png]]
2. 通过 Object[key] = value; 形式给 constructor 对象添加 key = 1 属性,对应的 value = 123 ；

3. 第二次 检测对象 constructor 时就有了属性 1 。

![[JavaScript题目-10.png]]