下载
创建实例
接着封装请求响应拦截器 
抛出
最后封装接口

axios.js
```js
//引入axios
import axios from' axios '
//创建实例
const api = axios. create({
	//请求地址的公共部分
	baseURL:'' ,
	//请求的超时时间
	timeout : 3000
})

//axios拦截器
api.interceptors.request.use(config => {
	//config请求的信息
	return config
},err => {
	//抛出错误
	Promise. reject(err)
})
api.interceptors.response.use(res => {
	console.log(res)
	return Promise.resolve(res)
},err=>{
	//抛出错误.
	Promise. reject(err)
})

export default api
```

request.js
```js
import api from ' axios.js
export const login = () => api({
	url:''
	method: 'get',
	params: params
})
```

使用
```js
//使用
import { login } from 'request.js'
	method:{
	login().then(res => {
		console.log(res)
})

```