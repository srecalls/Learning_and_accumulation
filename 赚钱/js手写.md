### 1. 数组去重

1. set() + Array.from()

   ```js
   return Array.from(new set(arr));
   ```

2. map()

   ```js
   const newArr = [];
   const map = new Map();
   arr.forEach((item,index)=>{
   	if(!map.has(item)){
           map.set(item,true);
   		newArr.push(item);
       }
   })
   ```

3. filter() + indexOf()

   ```js
   return arr.filter((item,index)=>{
   	return arr.indexOf(item) === index;
   })
   ```

4. reduce()

   ```js
   return arr.reduce((pre,cur)=>{
   	if(!pre.includes(cur)){
   		return pre.push(cur);
       }else{
           return pre;
       }
   },[])
   ```

### 2. 多维数组扁平化

1. flat()

   ```js
   return arr.flat(Infinity);  //里面的参数表示扁平化多少层，Infinity表示无穷大的数
   ```

2. reduce()

   ```js
   const fn = (arr)=>{
   	return arr.reduce((pre,cur)=>{
   		return pre.concat(Array.isArray(cur)?fn(cur):cur) 
       },[])
   }
   fn(arr);
   ```

### 3. new操作符

```js
function myNew(Fn,...args){
	let obj = Object.create(Fn.prototype);
    let res = Fn.call(obj,...args);
    if(res !== null && (typeof res === "object" || typeof res === "function")){
		return res;
    }
    return obj;
}
```

### 4. instanceof

```js
function myInstanceof(left,right){
    if(typeof left !== "object" && typeof left !== "function" || left == null){
        return false;
    }
    var a = left.__proto__,
    	b = right.prototype;
    while(a != null){
		if(a == b) return true;
        a = a.__proto__;
    }
    return false;
}
```

### 5. 手写数组filter方法

```js
Array.prototype.myFilter = function(callback, thisArg){
    if (typeof callback !== "function") {
		throw "参数必须为函数";
    }
    let newArr = [];
    for(let i = 0;i < this.length;i++) {
		let res = callback.call(thisArg,this[i],i,this);
        if (res) {
			newArr.push(this[i]);
        }
    }
    return newArr;
}
```

### 6. 手写数组map方法

```js
Array.prototype.myMap = function(callback,thisArg){
    if (typeof callback !== "function") {
        throw "参数必须为函数";
    }
    let newArr = [];
    for(let i = 0;i < this.length;i++) {
		newArr.push(callback.call(thisArg,this[i],i,this))
    }
    return newArr;
}
```

### 7. 手写数组reduce方法

```js
Array.prototype.myReduce = function(callback,initValue){
    if(typeof callback !== "function"){
        throw "参数必须为函数";
    }
    let pre = initValue;
    for(let i = 0;i < this.length;i++){
		if(!initValue && i === 0){
            pre = this[i];
            continue;
        }
        pre = callback(pre,this[i],i,this);
    }
    return pre;
}
```

### 8. 手写Object.is方法

```js
Object.prototype.myIs = function(x,y){
	if(x === y){
		return x !== 0 || y !== 0 || 1/x === 1/y;
    }else{
		return x !== x && 
    }
}
```

### 9. 封装工具类函数并进行全局挂载，如深拷贝对象、清空表单数据

```js
function deepClone(obj, newObj) {
    for (let key in obj) {
        if (obj.hasOwnProperty(key) && obj[key] instanceof Array) {
            newObj[key] = [];
            deepClone(obj[key], newObj[key]);
        } else if (obj.hasOwnProperty(key) && obj[key] instanceof Object) {
            newObj[key] = {};
            deepClone(obj[key], newObj[key]);
        } else if(obj.hasOwnProperty(key)){
            newObj[key] = obj[key]
        }
    }
    return newObj;
}
```

```js
export default function resetForm(fromRef: any, obj: any) {
    //清空数据
    Object.keys(obj).forEach(key => {
        obj[key] = ''
    })
    //清除表单的验证
    if (fromRef) {
        fromRef.resetFields();
        fromRef.clearValidate();
    }
}
```

### 10. 手写Promise

