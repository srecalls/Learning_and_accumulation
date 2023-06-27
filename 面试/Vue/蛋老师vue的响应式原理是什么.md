```js

```
![[Pasted image 20230524011930.png]]
![[Pasted image 20230524011913.png]]
![[Pasted image 20230524013755.png]]
![[Pasted image 20230524015014.png]]

Document.createDocumentFragment
https://developer.mozilla.org/zh-CN/docs/Web/API/Document/createDocumentFragment

append
# Element.append()
https://developer.mozilla.org/zh-CN/docs/Web/API/Element/append












通过数据劫持和发布订阅者模式来实现，同时利用O
![[Pasted image 20230410124428.png]]
通过数据劫持和发布订阅者模式来实现，同时利用object . defineProperty()劫持各个属性的setter和getter,
在数据发生改变的时候发布消息给订阅者，触发对应的监听回调演染视图，也就是说数据和视图时同步的，数据发生改变，视图跟着发生改变，视图改变，数据也会发生改变。
Vue.js 是采用数据劫持结合发布者-订阅者模式的方式，通过Object.defineProperty()来劫持各个属性的setter，getter，在数据变动时发布消息给订阅者，触发相应的监听回调。主要分为以下几个步骤:

		1. 需要observe的数据对象进行递归遍历，包括子属性对象的属性，都加上setter和getter这样的话，给这个对象的某个值赋值，就会触发setter，那么就能监听到了数据变化
		2. compile解析模板指令，将模板中的变量替换成数据，然后初始化渲染页面视图，并将每个指令对应的节点绑定更新函数，添加监听数据的订阅者，一旦数据有变动，收到通知，更新视图
		3. Watcher订阅者是Observer和Compile之间通信的桥梁，主要做的事情是: 
		   1. 在自身实例化时往属性订阅器(dep)里面添加自己
		   2. 自身必须有一个update()方法 
		   3. 待属性变动dep.notice()通知时，能调用自身的update()方法，并触发Compile中绑定的回调
		4. MVVM作为数据绑定的入口，整合Observer、Compile和Watcher三者，通过Observer来监听自己的model数据变化，通过Compile来解析编译模板指令，最终利用Watcher搭起Observer和Compile之间的通信桥梁，达到数据变化 ->视图更新，视图交互变化(input) -> 数据model变更的双向绑定效果。



比如说，当在输入框输入文字时，vue会检测到数据的变化，然后更新对应的视图。同样，如果你通过代码修改了数据，那么vue也会自动更新视图，其原理是通过数据劫持和发布订阅模式实现的。  
  
首先，Vue通过Object.defineProperty()方法对数据进行劫持，监听数据的变化，并通过getter和setter方法对数据进行读写。  
其次，Vue通过发布订阅模式，维护了一个订阅者数组，当数据发生变化时，Vue会通知所有订阅者进行更新。因此，当用户在页面上进行修改时，Vue会更新对应的数据，并更新所有订阅者更新视图，同时当数据发生变化时，Vue也会更新对应的视图，通过这样的机制，Vue实现了双向数据绑定，使得数据和视图的变化可以互相影响  
  
补充：订阅者是Vue中的一个概念，它是一个用于管理更新视图的对象，当数据发生变化时，Vue会通知所有的订阅者进行更新，在Vue中，每一个挂载到视图上的组件，或者每一个watcher，都可以被看成一个订阅者，他们订阅了某一个数据的变化，并等待数据发生变化时进行更新，订阅者是Vue实现双向数据绑定的关键组成部分，管理着数据和视图之间的关系，保证了数据的变化能够及时反应到视图上
![[Pasted image 20230627153705.png]]

