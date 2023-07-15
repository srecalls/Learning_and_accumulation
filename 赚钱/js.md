### 1. JavaScript有哪些基本数据类型，哪些引用数据类型？它们的区别是？

基本数据类型：Undefined、Null、Boolean、Number、String、Symbol、BigInt。

引用数据类型：对象、数组和函数

两种类型的区别在于**存储的位置不同**，基本数据类型存储在栈中，引用数据类型占据空间大、大小不固定，如果存储在栈中，将会影响程序运行的性能，故其存储在堆中。

栈是一段连续紧凑的空间，存储在CPU内存中，堆的内存结构比较大且不连续，存储在物理内存中，读取速度栈比堆快，因此选择把基本数据类型和引用数据类型的引用地址存到栈中，实际的引用数据类型则是放在堆中，等你要找一个对象时先去栈中快速的找到它在堆中的地址，再去堆中取，这样读取比较快。

### 2. 数据类型检测的方式有哪些？

1. **typeof**

​		能准确的判断出基本数据类型和函数，数组、对象和null都会被判断为object。

​		原理：对象在底层都表示为二进制，其二进制前三位存储它的类型信息，000：对象，100：字符串，110：布尔，null的二进制表示全为0，所以也会被判断为object。

```js
console.log(typeof 2);               // number
console.log(typeof true);            // boolean
console.log(typeof 'str');           // string
console.log(typeof []);              // object    
console.log(typeof function(){});    // function
console.log(typeof {});              // object
console.log(typeof undefined);       // undefined
console.log(typeof null);            // object
```

 2. **instanceof**

    能准确的判断出引用数据类型，不能判断基本数据类型。

```js
console.log(2 instanceof Number);                    // false
console.log(true instanceof Boolean);                // false 
console.log('str' instanceof String);                // false 

console.log([] instanceof Array);                    // true
console.log(function(){} instanceof Function);       // true
console.log({} instanceof Object);                   // true
```

 3. **constructor**

    如果其原型没有被改变，则能正确的判断出来，不能判断undefined和null，因为它们没有构造函数。

```js
console.log((2).constructor === Number); // true
console.log((true).constructor === Boolean); // true
console.log(('str').constructor === String); // true
console.log(([]).constructor === Array); // true
console.log((function() {}).constructor === Function); // true
console.log(({}).constructor === Object); // true
```

4. **Object.prototype.toString.call()**

   能正确的判断出来，不太懂

### 3. 判断数组的方法有哪些

1.  **instanceof**

   ```js
   console.log([] instanceof Array);  // true
   ```

2.  **constructor**

   ```js
   console.log(([]).constructor === Array);  // true
   ```

 3. **Object.prototype.toString.call()**

    ```js
    console.log(Object.prototype.toString.call([]) === '[object Array]') //true
    ```

 4. **Array.isArray()**

    ```
    console.log(Array.isArray([]);) //true
    ```

5. **Array.prototype.isPrototypeOf**

   ```js
   console.log(Array.prototype.isPrototypeOf([]))  //true
   ```

6. **通过原型链**

   ```js
   console.log([].__proto__ == Array.prototype) //true
   ```

### 4. undefined和null的区别

undefined和null都是基本数据类型，一般变量声明了但未被定义时会返回undefined，null一般用来赋值作为初始化。

使用void 0来安全的获取undefined。

当使用双等号时结果为true,三等号时结果为false。

### 5. 如何让0.1+0.2与0.3相等，为什么不相等？

1. 四舍五入

   ```js
   console.log((0.1 + 0.2).toFixed(1) == 0.3)  //true
   ```

2. 设置误差范围

   ```js
   console.log(Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON)  //true
   ```

### 6. typeof NaN 的结果是什么？

```js
console.log(typeof NaN)  //number
```

### 7. isNaN 和 Number.isNaN 函数的区别？

isNaN：任何**不能转化**为number的参数与NaN都返回true。

Number.isNaN:  只有NaN才返回true。

### 8. == 操作符的强制类型转换规则？

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c451c19e23dd4726b3f36223b6c18a1e~tplv-k3u1fbpfcp-zoom-in-crop-mark:3024:0:0:0.awebp)

### 9. object如何进行隐式转换

