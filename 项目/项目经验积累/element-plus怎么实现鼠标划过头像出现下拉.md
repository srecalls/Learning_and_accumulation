# element-plus怎么实现鼠标划过头像出现下拉
要实现鼠标划过头像出现下拉菜单，可以使用Element Plus中的el-dropdown组件和el-dropdown-item组件。以下是一个简单的示例：

1.  在HTML模板中，使用el-dropdown和el-avatar组件创建一个包含头像和下拉菜单的区域。
```html
<el-dropdown trigger="hover">
  <span class="avatar">
    <el-avatar src="avatar.png"></el-avatar>
  </span>
  <el-dropdown-menu slot="dropdown">
    <el-dropdown-item>个人信息</el-dropdown-item>
    <el-dropdown-item>设置</el-dropdown-item>
    <el-dropdown-item>退出登录</el-dropdown-item>
  </el-dropdown-menu>
</el-dropdown>
```
2.  使用CSS样式设置头像和下拉菜单的布局和样式。
```css
.avatar {
  display: inline-block;
  width: 48px;
  height: 48px;
  overflow: hidden;
  border-radius: 50%;
  margin-right: 10px;
  vertical-align: middle;
}

.el-dropdown-menu {
  width: 120px;
}
```
在上述示例中，el-dropdown的trigger属性设置为"hover"，表示当鼠标悬停在头像区域时触发下拉菜单。el-dropdown-menu组件包含了三个el-dropdown-item组件，用于创建下拉菜单的菜单项。CSS样式用于设置头像和下拉菜单的布局和样式。通过以上步骤，就可以实现鼠标划过头像出现下拉菜单的效果。