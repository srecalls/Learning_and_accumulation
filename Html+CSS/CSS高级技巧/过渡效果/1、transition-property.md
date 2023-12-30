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

`transition-property` 是 CSS 中的一个属性，用于指定应用过渡效果的 CSS 属性的名称。

具体来说，`transition-property` 用于定义在 CSS 过渡（transition）中要发生变化的属性。通过指定这些属性，可以使元素在发生状态改变时产生平滑的过渡效果。

以下是 `transition-property` 属性的作用：

1. **指定过渡属性：** 使用 `transition-property` 可以明确指定要应用过渡效果的 CSS 属性。只有被指定的属性发生变化时，过渡效果才会触发。可以指定单个属性或多个属性，多个属性之间用逗号分隔。

2. **实现属性过渡效果：** 通过 `transition-property` 结合其他过渡属性（如 `transition-duration`、`transition-timing-function` 和 `transition-delay`），可以实现属性的平滑过渡效果。当指定的属性值发生改变时，浏览器会根据设置的过渡属性和过渡时间来平滑地过渡到新的属性值。

下面是一个示例，展示了如何使用 `transition-property` 来定义过渡效果：

```css
.box {
  width: 100px;
  height: 100px;
  background-color: red;
  transition-property: width, background-color;
  transition-duration: 1s;
}

.box:hover {
  width: 200px;
  background-color: blue;
}
```

在上述示例中，`.box` 类的元素在 `width` 和 `background-color` 属性发生变化时会有过渡效果。当鼠标悬停在 `.box` 元素上时，宽度会从 100px 平滑过渡到 200px，背景颜色从红色平滑过渡到蓝色。

通过使用 `transition-property`，可以灵活地控制过渡效果应用的属性，实现更吸引人的用户界面交互效果。