`type`的值为`number`或者`string`。

**（1）当**`type`**为**`number`**时规则如下：**

- 调用`obj`的`valueOf`方法，如果为基本数据类型，则返回，否则下一步；
- 调用`obj`的`toString`方法，后续同上；
- 抛出`TypeError` 异常。

**（2）当**`type`**为**`string`**时规则如下：**

- 调用`obj`的`toString`方法，如果为基本数据类型，则返回，否则下一步；
- 调用`obj`的`valueOf`方法，后续同上；
- 抛出`TypeError` 异常。

可以看出两者的主要区别在于调用`toString`和`valueOf`的先后顺序。默认情况下：

- 如果对象为 Date 对象，则`type`默认为`string`；
- 其他情况下，`type`默认为`number`。

### 10. object.assign和扩展运算符是深拷贝还是浅拷贝

都是浅拷贝（第一层深拷贝，接下来的层都为浅拷贝）

### 11.  Object.is() 与比较操作符 “===”、“==” 的区别？

使用双等号（==）进行相等判断时，如果两边的类型不一致，则会进行强制类型转化后再进行比较。

使用三等号（===）进行相等判断时，如果两边的类型不一致时，不会做强制类型转换，直接返回 false。

使用 Object.is 来进行相等判断时，一般情况下和三等号的判断相同，它处理了一些特殊的情况，比如 -0 和 +0 不再相等，两个 NaN 是相等的。

### 12.什么是 JavaScript 中的包装类型？

基本类型是没有属性和方法的，为了便于操作基本类型的值，在调用基本类型的属性和方法里，后台会隐式的将基本类型转化为包装类型。

### 13. var let const的区别

**（1）块级作用域：** 块作用域由 `{ }`包括，let和const具有块级作用域，var不存在块级作用域。块级作用域解决了ES5中的两个问题：

- 内层变量可能覆盖外层变量
- 用来计数的循环变量泄露为全局变量

**（2）变量提升：** var和let存在变量提升，const不存在变量提升，但let只有创建被提升了，初始化并没有，也就是暂时性死区，暂时性死区就是不能在初始化之前使用，所以let和const只能在变量声明之后使用，否则会报错。（变量有创建、初始化、赋值三步骤，const没有赋值）

**（3）给全局添加属性：** 浏览器的全局对象是window，Node的全局对象是global。var声明的变量为全局变量，并且会将该变量添加为全局对象的属性，但是let和const不会。

**（4）初始值设置：** 在变量声明时，var 和 let 可以不用设置初始值。而const声明变量必须设置初始值。

**（5）指针指向：** let和const都是ES6新增的用于创建变量的语法。 let创建的变量是可以更改指针指向（可以重新赋值）。但const声明的变量是不允许改变指针的指向。

**（6）重复声明：** var声明变量时，可以重复声明变量，后声明的同名变量会覆盖之前声明的遍历。const和let不允许重复声明变量。

### 14. 箭头函数与普通函数的区别

**（1）箭头函数比普通函数更加简洁**

**（2）箭头函数的this是继承来上一层作用域的**

**（3）call()、apply()、bind()等方法不能改变箭头函数中this的指向**

**（4）箭头函数不能作为构造函数使用**

**（5）箭头函数没有自己的arguments，会继承上一层的arguments**

**（6）箭头函数没有prototype**

### 15. for和forEach的区别

1. for循环写得比较麻烦，forEach写起来比较舒服，可读性也更好；
2. for循环用continue跳过当次循环，break中断循环，forEach用return跳过当次循环，try catch中断循环；
3. for循环更加灵活，可以随意控制下标；
4. forEach会跳过稀疏数组，如[1,,,4]；
5. for循环效率高于forEach，因为forEach会创建一个新的函数，通过调用函数进行迭代。

### 16. new操作符的实现原理

（1）首先创建了一个新的空对象

（2）设置原型，将对象的原型设置为函数的 prototype 对象。

（3）让函数的 this 指向这个对象，执行构造函数的代码（为这个新对象添加属性）

（4）判断函数的返回值类型，如果是基本数据类型，返回创建的对象。如果是引用类型，就返回这个引用类型的对象。

### 17. JavaScript有哪些内置对象

