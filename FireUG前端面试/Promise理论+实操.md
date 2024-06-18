### 什么是Promise
#### 异步任务
我们经常会碰到异步编程问题，常常伴随一些问题，其中最突出的就是地狱回调问题，这种情况通常出现在需要执行多个异步操作的场景

#### 需求
假设有一个需求：
用户登陆后，按照顺序执行多个任务，包括获取用户信息、检查权限、加载配置等
![[Promise理论+实操.png]]

#### 写法
##### 未使用Promise
![[Promise理论+实操-1.png]]

回调地狱使代码变得难维护和理解
##### 使用Promise
![[Promise理论+实操-2.png]]

观感上好了很多，就可以让我们在写代码的时候更轻松、更优雅地处理异步操作

### 什么是Promise
![[Promise理论+实操-3.png]]

### Promise的状态变化
![[Promise理论+实操-5.png]]

#### 例子
![[Promise理论+实操-6.png]]

### Promise的两种异常捕获方式
![[Promise理论+实操-7.png]]

1. .then中的第二个参数

2.  catch

在平时开发中，更推荐使用Catch方法来处理异常，因为可读性更好
使用第一个方法来处理异常可能会导致代码的可读性较差，特别是在处理多个Promise的时候
还可以更方便地进行错误传递，如果在Promise链中多个地方需要处理异常，使用 .catch 方法可以更方便地传递和处理这些异常
使用.then的第二个参数，会导致异常处理代码分散在多个代码块中。不够集中
最后一个优点就是：
.catch的错误捕捉方面更全面

**使用第一个方法时它只能捕获前面 Promise 链中的异常，无法捕捉当前.then方法中的异常**

**.catch 方法不仅能够捕获当前.then方法中的异常还能捕获前面Promise链中的错误**

![[Promise理论+实操-8.png]]

### Promise引入链式调用
Promise解决地狱回调的原因，关键在他引入了链式调用概念
![[Promise理论+实操-9.png]]


```js
function login() {
	return fetch("https://api.example.com/login")
}

function getUserInfo() {
	return fetch("https://api.example.com/login")
}

function checkPermission() {
	return fetch("https://api.example.com/login")
}

function loadConfig() {
	return fetch("https://api.example.com/login")
}

// 每个函数都返回一个Promise对象用于处理相应的异步任务
// 通过灵活运用.then方法进行链式调用
// 我们实际上是告诉程序，当前面的Promise任务完成时就执行下一个操作，在这个例子里就是按照登陆，获取用户信息、管理权限和加载配置的顺序一步步走。如果所有的Promise都成功完成，最后的.*then方法中的代码将被执行显示欢迎信息，表示用户已成功登陆，如果任何一个Promise发生错误.catch方法将捕捉异常并处理执行代码

login()
	.then(() => getUserInfo())
	.then(() => checkPermission())
	.then(() => loadConfig())
	.then(() => {
		// 所有任务完成，用户已登陆，显示欢迎消息
		displayWelcomeMessage()
	})
	.catch(error => {
		console.error("登陆失败", error)
	})

```

### Promise的特殊场景


1. Promise.all
   ![[Promise理论+实操-10.png]]
   
Promise.all方法接受**一个包含多个Promise对象的数组**作为参数，当数组中所有的Promise对象都成功完成时，该方法返回一个成功状态的Promise对象，其成功的结果是由多个 Promise 对象成功结果组成的数组，但如果其中有一个 Promise 返回失败状态，该方法将返回一个失败状态的 Promise 对象，其失败的结果是其中一个失败的 Promise 的结果
**这个函数通常用于将多个 Promise 实例，包装成一个新的Promise实例，等待他们全部完成后执行某些操作**
这里我们需要注意下 Promise.all 的执行原理

Promise的执行原理：
![[Promise理论+实操-11.png]]

具体的业务场景

需求:处理多个可能出现错误的异步操作，如果其中任何一个失败，就记录错误。
![[Promise理论+实操-12.png]]

```js
const photos = [
	// 照片列表
]
const uploadPromises = [] // 用于存储每张照片上上传的Promise对象

function uploadPhotoToServer(photo) {
	const formData = new FormData()
	formData.append("photo", photo)

	// 返回一个Promise对象表示上传操作
	return fetch("https://api.excample.com/upload", {
		method: "POST",
		body: formData,
	}).then((response) => {
		response.ok ? response.json() : Promise.reject("上传失败")
	})
}

// 使用 forEach 遍历照片数组， 对每张照片都执行uploadPhtoToServer函数
photos.forEach((photo) => {
	const uploadPromise = uploadPhtotoToServer(photo)
	.then((uploadedPhoto) => handleUploadedPhoto(uploadedPhoto))
	.catch((error) => logUploadError(error))

	// 将每张照片的上传Promise添加到 uploadPromises 数组中
	uploadPromises.push(uploadPromise)
})

Promise.all(uploadPromises)
	.then(() => {
		// 所有照片上传完毕
		createPostWithPhotos()
	})
	.catch((erroe) => {
		// 在上传所有照片时至少有一个失败
		handleUploadedError(error)
	})
```

也就是必须等待所有的操作都执行完成,然后才能执行进一步的操作

2. Promise.race

![[Promise理论+实操-13.png]]

谁先到就用谁的

实际应用
先从本地缓冲拿数据，如果等待时间太长，就迅速转战服务器获取
```js
// 假设有两个异步操作，一个是从服务器获取数据，另一个是从本地缓存获取数据
function fetchDataFromServer() {
	return new Promise((resolve, reject) => {
		setTimeout(() => {
			resolve("服务器返回的数据")
		}, 2000)
	})
}

function fetchDataFromLocalStorage() {
	return new Promise((resolve, reject) => {
		setTimeout(() => {
			resolve("本地缓存的数据")
		}, 1000)
	})
}

// 使用 Promise.race 来获取数据，优先使用本地缓存，但是如果超时，则从服务器获取
function getDataWithRace() {
	return Promise.race([fetchDataFromLocalStorage(), fetchDataFromServer()])
}

// 调用
getDataWithRace()
	.then((data) => {
		console.log("Data received:", data)
	})
	.catch((error) => {
		console.error("Error:", error)
	})
```

场景：开发一个移动应用，需要在用户打开应用时尽快展示数据，就可以使用Promise.race方法，来同时从本地缓存和服务器获取数据，只要其中一个操作率先完成，无论成功或失败就返回相应的结果

