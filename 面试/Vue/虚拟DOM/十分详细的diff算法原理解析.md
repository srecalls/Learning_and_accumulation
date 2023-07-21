https://blog.csdn.net/m0_64023259/article/details/125476986
本文我们总结一下有关**diff**算法的相关内容和实现原理

开门见山，直接先给出大家**diff**算法的概念

**diff算法**可以看作是一种对比算法，对比的对象是**新旧虚拟Dom**。顾名思义，**diff算法**可以找到**新旧虚拟Dom**之间的差异，但**diff算法**中其实并不是只有对比**虚拟Dom**，还有根据对比后的结果更新**真实Dom**。

## 虚拟Dom
上面的概念我们提到了虚拟Dom，相信大家对这个名词并不陌生，下面为大家解释一下虚拟Dom的概念，以及diff算法中为什么要对比虚拟Dom，而不是直接去操作真实Dom。

**虚拟Dom，其实很简单，就是一个用来描述真实Dom的对象**

它有六个属性，`sel`表示当前节点标签名，`data`内是节点的属性，`children`表示当前节点的其他子标签节点，`elm`表示当前虚拟节点对应的真实节点（这里暂时没有），`key`即为当前节点的key，`text`表示当前节点下的文本，结构类似这样。
```js
let vnode = {
    sel: 'ul', 
    data: {},
    children: [ 
        {
            sel: 'li', data: { class: 'item' }, text: 'son1'
        },
        {
            sel: 'li', data: { class: 'item' }, text: 'son2'
        },    
    ],
    elm: undefined,
    key: undefined,
    text: undefined
}
```

那么虚拟Dom有什么用呢。我们其实可以把虚拟Dom理解成对应真实Dom的一种状态。当真实Dom发生变化后，虚拟Dom可以为我们提供这个真实Dom变化之前和变化之后的状态，我们通过对比这两个状态，即可得出真实Dom真正需要更新的部分，即可实现**最小量更新**。在一些比较复杂的Dom变化场景中，**通过对比虚拟Dom后更新真实Dom**会比**直接更新真实Dom的效率高**，这也就是虚拟Dom和diff算法真正存在的意义。

## h函数
在介绍diff算法原理之前还需要简单让大家了解一下**h函数**，因为我们要靠它为我们生成虚拟Dom。这个**h函数**大家应该也比较熟悉，就是render函数里面传入的那个**h函数**。
**h函数**可以接受多种类型的参数，但其实它内部只干了一件事，就是执行`vnode函数`。根据传入**h函数**的参数来决定执行`vnode函数`时传入的参数。那么`vnode函数`又是干什么的呢？`vnode函数`其实也只干了一件事，就是把传入**h函数**的参数转化为一个对象，即虚拟Dom。
```js
// vnode.js
export default function (sel, data, children, text, elm) {
    const key = data.key 
    return {sel, data, children, text, elm, key}
}
```
执行**h函数**后，内部会通过`vnode函数`生成虚拟Dom，**h函数**把这个虚拟在return出去。

```js
import App from './App.vue'
new Vue({
  router,
  store,
  i18n,
  // init localstorage, vuex, Logo message
  created: bootstrap,
  render: h => h(App)
}).$mount('#app')

```

## diff对比规则
明确了**h函数是干什么的**，我们可以简单用**h函数**生成两个不同的虚拟节点，我们将通过一个简易版的diff算法代码介绍diff对比的具体流程。
```js
// 第一个参数是sel 第二个参数是data 第三个参数是children
const myVnode1 = h("h1", {}, [
  h("p", {key: "a"}, "a"),
  h("p", {key: "b"}, "b"),
]);
​
const myVnode2 = h("h1", {}, [
  h("p", {key: "c"}, "c"),
  h("p", {key: "d"}, "d"),
]);
```

