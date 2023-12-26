**作用：可以控制class的方法或属性对于class外的代码是否可见**
```ts
可见性修饰符有
1. public（公有的）
2. protected（受保护的）
3. private（私有的）
注意，属性和方法都可以

跟c++的类很像
4. 除了可见性修饰符，常见修饰符
readonly（只读修饰符）注意：只能修饰属性，不能修饰方法
！！接口或者{}表示对对象类型，也可以用readonly的

1.public： 表示公有的，共有成员可以被任何地方访问，默认可见性。（类、子类与实例对象都行）
- 可以在类属性或方法前面添加public关键字，来修饰该属性或方法是共有的。
- public是默认可见性。可以直接省略
class Animal {
	public move() {
	
	}
}

2. protected 表示受保护的，仅对声明所在类和子类种（非实例对象）可见。就是类内可以，但是实例对象那不行。
class Animal {
	public move() {
	
	}
}
class Dog extends Animal {
	bark() {
		this.move()
	}
}
3. private: 表示私有的，只在当前类中可见。对实例对象以及子类都是不可见的（本类才可以，子类、实例对象不行）

4.readonly：表示只读，用来防止在构造函数之外对属性进行赋值（只有在本类的构造函数才能对属性值进行修改）
class Person {
	readonly age: number = 18
	constructor(age: number) {
		this.age = age
	}
}
```

当在 TypeScript 中定义对象类型时，可以使用接口（interface）或字面量对象类型（{}）来表示，并且可以使用 `readonly` 修饰符来指定只读属性。下面是一个使用接口和只读属性的示例：

```ts
interface Person {
  readonly name: string;
  age: number;
}

const person: Person = {
  name: 'John',
  age: 25,
};

// 以下代码会产生编译错误，因为 name 属性是只读的，无法修改
// person.name = 'Jane';

console.log(person.name);  // 输出: "John"
console.log(person.age);   // 输出: 25
```

在上述示例中，我们定义了一个名为 `Person` 的接口，其中包含了 `name` 属性和 `age` 属性。通过在 `name` 属性前面添加 `readonly` 修饰符，我们将其指定为只读属性。

然后，我们创建了一个名为 `person` 的对象，该对象符合 `Person` 接口的定义。由于 `name` 属性是只读的，我们无法在后续代码中修改它。

最后，我们通过 `console.log` 输出了 `person` 对象的 `name` 和 `age` 属性的值。

请注意，使用 `readonly` 修饰符只能在属性声明处使用，并且一旦属性被声明为只读，就无法在后续代码中修改它们的值。这可以提供更强的类型安全性，防止意外的属性修改。
# class类的可见修饰符
1.public
![[Pasted image 20230327163122.png]]
![[Pasted image 20230327163140.png]]
2.protected
![[Pasted image 20230327163032.png]]
![[Pasted image 20230327163111.png]]
3.private
![[Pasted image 20230327163208.png]]
![[Pasted image 20230327163227.png]]
4.readonly
![[Pasted image 20230327163436.png]]
![[Pasted image 20230327163547.png]]
![[Pasted image 20230327163612.png]]