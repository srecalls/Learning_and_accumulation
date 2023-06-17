Promise可以实现链式调用，既then之后可以接着使用then方法
```js
let p = new Promise((resolve, reject) => {
    resolve('a')
})
p.then((value) => {
    return value
},  (reason) => {
    return reason
}).then((value) => {
    console.log(value) //a
})
```

分析
- then的方法执行后返回一个Promise对象
- then中onFulfilled或onRejected执行的结果会传入下一个Promise中
	- 如果then中onFulfilled或onRejected执行的结果为普通值，则作为下一个promise中的resolve执行
	- 如果为Promise,则令其then执行，直到为普通值，讲结果传入下一个Promise中的resolve或reject
	- 如果出错，则 reject




## Promise对象里的resolve函数里如果是也是一个Promise对象，会对原本的Promise对象的状态进行更改吗
是的，如果在Promise对象的`resolve()`函数中返回另一个Promise对象，它会影响原来的Promise对象的状态和值。

具体来说，如果在Promise对象的`resolve()`函数中返回一个Promise对象，这个新的Promise对象的状态和值会传递到原来的Promise对象中。如果新的Promise对象状态为`resolved`，那么原来的Promise对象也会变为`resolved`状态，并将新Promise对象的值作为参数传递给原来的Promise对象的`.then()`方法；如果新的Promise对象状态为`rejected`，那么原来的Promise对象也会变为`rejected`状态，并将新Promise对象的错误对象作为参数传递给原来的Promise对象的`.catch()`方法。

下面是一个例子，说明在Promise对象的`resolve()`函数中返回另一个Promise对象的情况：

```javascript
const subPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Sub Promise Resolved");
    }, 500);
});

const mainPromise = new Promise((resolve, reject) => {
    resolve(subPromise);
});

mainPromise.then((data) => {
    console.log("Main Promise Resolved with: ", data);
}).catch((error) => {
    console.error("Main Promise Rejected with: ", error);
});
```

在这个例子中，我们创建了一个名为`subPromise`的Promise对象，它会在500毫秒后被resolved。然后，我们创建了一个名为`mainPromise`的Promise对象，并在它的`resolve()`函数中返回了`subPromise`。最后，我们使用`.then()`方法和`.catch()`方法来获取`mainPromise`的结果。

由于在`mainPromise`的`resolve()`函数中返回了`subPromise`，因此`mainPromise`的状态和值会受到`subPromise`的影响。当`subPromise`被resolved时，`mainPromise`也会被resolved，并将`subPromise`的值作为参数传递给`.then()`方法。因此，在这个例子中，当`subPromise`被resolved时，控制台会输出`Main Promise Resolved with: Sub Promise Resolved`。

## 不一定要异步
不一定需要使用`setTimeout()`函数来解决Promise对象的状态传递问题。实际上，如果`subPromise`对象的状态是同步可知的，我们可以直接将它返回给`mainPromise`对象的`resolve()`函数，而无需使用`setTimeout()`函数。

例如，假设我们的`subPromise`对象的状态是同步可知的，可以直接在`subPromise`对象的`executor`函数中返回一个resolved状态的Promise对象，如下所示：

```javascript
const subPromise = new Promise((resolve, reject) => {
    resolve("Sub Promise Resolved");
});

const mainPromise = new Promise((resolve, reject) => {
    resolve(subPromise);
});

mainPromise.then((data) => {
    console.log("Main Promise Resolved with: ", data);
}).catch((error) => {
    console.error("Main Promise Rejected with: ", error);
});
```

在这个例子中，我们创建了一个名为`subPromise`的Promise对象，并在它的`executor`函数中直接调用`resolve()`函数来设置Promise对象的状态为resolved，并将响应数据作为参数传递给`resolve()`函数。然后，我们创建了一个名为`mainPromise`的Promise对象，并在它的`resolve()`函数中返回了`subPromise`。最后，我们使用`.then()`方法和`.catch()`方法来获取`mainPromise`的结果。