```js
class Vue {
    constructor(obj_instance) {
        this.$data =obj_instance.$data
        Observer(this.$data)
        compile(obj_instance.el, this)
    }
}

// 数据劫持 - 监听实例里的数据
function Observer(data_instance) {
    // 递归出口
    if (!data_instance || typeof data_instance !== 'object') return
    Object.keys(data_instance).forEach(key => {
        let value = data_instance[key]
        Observer(value) // 递归 - 子属性数据劫持
        Object.defineProperty(data_instance, key, {
            enumerable: true,
            configurable: true,
            get() {
                console.log(`访问了属性: ${key} -> 值: ${value}`)
                // 订阅者加入依赖实例的数组
                Dependency.temp && Dependency.addSub(Dependency.temp)
                return value
            },
            set(newValue) {
                console.log(`属性${key}的值${value}修改为 -> ${newValue}`)
                value = newValue
                Observer(newValue)
                Dependency.notify()
            }
        })
    })
}

function compile(element, vm) {
    vm.$el = document.querySelector(element)
    const fragment = document.createDocumentFragment()
    let child
    while (child = vm.$el.firstChild) {
        fragment.append(child)
    }
    fragment_compile(fragment)
    // 替换文档碎片内容
    function fragment_compile(node) {
        const pattern = /\{\{\s*{\S+}\s*\}\}/
        if (node.nodeType === 3) {
            const xxx = node.value
            const result_regex = pattern.exec(node.nodeValue)
            if(result_regex) {
                const arr = result_regex[1].split('.')
                const value = arr.reduce(
                    (total, current) => total[current], vm.$data
                )
                node.nodeValue = xxx.replace(pattern, value)
                // 创建订阅者
                new Watcher(vm, result_regex[1], newValue => {
                    node.nodeValue = xxx.replace(pattern, newValue)
                })
            }
            return
        }
        if(node.nodeType === 1 && node.nodeName === 'INPUT') {
            const attr = Array.from(node.attributes)
            attr.forEach(i => {
                if(i.nodeName === 'v-model') {
                    const value = i.nodeValue.split('.').reduce(
                        (total, current) => total[current], vm.$data
                    )
                    node.value = value
                    new Watcher(vm, i.nodeValue, newValue => {
                        node.value = newValue
                    })
                    // 视图更新数据
                    node.addEventListener('input', e => {
                        // ['more', 'like']
                        const arr1 = i.nodeValue.split('.')
                        // ['more']
                        const arr2 = arr1.slice(0, arr1.length - 1)
                        // vm.$data.more
                        const final = arr2.reduce(
                            (total, current) => total[current], vm.$data
                        )
                        // vm.$data.more['like'] = e.target.value
                        final[arr1[arr1.length - 1]] = e.target.value
                    })
                }
            })
        }
        node.childNodes.forEach(child => fragment_compile(child))
    }
    vm.$el.appendChild(fragment)
}

// 依赖 - 收集和通知订阅者
class Dependency {
    constructor() {
        this.subscribers = []
    }
    addSub(sub) {
        this.subscribers.push(sub)
    }
    notify() {
        this.subscribers.forEach(sub => sub.update())
    }
}

// 订阅者 
class Watcher {
    constructor(vm, key, callback) {
        this.vm = vm
        this.key = key
        this.callback = callback
        // 临时属性 - 触发getter
        Dependency.temp = this
        key.split('.').reduce((total, current) => total[current], vm.$data)
    }
    update() {
        const value = this.key.split('.').reduce(
            (total, current) => total[current], this.vm.$data
        )
        this.callback(value)
    }
}
```


好的，下面我将对每一部分进行更加详细的介绍。

首先是Vue类：

```javascript
class Vue {
    constructor(obj_instance) {
        this.$data =obj_instance.$data
        Observer(this.$data)
        Complie(obj_instance.el, this)
    }
}
```

在构造函数中，我们从传入的对象实例中获取数据，并对数据进行数据劫持和模板编译。这个构造函数中使用了 Observer 和 Complie 两个函数，我们接下来分别介绍这两个函数。

## Observer 函数：

```javascript
function Observer(data_instance) {
    // 递归出口
    if (!data_instance || typeof data_instance !== 'object') return
    Object.keys(data_instance).forEach(key => {
        let value = data_instance[key]
        Observer(value) // 递归 - 子属性数据劫持
        Object.defineProperty(data_instance, key, {
            enumerable: true,
            configurable: true,
            get() {
                console.log(`访问了属性: ${key} -> 值: ${value}`)
                // 订阅者加入依赖实例的数组
                Dependency.temp && Dependency.addSub(Dependency.temp)
                return value
            },
            set(newValue) {
                console.log(`属性${key}的值${value}修改为 -> ${newValue}`)
                value = newValue
                Observer(newValue)
                Dependency.notify()
            }
        })
    })
}
```

Observer 函数实现了数据劫持的功能。它通过递归遍历对象的每个属性，为每个属性定义getter和setter，实现对属性的监听和更新。在getter中，我们将订阅者加入依赖实例的数组，以便数据更新时通知订阅者。在setter中，我们触发依赖的更新。

## Compile 函数：

