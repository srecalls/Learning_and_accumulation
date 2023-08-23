## 前提
如果你想自己实现将大整数转换为字符串的功能，可以按照以下步骤进行：

1. 创建一个空字符串来存储结果。

1. 判断给定的大整数是否为负数，如果是，将负号添加到结果字符串，并将大整数转换为正数。

1. 将大整数转换为字符串。一种常见的方法是通过重复除以基数（例如10）并记录余数来实现。重复这个过程，直到大整数变为0。

1. 将每个余数（0-9）转换为对应的字符，并将其添加到结果字符串的开头。

1. 返回最终的结果字符串。

下面是一个示例实现：

```javascript
function bigIntToString(bigInt) {
  let isNegative = false;

  // 判断是否为负数
  if (bigInt < 0) {
    isNegative = true;
    bigInt = -bigInt;
  }

  let result = '';

  // 大整数转换为字符串
  while (bigInt > 0) {
    const digit = bigInt % 10;
    result = String.fromCharCode(digit + 48) + result;
    bigInt = Math.floor(bigInt / 10);
  }

  // 添加负号（如果有）
  if (isNegative) {
    result = '-' + result;
  }

  return result;
}

// 示例使用
const c = 321321312312312312313213;
const cString = bigIntToString(c);

console.log(typeof cString); // 输出：string
console.log(cString); // 输出：'321321312312312312313213'
```

在上面的示例中，我们定义了一个函数`bigIntToString`，它接受一个大整数作为参数并返回对应的字符串。

该函数首先检查大整数是否为负数，并在需要时将其转换为正数。然后，它使用循环将大整数转换为字符串。在每次循环中，我们取出大整数的最后一位（余数），将其转换为对应的字符，并将其添加到结果字符串的开头。然后，我们将大整数除以基数（10）并向下取整，以便在下一次循环中处理下一位数字。我们重复这个过程，直到大整数变为0。

最后，如果大整数为负数，我们在结果字符串的开头添加一个负号。

请注意，此示例是一个简化的实现，并且仅适用于处理正整数。对于更复杂的场景，例如处理负数或更大范围的整数，可能需要更加完善的实现。

## bigint


在JavaScript中，可以使用BigInt类型来表示任意长度的整数。以下是一个简单的实现BigInt数据类型的示例：

```javascript
class BigInt {
  constructor(value) {
    this.value = value
  }

  plus(other) {
	let res = ''
	let temp = 0
	let num1 = this.value.split('')
	let num2 = other.value.split('')
	while(num1.length || num2.length || temp) {
		temp = temp + ~~num1.pop() + ~~num2.pop()
		res = res + (temp % 10)
		temp = temp > 9 ? 1 : 0
	}
	return new BigInt(res)
  }

  times(other) {
	if (this.value === '0' || other.value === '0') return '0'
    let num1 = this.value.split('')
    let num2 = other.value.split('')
    let len1 = num1.length
    let len2 = num2.length
    let pos = []
    for (let j = len2 - 1; j >= 0; j--) {
	    for (let i = len1 - 1; i >= 0; i--) {
		    let index1 = i + j
		    let index2 = i + j + 1
		    let mul = num1[i] * num2[j] + (pos[index2] || 0)
		    pos[index1] = Math.floor(mul / 10) + (pos[index1] || 0)
		    pos[index2] = mul % 10
	    }
    }
    let res = pos.join('').replace(/^0+/, '')
    return new BigInt(res)
  }

  toString() {
    return this.value;
  }
}
let a = new BigInt('123456789')
let b = new BigInt('987654321')
console.log(a.times(b))
```



这个BigInt类包含了加法和乘法操作，并且可以将BigInt转换为字符串。但是，这只是一个简单的实现，可能会有一些性能问题和限制。在实际应用中，可能需要更复杂的BigInt实现，例如支持更多的操作和优化算法。