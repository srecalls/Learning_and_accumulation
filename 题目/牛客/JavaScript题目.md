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

![[JavaScript题目.png]]


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

![[JavaScript题目-1.png]]


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
  
![[JavaScript题目-2.png]]


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

![[JavaScript题目-3.png]]

官方解析：

在对obj赋值的那一行语句可以看到应该拆分成两个表达式，前者的含义是计算obj.child，并暂存了当前的obj，之后才被赋值。而后者是改变了obj的指向覆盖了原本的变量obj，它的值是{num2：935}，所以找不到child这个属性故为undefined。这里的res代表的就是原本的变量obj，因此可以访问到num1和child。至于y在这里是会被认为是全局变量。


let obj = { num1: 117 } 

>     把obj放在栈里，把 { num1:117} 放在堆里，让obj指向堆里的 { num1:117 }     

    let res = obj;

> 把res放在栈里，把res也指向堆里的 { num1:117 }     

![[JavaScript题目-4.png]]
    obj.child  =  obj  =  { num2: 935 };
重点：赋值操作先定义变量(从左到右)，再进行赋值（从右到左）        
定义变量    obj.child，给堆里的{ num1:117 }加一个child属性，得{num1:117，child:undefined}      
定义变量    obj,之前在栈里的obj  

![[JavaScript题目-5.png]]

赋值    obj = { num2: 935 }，把{ num2: 935 }放在堆里，把栈里的obj指向堆里的{ num2: 935 }   


![[JavaScript题目-6.png]]  



赋值    obj.child = obj，把堆里的 {num1:117，child:undefined} 的child指向  {num2: 935}       

![[JavaScript题目-7.png]]         


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
![[JavaScript题目-8.png]]

  
  