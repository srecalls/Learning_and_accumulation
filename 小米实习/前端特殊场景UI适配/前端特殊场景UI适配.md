- 目前UI适配项目主要为appstore-mobile及appstore-ui
- appstore-ui为UI库，在构建组件时候，就需要考虑深色模式、大字体、机型的适配
- appstore-mobile为主项目，适配时从业务页面去考虑

# 深色模式

![[前端特殊场景UI适配.png]]
![[前端特殊场景UI适配-1.png]]

## 如何实现
    

- 主要通过CSS属性 filter 实现
- 在手机环境下，当深色模式开启时，客户端会向前端注入**深色模式相关的****CSS****样式**，整体实现页面元素反色效果，如：白色自动反色成黑色
- 具体注入的样式可见`z-inject-darkmode`文件
- 在本地开发环境下，可以在链接添加query参数 `a_darkMode=true`来模拟深色模式

## 如何适配
    

由于反色是整体进行，对于个别不达预期的地方需要做调整，使其符合规范

### 使用CSS中定义好的类
    
    1. `.keep-color`：不反色，如希望一个元素的background在深浅两种模式下都保持一个颜色时
    2. `.brighter`: 对当前颜色增亮处理

```js
<button class="keep-color" style="background:pink">我是有颜色的按钮</button>
```

### 顶级标识类.mi-darkmode
    

- 样式注入后，顶级标签将会添加**.mi-darkmode**，以此为标识，可以对指定类做样式的调整
- 比较需要注意的是**选择器的权重**，如果.mi-darkmode下设置的选择器权重不及浅色模式下高，那么覆盖将会失败
- 举例：一个元素在浅色模式下的字体颜色是黑色，其整体反色后字体颜色变为白色，但是按照要求应该为灰色

```js
<div class="title">我是标题</div>

<sytle>
// 浅色模式下
.title{
  color: #000
}

// 深色模式下,
.mi-darkmode{
  .title{
    color: rgba(0,0,0,.7) 
  }
}
</style>
```

### window.__miDarkmode
    

- 在javascript中，可以通过全局变量`**window.__miDarkmode**`判断是否在深色模式中
- 举例：格式化数据时，需要根据深浅两种模式给对应字段赋予不同值

```js
const urlMap = window.__miDarkmode ? darkIconTagUrlMap : iconTagUrlMap;
```

## 适配规范
    

- 设计方给出了深色模式的一份设计规范，包含了当前商店常用的颜色的深色模式，**请务必按照所提供的规范进行适配，保持****UI****规范**


# 大字体模式

![[前端特殊场景UI适配-2.png]]
![[前端特殊场景UI适配-3.png]]

 ## 如何实现
    

- 手机上用户可以设置字号的大小，当设置后，整个手机的字体将以乘以对应比例放大
- 可以通过客户端API `getFontScale` 获取当前页面字体的放大比例

## 如何适配
    

- 对于某些样式而言，过度放大字体会带来视觉上的问题，如拥挤、信息显示过少、元素移位等
- 按照设计规范，需要限制某些元素的放大比例，保持样式和信息完整