```javascript
function Compile(element, vm) {
    vm.$el = document.querySelector(element)
    const fragment = document.createDocumentFragment()
    let child
    while (child = vm.$el.firstChild) {
        fragment.append(child)
    }
    fragment_compile(fragment)
    // 替换文档碎片内容
    function fragment_compile(node) {
        const pattern = /\{\{\s*{\S+}\s*\}\}/
        if (node.nodeType === 3) {
            const xxx = node.value
            const result_regex = pattern.exec(node.nodeValue)
            if(result_regex) {
                const arr = result_regex[1].split('.')
                const value = arr.reduce(
                    (total, current) => total[current], vm.$data
                )
                node.nodeValue = xxx.replace(pattern, value)
                // 创建订阅者
                new Watcher(vm, result_regex[1], newValue => {
                    node.nodeValue = xxx.replace(pattern, newValue)
                })
            }
            return
        }
        if(node.nodeType === 1 && node.nodeName === 'INPUT') {
            const attr = Array.from(node.attributes)
            attr.forEach(i => {
                if(i.nodeName === 'v-model') {
                    const value = i.nodeValue.split('.').reduce(
                        (total, current) => total[current], vm.$data
                    )
                    node.value = value
                    new Watcher(vm, i.nodeValue, newValue => {
                        node.value = newValue
                    })
                    node.addEventListener('input', e => {
                        // ['more', 'like']
                        const arr1 = i.nodeValue.split('.')
                        // ['more']
                        const arr2 = arr1.slice(0, arr1.length - 1)
                        // vm.$data.more
                        const final = arr2.reduce(
                            (total, current) => total[current], vm.$data
                        )
                        // vm.$data.more['like'] = e.target.value
                        final[arr1[arr1.length - 1]] = e.target.value
                    })
                }
            })
        }
        node.childNodes.forEach(child => fragment_compile(child))
    }
    vm.$el.appendChild(fragment)
}
```

Complie 函数实现了模板编译的功能。首先，它将Vue模板解析成DOM树，并将DOM树保存在文档碎片中。然后，它遍历DOM树，对于每个文本节点，如果匹配到模板语法，创建一个订阅者对象，同时在输入框中，如果匹配到v-model指令，为其创建一个订阅者对象，并监听输入事件，将输入的值同步到数据中。

#### compile详细
Vue模板是一种类似HTML的语法，用于描述页面的结构和数据绑定关系。在Vue中，我们可以在模板中嵌入表达式、指令、事件等，从而实现数据绑定、条件渲染、列表渲染、样式绑定等功能。

在Vue框架中，模板编译是将Vue模板转化为可执行的JavaScript代码的过程。在编译过程中，我们需要对模板中的指令、表达式等进行解析，生成相应的渲染函数，并将渲染函数与Vue实例建立关联，从而实现数据的响应式更新。

下面是Vue框架中的compile函数的具体实现。在这个函数中，我们首先通过document.querySelector方法获取到模板对应的DOM节点，然后使用DocumentFragment来创建一个文档碎片，接着将原始DOM节点中的所有子节点追加到文档碎片中。

```javascript
function Complie(element, vm) {
    vm.$el = document.querySelector(element)
    const fragment = document.createDocumentFragment()
    let child
    while (child = vm.$el.firstChild) {
        fragment.append(child)
    }
```

接下来，我们对文档碎片中的每个节点进行递归处理，如果节点是文本节点，并且匹配到了模板语法，则创建一个订阅者对象，并将其加入到依赖实例的订阅者数组中。如果节点是输入框，并且匹配到了v-model指令，则为其创建一个订阅者对象，并监听输入事件，将输入的值同步到数据中。最后，我们递归处理节点的子节点。

```javascript
    fragment_compile(fragment)
    // 替换文档碎片内容
    function fragment_compile(node) {
        const pattern = /\{\{\s*{\S+}\s*\}\}/
        if (node.nodeType === 3) {
            const xxx = node.value
            const result_regex = pattern.exec(node.nodeValue)
            if(result_regex) {
                const arr = result_regex[1].split('.')
                const value = arr.reduce(
                    (total, current) => total[current], vm.$data
                )
                node.nodeValue = xxx.replace(pattern, value)
                // 创建订阅者
                new Watcher(vm, result_regex[1], newValue => {
                    node.nodeValue = xxx.replace(pattern, newValue)
                })
            }
            return
        }
        if(node.nodeType === 1 && node.nodeName === 'INPUT') {
            const attr = Array.from(node.attributes)
            attr.forEach(i => {
                if(i.nodeName === 'v-model') {
                    const value = i.nodeValue.split('.').reduce(
                        (total, current) => total[current], vm.$data
                    )
                    node.value = value
                    new Watcher(vm, i.nodeValue, newValue => {
                        node.value = newValue
                    })
                    node.addEventListener('input', e => {
                        // ['more', 'like']
                        const arr1 = i.nodeValue.split('.')
                        // ['more']
                        const arr2 = arr1.slice(0, arr1.length - 1)
                        // vm.$data.more
                        const final = arr2.reduce(
                            (total, current) => total[current], vm.$data
                        )
                        // vm.$data.more['like'] = e.target.value
                        final[arr1[arr1.length - 1]] = e.target.value
                    })
                }
            })
        }
        node.childNodes.forEach(child => fragment_compile(child))
    }
    vm.$el.appendChild(fragment)
}
```

