```js
<template>
    <bk-dialog v-model="isShowManual"> // 直接修改
        <!-- <div slot="header">
            title
        </div> -->
        <!-- <bk-from>
            <bk-form-item>
            </bk-form-item>
        </bk-from> -->
    </bk-dialog>
</template>

<script>
    export default {
        name: 'backup-dialog',
        props: {
            isShowManual: {
                type: Boolean,
                defalut: false
            },
            isShowAutomatic: {
                type: Boolean,
                defalut: false
            }
        },
```



`[Vue warn]: Avoid mutating a prop directly since the value will be overwritten whenever the parent component re-renders. Instead, use a data or computed property based on the prop's value. Prop being mutated: "isShowManual"`
这个Vue警告的意思是，你正在直接修改一个从父组件传递下来的prop值，这是不推荐的，因为当父组件重新渲染时，该prop的值会被覆盖。Vue的单向数据流规则要求子组件不能直接修改父组件传递下来的prop值，而应该通过触发事件来通知父组件进行修改。

解决这个问题的方法是，在子组件中定义一个与prop值相对应的data或computed属性，然后通过这个属性来修改子组件的状态。例如，如果你的prop名为`isShowManual`，则可以在子组件中定义一个data属性：

```js
props: {
  isShowManual: {
    type: Boolean,
    required: true
  }
},
data() {
  return {
    showManual: this.isShowManual
  }
}
```

在这个例子中，我们定义了一个名为`showManual`的data属性，并将其初始化为`isShowManual`的值。然后，我们在子组件中使用`showManual`来控制显示或隐藏相应的内容。如果需要修改`showManual`的值，可以在子组件中使用`this.showManual = newValue`，而不是直接修改`isShowManual`的值。

## 修改父组件的值
如果你需要将修改后的值传递给父组件，可以在子组件中定义一个自定义事件，然后通过这个事件来通知父组件进行修改。例如：

```js
this.$emit('update:isShowManual', newValue);
```

在这个例子中，我们定义了一个名为`update:isShowManual`的自定义事件，并将修改后的值作为参数传递给父组件。父组件可以通过监听这个事件来接收新的值，并进行相应的操作。

总之，避免直接修改从父组件传递下来的prop值是Vue编程中的重要原则之一。如果需要修改prop的值，应该通过定义data或computed属性来进行，并通过事件来通知父组件进行修改。



```js
<template>
    <bk-dialog v-model="isShowManual">
        <!-- <div slot="header">
            title
        </div> -->
        <!-- <bk-from>
            <bk-form-item>
            </bk-form-item>
        </bk-from> -->
    </bk-dialog>
</template>

<script>
    export default {
        name: 'backup-dialog',
        props: {
            isShowManual: {
                type: Boolean,
                defalut: false
            },
            isShowAutomatic: {
                type: Boolean,
                defalut: false
            }
        },
        data() {
            return {
                // showManual: this.isShowManual,
                // showAutomatic: this.isShowAutomatic
            }
        },
        computed: {
            showManual() {
                return this.isShowManual
            }
        },
```


## 不修改
你的处理方式是比较接近推荐的做法的。你在子组件中定义了一个名为`isShowManual`的prop，然后通过计算属性`showManual`来将其映射到子组件的状态中。这样做的好处是，你可以在子组件中修改`showManual`的值，而不会影响到从父组件传递下来的`isShowManual`的值，从而避免了直接修改prop值的问题。

不过，你的代码中有一个小问题。在`props`中定义`isShowManual`和`isShowAutomatic`时，你将`default`拼写成了`defalut`，这会导致默认值无法生效。正确的写法应该是：

```js
props: {
  isShowManual: {
    type: Boolean,
    default: false
  },
  isShowAutomatic: {
    type: Boolean,
    default: false
  }
},
```

另外，如果你想要在子组件中修改`showManual`的值并将其传递给父组件，你需要在子组件中触发一个名为`update:isShowManual`的事件。你可以通过`$emit`方法来触发这个事件，例如：

```js
this.$emit('update:isShowManual', newValue);
```

在这个例子中，我们触发了一个名为`update:isShowManual`的自定义事件，并将修改后的值作为参数传递给父组件。父组件可以通过监听这个事件来接收新的值，并进行相应的操作。


## 父组件怎么写
在父组件中，你需要监听子组件触发的自定义事件，并更新相应的prop值。具体来说，你可以在子组件上使用`v-model`指令来将`isShowManual`绑定到父组件上，例如：

```html
<backup-dialog v-model="isShowManual"></backup-dialog>
```

在这个例子中，我们使用了`v-model`指令来将子组件的`isShowManual`属性双向绑定到父组件的`isShowManual`属性上。这样，在子组件中修改`isShowManual`的值时，就会自动触发一个名为`update:isShowManual`的自定义事件，并将修改后的值作为参数传递给父组件。父组件可以通过监听这个事件，从而更新`isShowManual`的值。在父组件中，你可以这样写：

