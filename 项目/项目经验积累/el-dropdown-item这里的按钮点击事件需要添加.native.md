在使用`el-dropdown-item`组件时，如果想要在按钮被点击时触发一个原生的事件（即不是Vue组件自身的事件），需要使用`.native`修饰符。

例如，如果你想要在`el-dropdown-item`按钮被点击时触发一个`click`事件，可以这样写：
```html
<el-dropdown-item @click.native="handleClick">按钮</el-dropdown-item>

```
在这个例子中，`@click.native`表示绑定原生的`click`事件，而不是`el-dropdown-item`自身的`click`事件。当按钮被点击时，`handleClick`方法会被调用。

需要注意的是，如果你使用了`@click`而没有使用`.native`修饰符，那么实际上绑定的是`el-dropdown-item`自身的`click`事件，而不是原生的`click`事件。因此，如果你想要绑定原生的事件，请务必使用`.native`修饰符。