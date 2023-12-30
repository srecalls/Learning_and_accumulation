### 目录结构
![[@import的用法.png]]
### a.css
```css
p {
    color: pink
}
```

### b.css
```css
/* 引入 a.css， 注意结尾需要分号  */ 
@import 'a.css';	/* 或者 @import url('a.css'); */  
@import './a.css';
@import url('a.css')
@import url(a.css);
@import url(./a.css)
@import url("./a.css")

@import a.css; 是错的，没有引号
p {
    font-size: 30px;
}
```

### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        @import './style/b.css';
        p {
            font-style:italic;
        }
    </style>
</head>

<body>
    <p>style</p>
</body>
</html>

```

### 效果
![[@import的用法-1.png]]


### 注意事项

- **使用`@import`语句引入样式时，**结尾需要加分号`;`
- 在`html`文档中使用`@import`时，需要在`style`标签里面
- 不推荐使用`@import`语句
	- **`@import`引入的 CSS 将在页面加载完毕后被加载**
	- **`@import`是 CSS2.1 才有的语法，故只可在 IE5+ 才能识别**