值：undefined、null、NaN

函数：parseInt()、eval()

对象：Object、Function、Array、Boolean、Number、Set、Map等等，还有JSON、Math等等

构造函数：Data

### 18. JSON与js数据结构的转化

js数据结构转JSON： JSON.stringify()

JSON转js数据结构： JSON.parse()

### 19. JavaScript 类数组对象的定义？

一个拥有 length 属性和若干索引属性的对象就可以被称为类数组对象，但是不能调用数组的方法，常见的类数组对象有arguments和DOM方法返回的结果。类数组是Object而不是Array。

常见的类数组转换为数组的方法有这样几种：

（1）通过 call 调用数组的 slice 方法来实现转换

```javascript
Array.prototype.slice.call(arrayLike);
```

（2）通过 call 调用数组的 splice 方法来实现转换

```javascript
Array.prototype.splice.call(arrayLike, 0);
```

（3）通过 apply 调用数组的 concat 方法来实现转换

```javascript
Array.prototype.concat.apply([], arrayLike);
```

（4）通过 Array.from 方法来实现转换

```javascript
Array.from(arrayLike);
```

（5）通过扩展运算符来实现转换

```js
let newArrayLike = [...arrayLike];
```

### 20. 如何遍历类数组

（1）转换为数组 见19题

（2）使用for...in...

（3）使用call方法调用forEach

```js
Array.prototype.forEach.call(arrayLike, item => console.log(item))
```

### 21. 数组常用的方法（不含遍历方法）

1. push()

   在数组后面添加一个或多个元素，返回数组的最新长度

2. pop()

   删除数组最后一个元素，返回被删除的元素

3. unshift()

   在数组开头添加一个或多个元素，返回数组的最新长度

4. shift()

   删除数组中第一个元素，返回被删除的元素

5. slice()

   两个参数，第一个为开始索引，第二个为结束索引，左闭右开，不影响原数组，返回截取数组。

   如果第二个参数省略不写，则截取从开始索引往后的所有元素。

6. splice()

   第一个为开始索引，第二个为删除元素数量，第三个及以后的参数为插入元素，影响原数组，返回被删除的内容，结果为Array。

   可进行删除元素，也可以插入元素。

7. concat()

   可连接两个或多个数组，不影响原数组，返回新数组

8. join()

   将数组转化为字符串，可指定一个参数作为数组元素的连接符，不指定连接符默认','作为连接符。

9. toString()

   将数组转化为字符串

10. reverse()

    反转数组，影响原数组

11. sort()

    排序，可以传入一个函数，函数有两个参数，分别为前后两个值，返回值如果是正数则交换两个参数的位置，影响原数组

    默认是从小到大

    如果不传函数，数组内有负数，结果会不正确。

12. indexOf()

    一个参数，找到数组中第一次出现该参数的元素，返回其索引值，如果没有找到则返回-1

13. lastIndexOf()

    一个参数，找到数组中最后一次出现该参数的元素，返回其索引值，如果没有找到则返回-1

14. includes()

    一个参数，判断数组中是否含有该元素，是返回true，否则返回false

### 22. 数组常用的遍历方法

1. forEach()

   三个参数，第一个为当前元素，第二个为当前索引，第三个为数组，修改第一个参数不能更改数组，需要使用第三个参数（数组）加第二个参数（索引）进行修改，没有返回值

   没有continue，用return代替，没有break，如果需要可用try/catch

2. map()

   第一个参数为当前元素，不影响原数组，返回新数组

3. some()

   第一个参数为当前元素，检查数组是否有满足条件的元素，有返回true，否则返回false

4. every()

   第一个参数为当前元素，检查数组的每一项是否都满足条件，满足返回true，否则返回false

5. filter()

   第一个参数为当前元素，过滤数组返回一个新数组，不影响原数组

6. find()

   第一个参数为当前元素，返回符合条件的第一个元素，没有符合条件的返回undefined

7. findIndex()

   第一个参数为当前元素，返回符合条件的第一个元素索引，没有符合条件的返回-1

8. reduce()

   统计数组，四个参数，第一个为上一次函数返回的值 ，第二个为当前元素的值 ，第三个为当前元素的索引，第四个为该数组

   ```js
   let arr = [1,2,3,4,5]
   let a = arr1.reduce((a,b)=>{
     return a+b
   })
   console.log(a)  //15
   ```