由于`subPromise`对象的状态是同步可知的，并且在创建`mainPromise`对象时已经被resolved，因此我们可以直接将它返回给`mainPromise`对象的`resolve()`函数，而无需使用`setTimeout()`函数。在这个例子中，控制台会输出`Main Promise Resolved with: Sub Promise Resolved`。

需要注意的是，如果`subPromise`对象的状态是异步可知的，例如需要通过网络请求或文件读取等操作获取，那么我们就需要使用`setTimeout()`函数或其他异步操作来模拟异步获取结果的情况。

## 为什么会这样，为什么resolve里是一个promise的话，哪个promise的值会被传递给原来的promise
当在Promise对象的`resolve()`函数中返回另一个Promise对象时，原来的Promise对象会等待返回的Promise对象的状态改变，并且将返回的Promise对象的状态和值传递给原来的Promise对象。

具体来说，当在Promise对象的`resolve()`函数中返回另一个Promise对象时，原来的Promise对象会等待返回的Promise对象的状态改变。如果返回的Promise对象被resolved，那么原来的Promise对象也会变为resolved状态，并将返回的Promise对象的值作为参数传递给原来的Promise对象的`.then()`方法。如果返回的Promise对象被rejected，那么原来的Promise对象也会变为rejected状态，并将返回的Promise对象的错误对象作为参数传递给原来的Promise对象的`.catch()`方法。

具体哪个Promise对象的值会被传递给原来的Promise对象，取决于返回的Promise对象的状态。如果返回的Promise对象的状态为resolved，那么原来的Promise对象将传递返回的Promise对象的值。如果返回的Promise对象的状态为rejected，那么原来的Promise对象将传递返回的Promise对象的错误对象。

例如，假设我们有一个返回Promise对象的函数`getPromise()`，我们可以在另一个Promise对象的`resolve()`函数中调用`getPromise()`函数，并将其返回值作为参数传递给`resolve()`函数。在这种情况下，返回的Promise对象的状态和值将传递到原来的Promise对象中，如下所示：

```javascript
function getPromise() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Sub Promise Resolved");
        }, 500);
    });
}

const mainPromise = new Promise((resolve, reject) => {
    resolve(getPromise());
});

mainPromise.then((data) => {
    console.log("Main Promise Resolved with: ", data);
}).catch((error) => {
    console.error("Main Promise Rejected with: ", error);
});
```

在这个例子中，我们定义了一个返回Promise对象的函数`getPromise()`，它会在500毫秒后被resolved。然后，我们创建了一个名为`mainPromise`的Promise对象，并在它的`resolve()`函数中调用`getPromise()`函数，并将其返回值作为参数传递给`resolve()`函数。最后，我们使用`.then()`方法和`.catch()`方法来获取`mainPromise`的结果。

由于`mainPromise`的`resolve()`函数中返回了`getPromise()`函数的返回值，因此`mainPromise`对象将等待返回的Promise对象的状态改变，并将其状态和值传递给`mainPromise`对象。当`getPromise()`函数返回的Promise对象被resolved时，`mainPromise`对象也会被resolved，并将`getPromise()`函数返回的值作为参数传递给`.then()`方法。因此，在这个例子中，当`getPromise()`函数返回的Promise对象被resolved时，控制台会输出`Main Promise Resolved with: Sub Promise Resolved`。


## 运行顺序
```js
const subPromise = new Promise((resolve, reject) => {  
	setTimeout(() => {  
	console.log(1001)  
	resolve("Sub Promise Resolved");  
	}, 500)  
})

const mainPromise = new Promise((resolve, reject) => {  
	resolve(subPromise);  
})  

mainPromise.then(data => {  
	console.log(data)  
})  
// 说一下这个的运行顺序
```

当执行这段代码时，以下是大致的运行顺序：

1. 创建一个名为`subPromise`的Promise对象，并将一个带有`resolve()`方法和一个`setTimeout()`函数的函数作为参数传递给它的构造函数。同时，输出控制台信息`1001`。

2. `setTimeout()`函数被调用，并将包含`resolve()`方法的匿名函数作为要执行的代码，以及500毫秒作为延迟时间。

3. 创建一个名为`mainPromise`的Promise对象，并将一个带有`resolve()`方法的函数作为参数传递给它的构造函数。

