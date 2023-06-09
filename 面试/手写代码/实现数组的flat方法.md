```js
function __flat(arr ,depth) {
	if (!Array.isArray(arr) || depth <= 0) {
		return arr
	}
	return arr.reduce((prev, cur) => {
		if (Array.isArray(cur)) {
			return prev.concat(__flat(cur, depth - 1))
		} else {
			return prev.concat(cur)
		}
	}, [])
}
```

```js
function __flat(arr, depth) {
	if (!Array.isArray(arr) || depth <= 0) {
		return arr
	}
	return arr.reduce((prev, cur) => {
		return prev.concat(Array.isArray(cur)? __flat(cur, depth - 1) : cur)
	}, [])
}
```