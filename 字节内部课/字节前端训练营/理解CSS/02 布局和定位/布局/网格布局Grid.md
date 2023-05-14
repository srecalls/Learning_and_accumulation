## 网格布局
![[Pasted image 20230507004952.png]]
![[Pasted image 20230507005004.png]]
![[Pasted image 20230507005013.png]]

### 使用Grid布局的示例
![[Pasted image 20230507005100.png]]

## Grid 和Flex布局的使用策略
![[Pasted image 20230507005207.png]]
下面那个只是建议，不是绝对




在 Grid 布局中，grid-column 属性用于指定元素所占据的网格列区域。其属性值可以是一个或多个` <grid-line>`，表示元素所占据的网格线。

一个 `<grid-line>` 可以是一个 `<integer>`，表示具体的网格线位置，或者是一个 `<name>`，表示使用命名网格线。

在 grid-column 属性中，如果使用相同的 `<grid-line>` 来表示元素的开始和结束位置，例如 grid-column: 1/1，那么该元素实际上只会占据一个网格列。这是因为该属性表示元素在第一条网格线和第一条网格线之间的区域，而这两条网格线是重合的，因此元素只能占据一个网格列。

相反，如果使用不同的 `<grid-line>` 来表示元素的开始和结束位置，例如 grid-column: 1/2，那么该元素将会占据从第一条网格线到第二条网格线之间的区域，即两个相邻的网格列。

因此，使用 grid-column: 1/1 是没有意义的，因为元素实际上只会占据一个网格列，并不能达到布局的效果。如果需要让一个元素占据一个网格列，可以使用 grid-column-start 和 grid-column-end 属性，例如 grid-column-start: 1; grid-column-end: 2;。

总之，在 Grid 布局中，如果使用相同的 `<grid-line>` 来表示元素的开始和结束位置，例如 grid-column: 1/1，那么该元素实际上只会占据一个网格列，没有实际的布局效果。