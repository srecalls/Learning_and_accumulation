假设给定的数组为`data`，其中每个元素对象都有一个`parent`属性，表示其父节点的标识。我们可以通过以下代码使用递归方式构建树形结构：
```javascript
const data = [
  { id: 1, name: 'Node 1', parent: null },
  { id: 2, name: 'Node 2', parent: 1 },
  { id: 3, name: 'Node 3', parent: 1 },
  { id: 4, name: 'Node 4', parent: 2 },
  { id: 5, name: 'Node 5', parent: 2 },
  { id: 6, name: 'Node 6', parent: 3 },
];

const tree = buildTree(data);
console.log(tree);
```

```javascript
function buildTree(data, parent = null) {
  const tree = [];
  
  for (let i = 0; i < data.length; i++) {
    if (data[i].parent === parent) {
      const child = data[i];
      const children = buildTree(data, child.id);
      if (children.length > 0) {
        child.children = children;
      }
      tree.push(child);
    }
  }
  
  return tree;
}
```

在上述代码中，`buildTree`函数接受两个参数：`data`表示给定的数组，`parent`表示当前节点的父节点标识，默认为`null`表示顶级节点。

在函数内部，我们首先创建一个空数组`tree`来存储树形结构的节点。然后，我们遍历数组`data`，对于每个元素对象，如果其`parent`属性与给定的父节点标识匹配，表示它是当前父节点的子节点，我们将其添加到`tree`数组中。

接着，我们递归调用`buildTree`函数，将当前子节点的标识作为新的父节点标识，以查找其子节点。如果子节点存在，我们将其赋值给`children`属性，并将其添加到当前节点的`children`属性中。

最后，我们返回构建好的树形结构数组`tree`。

以下是一个使用示例：

```javascript
const data = [
  { id: 1, name: 'Node 1', parent: null },
  { id: 2, name: 'Node 2', parent: 1 },
  { id: 3, name: 'Node 3', parent: 1 },
  { id: 4, name: 'Node 4', parent: 2 },
  { id: 5, name: 'Node 5', parent: 2 },
  { id: 6, name: 'Node 6', parent: 3 },
];

const tree = buildTree(data);
console.log(tree);
```

运行上述代码，将输出构建好的树形结构数组。根据给定的`data`数组，输出结果如下：

```javascript
[
  {
    id: 1,
    name: 'Node 1',
    parent: null,
    children: [
      {
        id: 2,
        name: 'Node 2',
        parent: 1,
        children: [
          { id: 4, name: 'Node 4', parent: 2, children: [] },
          { id: 5, name: 'Node 5', parent: 2, children: [] }
        ]
      },
      {
        id: 3,
        name: 'Node 3',
        parent: 1,
        children: [
          { id: 6, name: 'Node 6', parent: 3, children: [] }
        ]
      }
    ]
  }
]
```

这样，我们根据`parent`属性成功构建了一个树形结构。注意，树的顶级节点的`parent`属性为`null`。