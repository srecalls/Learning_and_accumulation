```ts
继承方法有2种
1. 使用extends
2. 使用implements （implement · n. 工具;器具;)
说明： extends是本来js就有的，implements是ts额外提供的

1. 使用extends
class Animal {
	move() {
	
	}
}
class Dog extends Animal {
	back() {
	}
}
const dog = new Dog()
dog.move()

子类Dog继承父类Animal，Dog的实例对象就拥有父类Animal和子类Dog的所有属性和方法。注意，不只有方法，该属性和方法都有。

2. implements
interface Singlable {
	sing(): void
}
class Person implements Singable {
	sing() {
	
	}
}
注意，implements是让class实现接口（interface）
Person类实现接口Singable，意味着Person类种必须提供Singable接口种指定的所有方法和属性。就是Singable里有什么，Person类种就需要有什么
```
# class的继承方法
![[Pasted image 20230327161834.png]]
1.继承父类 extends   一个类和一个类
![[Pasted image 20230327161903.png]]
2.继承接口 implements   一个类和一个接口
![[Pasted image 20230327161913.png]]
![[Pasted image 20230327162406.png]]