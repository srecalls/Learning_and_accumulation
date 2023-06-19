## promsie出现的必要性
在javascript中，因为其被设计之初被设计为单线程，所有的代码都是在同步执行，因此此线程不能被阻塞，但有时候根据需求我们可能做一些可能阻塞线程的操作，所以就需要采取异步编程模式。

对于异步编程，我们习惯使用传统的回调或者事件触发来解决异步问题，比如ajax的回调函数，又或者触发特定的事件，才得到结果，本质上两者并没有什么区别，但是这也适用于代码量少的模式，随着我们前端工程的越来越复杂，回调函数和事件触发也显得那么的力不从心（好吧，其实就是代码看着越来越e，而且极其不容易维护），该模式下面临的两个问题：


	1.回调地狱：某个异步操作需要等待之前的异步操作完成，无论用回调还是事件，都会陷入不断的嵌套。
	2.异步之间的联系：某个异步操作要等待多个异步操作的结果，对这种联系的处理，会让代码的复杂度剧增。

这种代码量看着很少的看着还可以，可以在往下看
![[Pasted image 20230618035742.png]]

那再来看看这种回调嵌套回调，是不是很恶，下面有用promise的优化版
![[Pasted image 20230618035839.png]]



## promsie介绍
对于上述出现的问题，着实让每个开发者感到巨难受，这个时候呢，来了一个老大哥 `ES6`，它总结出了一套异步的通用模型，该模型可以覆盖几乎所有的异步场景，ES6 没抛弃掉过去的做法，只是基于该模型推出一个全新的 API--`promsie`，使用该API，会让异步处理更加的简洁优雅。

### 对于ES6推出的异步模型

1. Promise将某一件可能发生异步操作的事情，分为两个阶段：unsettled 和 settled

	- unsettled： 未决阶段，表示事情还在进行前期的处理，并没有发生通向结果的那件事
	- settled：已决阶段，事情已经有了一个结果，不管这个结果是好是坏，整件事情无法逆转

2. Promise分为三种状态： pending、resolved、rejected

	- pending: 挂起，处于未决阶段，则表示这件事情还在挂起（最终的结果还没出来）
	- resolved：已处理，已决阶段的一种状态，表示整件事情已经出现结果，并是一个可以按照正常逻辑进行下去的结果
	- rejected：已拒绝，已决阶段的一种状态，表示整件事情已经出现结果，并是一个无法按照正常逻辑进行下去的结果，通常用于表示有一个错误。

既然未决阶段有权力决定事情的走向，因此，未决阶段可以决定事情最终的状态！

我们将把事情变为**resolved状态的过程叫做：resolve**，推向该状态时，可能会传递一些数据

我们将把事情变为**rejected状态的过程叫做：reject**，推向该状态时，同样可能会传递一些数据，通常为错误信息。

**无论是阶段，还是状态，是不可逆的！**

3. 当事情达到已决阶段后，通常需要进行后续处理，不同的已决状态，决定了不同的后续处理。

resolved状态：这是一个正常的已决状态，后续处理表示为 **thenable**
rejected状态：这是一个非正常的已决状态，后续处理表示为 **catchable**
后续处理可能有多个，因此会形成作业队列，这些后续处理会按照顺序，当状态到达后依次执行。

图示：
![[Pasted image 20230618040124.png]]


##  Promise使用
	promise它是一个对象，通过reslove和reject将promise由未决阶段推向已决阶段，通过then方法，catch方法，进行后续的处理。对于使用，从题中来看：

注意点和总结：

	- 1. Promise的状态一经改变就不能再改变。
	- 2. 在Promise中，如果你的返回值不是个promise，它会将你的返回值包成一个promise对象返回。
	- 3. then方法和catch方法都会返回一个promise对象，并且可以被调用多次。
	- 4. catch不管被链到哪里，都会捕获上层未捕获到的错误。
	- 5. then方法和catch方法中return一个error对象并不会抛出错误，并不会被后续的catch所捕获。
	- 6. then方法 或catch方法 返回的值不能是 promise 本身，否则会造成死循环。
	- 7. then方法 或者catch方法的参数期望是函数，传入非函数则会发生值透传。
	- 8. finally方法也是返回一个Promise，他在Promise结束的时候，无论结果为resolved还是rejected，都会执行里面的回调函数，它的回调函数不会接受任何参数，在其中如果抛出异常，后续用catch也可以接收到。

