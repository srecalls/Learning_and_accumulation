

## 声明类型

```
let value1: any;
let value2: unknown;
let value3: never;
let value4: object;
let value5: Object;
let value6: Array<any>;
let value7: number[] | string[] | object[] | Array<any>[]; //等等
let value8: {};
//等等...
```

## 元组(Tuple)

不同类型组成的数组称为元组

```
const array: [string, number] = ['1', 1] //ok
const array: [string, number] = [1, 1]; //error

const array: [number, string] = [1, '1']; //ok 
const array: [number, string] = ['1', 1]; //error

const array: [number, string, Array<1 | 2>] = [2, '1', [1,2]] //ok
```

## Never与Unkown

#### never

`never` 类型表示那些永不存在的值的类型。

- never只能被never赋值
- never可以赋值给所有类型

```
function error():never {
    throw new Error('error')
} //ok

function getError():never{
    return error();
} //ok 

let neve: never;
let foo:any, bar: unknown;

neve = foo; //error
neve = bar; //error
neve = error(); //ok

----------

let value: any = neve; //ok 
let value1: unknown = neve; //ok 
let value2: never = neve; //ok 
let value3: string = neve; //ok 
let value4: number = neve; //ok
let value5: Array<any> = neve; //ok
let value6: Function = neve; //ok
```

#### unkown

`unknown` 类型是 `any` 类型对应的**安全类型**。

###### any

```
let value: any

value = true             // OK
value = 10               // OK
value = "Hello World"    // OK
value = []               // OK
value = {}               // OK
value = Math.random      // OK
value = null             // OK
value = undefined        // OK
value = new TypeError()  // OK
value = Symbol('name')   // OK

value.foo.bar            // OK
value.trim()             // OK
value()                  // OK
new value()              // OK
value[0][1]              // OK

--------------------------------------------------

let value1: unknown = value   // OK
let value2: any = value       // OK

let value3: boolean = value   // OK
let value4: number = value    // OK
let value5: string = value    // OK
let value6: object = value    // OK
let value7: any[] = value     // OK
```

###### unkown

```
let value: unknown

value = true             // OK
value = 10               // OK
value = "Hello World"    // OK
value = []               // OK
value = {}               // OK
value = Math.random      // OK
value = null             // OK
value = undefined        // OK
value = new TypeError()  // OK
value = Symbol('name')   // OK

value.foo.bar  // Error
value.trim()   // Error
value()        // Error
new value()    // Error
value[0][1]    // Error

--------------------------------------------------

let value1: unknown = value   // OK
let value2: any = value       // OK

let value3: boolean = value   // Error
let value4: number = value    // Error
let value5: string = value    // Error
let value6: object = value    // Error
let value7: any[] = value     // Error

```

## 类（Class）

#### 抽象类

抽象类作为其它派生类的基类使用，它们一般不会直接被实例化，和接口不太一样，抽象类可以包含成员的实现细节。

`abstract` 关键字是用于定义抽象类和在抽象类内部定义抽象方法。

```
abstract class Service {
    abstract getUrl(): string;
    get(): Promise<someType> {
        console.log('roaming the earch...');
    }
}

const service = new Service() // Error, 无法创建抽象类实例
```

通常我们需要创建子类继承抽象类，将抽象类中的抽象方法一一实现，这样在大型项目中可以很好的约束子类的实现。

```
class GetUserInfoService extends Service {
    getUrl(): string{
        return '/api/to/getUserInfo'
    }
}

const service = new GetUserInfoService();
service.get(); 
```

## 函数（Function）

#### 参数

```
//可选参数

function test(a:string, b?:number) {}

test(a); // ok
test(a,b); // ok

//默认参数

function test(a:string = 1) {}
test(); // ok
test(2); // ok

//剩余参数（rest）
function test(...arg) {}
test(1); //ok
test(1,2);//ok
test(1,2,3);//ok
。。。
```

#### 重载(overload)

函数重载是指函数根据传入不同的参数，返回不同类型的数据。

它的意义在于让你清晰的知道传入不同的参数得到不同的结果，如果传入的参数不同，但是得到相同类型的数据，那就不需要使用函数重载。

###### 重载签名与实现签名

```
//重载签名
function test(param1:string): void; //ok
function test(param1:number): number; //ok

//实现签名
function test(param1: string| number) {
    if(typeof param1 === 'string') {
        return;
    }
    if(typeof param1 === 'number') {
        return 1;
    }
}

```

重载与实现必须一致

```
function fn(x: string): void;
function fn() {
  // ...
}
fn(); //error ,必须传一个参数
```

## Typescript特殊类型与机制

#### 字面量类型

```
const value: 'content' = 'content'; //ok，只能为content
const value: '1' | '2';
const value: 1 | 2 | 3 | 4 | 5 | 6
const value: true | false;
```

#### 类型推断

```
let x = 3             // let x: number
let y = 'hello world' // let y: string
let z                 // let z: any

// return type number
function plus(a:number, b:10) {
  return a + b
}

const target = {
  name: 100, // number
  name2: 'hello world' //string
}
obj.name2 = 15 // error


let value = [1, '1', null]; // (number | string)[]
```

#### 类型断言

```
type Value = {
    type: string;
}
let value = {} as Value; //as关键字

let value = <Value>{}; //前置收尾标签

//如果编译器不能够去除 null 或 undefined，可以使用非空断言 ! 手动去除
function value(name: string | null): string {
  return name!.charAt(0); //！
}

let value = {} as any as Value // 多重断言
```

#### 类型保护

可以通过 `typeof`、`instanceof`、`in` 和 `字面量类型` 将代码分割成范围更小的代码块，在这一小块中，变量的类型是确定的

```
function value(arg: string| number) {
    if(typeof arg === 'number') arg.toFixed(2);
    //instanceof 与 in同理
}


//字面量类型保护
type A = {
    yes: true
    run1: Function
}

type B = {
    yes: false,
    run2: Function
}

function value(arg: A | B){
    if(arg.yes === true) {
        arg.run1();
    } else {
        arg.run2();
    }
}
```

###### 类型谓词 `is`

这里可以注意到我们不得不多次使用类型断言。 假若我们一旦检查过类型，就能在之后的每个分支里清楚地知道 `A`或者`B` 的类型的话就好了。

TypeScript里的 _类型保护_机制让它成为了现实。 类型保护就是一些表达式，它们会在运行时检查以确保在某个作用域里的类型。 要定义一个类型保护，我们只要简单地定义一个函数，它的返回值是一个 _类型谓词_：

```
type Dog = {
    buk: Function
}

type Cat = {
    Miao:Function
}


function getPet(): Cat | Dog {
    return {} as Cat | {} as Dog;
}

let pet = getPet();
// 每一个成员访问都会报错
if (pet.buk) { 
    pet.buk();
}else if (pet.Miao) {
    pet.Miao();
}
 
//类型转换 ok
if ((<Cat>pet).Miao) {
    (<Cat>pet).Miao();
}else {
    (<Dog>pet).buk();
}

// is自定义类型保护 ok

function isCat(pet: Cat | Dog): pet is Cat {
    return (<Cat>pet).Miao !== undefined;
}

if (isCat(pet)) {
    pet.Miao();
} else {
    pet.buk();
}
```

## 链接

[typescript官方文档](https://www.typescriptlang.org/docs/)

下一篇：[typescript类型之范型与类型兼容性](https://xiaomi.f.mioffice.cn/docs/dock46fZMfIH5xZg9ur248tG3Mb)