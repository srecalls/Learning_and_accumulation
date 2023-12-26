# 接口继承 extends
作用：**如果有两个接口之间有相同的属性或方法，可以将公共的属性或方法抽离出来，通过继承实现复用**
```ts
interface Point2D {
	x: number;
	y: number;
}
interface Point3D {
	x: number;
	y: number; 
	z: number,
}

修改成
interface Point2D {
	x: number;
	y: number;
}

interface Point3D extends Point2D {
	z: number
}
```

**接口继承**
接口（interface）在 TypeScript 中支持继承关系。您可以使用 `extends` 关键字来扩展一个接口，从而继承其属性和方法。下面是一个使用接口继承的示例：

```ts
interface Animal {
  name: string;
  eat(): void;
}

interface Dog extends Animal {
  bark(): void;
}

const dog: Dog = {
  name: 'Buddy',
  eat() {
    console.log('Eating...');
  },
  bark() {
    console.log('Woof!');
  },
};

dog.eat();  // 输出: "Eating..."
dog.bark(); // 输出: "Woof!"
console.log(dog.name); // 输出: "Buddy"
```
在上述示例中，我们定义了一个 `Animal` 接口，它有一个 `name` 属性和一个 `eat` 方法。
然后，我们使用 `extends` 关键字创建了一个 `Dog` 接口，它继承自 `Animal` 接口，并且额外添加了一个 `bark` 方法。
接着，我们创建了一个 `dog` 对象，它符合 `Dog` 接口的定义。该对象拥有继承自 `Animal` 接口的 `name` 属性和 `eat` 方法，以及 `Dog` 接口的 `bark` 方法。
最后，我们通过调用 `dog` 对象的方法和访问其属性，来展示继承关系的使用。
通过接口的继承，可以实现代码的重用和组合，同时保持类型检查的严谨性。

![[Pasted image 20230327012547.png]]
![[Pasted image 20230327012753.png]]