### exercises：promise的简单使用
```js
const pro = new Promise((resolve, reject) => {
    console.log("未决阶段")
    resolve(123);
})
pro.then(data => {
    // pro的状态是pending
    console.log(data);
})
```

```js
未决阶段
123
```
分析：通过reslove将状态由pendding推向resloved，传入数据123，在pro.then函数调用时，将123作为参数传给函数，交给后续函数体进行处理。

#### 验证观点1

**1. Promise的状态一经改变就不能再改变。**
```js
const pro = new Promise((resolve, reject) => {
    reject("error");
    reject(1);
    resolve("success2");
})
pro.then((result) => {
    console.log(result);
}).catch(err => {
    console.log(err);
})
```

输出：
```js
error
```

结果：error 状态一经改变将不能在变


#### 验证观点2

**2. 在Promise中，如果你的返回值不是个promise，它会将你的返回值包成一个promise对象返回。**
```js
then(data => return 2) ==> return promise.reslove(2)
```

```js
Promise.resolve(1)
    .then(data => {
        return 2
    })
    .then(data => {
        console.log(data)
    })
```

输出
```js
2
```

#### 验证观点3

**3. then方法和catch方法都会返回一个promise对象，并且可以被调用多次。**
```js
const pro = new Promise((resolve, reject) => {
    resolve("success2");
})
let newPro = pro.then((result) => {
    return result
})
newPro.then(data => {
    console.log(data);
})
console.log(pro);
```

输出
```js
Promise {<fullfilled>: success2}
success2
```

结果分析：
return出去的result是一个promise对象newPro

#### 验证观点4

**4. catch不管被链到哪里，都会捕获上层未捕获到的错误。**
```js
const promise = new Promise((resolve, reject) => {
  reject("error");
  resolve("success2");
});
promise
.then(res => {
    console.log("then1: ", res);
  }).then(res => {
    console.log("then2: ", res);
  }).catch(err => {
    console.log("catch: ", err);
  }).then(res => {
    console.log("then3: ", res);
  })
```

输出
```js
"catch: " "error"
"then3: " undefined
```

#### 验证观点5
**5. then方法和catch方法中return一个error对象并不会抛出错误，并不会被后续的catch所捕获。**
```js
Promise.resolve().then(() => {
  return new Error('error!!!')
}).then(res => {
  console.log("then: ", res)
}).catch(err => {
  console.log("catch: ", err)
})
```

输出
```js
"catch: " "Error: error!!!"
```
结果：

 `"then: " "Error: error!!!"
 
这也验证了第2点和第5点，返回任意一个非 promise 的值都会被包裹成 `promise` 对象，因此这里的`return new Error(‘error!!!’)`也被包裹成了`return Promise.resolve(new Error(‘error!!!’))`

#### 验证观点6

**6. then方法 或catch方法 返回的值不能是 promise 本身，否则会造成死循环。
```js
const promise = Promise.resolve().then(() => {
	return promise
})
promise.catch(console.err)
```

输出
```js
Uncaught (in promise) TypeError: Chaining cycle detected for promise #<Promise>
```


#### 验证观点7

**7. then方法 或者catch方法的参数期望是函数，传入非函数则会发生值透传。**

```js
Promise.resolve(1)
	.then(2)
	.then(Promise.resolve(3))
	.then(console.log)
```

输出结果
```js
1
```


#### 验证观点8

**8. finally方法也是返回一个Promise，他在Promise结束的时候，无论结果为resolved还是rejected，都会执行里面的回调函数，它的回调函数不会接受任何参数，在其中如果抛出异常，后续用catch也可以接收到。**
 
```js
Promise.resolve('1')
	.then(res => {
		console.log(res)
	})
	.finally(() => {
		console.log('finally')
	})
