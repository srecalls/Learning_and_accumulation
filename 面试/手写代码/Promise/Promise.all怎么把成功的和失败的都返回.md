![[Pasted image 20230717153827.png]]

```js
let p1 = new Promise((resolve, reject) => {
	setTimeout(() => {
		resolve(1)
	}, 1000)
})
let p2 = new Promise((resolve, reject) => {
	setTimeout(() => {
		reject(2)
	}, 3000)
})
let p3 = new Promise((resolve, reject) => {
	setTimeout(() => {
		reject(3)
	}, 2000)
})

Promise.all(
	(
		[p1, p2, p3].map(item => {
			return item.then(res => {
				return 'res' + res
			}, reject => {
				throw Error('reject' + reject) 
			}).catch(err => {
				return err
			})
		})
	)
)
	.then(res => {
		console.log('res', res)
  }, reject => {
    console.log('reject', reject)
  })
	.catch(err => {
		console.log('err', err)
	})
```

![[Promise.all怎么把成功的和失败的都返回.png]]