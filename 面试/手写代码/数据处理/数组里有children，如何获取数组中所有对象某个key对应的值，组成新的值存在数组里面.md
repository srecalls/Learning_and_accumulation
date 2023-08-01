1，在实际开发中我们会遇到数组中包含chidren的数组，我们如果想要获取数组中某个指定的key对应值的组成新的key和value的时候，这时候我们改怎么简单方便的操作呢？


#### 1：如何获取里面所有的id值，包括children里的
```js
[
  {
       id: 1,
       age: 23,
       name: '测试1',
       children: [
         {
              id: 2,
              age: 24,
              name: '测试11',
              children: [
           {
               id: 3,
               age: 244,
               name: '测试111'
            },
        ]
         }
       ]
   },
   {
       id: 4,
       age: 26,
       name: '测试2',
       children: [],
   }
]
```

##### 方法一…运算符使用解决：
```js
let a = [
  {
       id: 1,
       age: 23,
       name: '测试1',
       children: [
         {
              id: 2,
              age: 24,
              name: '测试11',
              children: [
           {
               id: 3,
               age: 244,
               name: '测试111'
            },
        ]
         }
       ]
   },
   {
       id: 4,
       age: 26,
       name: '测试2',
       children: [],
   }
]

// (1)
function func(arr){
  return arr.reduce((a, b) => {
    let res = [...a,b.id];
    if (b.children) res = [...res, ...func(b.children)];
    return res;
  }, []);
}

// (2)
function func(arr) {
   return arr.reduce((a, b) => {
     return b.children
       ? [...a, b.id, ...func(b.children)]
       : [...a, b.id];
   }, []);
 }
console.log(func(a))  
// 结果： [1,2,3,4]
```


##### 方法二： 使用for循环遍历，然后在递归
```js
// （1）
let arr= [
   { id: 1, children: [{ id: 2 },{ id: 3 }] },
   { id: 4, children: [] }
 ];
// 获取对应id
const getIds = function(arr) {
const res = arr.reduce((prev, next) => {
	 if (next.id) prev.push(next.id);
	 if (next.children && next.children.length) return prev.concat(getIds(next.children));
	    return prev;
	    }, []);
	    return res;
  };
 const res = getIds(arr);
 console.log(res);
 
 // 获取对应需要的key
 function getKeys(list, key) {
    return list.reduce((res, v) => {
        if(v.children && v.children.length) res = res.concat(getKeys(v.children,key))
        res.push(v[key]);
        return res;
    }, [])
}
console.log(getKeys(arr, 'id'))

// （2）
const getIdsArry = (arr) => {
  const ans = [];

  const dfs = (root, ans) => {
    let neighbor;
    if (Array.isArray(root)) {
      neighbor = root;
    } else {
      ans.push(root.id);
      neighbor = root.children;
    }

    if (!neighbor) return;

    for (let i = 0; i < neighbor.length; ++i) {
      dfs(neighbor[i], ans);
    }
  };

  dfs(arr, ans);

  return ans;
};
console.log(getIds (arr))

```

#### 2：跟上面借结构一样，获取children里面对应的id `[2,3]`
```js
let a = [
   { id: 1, children: [{ id: 2 },{ id: 3 }] },
   { id: 4, children: [] }
 ];
 function func(arr) {
   return arr.reduce((a, b) => {
     return b.children ? [...a, ...func(b.children)] : [...a, b.id];
   }, []);
 }
 console.log(func(a));
 // 结果  [2,3]

```

#### 3，组成新的值存放数组里面
![[数组里有children，如何获取数组中所有对象某个key对应的值，组成新的值存在数组里面.png]]

```js
var aa = [
  {
        id: 1,
        age: 23,
        name: '测试1',
        children: [
          {
               id: 2,
               age: 24,
               name: '测试11',
               children: [
	           {
                id: 3,
                age: 244,
                name: '测试111'
	            },
	        ]
          }
        ]
    },
    {
        id: 4,
        age: 26,
        name: '测试2',
        children: [],
    }
    ]
for (var itemproject = 0; itemproject < aa.length; itemproject++) {
     if (aa[itemproject].children && aa[itemproject].children.length > 0) {
        aa[itemproject].selectedFields = getidarry(aa[itemproject].children)
      } else {
        aa[itemproject].selectedFields = []
      }
}
function getidarry (arr) {
  	  return arr.reduce((a, b) => {
	   let res = [...a,b.id];
	   if (b.children) res = [...res, ...getidarry(b.children)];
	   return res;
	 }, []);
}
console.log('新数组', aa)

```

## AI
可以使用递归的方式来遍历这个嵌套的对象数组，并提取所有的id值。具体实现如下：

```js
function getAllIds(data) {
  const ids = [];
  for (let i = 0; i < data.length; i++) {
    ids.push(data[i].id);
    if (data[i].children && data[i].children.length > 0) {
      ids.push(...getAllIds(data[i].children));
    }
  }
  return ids;
}

const data = [
  {
    id: 1,
    age: 23,
    name: '测试1',
    children: [
      {
        id: 2,
        age: 24,
        name: '测试11',
        children: [
          {
            id: 3,
            age: 244,
            name: '测试111'
          },
        ]
      }
    ]
  },
  {
    id: 4,
    age: 26,
    name: '测试2',
    children: [],
  }
];

const ids = getAllIds(data);
console.log(ids); // [1, 2, 3, 4]
```

这里定义了一个`getAllIds`函数，它接收一个嵌套的对象数组作为参数，并返回其中所有的id值。对于每个对象，我们先将其id值加入到`ids`数组中，然后判断其是否有`children`属性，如果有则递归调用`getAllIds`函数来获取其子节点的id值，并将它们合并到`ids`数组中。最终返回`ids`数组即可。