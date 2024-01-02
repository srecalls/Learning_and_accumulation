![[Pasted image 20230311201703.png]]
bind、call、apply都是用来指定一个函数内部的this的值， 先看看bind、call、apply的用法

```js
var year = 2021
function getDate(month, day) {
  return this.year + '-' + month + '-' + day
}

let obj = {year: 2022}
getDate.call(null, 3, 8)    //2021-3-8
getDate.call(obj, 3, 8)     //2022-3-8
getDate.apply(obj, [6, 8])  //2022-6-8
getDate.bind(obj)(3, 8)     //2022-3-8
```
## 1. apply()
**语法: apply(thisObj,argArr)**
使用 apply， 我们可以只写一次这个方法然后在另一个对象中继承它，而不用在新对象中重复写该方法。
- apply 与 call() 非常相似，不同之处在于提供参数的方式。
- apply 使用参数数组而不是一组参数列表。
- apply 可以使用**数组字面量（array literal）**，如 `fun.apply(this, ['eat', 'bananas'])`，或**数组对象**， 如 `fun.apply(this, new Array('eat', 'bananas'))`。

apply方法接受一个或两个参数，
- 当接收一个参数时，第一个参数表示要改变的原函数的执行上下文(this)；
- 接收两个参数时，第二个参数必须是数组(或伪数组)，用于替换原函数中arguments保存的参数。

将开始的代码使用apply方法改成如下代码，即可让对象B具有对象A的fn方法

```JS
var A = {
    name: "AAA",
    fn: function(skill){
    // 这里传入的参数加入this里
    this.skill = skill;
        console.log("my name is " + this.name +", my skills are " + this.skill);
    }
}
var B = {
    name: "BBB"
}
A.fn("sing");                  //my name is AAA, my skills are sing
// 此处改动产生的效果为：
// 在执行A对象的函数fn时，通过apply将函数fn的执行上下文(this)暂时修改为对象B，
// 此时fn中的this指向对象B，同时修改原函数fn的参数为“dance”(注意“dance”参数必须是数组的形式)，
//apply方法自动执行改变之后的原函数
A.fn.apply(B,["dance"]);       //my name is BBB, my skills are dance
```
### apply方法调用一个具有给定this值的函数，以及以一个数组的形式提供参数。
```js
var array = ['marshall','eminem'];
var elements = [0,1,2];
// 这里只是参数必须包含在数组里，而不是传入一个数组
// 即使是数组也必须用数组包，不会转换
array.push.apply(array,elements);
console.log(array);  //['marshall','eminem',0,1,2]
```
### 使用apply和内置函数
```js
//找出数组中最大值和最小值
var numbers = [5, 6, 2, 3, 7];
//使用Math.min和Math.max以及apply函数时的代码
var max = Math.max.apply(null, numbers);
var min = Math.min.apply(null, numbers);
```
上边这种调用apply的方法，有超出JavaScript引擎参数长度上限的风险。


![[Pasted image 20230311202109.png]]
![[Pasted image 20230311202344.png]]
![[Pasted image 20230311202417.png]]



## 2. call()
**语法：call(thisObj,arg1,arg2,arg3,……)**
call()方法接受的语法和作用与apply()方法类似，只有一个区别就是call()接受的是一个参数列表，而apply()方法接受的是一个包含多个参数的数组。

call方法接收一个或一个以上的参数，
- 当接收一个参数时，第一个参数表示要改变的原函数的执行上下文(this)
- 接收多个参数时，第二个参数及后面所有参数用来替换原函数的参数。
```js
var A = {
    name: "AAA",
    fn: function(skill){
        this.skill = skill;
        console.log("my name is " + this.name +", my skills are " + this.skill);
    }
}
var B = {
    name: "BBB"
}
A.fn("sing");                 //my name is AAA, my skills are sing
//此处改动产生的效果为：
//在执行A对象的函数fn时，通过call将函数fn的执行上下文(this)暂时修改为对象B，
//此时fn中的this指向对象B，同时修改原函数fn的参数为“dance”，
//call方法自动执行改变之后的原函数
A.fn.call(B,"dance");         //my name is BBB, my skills are dance

```

