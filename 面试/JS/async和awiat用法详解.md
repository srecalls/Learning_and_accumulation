当涉及到异步操作时，JavaScript 中的 `async` 和 `await` 是用于处理异步代码的关键字。它们提供了一种更简洁、更易读的方式来编写和处理异步任务。

- `async`：`async` 关键字用于定义一个函数，表示该函数是一个异步函数。异步函数内部可以包含 `await` 关键字，用于暂停函数的执行，等待一个 Promise 对象的解析结果。

- `await`：`await` 关键字只能在异步函数内部使用。它用于等待一个 Promise 对象的解析结果。当遇到 `await` 关键字时，代码会暂停执行，直到 Promise 对象状态变为已解析（resolved）或已拒绝（rejected），然后继续执行后续代码。

下面是一些常见的用法和易错案例，以及一些特殊案例的说明：

**常见用法**：


1. 异步函数声明：
   ```javascript
   async function fetchData() {
     // 异步操作
     // 使用 await 等待 Promise 对象的解析结果
     // 返回值将被包装成一个已解析的 Promise 对象
     return await someAsyncOperation();
   }
   ```
1. 调用异步函数：
   ```javascript
   async function main() {
     try {
       const result = await fetchData();
       console.log(result);
     } catch (error) {
       console.error(error);
     }
   }
   main();
   ```

**易错案例**：

1. 忘记在异步函数前声明 `async` 关键字：

   ```javascript
   // 错误示例
   function fetchData() {
     // ...
   }

   async function main() {
     try {
       const result = await fetchData(); // 抛出错误：fetchData is not a function
       console.log(result);
     } catch (error) {
       console.error(error);
     }
   }
   main();
   ```

   正确示例：

   ```javascript
   // 正确示例
   async function fetchData() {
     // ...
   }

   async function main() {
     try {
       const result = await fetchData();
       console.log(result);
     } catch (error) {
       console.error(error);
     }
   }
   main();
   ```

1. 在非异步函数中使用 `await`：

   ```javascript
   // 错误示例
   function fetchData() {
     // ...
   }

   function main() {
     try {
       const result = await fetchData(); // 抛出错误：SyntaxError: await is only valid in async function
       console.log(result);
     } catch (error) {
       console.error(error);
     }
   }
   main();
   ```

   正确示例：

   ```javascript
   // 正确示例
   function fetchData() {
     // ...
   }

   async function main() {
     try {
       const result = await fetchData();
       console.log(result);
     } catch (error) {
       console.error(error);
     }
   }
   main();
   ```

**特殊案例**：

1. 并行执行多个异步任务：

   ```javascript
   async function fetchMultipleData() {
     const promise1 = someAsyncOperation1();
     const promise2 = someAsyncOperation2();
     const promise3 = someAsyncOperation3();

     // 使用 Promise.all 等待所有 Promise 对象解析完毕
     const [result1, result2, result3] = await Promise.all([promise1, promise2, promise3]);

     return [result1, result2, result3];
   }
   ```

1. `await` 后面不是 Promise 对象：

   ```javascript
   async function main() {
     const result = await 123; // 立即解析为一个已解析的 Promise 对象，相当于 Promise.resolve(123)
     console.log(result); // 输出 123
   }
   main();
   ```

`async` 和 `await` 提供了一种更简洁的方式来处理异步代码，使得代码更易读和维护。它们广泛应用于处理异步请求、调用 API、读取文件等涉及等待异步结果的场景。然而，需要注意的是，在使用 `await` 时必须在异步函数内部，并且在调用异步函数时使用 `await` 或 `.then()`方法来等待其解析结果。此外，`await` 关键字只能在异步函数内部使用。