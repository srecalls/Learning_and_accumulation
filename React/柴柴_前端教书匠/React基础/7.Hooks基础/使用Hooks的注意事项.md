### Hook使用注意的事项
1. Hook 不能在 class 组件中使用( hooks不能在类组件中使用 )
```js
class APP extends React.Component {
	constructor() {
		super()
		state = {
			count: 1
		}
	}
	// 错误演示
	[count, setCount] = useState(0)
}
```
2. 只能在函数最外层调用 Hook。不要在循环、条件判断或者子函数中调用
3. 只能在 React 的函数组件中调用 Hook。不要在其他 JavaScript 函数中调用