9. reduceRight()

   同上，只不过是逆序操作

10. for...of...

    用于遍历数组、类数组、set、map、字符串等，不能用于遍历对象

11. for...in...

    会遍历自定义属性和原型链，一般用来遍历对象，不适合用来遍历数组。

### 23. 什么是尾调用，使用尾调用有什么好处？

尾调用是指函数的最后一步调用另一个函数。在一个函数里调用另一个函数时会保留当前执行的上下文，在严格模式下使用尾调用，则不保留当前执行的上下文，从而节省内存。尾调用优化只在严格模式下开启。

### 24. ajax、axios、fetch的区别

1. ajax是一种无需重新加载整个网页的情况下，实现更新部分网页的技术，会导致回调地狱

2. fetch使用了promise对象，不是对ajax的封装，是原生的js，没有使用XHR对象

   优点：基于promise，支持async/await，提供了更多的API，脱离了XHR。

   缺点：只对网络请求报错，400，500的状态码都当做成功的请求，默认不带cookie

3. axios是对ajax的封装，使用了promise，浏览器端发起XHR请求，node端发起http请求，自动转换json数据，客户端支持抵御CSRF攻击

### 25. 原型和原型链

js中是使用构造函数创建对象的，每一个构造函数都有一个prototype属性，属性值为一个对象，用来存放共享的属性和方法，当使用该构造函数创建新的实例时，该实例有一个proto属性指向prototype，这称为原型。

原型链：当访问一个对象属性时，该对象内部不存在这个属性，那么就会去prototype上去查找，这个prototype又有自己的prototype，一直这样查找下去直到取到null为止。

![image-20220712213242479](C:\Users\123\AppData\Roaming\Typora\typora-user-images\image-20220712213242479.png)

### 26. 如何获得对象非原型链上的属性？

使用后`hasOwnProperty()`方法来判断属性是否属于原型链的属性：

```javascript
let str = new String();
console.log(str.hasOwnProperty('split'));  // false
console.log(String.prototype.hasOwnProperty('split'));  // true
```

### 27. 实现深拷贝

1. 扩展运算符：只能深拷贝一层

2. Object.assign()：只能深拷贝一层

3.  JSON转化：当值为undefined和function时在转化过程中会被忽略

   ```js
   let newObj = JSON.parse(JSON.stringify(obj));
   ```

4. 利用循环和递归

   ```js
   function deepClone(obj, newObj) {
     for (let key in obj) {
       if(obj[key] instanceof Array){
         newObj[key] = [];
         deepClone(obj[key], newObj[key]);
       }else if(obj[key] instanceof Object){
         newObj[key] = {};
         deepClone(obj[key], newObj[key]);
       }else{
         newObj[key] = obj[key]
       }
     }
     return newObj;
   }
   ```


### 28. JS脚本延迟加载的几种方式？

默认是解析HTML，遇到javascript标签时请求脚本，执行脚本，继续解析HTML。

1. defer：解析HTML，遇到javascript标签则解析HTML的同时请求脚本，即使脚本请求完毕也会等待HTML解析完毕再执行。

2. async：解析HTML，遇到javascript标签则解析HTML的同时请求脚本，脚本请求完毕后立即执行，如此时HTML未解析完会被阻塞。

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20190924222353217.png)

3. 把javascript放到最下面。

4. 使用setTimeout

### 29. 数组的includes比indexOf方法好在哪？

includes方法可以检测NaN和undefined，indexOf不行。

### 30. Commonjs 和 ES6 Module的区别

1. Commonjs模块是module.exports导出，require导入，ES6模块是export导出，import导入。
2. Commonjs模块是运行时动态加载，运行时才能确定依赖关系，ES6模块是编译时静态加载，编译时就能确定依赖关系，静态编译才能tree shaking（webpack5新增支持commonjs模块的tree shaking，就是把commonjs转成esm，根据静态分析的结果去判断哪些代码可以删除，但实际的效果可能没那么好）。
3. Commonjs模块输出的是值的拷贝，会对加载结果进行缓存，取到值后进行修改不会影响到外部，ES6模块输出的是值的引用，修改后会同步影响到外部。
4. ES6模块在编译期间会把import提升到顶部，Commonjs模块不会提升require。