> 参数区别
```js
let obj = {
    a: 1,
    get: function(){
        return 2
    }
}
let g = obj.get
g.call({},1,2,3) // 参数列表
g.apply({},[1,2,3]) // 一个包含多个参数的数组
```

### call方法调用父构造函数
```js
function Product(name, price){
    this.name = name;
    this.price = price;
}

// 调用父构造函数的call方法来实现继承
function Food(name, price){
    Product.call(this, name, price);
    this.category = 'food';
}

function Toy(name, price){
    Product.call(this, name, price);
    this.category = 'toy';
}

var cheese = new Food('feta', 5);
var fun = new Toy('robot', 40);
```

### call方法调用匿名函数
```js
var animals = [
    {species: 'Lion', name: 'King'},
    {species: 'Whale', name: 'Fail'}
];

for(var i = 0; i < animals.length; i++){
    (function(i) {
        this.print = function(){
            console.log('#' + i + ' ' + this.species + ': ' + this.name);
        }
        this.print(); 
    }).call(animals[i], i); //call调用匿名函数
    // #0 Lion: King
	// #1 Whale: Fail
}
```

### call方法调用函数并且指定上下文的this
```js
var obj = {
    animal: 'cats', sleepDuration: '12 and 16 hours'
};

function greet(){
    var reply = [this.animal, 'typically sleep between', this.sleepDuration].join(' ');
    console.log(reply);
}

greet.call(obj);  //"cats typically sleep between 12 and 16 hours"
```

### call方法调用函数并且不指定第一个参数(argument)
```js
var sData = 'marshall';

function display(){
    console.log("sData's value is %s",this.sData);
}

display.call();  // sData value is marshall
```
但是在严格模式下，this 的值将会是undefined

```js
var sData = 'marshall';

function display(){
    console.log("sData's value is %s",this.sData);
}

display.call();  // Cannot read the property of 'sData' of undefined
```

二者都是函数对象Function的方法，且第一个参数都是要绑定对象的上下文
![[Pasted image 20230311201737.png]]
![[Pasted image 20230311202044.png]]

![[Pasted image 20230311202637.png]]


## 3. bind()
bind()函数会创建一个新的绑定函数，这个绑定函数包装了原函数的对象。调用绑定函数通常会执行包装函数。  
绑定函数内部属性：

- 包装的函数对象
- 在调用包装函数时始终作为this传递的值
- 在对包装函数做任何调用时都会优先用列表元素填充参数列表。

而原函数 retrieveX 中的 this 并没有被改变，依旧指向全局对象 window。
```js
this.x = 9; //this指向全局的window对象
var module = {
    x: 81,
    getX: function(){return this.x;}
};

console.log(module.getX()); //81

var retrieveX = module.getX;
console.log(retrieveX()); //9,因为函数是在全局作用域中调用的

// 创建一个新函数，把this绑定到module对象
// 不要将全局变量 x 与 module 的属性 x 混淆
var boundGetX = retrieveX.bind(module);
console.log(boundGetX()); //81
```
### bind传递参数问题
在通过bind改变this指向的时候所传入的参数会拼接在调用返回函数所传参数之前，多余参数不起作用。

```js
var newShowName = showName.bind(newThis, 'hello');
//在通过bind改变this指向的时候只传了“hello”一个参数，
//在调用newShowName这个返回参数的时候，bind传参拼接在其前
newShowName('world'); //输出：newThis hello world
```

