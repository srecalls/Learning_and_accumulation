## 1.charAt()方法
charAt() 方法可返回字符串中指定位置的字符。

```js
let str = "Hello";
let s = str.charAt(1);
console.log(s);//e
```

语法：
```js
string.charAt(index)
```
index 必需值。表示字符串中某个位置的数字，即字符在字符串中的位置。

## 2.concat() 方法
concat() 方法用于连接两个或多个字符串。
该方法没有改变原有字符串，但是会返回连接两个或多个字符串新字符串

```js
let str = "Hello";
let str2 = "World";
let s = str.concat(str2);
console.log(s); //HelloWorld
```

语法：
```js
string.concat(string1, string2, …, stringX)
```
string1, string2, …, stringX 必需值。将被连接为一个字符串的一个或多个字符串对象。

## 3.indexOf() 方法
indexOf() 方法可返回某个指定的字符串值在字符串中首次出现的位置。
如果没有找到匹配的字符串则返回 -1。

```js
let str = "Hello";
let s = str.indexOf("e");
console.log(s); //1
```

语法：
```js
string.indexOf(searchvalue,start)
```
searchvalue 必需值。规定需检索的字符串值。
start 可选的整数参数。规定在字符串中开始检索的位置。它的合法取值是 0 到 string Object.length - 1。如省略该参数，则将从字符串的首字符开始检索。

## 4.includes() 方法
includes() 方法用于判断字符串是否包含指定的子字符串。

```js
let str = "Hello";
let s = str.includes("e");
console.log(s); //true
```

语法：
```js
string.includes(searchvalue, start)
```
searchvalue 必需值，要查找的字符串。
start 可选值，设置从那个位置开始查找，默认为 0。

## 5.match() 方法
match() 方法可在字符串内检索指定的值，或找到一个或多个正则表达式的匹配。

```js
let str = "Hello";
let s = str.match(/l/g);
console.log(s); //[ 'l', 'l' ]
```

语法：
```js
string.match(regexp)
```
regexp 必需。规定要匹配的模式的 RegExp 对象。如果该参数不是 RegExp 对象，则需要首先把它传递给 RegExp 构造函数，将其转换为 RegExp 对象。

## 6.repeat() 方法
repeat() 方法字符串复制指定次数。

```js
let str = "Hello";
let s = str.repeat(2);
console.log(s); //HelloHello
```

语法：
```js
string.repeat(count)
```
count 必需，设置要复制的次数。

## 7.replace() 方法
replace() 方法用于在字符串中用一些字符替换另一些字符，或替换一个与正则表达式匹配的子串。

```js
let str = "Hello";
let s = str.replace("l", "o");
console.log(s); //Heolo
```

语法：
```js
string.replace(searchvalue,newvalue)
```
searchvalue 必须。规定子字符串或要替换的模式的 RegExp 对象。
请注意，如果该值是一个字符串，则将它作为要检索的直接量文本模式，而不是首先被转换为 RegExp 对象。
newvalue 必需。一个字符串值。规定了替换文本或生成替换文本的函数。

## 8.replaceAll()方法
replaceAll() 方法用于在字符串中用一些字符替换另一些字符，或替换一个与正则表达式匹配的子串，该函数会替换所有匹配到的子字符串。

```js
let str = "Hello";
let s = str.replaceAll("l", "o");
console.log(s); //Heooo
```

语法同replace方法相同

## 9.search() 方法
search() 方法用于检索字符串中指定的子字符串，或检索与正则表达式相匹配的子字符串。返回与指定查找的字符串或者正则表达式相匹配的 String 对象起始位置。

```js
let str = "Hello";
let s = str.search("lo");
console.log(s); //3
```

语法：
```js
string.search(searchvalue)
```
searchvalue 必须。查找的字符串或者正则表达式。

## 10.slice() 方法
slice(start, end) 方法可提取字符串的某个部分，并以新的字符串返回被提取的部分。

```js
let str = "Hello";
let s = str.slice(1, 2);
console.log(s); //e
```

语法:
```js
string.slice(start,end)
```
start 必须。 要抽取的片断的起始下标，第一个字符位置为 0。如果为负数，则从尾部开始截取。
end 可选。 紧接着要截取的片段结尾的下标。若未指定此参数，则要提取的子串包括 start 到原字符串结尾的字符串。如果该参数是负数，那么它规定的是从字符串的尾部开始算起的位置。slice(-2) 表示提取原数组中的倒数第二个元素到最后一个元素（包含最后一个元素）。

## 11.split() 方法
split() 方法用于把一个字符串分割成字符串数组。

```js
let str = "Hello";
let s = str.split("e");
console.log(str); //Hello
console.log(s); //[ 'H', 'llo' ]
```

语法：
```js
string.split(separator,limit
```
separator 可选。字符串或正则表达式，从该参数指定的地方分割 string Object。
limit 可选。该参数可指定返回的数组的最大长度。如果设置了该参数，返回的子串不会多于这个参数指定的数组。如果没有设置该参数，整个字符串都会被分割，不考虑它的长度。

## 12.substring() 方法
substring() 方法用于提取字符串中介于两个指定下标之间的字符。

```js
let str = "Hello";
let s = str.substring(1, 3);
console.log(str); //Hello
console.log(s); //el
```

语法：
```js
string.substring(from, to)
```
from 必需。一个非负的整数，规定要提取的子串的第一个字符在 string Object 中的位置。
to 可选。一个非负的整数，比要提取的子串的最后一个字符在 string Object 中的位置多 1。
如果省略该参数，那么返回的子串会一直到字符串的结尾。

## 13.toLowerCase()和toUpperCase()方法
toLowerCase() 方法用于把字符串转换为小写。
toUpperCase() 方法用于把字符串转换为大写。

```js
let str = "Hello";
let s = str.toLowerCase();
let s2 = str.toUpperCase();
console.log(str); //Hello
console.log(s); //hello
console.log(s2);//HELLO
```

## 14.trim() 方法
trim() 方法用于删除字符串的头尾空白符，空白符包括：空格、制表符 tab、换行符等其他空白符等。

```js
let str = "    Hello   ";
let s = str.trim();
console.log(str); //    Hello
console.log(s); //Hello
```

