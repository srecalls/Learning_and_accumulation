
###### 对象方法
## 一、Object.assign
1. `Object.assign()`方法将所有`可枚举属性`的值从一个或多个源对象复制到目标对象，它将返回目标对象。

```jsx
var target = {a:1,b:2,c:666}
var source = {c:3,d:4}
var assignObj = Object.assign(target,source);

console.log(target);  //{a:1,b:2,c:3,d:4}
console.log(assignObj);  //{a:1,b:2,c:3,d:4}
```

根据概念以及以上代码理解：  
合并的对象仅仅只是将`可枚举属性`拿过来合并，也就是说继承属性和不可枚举属性是不能拷贝的。  
合并对象时目标对象target会被`改变`  
合并对象时相同属性的值，source的属性会`覆盖`之前其他对象的相同属性。比如target的c属性。  
此方法不能实现`深拷贝`，假如源对象的属性值是一个对象的引用，那么它也只指向那个引用。

## 二、Object.create()
[[手写Object.create]]
2. `Object.create()`方法创建一个新对象，使用现有对象来提供新创建对象的`__proto__`。
![[Pasted image 20230531172505.png]]

如上图所示，使用现有对象`obj`，来提供新对象`o`的`__proto__`。

`Object.create()`方法接收两个参数，  
第二个参数可省略,具体可参考我总结的这篇文章[《JavaScript ES6数据类型》](https://www.jianshu.com/p/2206959c0019)

留个代码图，注意看o.p的值是不可修改的。
  
![[Pasted image 20230531172518.png]]
create第二个参数

## 三、Object.entries()
3. `Object.entries()`方法返回一个给定对象自身可枚举属性的`键值对数组`。

```bash
var obj = {name:"zhang",age:100,sex:"male"};
console.log(Object.entries(obj));

/*
  [ ["name", "zhang"], ["age", 100], ["sex", "male"] ]
*/
```
**可以配合Map**

## 四、Object.freeze()
4. `Object.freeze()`方法可以冻结一个对象。一个被冻结的对象再也不能被修改，也不能添加新属性，不能删除新属性，也不能修改其`数据属性`,该对象的原型也不能修改。`freeze()`返回和传入的参数相同的对象。

```jsx
var obj = {
  name:"tll",
  age:18
}
Object.freeze(obj);
obj.name = "zhangsan";

console.log(obj); // obj{  name:"tll",age:18}
console.log(obj ===  Object.freeze(obj)); //true
```

## 五、Object.getOwnPropertyDescriptor()
5. `Object.getOwnPropertyDescriptor(obj,prop)`方法返回指定对象上自有属性对应的属性描述符。（自有属性指的是直接赋予该对象的属性，不需要从原型链上进行查找的属性）。

```bash
var obj = {
  name:"lucy"
}
Object.getOwnPropertyDescriptor(obj,"name");
/*
{
 configurable: true
 enumerable: true
 value: "lucy"
 writable: true
}
*/

```

`Object.getOwnPropertyDescriptors(obj)`方法用来获取一个对象的所有自身属性的描述符。

## 六、Object.getOwnPropertyNames()
6. `Object.getOwnPropertyNames()`方法返回一个由指定对象的所有`自身属性`的属性名（包括不可枚举属性但不包括Symbol值作为名称的属性）组成的数组。

```ruby
var obj = {a:1,b:2,c:3}
Object.getOwnPropertyNames(obj);
//["a","b","c"]

obj.__proto__.d = 4;
Object.getOwnPropertyNames(obj);
//["a","b","c"]
```

## 七、Object.keys()
7. `Object.keys()`方法会返回一个由一个给定对象的`自身可枚举`属性组成的数组。

```dart
var obj = {
  a:1,
  b:2,
  c:3
}
Object.keys(obj);
// ["a","b","c"]

var o = Object.create(obj);
o.name = "oooo";
Object.keys(o);
// ["name"]
```

这里有个重点需要注意一下就是`Object.getOwnPropertyNames()`，`Object.keys()`,`for-in`都是可以获取到对象的属性的，但是他们是有区别的这里简单总结一下。

`for in`:使用for..in循环时，返回的是`所有能够通过对象访问的、可枚举的属性`，既包括存在于实例中的属性，也包括存在于原型中的属性。  
`Object.keys()`:用于获取对象`自身所有的可枚举的属性值`，但`不包括原型中的属性`，然后返回一个由属性名组成的数组  
`Object.getOwnPropertyNames()`:方法返回对象的`所有自身属性的属性名`（`包括不可枚举的属性`）组成的数组，但不会获取原型链上的属性  
差异主要在属性`是否可枚举`，`是来自原型`，`还是实例`。

## 八、Object.getPrototypeOf()
8. `Object.getPrototypeOf()`方法返回指定对象的原型。

```dart
var protoobj = {};
var obj = Object.create(protoobj);
Object.getPrototypeOf(obj) === protoobj // true
Object.getPrototypeOf(obj) === obj.__proto__// true
```

注意：`Object.getPrototypeOf(Object)`不是`Object.prototype`。这个仔细想想，想不明白可以查看我之前文章[JavaScript原型理解](https://www.jianshu.com/p/3c5bbe55fa2c)

## 九、Object.setPrototypeOf()
9. `Object.setPrototypeOf()`方法设置一个指定的对象的原型为另一个对象或null。

```dart
var obj = {a:1}
Object.setPrototypeOf(obj,{b:2});
```
![[Pasted image 20230531172543.png]]
Object.setPrototypeOf()

这个方法作用实际上跟`obj.__proto__.b = 2`实际上是一样的，只不过由于规范原因，所以其实两者都可以使用。MDN上是这么说的：`Object.setPrototypeOf()是`ECMAScript 6最新草案中的方法，相对于 `Object.prototype.__proto__`，它被认为是修改对象原型更合适的方法。

## 十、Object.hasOwnProperty(propertyName)
hasOwnProperty(propertyName)方法 是用来检测属性是否为对象的自有属性，如果是，返回true，否者false; 参数propertyName指要检测的属性名；
用法：
`object.hasOwnProperty(propertyName) // true/false`

hasOwnProperty() 只会检查对象的自有属性，对象原形上的属性其不会检测；但是对于原型对象本身来说，这些原型上的属性又是原型对象的自有属性，所以原形对象也可以使用hasOwnProperty()检测自己的自有属性；

```js
let obj = {
    name:'张睿',
    age:18,
    eat:{
        eatname:'面条',
        water:{
            watername:'农夫山泉'
        }
    }
}
console.log(obj.hasOwnProperty('name')) //true
console.log(obj.hasOwnProperty('age'))  //true
console.log(obj.hasOwnProperty('eat'))  //true
console.log(obj.hasOwnProperty('eatname'))  //false
console.log(obj.hasOwnProperty('water'))  //false
console.log(obj.hasOwnProperty('watername'))  //false
console.log(obj.eat.hasOwnProperty('eatname'))  //true
console.log(obj.eat.hasOwnProperty('water'))  //true
console.log(obj.eat.hasOwnProperty('watername'))  //false
console.log(obj.eat.water.hasOwnProperty('watername'))  //true
```

链接：https://www.jianshu.com/p/3d0c39b179fd  
来源：简书  