### 31. 常见的DOM方法

创建节点：`document.createElement("标签名")`;

删除节点：`父节点.removeChild(子节点)`;

插入节点：`节点.appendChild(Node)` //在节点内最后面追加一个Node

​				   `节点.insertBefore(插入节点,参照物节点)` //在参照物节点前面插入一个新的节点

获取属性值：`节点.getAttribute(attributeName)` //传入属性名，返回属性值

设置属性值：`节点.setAttribute(attributeName,attributeValue)` 

### 32. WeakSet、WeakMap

WeakSet的值和WeakMap的键名只接受对象（数组、对象、函数），WeakMap的值可以是任意，都不能遍历，都为弱引用，有利于垃圾回收，防止内存泄露。都没有size属性。

WeakSet方法：add、delete、has；

WeakMap方法：get、set、delete、has。

WeakMap的使用场景：当我们想给对象添加数据，又不想修改对象时，就可以使用map添加元数据(meta)，但当这个对象不再被使用时，因为map中有映射关系，所以这个对象和map都无法被垃圾回收，除非手动把映射关系取消，如果你没有遍历map这个需求，可以把map换成WeakMap，这样对象不再使用的时候，对象和weakmap都可以被垃圾回收。

WeakSet的使用场景：需要打标记，但不需要遍历，可以用weakset，比如把禁用的DOM都放到这个weakset里，用has就能判断是否禁用了，这个DOM被删除后也不用自己手动去delete就能垃圾回收。

### 33. 原型污染是什么？怎么解决？

原型污染是指攻击者通过某些手段修改js的原型

```js
Object.prototype.toString = function(){};
```

解决方法：

```js
Object.freeze(Object.prototype);
```

### 34. 说说对闭包的理解

闭包就是能够读取其它函数内部变量的函数。一般是函数A return一个函数B，函数A执行完后它的变量不会销毁，并且函数B能访问到函数A中的变量，可以用来创建私有变量，避免全局变量的污染。

闭包原理：作用域链，当前作用域可以访问上级作用域中的变量。Vue2中响应式原理的Observer就使用闭包。

带来的问题：垃圾回收器不会将闭包中的函数变量销毁，会造成内存泄露，内存泄露多了容易导致内存溢出。

### 35.call、apply、bind

它们的作用是改变this的指向。

call与apply传参不同，其它一样，call是一个一个传，apply是传一个数组或类数组，call和apply是直接调用，bind返回函数便于后续调用。

### 36. 字符串方法

1. charAt()
2. indexOf() 两个参数，第一个参数是查找的字符串，第二个参数是从哪个索引位置开始查找，返回索引值
3. lastIndexOf() 从后往前查找，同上
4. includes() 两个参数，第一个参数是查找的字符串，第二个参数是从哪个索引位置开始查找，返回true或false
5. startWith() 检测是否以该字符串开头
6. endWith() 检测是否以该字符串结尾
7. concat() 连接字符串
8. split() 字符串分割成数组
9. slice() 截取字符串，左闭右开
10. substring() 同上
11. toLowerCase() 转化为小写
12. toUpperCase() 转化为大写
13. replace() 替换字符
14. trim() 移除首尾的空白符

### 37. Object.freeze()的了解

冻结对象或数组，使其不能添加新属性，不能删除属性，不能修改已有属性，不能修改原型，不能修改已有属性的可枚举性、可配置性、可写性；

是浅冻结，只能冻结一层。

在Vue中使用Object.freeze()冻结不需要修改的数据，可以让数据不做数据劫持，提升性能。

```js
data(){
    return {
		obj: Object.freeze({test:1});
    }
}
```

### 38. document.ready和document.onload两个事件的区别

document.ready是指文档结构加载完成，document.onload是指页面中包含图片在内的所有元素都加载完成。

### 39. ES6的新特性

1. 块级作用域let、const
2. 基本数据类型Symbol
3. 解构赋值
4. 模版字面量
5. 扩展运算符
6. 模块化（import / export）
7. set、map数据结构
8. 箭头函数
9. class类
10. 构造函数Proxy
11. promise