```js
var newShowName = showName.bind(newThis, 'hello');
//在通过bind改变this指向的时候只传了“hello”一个参数，
//在调用newShowName这个返回参数的时候，bind传参拼接在其前，
//这时newShowName的参数为“hello”，“a”，“world”
//而该函数只需要两个参数，则第三个参数被忽略
 newShowName('a','world'); //输出：newThis hello a
```
bind传入的参数和newShowName方法传入的参数会**拼接在一起**，一齐传给showName方法。

```js
var name = 'window';
var newThis = { name: 'newThis' };
function showName(info1, info2) {
    console.log(this.name, info1, info2);
}
showName('a', 'b'); //输出：window a b

// 通过bind改变this指向
var newShowName = showName.bind(newThis, 'hello','1','2');
newShowName('a','world'); //输出：newThis hello 1

console.log(new newShowName().constructor); //输出：showName函数体
```
可以看出，通过bind改变this指向返回函数的构造器还是最开始的showName函数。

new newShowName()实例化了一个新的方法，这个方法的this也不再指向newThis。

![[Pasted image 20230311202732.png]]
![[Pasted image 20230311202814.png]]
![[Pasted image 20230311202947.png]]

## 4. apply 和 call 区别
- call可以接受一个或以上的参数，当接受多个参数时，从第二个参数开始，后面所有的参数都会改变原函数的参数；
- apply只能接受一个或两个参数，当接受两个参数时，第二个参数必须是**一个数组或类数组**，数组中的数据，会改变原函数arguments中的参数。
而call和apply的第一个参数，都是用来改变原函数的this指向。

JavaScript 中，某个函数的参数数量是不固定的，因此要说适用条件的话

- 当你的参数是明确知道数量时用 call 。
- 而不确定的时候用 apply，然后把参数 push 进数组传递进去。当参数数量不确定时，函数内部也可以通过 arguments 这个伪数组来遍历所有的参数。
### 常用用法
#### 1.数组之间的追加
```js
var array1 = [12 , "foo" , {name: "Joe"} , -2458]; 
var array2 = ["Doe" , 555 , 100]; 
array1.concat(array2) // array1 值仍为 [12 , "foo" , {name: "Joe"} , -2458]
Array.prototype.push.apply(array1, array2); 
/* array1 值为  [12 , "foo" , {name "Joe"} , -2458 , "Doe" , 555 , 100] */
```
和concat的区别就是这个追加会更改原数组，而concat不会

#### 2.获取数组中最大值和最小值
```js
var  numbers = [5, 458 , 120 , -215 ]; 
var maxInNumbers = Math.max.apply(Math, numbers)   //458
var maxInNumbers = Math.max.call(Math,5, 458 , 120 , -215) //458
```

#### 3.验证是否是数组（前提是toString()方法没有被重写过）
```js
let obj = [1, 2, 3]
// 一个是数组的toString方法
// 一个是Object对象的toString方法
console.log(obj.toString()) // 1, 2, 3
console.log(Object.prototype.toString.call(obj)) // [object Array]'
functionisArray(obj){ 
    return Object.prototype.toString.call(obj) === '[object Array]' ;
}
```

## 5. apply、call、bind比较
```js
var obj = {
    x: 81,
};
 
var foo = {
    getX: function() {
        return this.x;
    }
}
 
console.log(foo.getX.bind(obj)());  //81
console.log(foo.getX.call(obj));    //81
console.log(foo.getX.apply(obj));   //81
```
三个输出的都是81，但是注意看使用 bind() 方法的，他后面多了对括号。  
也就是说，区别是，当你希望改变上下文环境之后并**非立即执行**，而是回调执行的时候，使用 bind() 方法。而 apply/call 则会立即执行函数。

### 总结一下

- apply 、 call 、bind 三者都是用来改变函数的this对象的指向的；
- apply 、 call 、bind 三者第一个参数都是this要指向的对象，也就是想指定的上下文;
- apply 、 call 、bind 三者都可以利用后续参数传参；
- bind 是返回对应函数，便于稍后调用；apply 、call 则是立即调用 。

## 总结
![[Pasted image 20230311203009.png]]