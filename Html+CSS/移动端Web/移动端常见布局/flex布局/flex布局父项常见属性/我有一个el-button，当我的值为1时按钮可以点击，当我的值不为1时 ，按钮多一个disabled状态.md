我有一个el-button，当我的值为1时按钮可以点击，当我的值不为1时 ，按钮多一个disabled状态
你可以使用 `:disabled` 属性来控制 `el-button` 是否可以点击。当值为1时，该属性不应该存在，因此按钮是可以点击的。当值不为1时，你可以添加 `:disabled` 属性，这将使按钮变成禁用状态。
以下是一个示例代码，可以帮助你更好地理解：
```css html
<template>
  <div>
    <el-button :disabled="value !== 1" @click="handleClick">Click me</el-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      value: 1
    };
  },
  methods: {
    handleClick() {
      // handle button click event
    }
  }
};
</script>
```

在上面的示例中，当 `value` 的值不为1时，`el-button` 将被禁用。当 `value` 的值为1时，按钮将可点击。如果需要更改按钮的状态，只需要更改 `value` 的值即可。