在编译过程中，我们将模板解析成DOM树，并将其保存在文档碎片中。通过对DOM树的遍历，我们实现了对模板语法的解析，并创建了相应的订阅者对象，从而实现了数据的响应式更新。最终，我们将文档碎片的内容替换回原始的DOM节点中，完成了模板的编译过程。

## 订阅者类 Watcher：

```javascript
class Watcher {
    constructor(vm, key, callback) {
        this.vm = vm
        this.key = key
        this.callback = callback
        // 临时属性 - 触发getter
        Dependency.temp = this
        key.split('.').reduce((total, current) => total[current], vm.$data)
    }
    update() {
        const value = this.key.split('.').reduce(
            (total, current) => total[current], this.vm.$data
        )
        this.callback(value)
    }
}
```

Watcher 类用于观察数据变化并执行回调函数，其中构造函数中将订阅者加入依赖实例的数组并触发getter，update函数中获取最新的数据值并执行回调函数。

## 依赖类 Dependency：

```javascript
class Dependency {
    constructor() {
        this.subscribers = []
    }
    addSub(sub) {
        this.subscribers.push(sub)
    }
    notify() {
        this.subscribers.forEach(sub => sub.update())
    }
}
```

Dependency 类用于收集和通知订阅者的变化。它具有一个订阅者数组和两个方法，addSub 用于添加订阅者，notify 用于通知所有订阅者。

总的来说，这段代码实现了一个简单的双向数据绑定的Vue框架，它包括了数据劫持、模板编译、订阅者和依赖等核心功能。这个框架可以帮助我们更加方便地实现数据的响应式更新，从而提高开发效率。


## 双向数据绑定过程
Vue的双向数据绑定是指，当数据发生变化时，视图会自动更新，当用户在视图中输入数据时，数据也会自动更新。这一过程实际上是通过Vue的响应式系统来实现的，下面是一个完整的双向数据绑定的过程：

### 1. 初始化Vue实例

在初始化Vue实例时，Vue会对数据对象进行递归遍历，将每个属性都转换为getter/setter，并且在内部维护一个依赖列表。当数据发生变化时，Vue会通知依赖列表中所有的Watcher对象，通知它们重新渲染视图。

### 2. 解析模板

Vue的模板可以包含大量的指令和表达式，这些指令和表达式需要被解析，并转换为可执行的JavaScript代码。在解析模板时，Vue会根据指令和表达式创建Watcher对象，并将其加入到依赖列表中。

### 3. 渲染视图

Vue使用Virtual DOM来渲染视图，当数据发生变化时，Vue会重新计算Virtual DOM的差异，并将差异应用到真实的DOM上，从而更新视图。在计算Virtual DOM的过程中，Vue会调用Watcher对象的update方法，该方法会触发视图的重新渲染。

### 4. 用户输入数据

当用户在视图中输入数据时，Vue会通过v-model指令将输入框的值与数据对象中的对应属性双向绑定。在绑定过程中，Vue会创建一个Watcher对象，用于监听数据对象中对应属性的变化，当数据发生变化时，Watcher对象会通知绑定的视图更新。

### 5. 数据变化

当数据对象中的属性发生变化时，Vue会通过触发setter方法来通知依赖列表中的Watcher对象。Watcher对象会将通知转发给对应的视图组件，从而触发视图的重新渲染。

### 6. 视图更新

当视图重新渲染时，Vue会重新计算Virtual DOM的差异，并将差异应用到真实的DOM上，从而更新视图。在计算Virtual DOM的过程中，Vue会调用Watcher对象的update方法，该方法会触发视图的重新渲染。

通过上述过程，Vue实现了双向数据绑定，使得数据和视图之间能够自动同步更新，从而提高了开发效率和用户体验。