> 将数组中所有id变为code，所有title变为name

```js
<script>
const list = [{
    id: 'a',
    title: 'A'
}, {
    id: 'b',
    title: 'B',
    children: [{
        id: 'c',
        title: 'C'
    }, {
        id: 'd',
        title: 'D'
    }]
}]
</script>
```

目前解决方法有俩

## 1. 通过JSON+正则修改对象属性

```js
JSON.parse(JSON.stringify(list).replace(/title/g, 'name')）
```

- **1.JSON.stringify()将json对象转为JSON字符串**
- **2.使用正则的replace(/title/g, 'name')）方法将title替换为name**
- **3.JSON.parse()将json字符串转为json对象**

方法1可以链式调用哦，如下：

 ```js
let res = JSON.parse(JSON.stringify(list[i]).replace(/title/g, 'name').replace(/id/g, "code"));
```

既替换title为name，也替换id为code。

所以题目通过方法一解决的代码来了~~

```js
  <script>
    // 将数组中所有id变为code，所有title变为name
    const list = [{
      id: 'a',
      title: 'A'
    }, {
      id: 'b',
      title: 'B',
      children: [{
        id: 'c',
        title: 'C'
      }, {
        id: 'd',
        title: 'D'
      }]
    }]
    let result = [];//结果保存
    for (let i = 0; i < list.length; i++) {
      //获取到list的第i个对象，修改后返回一个新对象，不修改原对象
      let res = JSON.parse(JSON.stringify(list[i]).replace(/title/g, 'name').replace(/id/g, "code"));
      //判断是否还有孩子，有就执行下面的操作
      if (list[i].children) {
        let childs = []//存孩子修改后的对象
        //遍历children下对象数组
        for (let j = 0; j < list[i].children.length; j++) {
          //获取到孩子的第j个对象，修改后返回一个新对象，不修改原对象
          let ch = JSON.parse(JSON.stringify(list[i].children[j]).replace(/title/g, 'name').replace(/id/g, "code"));
          childs.push(ch);
        }
        //将孩子修改后的属性赋值给res
        res.children = childs;
      }
      //将res装入result
      result.push(res)
    }
    console.log(result);
  </script>
```

![[Pasted image 20230714134445.png]]

但是！！！上面的方法**会修改键值对的值包含title和id的字符**！因此严格上以上方法效率较高却不准确~


 下面来看一下
 ## 方法2：通过数组方法map（）修改属性名。
通过数组方法map（）修改属性名。

例如：

```js
let res = data.map(item=>{return {name:item.title,code:item.id}});
```


```js
let result2 = [];
    let s = list.map(item => {
      let res = {};
      res.code = item.id;
      res.name = item.title;
      if (item.children) {
        res.children = item.children.map(data => { return { code: data.id, name: data.title } });
      }
      return res;
    })
    console.log(s);
```

![[Pasted image 20230714134625.png]]

## AI
你可以使用数组的 `map` 方法和对象的解构赋值来实现将数组中所有 `id` 变为 `code`，所有 `title` 变为 `name` 的操作。具体代码如下：

```js
const list = [{
  id: 'a',
  title: 'A'
}, {
  id: 'b',
  title: 'B',
  children: [{
    id: 'c',
    title: 'C'
  }, {
    id: 'd',
    title: 'D'
  }]
}];

const newList = list.map(({ id, title, children }) => ({
  code: id,
  name: title,
  ...(children && { children: children.map(({ id, title }) => ({ code: id, name: title })) })
}));

console.log(newList);
```

这段代码首先使用 `map` 方法遍历原数组中的每个元素，使用对象的解构赋值将其中的 `id` 和 `title` 属性赋值给新的属性 `code` 和 `name`。如果原数组中的元素含有 `children` 属性，也使用 `map` 方法遍历其中的每个元素进行同样的操作。最终得到一个新的数组 `newList`，其中所有的 `id` 都变成了 `code`，所有的 `title` 都变成了 `name`。