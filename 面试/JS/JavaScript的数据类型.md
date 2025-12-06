# JavaScript的数据类型

1.  数字类型 (Number)：表示数值，例如：`42`、`3.1415`。
2.  字符串类型 (String)：表示文本，例如：`"hello world"`、`'JavaScript'`。
3.  布尔类型 (Boolean)：表示 true 或 false 值。
4.  空值类型 (Null)：表示空值或无值，只有一个值：`null`。
5.  未定义类型 (Undefined)：表示未定义的值，只有一个值：`undefined`。
6.  对象类型 (Object)：表示复杂数据结构，例如：`{name: "John", age: 30}`、`[1, 2, 3]`。
7.  函数类型 (Function)：表示可调用的代码块，例如：`function myFunction() {...}`。
8.  符号类型 (Symbol)：表示唯一的标识符，ES6 新增，用于对象属性的键。

JavaScript数据类型分为引用数据类型和基本数据类型（Primitive Data Types）。

JavaScript的基本数据类型包括：

-   数值（Number）：整数和浮点数。
-   字符串（String）：文本字符串。
-   布尔值（Boolean）：true 或 false。
-   undefined：表示未定义的值。
-   null：表示空对象指针。
-   Symbol：ES6中新增的一种数据类型，表示独一无二的值。[[Symbol的特性]] [[Symbol的基本使用]]

引用数据类型包括：

-   对象（Object）：表示一组相关属性和方法的集合。
-   数组（Array）：表示一个有序的值列表。
-   函数（Function）：表示可执行的代码块，可以接受参数和返回值。
-   日期（Date）：表示日期和时间的对象。
-   正则表达式（RegExp）：表示正则表达式的对象。
-   等等。

基本数据类型和引用数据类型
还是 原始类型 + 对象类型
## 🎯 结论：第二种说法（7 种原始类型 + 1 种对象类型）**更准确、更符合现代 JavaScript 规范**。

---

## 详细对比和解释

### 1. 原始类型 vs. 引用类型 (基本数据类型 vs. 引用数据类型)

这个二分法是 JavaScript 中最核心和最常用的分类方式，它主要关注**数据在内存中的存储方式**和**变量之间的赋值方式**。

|**类别**|**7 种原始类型 (Primitive Data Types)**|**引用类型 (Reference Type)**|
|---|---|---|
|**包含**|`Number`, `String`, `Boolean`, `undefined`, `null`, **`Symbol`**, **`BigInt`**|`Object` (包括 `Array`, `Function`, `Date`, `RegExp` 等)|
|**存储**|值直接存储在 **栈 (Stack)** 中。|实际对象存储在 **堆 (Heap)** 中，栈中存储指向堆的 **地址/指针**。|
|**赋值**|赋值是值的复制。|赋值是地址/指针的复制。|

**因此，您的第二种说法是基于这个核心分类的现代版本。**

### 2. 对您提供的两种说法的分析

#### 🔹 您的第一种说法分析 (包含 8 种类型，但分类不严谨)

1. **数字 (Number)、字符串 (String)、布尔 (Boolean)、空值 (Null)、未定义 (Undefined)、符号 (Symbol)**：这些都是原始类型，但缺少了 `BigInt`。
    
2. **对象 (Object)**：广义的引用类型。
    
3. **函数 (Function)**：`Function` 在技术上是 `Object` 的一个特殊子类型（`typeof` 运算符会返回 `"function"`），但在分类时将其独立列出，这在某些教学场合很常见，但**不属于最底层的规范分类**。
    
4. **引用数据类型部分**：将 `Array`、`Date`、`RegExp` 等和 `Object` 并列，这也是**不准确**的，因为它们本质上都属于 `Object`。
    

#### 🔹 您的第二种说法分析 (最准确、最规范)

- **原始类型 (Primitive Data Types)**：`Number`、`String`、`Boolean`、`Symbol`、**`BigInt`**、`undefined`、`null` **(7 种)**。
    
- **对象类型 (Object Type)**：`Object`。
    

**这是当前 ECMAScript 规范定义的数据类型分类。**

> **注意：** 在早期 ES5 或更早的版本中，确实只有 5 种原始类型 (`Number`, `String`, `Boolean`, `undefined`, `null`)。随着 JavaScript 的发展，ES6 引入了 `Symbol`，ES2020 引入了 `BigInt`，因此现在是 **7 种原始类型**。

### 3. `typeof` 运算符的特殊情况

虽然规范上有 7 种原始类型，但 `typeof` 运算符在检查类型时，对 `null` 和 `Function` 有特殊的返回值：

|**表达式**|**返回值 (结果)**|**实际类型 (规范)**|**备注**|
|---|---|---|---|
|`typeof 42`|`"number"`|原始类型||
|`typeof "hi"`|`"string"`|原始类型||
|`typeof true`|`"boolean"`|原始类型||
|`typeof Symbol()`|`"symbol"`|原始类型||
|`typeof 1n`|`"bigint"`|原始类型||
|`typeof undefined`|`"undefined"`|原始类型||
|`typeof null`|**`"object"`**|**原始类型**|这是一个历史遗留的 Bug，但不会修复。|
|`typeof {}`|`"object"`|引用类型||
|`typeof []`|`"object"`|引用类型||
|`typeof function() {}`|**`"function"`**|**引用类型 (Object)**|尽管是对象，但 `typeof` 返回 `"function"`。|

---

**总结：**

- **底层规范分类：** 7 种原始类型 (`Number`, `String`, `Boolean`, `Symbol`, `BigInt`, `undefined`, `null`) + `Object` (引用类型)。
    
- **实用分类/内存分类：** 基本数据类型 (7种原始类型) vs. 引用数据类型 (`Object` 及所有子类)。
    

因此，建议您采纳 **7 种原始类型 + 1 种对象类型** 的分类方式。

您想进一步了解 **BigInt** 或 **Symbol** 这两种新的原始类型吗？