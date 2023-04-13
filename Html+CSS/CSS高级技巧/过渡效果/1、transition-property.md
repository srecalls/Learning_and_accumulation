transition-property 属性用来设置元素中参与过渡的属性名称，语法格式如下：

> transition-property: none | all | property;

参数说明如下：

-   none：表示没有属性参与过渡效果；
-   all：表示所有属性都参与过渡效果；
-   property：定义应用过渡效果的 CSS 属性名称列表，多个属性名称之间使用逗号,进行分隔。

示例代码如下：
```css
<!DOCTYPE html>
<html>
<head>
    <style>
        div {
            width: 100px;
            height: 100px;
            border: 3px solid black;
            margin: 10px 0px 0px 10px;
            transition-property: width, background;
        }
        div:hover {
            width: 200px;
            background-color: blue;
        }
    </style>
</head>
<body>
    <div></div>
</body>
</html>

```