```html
<template>
  <div>
    <backup-dialog v-model="isShowManual"></backup-dialog>
    <!-- 其他组件 -->
  </div>
</template>

<script>
  import BackupDialog from './BackupDialog.vue';

  export default {
    components: {
      BackupDialog
    },
    data() {
      return {
        isShowManual: false
      }
    },
    methods: {
      handleShowManual(newValue) {
        this.isShowManual = newValue;
      }
    },
    created() {
      this.$on('update:isShowManual', this.handleShowManual);
    },
    destroyed() {
      this.$off('update:isShowManual', this.handleShowManual);
    }
  }
</script>
```

在这个例子中，我们在父组件中定义了一个名为`isShowManual`的data属性，并将其初始化为`false`。然后，我们在父组件的`created`生命周期钩子中监听子组件触发的`update:isShowManual`事件，并在事件处理函数中更新`isShowManual`的值。需要注意的是，在父组件销毁时，我们需要使用`$off`方法来移除事件监听器，避免内存泄漏。


## 子组件怎么写
在子组件中，你需要定义一个名为`isShowManual`的prop，并将其双向绑定到`visible`属性上，例如：

```html
<template>
  <bk-dialog v-model="visible">
    <!-- 对话框的内容 -->
  </bk-dialog>
</template>

<script>
  export default {
    name: 'BackupDialog',
    props: {
      isShowManual: {
        type: Boolean,
        default: false
      }
    },
    computed: {
      visible: {
        get() {
          return this.isShowManual;
        },
        set(value) {
          this.$emit('update:isShowManual', value);
        }
      }
    }
  }
</script>
```

在这个例子中，我们定义了一个名为`isShowManual`的prop，并将其默认值设置为`false`。然后，我们使用`v-model`指令来将子组件的`visible`属性双向绑定到`isShowManual`上。在`computed`属性中，我们定义了一个名为`visible`的计算属性，并将其`get`方法返回`isShowManual`的值，将其`set`方法触发一个名为`update:isShowManual`的自定义事件，并将修改后的值作为参数传递给父组件。这样，当子组件中的`visible`属性发生变化时，就会自动触发一个`update:isShowManual`事件，从而将修改后的值传递给父组件。

需要注意的是，为了使`v-model`指令能够正常工作，你需要将子组件内部的`visible`属性与父组件传递下来的`isShowManual`属性保持同步。在上面的代码中，我们通过计算属性`visible`来实现这一点。在子组件中，你应该尽量避免直接修改从父组件传递下来的prop值，而应该通过触发事件来通知父组件进行修改。


## 如果用data 的话就用watch
你可以使用`data`选项来定义一个名为`visible`的状态，并在`props`选项中定义一个名为`isShowManual`的prop，然后在`created`生命周期钩子中将`isShowManual`的值赋值给`visible`。这样，当`isShowManual`的值发生变化时，`visible`的值也会同步更新。具体来说，你可以这样写：

```html
<template>
  <bk-dialog :visible="visible">
    <!-- 对话框的内容 -->
  </bk-dialog>
</template>

<script>
  export default {
    name: 'BackupDialog',
    props: {
      isShowManual: {
        type: Boolean,
        default: false
      }
    },
    data() {
      return {
        visible: this.isShowManual
      }
    },
    created() {
      this.visible = this.isShowManual;
    },
    watch: {
      isShowManual(newValue) {
        this.visible = newValue;
      }
    }
  }
</script>
```

在这个例子中，我们定义了一个名为`visible`的状态，并将其初始化为`isShowManual`的值。然后，我们在`created`生命周期钩子中将`isShowManual`的值赋值给`visible`，以确保二者初始值相同。在`watch`选项中，我们监听`isShowManual`的变化，并在变化时将其值赋值给`visible`，以确保二者始终保持同步。

需要注意的是，直接在子组件中修改从父组件传递下来的prop值是不推荐的做法，因为这会导致Vue的警告。如果你要修改prop的值，你应该通过触发一个自定义事件来通知父组件进行修改，这样才能避免这个问题。


## final
根据你的代码，可以使用以下方式来修改子组件：

```html
<template>
  <bk-dialog v-model="visible">
    <!-- 对话框的内容 -->
  </bk-dialog>
</template>

<script>
  export default {
    name: 'BackupDialog',
    props: {
      isShowManual: {
        type: Boolean,
        default: false
      }
    },
    data() {
      return {
        visible: this.isShowManual
      }
    },
    watch: {
      isShowManual(newValue) {
        this.visible = newValue;
      }
    }
  }
</script>
```

在这个例子中，我们使用了`v-model`指令来绑定`visible`状态，并在`props`选项中定义了一个名为`isShowManual`的属性。在`data`选项中，我们将`isShowManual`的值赋值给了`visible`，以确保二者初始值相同。然后，我们在`watch`选项中监听`isShowManual`的变化，并在变化时将其值赋值给`visible`，以确保二者始终保持同步。

在父组件中使用子组件时，你需要将`showManualBackup`作为`is-show-manual`的值传递给子组件，例如：

```html
<backup-dialog :is-show-manual="showManualBackup"></backup-dialog>
```

在这个例子中，我们使用了`v-bind:is-show-manual="showManualBackup"`来将父组件的`showManualBackup`属性传递给子组件的`is-show-manual`属性。当父组件中的`showManualBackup`属性发生变化时，子组件的`is-show-manual`属性也会相应地发生变化，并且子组件的`visible`状态也会随之变化。


