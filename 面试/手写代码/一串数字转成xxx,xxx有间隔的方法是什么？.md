## version1
```js
// 格式化 人民币
formatRmb(value) {
	value = value.split(',').join('')
	const num = parseFloat(value)
	const final = num.toLocaleString('zh', {
		style: 'decimal',
	    currency: 'USD',
	    minimumFractionDigits: 2,
	    maximumFractionDigits: 2
	})
	this.formData.revise = final
	return final
}
```

## version2
```js
let num=1234567; // 1,234,567
let numtostr = num.toString()
let str = ''
for(let i = numtostr.length - 1; i >= 0; i--){
	if((str.length + 1) % 4 == 0){
		str= ',' + str
		i++
	} else {
		str=numtostr[i] + str
	}
}
console.log(str);
```