```js
/*
 1. 初始化
 2. 状态不可变
 3. 异常处理
 4. 确保参数是函数
 5. 回调保存
 6. 微任务
 7. 链式调用
*/
class myPromise {
    constructor(executor) {
        this.PromiseState = 'pending';
        this.PromiseResult = null;
        this.onFulfilledCallbacks = [];
        this.onRejectedCallbacks = [];
        try {
            executor(this.resolve.bind(this), this.reject.bind(this));
        } catch (error) {
            this.reject(error);
        }
    }
    resolve(result) {
        if (this.PromiseState === 'pending') {
            this.PromiseState = 'fulfilled';
            this.PromiseResult = result;
            this.onFulfilledCallbacks.forEach(callback => {
                callback(result);
            })
        }
    }
    reject(reason) {
        if (this.PromiseState === 'pending') {
            this.PromiseState = 'rejected';
            this.PromiseResult = reason;
            this.onRejectedCallbacks.forEach(callback => {
                callback(reason);
            })
        }
    }
    then(onFulfilled, onRejected) {
        return new myPromise((resolve, reject) => {
            let fulfilled = () => {
                queueMicrotask(() => {
                    try {
                        if (typeof onFulfilled !== 'function') {
                            resolve(this.PromiseResult);
                        } else {
                            const x = onFulfilled(this.PromiseResult);
                            return x instanceof myPromise ? x.then(resolve, reject) : resolve(x);
                        }
                    } catch (error) {
                        reject(error);
                    }
                })
            }
            let rejected = () => {
                queueMicrotask(() => {
                    try {
                        if (typeof onRejected !== 'function') {
                            reject(this.PromiseResult);
                        } else {
                            const x = onRejected(this.PromiseResult);
                            return x instanceof myPromise ? x.then(resolve, reject) : reject(x);
                        }
                    } catch (error) {
                        reject(error);
                    }
                })
            }
            switch (this.PromiseState) {
                case 'pending':
                    this.onFulfilledCallbacks.push(fulfilled);
                    this.onRejectedCallbacks.push(rejected);
                    break;
                case 'fulfilled':
                    fulfilled();
                    break;
                case 'rejected':
                    rejected();
                    break;
            }
        })
    }
}
```

### 11. 手写Promise各式方法

```js
myPromise.resolve = (value) => {
    return value instanceof myPromise ? value : new myPromise((resolve => resolve(value)));
}

myPromise.reject = (reason) => {
    return new myPromise((resolve,reject) => {
        reject(reason);
    }) 
}

myPromise.all = (promises) => {
    return new myPromise((resolve, reject) => {
        if (Array.isArray(promises)) {
            if (promises.length === 0) {
                return resolve(promises);
            }
            let result = [];
            let count = 0;
            promises.forEach((item, index) => {
                myPromise.resolve(promises[index]).then(
                    value => {
                        count++;
                        result[index] = value;
                        count === promises.length && resolve(result);
                    },
                    error => {
                        reject(error)
                    }
                )
            })
        } else {
            return reject(new TypeError('error'))
        }
    })
}

myPromise.race = (promises) => {
    return new myPromise((resolve, reject) => {
        if(Array.isArray(promises)){
            promises.forEach(item => {
                myPromise.resolve(item).then(resolve,reject);
            })
        }else{
            return reject(new TypeError('error'))
        }
    })
}
```

### 12. 使用promise实现并发

```js
// 模拟请求
const getData = url => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log(url, new Date());
            resolve({ url, data: new Date() })
        }, Math.round(Math.random() * 15) * 100);
    })
}
// 使用promise实现并发
function limitQueue(urls, limit) {
    let count = 0;
    for (let i = 0; i < limit; i++) {
        run();
    }
    function run() {
        new Promise((resolve, reject) => {
            resolve(getData(urls[count++]));
        }).then(() => {
            if (count < urls.length) run();
        })
    }
}
// 测试
const urls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
( _ => {
    limitQueue(urls, 4);
})()
```

### 13. 数组乱序（洗牌算法）

```js
let arr = [1, 2, 3, 4, 5]
const shuffle = (arr) => {
    let length = arr.length;
    while (length !== 0) {
        let random = Math.floor(Math.random() * length)
        tmp = arr[length-1]
        arr[length-1] = arr[random]
        arr[random] = tmp
        length--;
    }
    return arr;
}
```

### 14. 打印当前页面有什么标签

```js
[...new Set([...document.querySelectorAll('*')].map(el => el.tagName))]
```

### 15. dom节点输出成json格式

### 16. 实现一个发布订阅

### 17. 实现一个call

```js
Function.prototype.myCall = function(context, ...rest) {
	context = context || window;
    let fn = Symbol();
    context[fn] = this;
    return context[fn](...rest);
}
```

### 18. 实现一个bind

### 19. 使用事件委托实现点击li，输出是第几个

### 20. 版本号排序