### patch
比较的第一步就是执行**patch**，它相当于对比的入口。既然是对比两个虚拟Dom，那么就将两个虚拟Dom作为参数传入**patch**中。**patch**的主要作用是对比两个虚拟Dom的根节点，并根据对比结果操作真实Dom。
patch函数的核心代码如下，注意注释。
```js
// patch.js
​
import vnode from "./vnode"
import patchDetails from "./patchVnode"
import createEle from "./createEle"
​
/**
 * @description 用来对比两个虚拟dom的根节点，并根据对比结果操作真实Dom
 * @param {*} oldVnode 
 * @param {*} newVnode 
 */
export function patch(oldVnode, newVnode) {
  // 1.判断oldVnode是否为虚拟节点，不是的话转化为虚拟节点
  if(!oldVnode.sel) {
    // 转化为虚拟节点
    oldVnode = vnode(oldVnode.tagName.toLowerCase(), {}, [], undefined, oldVnode)
  }
​
  // 2.判断oldVnode和newVnode是否为同一个节点
  if(oldVnode.key == newVnode.key && oldVnode.sel == newVnode.sel) {
    console.log('是同一个节点')
    // 比较子节点
    patchDetails(oldVnode, newVnode)
  }else {
    console.log('不是同一个节点')
    // 插入newVnode 
    const newNode = createEle(newVnode) // 插入之前需要先将newVnode转化为dom
    oldVnode.elm.parentNode.insertBefore(newNode, oldVnode.elm) // 插入操作
    // 删除oldVnode
    oldVnode.elm.parentNode.removeChild(oldVnode.elm)
  }
}
​
// createEle.js
​
/**
 * @description 根据传入的虚拟Dom生成真实Dom
 * @param {*} vnode 
 * @returns real node
 */
export default function createEle (vnode) {
  const realNode = document.createElement(vnode.sel)
​
  // 子节点转换
  if(vnode.text && (vnode.children == undefined || (vnode.children && vnode.children.length == 0)) ) {
    // 子节点只含有文本
    realNode.innerText = vnode.text  
  }else if(Array.isArray(vnode.children) && vnode.children.length > 0) {
    // 子节点为其他虚拟节点 递归添加node
    for(let i = 0; i < vnode.children.length; i++) {
      const childNode = createEle(vnode.children[i])
      realNode.appendChild(childNode)
    }
  }
​
  // 补充vnode的elm属性
  vnode.elm = realNode
​
  return vnode.elm
}

```

### patchVnode
**patchVnode**用来比较两个虚拟节点的子节点并更新其子节点对应的真实Dom节点
```js
// patchVnode.js
​
import updateChildren from "./updateChildren"
import createEle from "./createEle"
​
/**
 * @description 比较两个虚拟节点的子节点（children or text） 并更新其子节点对应的真实dom节点
 * @param {*} oldVnode 
 * @param {*} newVnode 
 * @returns 
 */
export function patchDetails(oldVnode, newVnode) {
  // 判断oldVnode和newVnode是否为同一个对象, 是的话直接不用比了
  if(oldVnode == newVnode) return 
​
  // 默认newVnode和oldVnode只有text和children其中之一，真实的源码这里的情况会更多一些，不过大同小异。
​
  if(hasText(newVnode)) {
    // newVnode有text但没有children
​
    /**
     *  newVnode.text !== oldVnode.text 直接囊括了两种情况
     *  1.oldVnode有text无children 但是text和newVnode的text内容不同
     *  2.oldVnode无text有children 此时oldVnode.text为undefined 
     *  两种情况都可以通过innerText属性直接完成dom更新 
     *  情况1直接更新text 情况2相当于去掉了children后加了新的text
     */
    if(newVnode.text !== oldVnode.text) {
      oldVnode.elm.innerText = newVnode.text
    }
​
  }else if(hasChildren(newVnode)) {
    // newVnode有children但是没有text
    
    if(hasText(oldVnode)) {
      // oldVnode有text但是没有children
      
      oldVnode.elm.innerText = '' // 删除oldVnode的text
      // 添加newVnode的children
      for(let i = 0; i < newVnode.children.length; i++) {
        oldVnode.elm.appendChild(createEle(newVnode.children[i]))
      }
​
    }else if(hasChildren(oldVnode)) {
      // oldVnode有children但是没有text
​
      // 对比两个节点的children 并更新对应的真实dom节点
      updateChildren(oldVnode.children, newVnode.children, oldVnode.elm)
    }
  }
}
​
// 有children没有text
function hasChildren(node) {
  return !node.text && (node.children && node.children.length > 0)
} 
​
// 有text没有children
function hasText(node) {
  return node.text && (node.children == undefined || (node.children && node.children.length == 0))
} 

```

### updateChildren

该方法是diff算法中最复杂的方法（大的要来了）。对应上面**patchVnode**中`oldVnode`和`newVnode`都有children的情况。

首先我们需要介绍一下这里的对比规则。

对比过程中会引入四个指针，分别指向`oldVnode`子节点列表中的第一个节点和最后一个节点（后面我们简称为**旧前**和**旧后**）以及指向`newVnode`子节点列表中的第一个节点和最后一个节点（后面我们简称为**新前**和**新后**）

对比时，每一次对比按照以下顺序进行**命中查找**

- 旧前与新前节点对比（1）
- 旧后与新后节点对比（2）
- 旧前与新后节点对比（3）
- 旧后与新前节点对比（4）

