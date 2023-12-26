# 泛型  \<Type>
作用： **保证类型安全的前提下，让函数等与多种类型一起工作，实现复用。常用与： 函数、接口、class中**



原因: 
```ts
function id(value: number): number { return value } // 只能用于number类型，无法用于其他类型
function id(value: any): any { return value } // 是去TS的类型保护，类型不安全

function id<Type>(value: Type): Type { return value }

1. Type可以是任何合法的值
2. 在<>简括好中添加类型变量
3. 类型变量Type，特殊类型的变量，它只处理类型，不处理值
function id<Type, Props>(value: Type): Props { return value }
```

当使用泛型（generics）时，可以在函数、类或接口中定义通用的类型参数，以实现对多种类型的复用，并在保持类型安全的同时提高代码的灵活性。以下是一个示例，展示了如何使用泛型来实现函数的复用：

```ts
function printArray<T>(arr: T[]): void {
  for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
  }
}

const numbers = [1, 2, 3, 4, 5];
const names = ['Alice', 'Bob', 'Charlie'];

printArray(numbers); // 打印数组中的每个数字
printArray(names);   // 打印数组中的每个字符串
```

在上述示例中，我们定义了一个名为 `printArray` 的函数，它接受一个类型为 `T` 的数组作为参数，并遍历打印数组中的每个元素。

通过在函数名称后面使用 `<T>`，我们将 `T` 声明为一个类型参数。这样，我们可以在函数的参数、返回值或函数体中使用该类型参数 `T`。

在函数调用时，我们可以传入不同类型的数组作为参数，例如 `numbers` 数组和 `names` 数组。由于 `printArray` 函数使用了泛型类型参数 `T`，它可以与多种类型的数组一起工作，并实现代码的复用。

通过使用泛型，我们可以编写更通用、灵活和可复用的代码，而无需为每种类型编写重复的函数或逻辑。这提高了代码的可维护性和可扩展性，并在保持类型安全性的同时提供了更大的灵活性。

![[Pasted image 20230328012628.png]]
![[Pasted image 20230328013130.png]]
![[Pasted image 20230328013321.png]]
![[Pasted image 20230328013402.png]]
