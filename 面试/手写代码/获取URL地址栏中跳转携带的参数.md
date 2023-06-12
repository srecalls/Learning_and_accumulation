# 获取URL地址栏中跳转携带的参数

**`window.location.href`来获取当前页面的URL**
## 1. vue
```js
data() {
	return {
		username: ''
	}
},
 created() {
	this.username= this.getUrlKey("username", window.location.href)
},
methods: {
	getUrlKey(name, url) {
		return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(url) || [, ""])[1].replace(/\+/g, '%20')) || null
	}
	// 'http://www.baidu.com?user=%E9%98%BF%E9%A3%9E&age=16'
 }

```

## 2.用decodeURIComponent解码，通过name返回需要的值
```js
// 获取url参数
function getUrlKey (name) {
	return (
		decodeURIComponent(
			(new RegExp(
				"[?|&]" + name + "=" + "([^&;]+?)(&|#|;|$)"
			).exec(location.href) || [, ""])[1].replace(/\+/g, "%20")
		) || null
	);
},
//调用方法
getUrlKey("token")
```

## 3.用decodeURIComponent解码，直接返回对象
```js
function getParams(url) {
  const res = {}
  if (url.includes('?')) {
    const str = url.split('?')[1]
    const arr = str.split('&')
    arr.forEach(item => {
      const key = item.split('=')[0]
      const val = item.split('=')[1]
      res[key] = decodeURIComponent(val) // 解码
    })
  }
  return res
}

// 测试
const user = getParams('http://www.baidu.com?user=%E9%98%BF%E9%A3%9E&age=16')
console.log(user) // { user: '阿飞', age: '16' }
```


```js
function getURLKey(url, targetKey) {
  const res = ''
  if (url.includes('?')) {
    const str = url.split('?')[1]
    const arr = str.split('&')
    for (let i = 0; i < arr.length; i++) {
	    const key = arr[i].split('=')[0]
	    const val = arr[i].split('=')[1]
	    if (key === targetKey) {
		    return decodeURIComponent(val) // 解码
	    }
    }
  }
  return res
}

// 测试
const user = getURLKey('http://www.baidu.com?user=%E9%98%BF%E9%A3%9E&age=16', 'user')
console.log(user) // '阿飞'
```