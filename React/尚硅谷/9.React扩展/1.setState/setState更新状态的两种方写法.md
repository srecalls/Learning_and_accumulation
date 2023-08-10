## (1).`setState(stateChange, [ca1lback])`--------对象式的setState
	1.stateChange为状态改变对象(该对象可以体现出状态的更改)
	2.callback是可选的回调函数，它在状态更新完毕、界面也更新后(render调用后)才被调用

### 对象式
```js
export default class Demo extends Component {
	state = { count: 0 }
	add = () => {
		// 对象式的setState
		// 1. 获取原来的count值
		const { count } = this.state
		// 2.更新状态
		this.setState({ count: count + 1}, () => {
			console.log(this.state.count) // 1
		})
		console.log(this.state.count).  // 0
	}
}

```

### 函数式
```js
export default class Demo extends Component {
	state = { count: 0 }
	add = () => {
		this.setState( state => {
			return { count: state.count + 1 }
		}, () => {
			console.log(this.state.count) // 1
		})
		// 简写
		// 依赖于原来的state
		this.setState( state => { count: state.count + 1 })
	}
}
```

(2). `setState(updater, [cal1back])`------函数式的setState
	1.updater为返回stateChange对象的函数。
	2.updater可以接收到state和props
	3.callback是可选的回调函数，它在状态更新、界面也更新后(render调用后)才被调用

总结:
1.对象式的setstate是函数式的setstate的简写方式(语法糖)
2.使用原则:
	(1).如果新状态不依赖于原状态 ===> 使用对象方式
	(2).如果新状态依赖于原状态===> 使用函数方式
	(3).如果需要在setstate()执行后获取最新的状态数据要在第二个callback函数中读取
