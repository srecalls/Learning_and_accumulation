js es6 promise 中 resolve 如何传递多个参数?
```js
//我希望类似与这样使用，但实际上后面两个参数无法获取
promise = new Promise((resolve,reject)=>{
    let a = 1
    let b = 2
    let c = 3
    resolve(a,b,c) 
})
promise.then((a,b,c)=>{
    console.log(a,b,c)
})

```

\resolve() 只能接受并处理一个参数，多余的参数会被忽略掉。  
如果想多个用数组，或者对象方式。。
'

数组
```js
promise = new Promise((resolve,reject)=>{
    resolve([1,2,3]) 
})
promise.then((arr)=>{
    console.log(arr[0],arr[1],arr[2])
})
```

对象
```js
promise = new Promise((resolve,reject)=>{
    resolve({a:1,b:2,c:3}) 
})
promise.then(obj=>{
    console.log(obj.a,obj.b,obj.c)
})
```