上述四种情况，如果某一种情况两个指针对应的虚拟Dom相同，那么我们称之为**命中**。命中后就不会接着查找了，指针会移动，（还有可能会操作真实Dom，3或者4命中时会操作真实Dom移动节点）之后开始下一次对比。如果都没有命中，则去`oldVnode`子节点列表循环查找当前**新前**指针所指向的节点，如果查到了，那么操作真实Dom移动节点，没查到则新增真实Dom节点插入。

这种模式的对比会一直进行，直到满足了终止条件。即**旧前指针移动到了旧后指针的后面**或者**新前指针移动到了新后指针的后面**，我们可以理解为**旧子节点先处理完毕**和**新子节点处理完毕**。那么我们可以预想到新旧子节点中总会有其一先处理完，对比结束后，我们会根据没有处理完子节点的那一对前后指针决定是要插入真实Dom还是删除真实Dom。

- 如果旧子节点先处理完了，新子节点有剩余，说明有要新增的节点。将根据最终**新前**和**新后**之间的虚拟节点执行插入操作
- 如果新子节点先处理完了，旧子节点有剩余，说明有要删除的节点。将根据最终**旧前**和**旧后**之间的虚拟节点执行删除操作
下面将呈现代码，注意注释
```js
// updateChildren.js
​
import patchDetails from "./patchVnode"
import createEle from "./createEle";
​
/**
 * @description 对比子节点列表并更新真实Dom
 * @param {*} oldCh 旧虚拟Dom子节点列表 
 * @param {*} newCh 新虚拟Dom子节点列表 
 * @param {*} parent 新旧虚拟节点对应的真实Dom
 * @returns 
 */
​
export default function updateChildren(oldCh, newCh, parent) {
  // 定义四个指针 旧前 旧后 新前 新后 （四个指针两两一对，每一对前后指针所指向的节点以及其之间的节点为未处理的子节点）
  let oldStartIndex = 0;
  let oldEndIndex = oldCh.length - 1;
  let newStartIndex = 0;
  let newEndIndex = newCh.length - 1;
​
  // 四个指针对应的节点
  let oldStartNode = oldCh[oldStartIndex];
  let oldEndNode = oldCh[oldEndIndex];
  let newStartNode = newCh[newStartIndex];
  let newEndNode = newCh[newEndIndex];
​
  // oldCh中每个子节点 key 与 index的哈希表 用于四种对比规则都不匹配的情况下在oldCh中寻找节点
  const keyMap = new Map();
​
  /**
   * 开始遍历两个children数组进行细节对比
   * 对比规则：旧前-新前 旧后-新后 旧前-新后 旧后-新前
   * 对比之后指针进行移动
   * 直到指针不满足以下条件 意味着有一对前后指针之间再无未处理的子节点 则停止对比 直接操作DOM
   */
​
  while (oldStartIndex <= oldEndIndex && newStartIndex <= newEndIndex) {
    // 这四种情况是为了让指针在移动的过程中跳过空节点
    if (oldStartNode == undefined) {
      oldStartNode = oldCh[++oldStartIndex];
    } else if (oldEndNode == undefined) {
      oldEndNode = oldCh[--oldEndIndex];
    } else if (newStartNode == undefined) {
      newStartNode = newCh[++newStartIndex];
    } else if (newEndNode == undefined) {
      newEndNode = newCh[--newEndIndex];
    } else if (isSame(oldStartNode, newStartNode)) {
      console.log("method1");
      // 旧前-新前是同一个虚拟节点
​
      // 两个子节点再对比他们的子节点并更新dom （递归切入点）
      patchDetails(oldStartNode, newStartNode);
      // 指针移动
      oldStartNode = oldCh[++oldStartIndex];
      newStartNode = newCh[++newStartIndex];
    } else if (isSame(oldEndNode, newEndNode)) {
      console.log("method2");
      // 旧后-新后是同一个虚拟节点
​
      // 两个子节点再对比他们的子节点并更新dom （递归切入点）
      patchDetails(oldEndNode, newEndNode);
      // 指针移动
      oldEndNode = oldCh[--oldEndIndex];
      newEndNode = newCh[--newEndIndex];
    } else if (isSame(oldStartNode, newEndNode)) {
      console.log("method3");
      // 旧前-新后是同一个虚拟节点
​
      // 两个子节点再对比他们的子节点并更新dom （递归切入点）
      patchDetails(oldStartNode, newEndNode);
​
      /**
       *  这一步多一个移动(真实)节点的操作
       *  需要把当前指针所指向的子节点 移动到 oldEndIndex所对应真实节点之后（也就是未处理真实节点的尾部）
       *  注意：这一步是在操作真实节点
       */
      parent.insertBefore(oldStartNode.elm, oldEndNode.elm.nextSibling);
​
      // 指针移动
      oldStartNode = oldCh[++oldStartIndex];
      newEndNode = newCh[--newEndIndex];
    } else if (isSame(oldEndNode, newStartNode)) {
      console.log("method4");
      // 旧后-新前 是同一个虚拟节点
​
      // 两个子节点再对比他们的子节点并更新dom （递归切入点）
      patchDetails(oldEndNode, newStartNode);
      /**
       *  这一步多一个移动(真实)节点的操作
       *  与method3不同在移动位置
       *  需要把当前指针所指向的子节点 移动到 oldStartIndex所对应真实节点之前（也就是未处理真实节点的顶部）
       *  注意：这一步是在操作真实节点
       */
      parent.insertBefore(oldEndNode.elm, oldCh[oldStartIndex].elm);
​
      // 指针移动
      oldEndNode = oldCh[--oldEndIndex];
      newStartNode = newCh[++newStartIndex];
    } else {
      console.log("does not match");
      // 四种规则都不匹配
​
      // 生成keyMap
      if (keyMap.size == 0) {
        for (let i = oldStartIndex; i <= oldEndIndex; i++) {
          if (oldCh[i].key) keyMap.set(oldCh[i].key, i);
        }
      }
​
      // 在oldCh中搜索当前newStartIndex所指向的节点
      if (keyMap.has(newStartNode.key)) {
        // 搜索到了
​
        // 先获取oldCh中该虚拟节点
        const oldMoveNode = oldCh[keyMap.get(newStartNode.key)];
        // 两个子节点再对比他们的子节点并更新dom （递归切入点）
        patchDetails(oldMoveNode, newStartNode);
​
        // 移动这个节点（移动的是真实节点）
        parent.insertBefore(oldMoveNode.elm, oldStartNode.elm);
​
        // 该虚拟节点设置为undefined（还记得最开始的四个条件吗，因为这里会将子节点制空，所以加了那四个条件）
        oldCh[keyMap.get(newStartNode.key)] = undefined;
          
      } else {
        // 没搜索到 直接插入
        parent.insertBefore(createEle(newStartNode), oldStartNode.elm);
      }
​
      // 指针移动
      newStartNode = newCh[++newStartIndex];
    }
  }
​
  /**
   * 插入和删除节点
   * while结束后 有一对前后指针之间仍然有未处理的子节点，那么就会进行插入或者删除操作
   * oldCh的双指针中有未处理的子节点，进行删除操作
   * newCh的双指针中有未处理的子节点，进行插入操作
   */
  if (oldStartIndex <= oldEndIndex) {
    // 删除
    for (let i = oldStartIndex; i <= oldEndIndex; i++) {
      // 加判断是因为oldCh[i]有可能为undefined
      if(oldCh[i]) parent.removeChild(oldCh[i].elm);
    }
  } else if (newStartIndex <= newEndIndex) {
    /**
     * 插入
     * 这里需要注意的点是从哪里插入，也就是appendChild的第二个参数
     * 应该从oldStartIndex对应的位置插入
     */
    for (let i = newStartIndex; i <= newEndIndex; i++) {
      // oldCh[oldStartIndex]存在是从头部插入
      parent.insertBefore(createEle(newCh[i]), oldCh[oldStartIndex] ? oldCh[oldStartIndex].elm : undefined);
    }
  }
}
​
// 判断两个虚拟节点是否为同一个虚拟节点
function isSame(a, b) {
  return a.sel == b.sel && a.key == b.key;
}

```

## 总结
由于**diff**算法对比的是**虚拟Dom**，而**虚拟Dom**是呈树状的，所以我们可以发现，diff算法中充满了递归。总结起来，其实diff算法就是一个 patch —> patchVnode —> updateChildren —> patchVnode —> updateChildren —> patchVnode这样的一个循环递归的过程。


这里再提一嘴`key`，我们面试中经常会被问到vue中`key`的作用。根据上面我们分析的，`key`的主要作用其实就是对比两个虚拟节点时，判断其是否为相同节点。加了key以后，我们可以更为明确的判断两个节点是否为同一个虚拟节点，是的话判断子节点是否有变更（有变更更新真实Dom），不是的话继续比。如果不加`key`的话，如果两个不同节点的标签名恰好相同，那么就会被判定为同一个节点（key都为undefined），结果一对比这两个节点的子节点发现不一样，这样会凭空增加很多对真实Dom的操作，从而导致页面更频繁得进行重绘和回流。

所以我认为合理利用`key`可以有效减少真实Dom的变动，从而减少页面重绘和回流的频率，进而提高页面更新的效率。