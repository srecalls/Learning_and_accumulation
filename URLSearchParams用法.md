`URLSearchParams` 是 JavaScript 中用于处理 URL 查询字符串的一个内置接口，它提供了一系列方法来操作查询参数。通过 `URLSearchParams`，开发者可以轻松地解析、修改和生成 URL 查询字符串，而无需手动进行字符串拼接或解析。下面详细介绍其用法。

### 创建 `URLSearchParams` 实例

可以通过多种方式创建 `URLSearchParams` 实例：

1. **不传参数**：创建一个空的 `URLSearchParams` 对象。
   ```javascript
   const params = new URLSearchParams();
   console.log(params.toString()); // 输出: ""
   ```

2. **传入字符串**：传入一个查询字符串，`URLSearchParams` 会自动解析该字符串。
   ```javascript
   const paramsString = "name=John&age=30";
   const searchParams = new URLSearchParams(paramsString);
   console.log(searchParams.get('name')); // 输出: "John"
   ```

3. **传入数组**：传入一个二维数组，每个子数组包含键值对。
   ```javascript
   const paramsArray = [['name', 'John'], ['age', '30']];
   const searchParams = new URLSearchParams(paramsArray);
   console.log(searchParams.get('age')); // 输出: "30"
   ```

4. **传入对象**：传入一个对象，键为参数名，值为参数值。
   ```javascript
   const paramsObject = { name: 'John', age: '30' };
   const searchParams = new URLSearchParams(paramsObject);
   console.log(searchParams.get('name')); // 输出: "John"
   ```

5. **从 URL 对象中获取**：可以从 `URL` 对象中直接获取 `searchParams` 属性。
   ```javascript
   const url = new URL("https://example.com/?name=John&age=30");
   const searchParams = url.searchParams;
   console.log(searchParams.get('age')); // 输出: "30"
   ```

### 常用方法

`URLSearchParams` 提供了许多实用的方法来操作查询参数：

- **`append(name, value)`**：添加一个新的键值对。
  ```javascript
  const params = new URLSearchParams();
  params.append('name', 'John');
  console.log(params.toString()); // 输出: "name=John"
  ```

- **`delete(name)`**：删除指定的键及其对应的值。
  ```javascript
  const params = new URLSearchParams("name=John&age=30");
  params.delete('age');
  console.log(params.toString()); // 输出: "name=John"
  ```

- **`get(name)`**：获取指定键的第一个值。
  ```javascript
  const params = new URLSearchParams("name=John&name=Doe");
  console.log(params.get('name')); // 输出: "John"
  ```

- **`getAll(name)`**：获取指定键的所有值，返回一个数组。
  ```javascript
  const params = new URLSearchParams("name=John&name=Doe");
  console.log(params.getAll('name')); // 输出: ["John", "Doe"]
  ```

- **`has(name)`**：检查是否存在指定的键。
  ```javascript
  const params = new URLSearchParams("name=John");
  console.log(params.has('name')); // 输出: true
  console.log(params.has('age')); // 输出: false
  ```

- **`set(name, value)`**：设置指定键的新值，如果存在多个值，则删除其他所有值。
  ```javascript
  const params = new URLSearchParams("name=John&name=Doe");
  params.set('name', 'Jane');
  console.log(params.getAll('name')); // 输出: ["Jane"]
  ```

- **`sort()`**：按键名排序。
  ```javascript
  const params = new URLSearchParams("b=2&a=1");
  params.sort();
  console.log(params.toString()); // 输出: "a=1&b=2"
  ```

- **`toString()`**：返回查询参数组成的字符串。
  ```javascript
  const params = new URLSearchParams("name=John&age=30");
  console.log(params.toString()); // 输出: "name=John&age=30"
  ```

### 遍历 `URLSearchParams`

`URLSearchParams` 实例可以直接用于 `for...of` 循环，也可以通过 `.entries()`、`.keys()` 和 `.values()` 方法来遍历。

```javascript
const params = new URLSearchParams("name=John&age=30");

// 使用 for...of
for (const [key, value] of params) {
  console.log(`${key}: ${value}`);
}

// 使用 entries()
for (const pair of params.entries()) {
  console.log(pair[0], pair[1]);
}

// 使用 keys()
for (const key of params.keys()) {
  console.log(key);
}

// 使用 values()
for (const value of params.values()) {
  console.log(value);
}
```

### 兼容性

`URLSearchParams` 在现代浏览器中得到了广泛支持，但在 IE 浏览器中不受支持。因此，在使用时需要考虑目标用户的浏览器环境，必要时可以使用 polyfill 来填补兼容性问题。

### 总结

`URLSearchParams` 提供了一种简单且强大的方式来处理 URL 查询字符串，使得开发者可以更加专注于业务逻辑而不是字符串操作。无论是解析现有 URL 的查询参数，还是构建新的查询字符串，`URLSearchParams` 都能高效完成任务。

### 不同场景的情况

```js
  // 测试空对象输入
  it('应该在输入为空对象时返回空字符串', () => {
    const result = queryBuilder({});
    expect(result).toBe('');
  });

  // 测试单个键值对输入
  it('应该正确处理单个键值对', () => {
    const result = queryBuilder({ key: 'value' });
    expect(result).toBe('key=value');
  });

  // 测试多个键值对输入
  it('应该正确处理多个键值对', () => {
    const result = queryBuilder({ key1: 'value1', key2: 'value2' });
    expect(result).toStrictEqual('key1=value1&key2=value2'); // 注意顺序可能不同
  });

  // 测试带有特殊字符的键或值
  it('应该正确编码带有特殊字符的键或值', () => {
    const result = queryBuilder({ key: 'val+ue=with&special#chars' });
    expect(result).toBe('key=val%2Bue%3Dwith%26special%23chars');
  });

  // 测试数组类型的值
  it('应该正确处理数组类型的值', () => {
    const result = queryBuilder({ key: ['value1', 'value2'] });
    expect(result).toBe('key=value1&key=value2');
  });

  // 测试嵌套对象类型的值
  it('应该忽略嵌套对象类型的值', () => {
    const result = queryBuilder({ key: { nestedKey: 'nestedValue' } });
    expect(result).toBe('key=[object%20Object]');
  });

  // 测试含有null或undefined的值
  it('应该忽略null或undefined的值', () => {
    const result = queryBuilder({ key1: null, key2: undefined, key3: 'value' });
    expect(result).toBe('key3=value');
  });
  ```