Promise.resolve('2')
	.finally(()=> {
		console.log('finally2')
		return '我是finally2返回的值'
	})
	.then(res => {
		console.log('finally2后面的then函数', res)
	})
```

输出
```js
1
finally2
finally
finally2后面的then函数 2
```

分析：这两个Promise的.finally都会执行，且就算finally2返回了新的值，它后面的then()函数接收到的结果却还是’2’。

## Promise.all)

此方法也会返回一个`promise`对象，它通常处理的是多个`promise`对象的集合（数组），如果集合中的每一个`promise`对象都成功才触发它成功的回调，一旦有一个失败，则立即触发它的失败。

这个新的`promise`对象在**触发成功状态**以后，会把一个包含数组里所有`promise`返回值的数组作为成功回调的返回值，**顺序跟数组的顺序保持一致**；如果这个新的`promise`对象触发了失败状态，它会把数组里**第一个触发失败的`promise`对象的错误信息作为它的失败错误信息。**
```js
function biaobai(god) {
	return new Promise((resolve, reject) => {
		setTimeout(() => {
			if (Math.random() > 0.1) {
				console.log(`${god}同意了`)
				resolve("成功")
			} else {
				// resolve
				console.log(`${god}拒绝了`)
				resolve("失败")
			}
		}, 1000)
	})
}
let arr = []
for (let i =0; i < 5; i++) {
	arr.push(biaobai(`${'女神' + i}`))
}
Promise.all(arr).then(data => {
	console.log((data), '同意了'),
	err => {
		console.log(err, '拒绝了')
	}
})
```
成功的回调：33行的打印
![[Pasted image 20230618043400.png]]
失败的回调：34行的打印
![[Pasted image 20230618043405.png]]

## Promise.race()
它和promise.all相反，race竞赛的意思，就是你数组中`子promise`成功或者失败后，它会` 立即拿到第一个子promise `的返回值作为其参数执行其回调，就是你第一个触发成功回到，那么它也会触发成功回调，反之则触发其失败回调。

当数组里的` 任意一个子promise被成功或失败 `后，父promise马上也会用子promise的成功返回值或失败详情作为参数调用父promise绑定的相应句柄，并返回该promise对象。

两者总结：

1. Promise.all()的作用是接收一组异步任务，然后并行执行异步任务，并且在所有异步操作执行完后才执行回调。

2. Promise.race()的作用也是接收一组异步任务，然后并行执行异步任务，只保留取第一个执行完成的异步操作的结果，其他的方法仍在执行，不过执行结果会被抛弃。

3. Promise.all().then()结果中数组的顺序和Promise.all()接收到的数组顺序一致。

4. all和race传入的数组中如果有会抛出异常的异步任务，那么只有最先抛出的错误会被捕获，并且是被then的第二个参数或者后面的catch捕获；但并不会影响数组中其它的异步任务的执行。

总结考了一份大佬的，还有上面有些例题也是看他的，写这篇文章也是受到了他启发，文章的地址：
https://juejin.im/post/5e58c618e51d4526ed66b5cf#heading-17
，作者：LinDaiDai_霖呆呆，写的很多东西都很好，建议大家可以多去看看。

对上面的回调地狱用promise处理：
```js
// 封装后的ajax返回的是一个promise，重点不在这，看下面和上面回调地狱的对比
// 代码没有那么恶，优美了许多，而且更容易维护了些。
 const pro = ajax({
     url: "./data/students.json"
 })
 pro.then(resp => {
     for (let i = 0; i < resp.length; i++) {
         if (resp[i].name === "李华") {
             return resp[i].classId; //班级id
         }
     }
 }).then(cid => {
     return ajax({
         url: "./data/classes.json?cid=" + cid
     }).then(cls => {
         for (let i = 0; i < cls.length; i++) {
             if (cls[i].id === cid) {
                 return cls[i].teacherId;
             }
         }
     })
 }).then(tid => {
     return ajax({
         url: "./data/teachers.json"
     }).then(ts => {
         for (let i = 0; i < ts.length; i++) {
             if (ts[i].id === tid) {
                 return ts[i];
             }
         }
     })
 }).then(teacher => {
     console.log(teacher);
 })
```
