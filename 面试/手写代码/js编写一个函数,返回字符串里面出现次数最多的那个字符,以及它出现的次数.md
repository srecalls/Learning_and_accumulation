好的，以下是一个实现该功能的 JavaScript 函数：

```javascript
function findMostFrequentChar(str) {
  // 用一个对象来记录每个字符出现的次数
  const charCount = {};
  for (let i = 0; i < str.length; i++) {
    const char = str[i];
    charCount[char] = charCount[char] ? charCount[char] + 1 : 1;
  }

  // 遍历对象，找到出现次数最多的字符
  let mostFrequentChar = '';
  let maxCount = 0;
  for (const char in charCount) {
    if (charCount[char] > maxCount) {
      mostFrequentChar = char;
      maxCount = charCount[char];
    }
  }

  return { char: mostFrequentChar, count: maxCount };
}
```

该函数接受一个字符串作为参数，返回一个对象，该对象包含字符串中出现次数最多的那个字符及其出现的次数。该函数首先遍历字符串，用一个对象来记录每个字符出现的次数，然后遍历对象，找到出现次数最多的字符。最后返回一个包含最多字符和出现次数的对象。