### 40. 对作用域和作用域链的理解

作用域分为全局作用域和函数作用域，ES6新增了块级作用域。

全局作用域：在任何位置都能访问，window的的内置属性就是全局作用域；

函数作用域：只有在函数体内才能访问到，就是私有作用域；

块级作用域：在大括号中使用let和const会产生块级作用域，如在if、while、for、switch中；

作用域链：一般情况使用的变量取值是在当前执行环境的作用域中查找，如果当前作用域没有查到这个变量，就会向上级作用域查找，直到查找到全局作用域，这么一个查找过程叫做作用域链。

### 41. 对this的理解 

1. this总是指向函数的直接调用者，函数的this可以用call、apply、bind改变；
2. 如果有new关键字，this指向创建的实例对象；
3. 在事件中，this指向触发这个事件的对象。

### 42. 继承

1. 原型链继承

2. 构造继承

3. 组合式继承（原型链+构造）

   ```js
   function Father(name){
   	this.name = name;
   }
   function Son(name){
   	Fahter.call(this,name);
   }
   Son.prototype = new Father();
   ```

4. 原型式继承

5. 寄生式继承

6. 寄生组合式继承

   ```js
   function Father(name){
   	this.name = name;
   }
   function Son(name){
   	Fahter.call(this,name);
   }
   Son.prototype = Object.create(Father.prototype);
   Son.prototype.constructor = Son;
   ```

7. class类继承

   ```js
   class Father(){
       constructor(name){
           this.name = name;
       }
       fn(){
   		console.log(1);
       }
   }
   class Son extends Father(){
       constructor(name,age){
   		super(name)
           this.age = age
       }
   }
   ```

### 43. Ajax的基本使用

```js
xhr = new XMLHttpRequest();
xhr.open("GET","www.baidu.com");
xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
xhr.onreadystatechange = function(){
	if(xhr.readyState === 4){
		if(xhr.status === 200){
            console.log(JSON.parse(xhr.response))
        }
    }
}
xhr.send();
```

readystate:

0：还没调用send()方法；

1：已经调用send()方法正在发送请求；

2：send()执行完毕，已经接着全部响应内容；

3：正在解析响应内容；

4：响应内容解析完成，可以在客户端内调用。 

### 44. js的严格模式

严格模式对js代码作了一些限制，减少一些怪异行为。如：禁止this指向全局对象，顶层的this为undefined；变量必须声明后再使用；函数的参数不能有同名属性；不能删除不可删除的变量；不能赋值只读属性等。

### 45. 对Promise的理解

Promise是对异步编程的一种解决方案，避免了回调地狱，它有三种状态，Pending、Resolved、Rejected，一旦从Pending改为Resolved或Rejected后就不能改变了，它的回调函数是微任务。它有then、catch、all、race方法。

### 46.promise和async的区别

Promise是对异步编程的一种解决方案，避免了回调地狱，async是使异步代码看起来像同步，async函数一定会返回一个Promise对象，async是基于promise实现的，可以说是改良版Promise，捕捉错误的时候是用try catch。

### 47. type和interface的区别

1. type是类型别名，interface是接口，都可以用来定义对象或函数；
2. type用&来继承，interface用extends来继承；
3. interface可以多次定义并自动合并，type不可以；
4. type可以用于基本类型，联合类型，元组类型，interface不支持。

### 48. 使用requestAnimationFrame比setTimeout做动画的优势

1. 流畅：requestAnimationFrame是在每次渲染之前调用，根据的是屏幕的刷新频率，做动画比较流畅，而setTimeout是把回调函数放到任务队列里去执行的，执行时间是不确定的，有可能会出现丢帧，闪屏的现象；
2. 性能：requestAnimationFrame还会把每一帧的动画集中起来，在一次回流中完成，减少回流，性能更好；
3. 优化：当页面被隐藏（tab页面切换），requestAnimationFrame的回调函数会暂停执行，即动画会停止，而setTimeout会继续执行。

### 49. 如何设置一个有时效的localStorage

1. 惰性删除，多存一个时间，在获取的时候判断是否过期
2. 定时删除，设置个定时器，关闭页面后定时器会失效，需要使用load事件让他重新计时