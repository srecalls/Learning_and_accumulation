## 效果
![[refs-2.png]]
## 理解
组件内的标签可以定义 ref 属性来标识自己
![[refs-1.png]]
![[refs.png]]

## 编码
### 字符串类型ref （不被推荐）
```js
class Demo extends React.Component {
	// 展示左侧输入框的数据
	showData1 = () => {
		const { input1 } = this.refs
		alert(input1.value)
	}
	// 展示右侧输入框的数据
	showData2 = () => {
		const { input2 } = this.refs
		alert(input2.value)
	}
	render() {
		return (
			<div>
				<input ref="input1" type="text" placeholder="点击提示"/>
				<button onClick={this.showData1}></button>
				<input ref="input2" onBlur={this.showData2} type="text" placeholder="点击提示"/>
		)
	}
}
```

![[refs-3.png]]

	**过时 APl:String 类型的 Refs**
	如果你之前使用过 React，你可能了解过之前的 API 中的 string 类型的 ref 属性，例如 `"textInput"`。你可以通过 `this.refs.textInput` 来访问 DOM 节点。我们不建议使用它，因为 string 类型的 refs 存在一些问题。它已过时并可能会在未来的版本被移除。
	**注意**
	如果你目前还在使用 this.refs.textInput 这种方式访问 refs，我们建议用回调函数或createRef API的方式代替

效率问题


### 回调形式ref

```js
<input ref={(a) => {console.log(a)}} type="text" placeholder="点击提醒"/>
// <input type="text" placeholder="点击提醒"/>
```


```js
class Demo extends React.Component {
	// 展示左侧输入框的数据
	showData1 = () => {
		const { input1 } = this
		alert(input1.value)
	}
	// 展示右侧输入框的数据
	showData2 = () => {
		const { input2 } = this
		alert(input2.value)
	}
	render() {
		return (
			<div>
				<input ref={(currentNode) => {this.input1 = currentNode} type="text" placeholder="点击提醒"/>
				<button onClick={this.showData1}></button>
				<input ref={(currentNode) => {this.input2 = currentNode} onBlur={this.showData2} type="text" placeholder="点击提示"/>
		)
	}
}
```

### 回调ref中回调次数的问题

如果 ref 回调函数是以内联函数的方式定义的，在更新过程中它会被执行两次，第一次传入数 null，然后第二次会传入参数 DOM 元素。这是因为在每次渲染时会创建一个新的函数实例，所以 React 清空旧的 ref 并且设置新的。通过将ref 的回调函数定义成 cass 的绑定函数的方式可以避免上述问题，但是大多数情况下它是无关紧要的.

#### 内联函数
为了保证上一次旧的ref被清空。所以先调用一遍，置为null
```js
class Demo extends React.Component {
	// 展示左侧输入框的数据
	showData1 = () => {
		const { input1 } = this
		alert(input1.value)
	}
	changeWeather = () => {
		// 获取原来的状态
		const {isHot} = this.state
		// 更新状态
		this.setState({isHot: !isHot})
	}
	render() {
		return (
			<div>
				<h2>{this.state.isHot? '炎热' : '凉爽'}</h2>
				// 直接写，就是内联
				<input ref={(currentNode) => {this.input1 = currentNode; console.log('@', currentNode)} onClick={this.showData1} type="text" placeholder="点击提醒"/>
				<button onClick={this.changeWeather}>点我切换天气</button>
			</div>
		)
	}
}
```

点击button后
```js
@ null
@ <input type="text" placeholder="点击提醒">
```

#### class的绑定函数
```Js
class Demo extends React.Component {
	changeWeather = () => {
		// 获取原来的状态
		const {isHot} = this.state
		// 更新状态
		this.setState({isHot: !isHot})
	}
	saveInput = (currentNode) => {
		this.input1 = currentNode
		console.log('@')
	}
	render() {
		return (
			<div>
				<h2>{this.state.isHot? '炎热' : '凉爽'}</h2>
				// 绑定到class
				<input ref={this.saveInput} type="text" placeholder="提醒">
				<button onClick={this.changeWeather}>点我切换天气</button>
			</div>
		)
	}
}
```

### createRef
```js
class Demo extends React.Component {
	/*
		React.createRef 调用后可以返回一个容器, 该容器可以存储被ref所标识的节点
	*/
	myRef = React.createRef()
	myRef2 = React.createRef()
	showData = () => {
		console.log(this.myRef)
		// {current: input}
		console.log(this.myRef.current)
		<input type="text" placeholder="提醒">
	}
	render() {
		return (
			<div>
				<input ref={this.myRef} type="text" placeholder="提醒">
				// 如果下面的button也放进容器了，会把input覆盖，因为容器是专人专用的
				/* <button ref={this.myRef} onClick={this.showData}>点击提醒</button> 」*/
				<input ref={this.myRef2} type="text" placeholder="提醒">
			</div>
		)
	}
}
```

## 扩展 JSX里的注释
```jsx
{/* <h2>{this.state.isHot? '炎热' : '凉爽'}</h2> */}
```