4. 在`resolve()`方法中，将`subPromise`对象作为参数传递给它。这将导致`mainPromise`对象等待`subPromise`对象的状态改变。

5. `mainPromise`对象的`then()`方法被调用，并将一个函数作为参数传递给它。

6. 500毫秒后，`setTimeout()`函数中的匿名函数被执行。在该函数中，`resolve()`方法被调用，并将字符串`"Sub Promise Resolved"`作为参数传递给它。这将使`subPromise`对象的状态从`pending`变为`fulfilled`，同时将该字符串作为结果值。

7. `subPromise`对象的状态已经改变为`fulfilled`，并且结果值是字符串`"Sub Promise Resolved"`。这将导致`mainPromise`对象的状态也改变为`fulfilled`，同时将该字符串作为结果值。

8. `mainPromise`对象的`then()`方法中的函数被调用，并将字符串`"Sub Promise Resolved"`作为参数传递给它。该函数将输出该字符串到控制台。

因此，最终控制台将输出以下内容：

```
1001
Sub Promise Resolved
```

需要注意的是，`console.log(1001)`和`resolve("Sub Promise Resolved")`可能不会按照顺序执行，因为`setTimeout()`函数是异步的。但是，无论哪个先执行，最终输出的结果都将是一样的。
##  Promise对象接受多少个参数
在JavaScript中，Promise对象的构造函数只接受一个函数作为参数，该函数通常称为执行器函数（executor function），它可以接受两个参数：resolve函数和reject函数。resolve函数和reject函数分别用于将Promise对象的状态从pending（进行中）转换为fulfilled（已成功）或rejected（已失败），并传递成功或失败的结果。

注意，resolve函数和reject函数只能被调用一次，并且它们只接受一个参数。如果resolve函数被调用，则Promise对象的状态被设置为fulfilled，并将resolve函数的参数作为Promise对象的值；如果reject函数被调用，则Promise对象的状态被设置为rejected，并将reject函数的参数作为Promise对象的原因。

例如，以下是一个使用Promise对象的示例，展示了如何使用构造函数中传入的执行器函数来创建Promise对象：

```js
const myPromise = new Promise((resolve, reject) => {
  // 如果操作成功，则调用resolve函数，并传递成功的结果
  // 如果操作失败，则调用reject函数，并传递失败的原因
});
```

在上面的示例中，我们创建了一个名为myPromise的Promise对象，并传入一个执行器函数作为参数。在执行器函数中，可以执行任何异步操作，并在操作成功或失败后调用resolve函数或reject函数。

需要注意的是，在Promise对象被创建后，它的状态一开始是pending（进行中），并且它的值和原因都是undefined。只有当执行器函数中调用了resolve函数或reject函数后，Promise对象的状态才会从pending转换为fulfilled或rejected，并将结果存储在Promise对象中。

```js
const response = {
    status: 200,
    data: "Hello, World!",
};

const error = 'fail'

const myPromise = new Promise((resolve, reject) => {
		resolve(response);
		// reject(error);
});

myPromise
    .then((resolvedResponse) => {
        console.log("Promise resolved with: ", resolvedResponse);
    })
    .catch((error) => {
        console.error("Promise rejected with: ", error);
    });
```


是的，`axios.get`方法返回一个Promise对象，这个Promise对象的状态会根据HTTP请求的结果来决定是resolved还是rejected。当HTTP请求成功时，Promise对象的状态会被设置为resolved，并将响应数据作为参数传递给`resolve`函数；当HTTP请求失败时，Promise对象的状态会被设置为rejected，并将一个Error对象作为参数传递给`reject`函数。

因此，我们不需要在Promise构造函数中手动调用`resolve`或`reject`函数来设置Promise对象的状态，也不需要在`.then()`方法或`.catch()`方法中手动判断Promise对象的状态。Axios会自动处理这些细节，我们只需要在`.then()`方法中处理resolved状态的响应数据，在`.catch()`方法中处理rejected状态的错误信息即可。


