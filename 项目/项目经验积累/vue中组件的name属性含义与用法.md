#  vue中组件的name属性含义与用法
name属性：只有作为组件选项时起作用，用来**注册组件名**
#### 1、注册组件名

局部注册组件，语法：`export default{ components:{"组件名":组件对象}}`

其中，`"组件名"`注册方法：
##### 方法一：随便取名，
例：`export default{components:{"ComMy"：{template:'<h1><h1>'}}`随便取名为：`ComMy`
##### 方法二：用组件对象中的name属性值
组件对象name属性：是指要引用的子组件对象，向外暴露的name属性  
例：
file1.vue中：组件中定义`name属性`和`name属性值`
```JS
<script>
    export default{
        name:"ComNameHello"
    }
</script>

```
file2.vue中：创建组件–>引用组件–>注册组件–>使用组件
```JS
// 1.创建组件
<template>
   <div>
      <ComNameHello></ComNameHello>  //4.使用组件  可使用组件file1.vue
   </div>
</template>
<script>
   import ComName from "./file1.vue"  //2.引用组件  ComName为file1.vue的组件对象
   export default{
        componemts:{  // 3.注册组件
            [ComName.name]: ComName  
            // ComName.name用来获取：file1.vue的组件对象的name属性值，
            //                      -->是一个字符串"ComNameHello"，
            //                      -->被用做：组件名
            // key是变量，必须用“[]”包起来
            // ComName 是组件对象
            // 即：components:{"组件名":组件对象}
        }
    }
</script>

```