typescript类型之范型与类型兼容性

## 范型(Generic)

泛型在传统的面向对象语言中极为常见，可以使用泛型来创建可重用的组件，一个组件可以支持多种类型的数据。

**通俗来讲**：泛型是指在定义函数、接口或者类时，未指定其参数类型，只有在运行时传入才能确定。那么此时的参数类型就是一个变量，通常用大写字母 `T` 来表示，当然你也可以使用其他字符，如：`U`、`K`等。

**语法**：在函数名、接口名或者类名添加后缀 `<T>`：

#### 简单范型

```
function test(name: string) : string {
    //逻辑A
    //逻辑B
    return name;
}

function test(name: number) : number {
    //逻辑A
    //逻辑B
    return name;
}

//类型不同需要运行时确定类型
function test<T>(name: T): T {
    //逻辑A
    //逻辑B
    return name;
}

//多个类型

function test<T, U>(name: T, arg: U): T & U {}
```

#### 范型参数默认类型

```
function test<T = string>(name: T): T {}

test(); // return type: string
```

#### 泛型类型与泛型接口

```
//范型类型
type TestType = {<T>(name: T): T};
type TestType = <T>(name: T) => T;

//范型接口(两者有什么区别？)
interface TestType<T> {
    (name: T): T;
}

interface TestType {
    <T>(name: T): T
}
```

#### 泛型类

```
class Test<T, U> {
    name: T[] = [];
    
    props: {[key: string]: T & U};
    
    add(name: T ): U{
        let value: U;
        return value;
    }
    
}
```

#### 范型约束

```
interface A {
    type: number;
    propA: string;
}

interface B {
    type: number;
    propB: string
}

function Test<T extends A & B>(name: T): string{
    return name.type + "test";
}

```

## 类型兼容性

类型兼容性用于确定一个类型是否能赋值给其他类型。

TypeScript 的类型检查机制都是为了让开发者在编译阶段就可以直观的发现代码书写问题，养成良好的代码规范从而避免很多低级错误。

#### 数据结构兼容性

```
type User = { //将type与interface也一样
    name: string;
    sex: string;
}

const tom = {
    name: '那么多',
    sex: '难',
    ride: ()=>{}
}

const marry = {
    sex: '旅',
    run: ()=>{}
}

const user: User = tom; //ok
const user1: User = marry; // error


```

#### 函数兼容性

参数

```
type Func = (name: string) => number;

let test1 = (): number => {
    return 1
}

let test2 = (n: string): number => {
    return 1
}

let test3 = (n: string, m: number): number  => {
    return 1
}

let test4 = (n:string | number, m?: number): number =>  {
    return 1;
}
const func1: Func = test1; //ok
const func2: Func = test2; // ok
const func3: Func = test3; // error
const func4: Func = test4; // ok

test1 = test2; // error
test2 = test1; // ok
test3 = test4; // ok
test4 = test3; // error
```

函数返回

```
let a = () => ({name: '2'})
let b = () => ({name: '3', sex: '旅'})

a = b // ok
b = a // rrror

let x : () => void
let y = () => '1'

x = y // ok
y = x; // error
```

#### 枚举的类型兼容性

```
enum Status {
  Pending,
  Resolved,
  Rejected
}

let current = Status.Pending
let num = 0

//与数字的兼容性
current = num //ok
num = current // ok

enum tet {
    N = 'Normal'
}

---------------------------------------

let n = tet.N;
let str = 'Normal';
//与字符串的兼容性
n = str; // error
str = n; // ok

---------------------------------------

enum Status { Pending, Resolved, Rejected }
enum Color { Red, Blue, Green }

//枚举与枚举的兼容性
let current = Status.Pending
current = Color.Red // Error

```

#### 类的类型兼容性

类与对象字面量和接口的兼容性非常类似，但是类分实例部分和静态部分。

**比较两个类类型数据时，只有实例成员会被比较，静态成员和构造函数不会比较。**

```
class Animal {
  feet!: number
  constructor(name: string, numFeet: number) { }
}

class Size {
  feet!: number
  constructor(numFeet: number) { }
}

let a: Animal
let s: Size

a = s!  // OK
s = a  // OK
```

**代码解释：** 类 Animal 和类 Size 有相同的实例成员 `feat` 属性，且类型相同，构造函数参数虽然不同，但构造函数不参与两个类类型比较，所以最后两行可以相互赋值。

**类的私有成员和受保护成员会影响兼容性。** 允许子类赋值给父类，但是不能赋值给其它有同样类型的类。

```
class Animal {
  protected feet!: number
  constructor(name: string, numFeet: number) { }
}

class Dog extends Animal {}

let a: Animal
let d: Dog

a = d // OK
d = a // OK

class Size {
  feet!: number
  constructor(numFeet: number) { }
}

let s: Size

a = s! // Error
```

#### 泛型的类型兼容性

泛型的类型兼容性根据其是否被成员使用而不同。先看一段代码示例

```
interface Empty<T> {}

let x: Empty<number>
let y: Empty<string>

x = y // OK
```

上面代码里，x 和 y 是兼容的，因为它们的结构使用类型参数时并没有什么不同。但是当泛型被成员使用时

```
interface NotEmpty<T> {
  data: T
}
let x: NotEmpty<number>
let y: NotEmpty<string>

x = y! // Error
```

**代码解释：** 因为第 4 行，泛型参数是 number 类型，第 5 行，泛型参数是 string 类型，所以最后一行赋值失败。

如果没有指定泛型类型的泛型参数，会把所有泛型参数当成 any 类型比较:

```
let identity = function<T>(x: T): void {
  // ...
}

let reverse = function<U>(y: U): void {
  // ...
}

identity = reverse // OK
```

## 链接

[typescript官方文档](https://www.typescriptlang.org/docs/)

下一篇：[typescript教程之进阶](https://xiaomi.f.mioffice.cn/docs/dock45wwO3WQlfb9ZkYWv0w8sZc#)