## promise在调用.then后resolve内的值会传递给promise吗
是的，在`Promise`对象的`resolve()`方法中传递的值会在调用`.then()`方法时被传递给处理程序中的函数。具体来说，当`Promise`对象的状态从`pending`变为`fulfilled`时，它的结果值将会被传递给`.then()`方法中的回调函数。

例如，考虑以下示例代码：

```
const myPromise = new Promise((resolve, reject) => {
  resolve("Hello, world!");
});

myPromise.then((result) => {
  console.log(result);
});
```

在这个示例中，当`myPromise`对象的`resolve()`方法被调用时，它的状态将从`pending`变为`fulfilled`，并且结果值`"Hello, world!"`将被传递给`.then()`方法中的回调函数。因此，当`.then()`方法被调用时，它将打印出`"Hello, world!"`。

需要注意的是，如果`Promise`对象的状态从`pending`变为`rejected`，则其结果值将被传递给`.catch()`方法中的回调函数。因此，无论`Promise`对象的状态是`fulfilled`还是`rejected`，其结果值都将被传递给相应的处理程序中的函数。

##   但是promise对象里面不会有result的值吗
在`Promise`对象中，`resolve()`方法中传递的值并不会直接保存在`Promise`对象中，而是作为结果值传递给`then()`方法中的回调函数。因此，`Promise`对象本身并不会包含结果值。

当`Promise`对象的状态从`pending`变为`fulfilled`时，`Promise`对象的结果值将被传递给`.then()`方法中的回调函数。如果在`.then()`方法中返回了一个值，那么这个值将成为下一个`.then()`方法中的回调函数的输入参数。这样，通过链式调用`.then()`方法，可以将结果值传递给多个回调函数。

例如，考虑以下示例代码：

```
const myPromise = new Promise((resolve, reject) => {
  resolve("Hello, world!");
});

myPromise.then((result) => {
  console.log(result);
  return "Hello, JavaScript!";
}).then((result) => {
  console.log(result);
});
```

在这个示例中，当`myPromise`对象的`resolve()`方法被调用时，它的状态将从`pending`变为`fulfilled`，并且结果值`"Hello, world!"`将被传递给第一个`.then()`方法中的回调函数。该函数将打印出`"Hello, world!"`，并返回字符串`"Hello, JavaScript!"`。这个字符串将成为下一个`.then()`方法中的回调函数的输入参数，并被打印出来。

因此，在`Promise`对象中，结果值并不会直接存储在对象中，而是通过`.then()`方法中的回调函数进行传递和处理。

## 既然是只作为值传递给promise.then，那为什么如果值是一个promise对象，会根据这个promise对象的状态来改变原来的promise呢

当将一个`Promise`对象作为另一个`Promise`对象的结果值时（例如，在`resolve()`方法中传递一个`Promise`对象），它将被视为一个普通的值，会被传递给调用该`Promise`对象的`.then()`方法的处理程序。

然而，由于`Promise`对象本身是一种异步编程的工具，它的异步特性使得它可以等待其他`Promise`对象的状态变化，并将它们的状态和结果值传递给后续的`.then()`方法中的处理程序。这种行为被称为 Promise 链（Promise chaining）。

具体来说，当一个`Promise`对象的状态从`pending`变为`fulfilled`时，并且它的结果值是一个`Promise`对象时，该`Promise`对象会等待该`Promise`对象的状态发生变化，并将其状态和结果值传递给调用该`Promise`对象的`.then()`方法的处理程序。如果该`Promise`对象的状态为`fulfilled`，则调用该`Promise`对象的`.then()`方法的处理程序的状态为`fulfilled`，并且结果值为该`Promise`对象的结果值。如果该`Promise`对象的状态为`rejected`，则调用该`Promise`对象的`.then()`方法的处理程序的状态为`rejected`，并且结果值为该`Promise`对象的错误对象。

因此，当将一个`Promise`对象作为另一个`Promise`对象的结果值时，该`Promise`对象的状态和结果值将被传递给调用该`Promise`对象的`.then()`方法的处理程序，并根据该`Promise`对象的状态来决定下一个`Promise`对象的状态。这种行为使得我们可以在异步编程中更加方便地组合和处理`Promise`对象。