_ATTACHMENT_翻译：連接, 附件；附屬物；
`background-attachment` 属性用于指定背景图片的滚动行为，即当内容滚动时，背景图片是固定的还是随着内容一起滚动。

`background-attachment` 属性接受以下值：

- `scroll`：背景图片随内容一起滚动。当内容滚动时，背景图片会相对于元素滚动。
- `fixed`：背景图片固定在元素的视口中，不会随内容滚动。当内容滚动时，背景图片保持在固定位置。
- `local`：背景图片滚动与元素内部的内容一起。当内容滚动时，背景图片相对于元素的内部滚动。


`background-attachment` 属性的默认值是 `scroll`，即背景图片会随内容一起滚动。
如果未显式设置 `background-attachment` 属性，则会使用默认值 `scroll`。这意味着当内容滚动时，背景图片会相对于元素滚动


以下是 `background-attachment` 属性的示例用法：

```css
div {
  background-image: url("image.jpg");
  background-attachment: fixed;
}
```

在上述示例中，`div` 元素的背景图片被设置为 "image.jpg"，并且背景图片的滚动行为被设置为固定（`fixed`）。这意味着当内容滚动时，背景图片将保持在固定位置，不会随内容滚动。

```css
div {
  background-image: url("image.jpg");
  background-attachment: scroll;
}
```

在上述示例中，背景图片的滚动行为被设置为随内容滚动（`scroll`）。这意味着当内容滚动时，背景图片会相对于元素滚动。

```css
div {
  background-image: url("image.jpg");
  background-attachment: local;
}
```

在上述示例中，背景图片的滚动行为被设置为与元素内部的内容一起滚动（`local`）。这意味着当内容滚动时，背景图片相对于元素内部滚动。

通过使用 `background-attachment` 属性，您可以控制背景图片的滚动行为，以实现不同的视觉效果和滚动效果。