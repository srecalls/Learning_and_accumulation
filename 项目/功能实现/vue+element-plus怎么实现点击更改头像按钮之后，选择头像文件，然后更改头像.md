要实现点击更改头像按钮之后，选择头像文件，然后更改头像，你可以使用 `el-upload` 组件来实现文件上传，并在上传成功后更新用户的头像。

首先，在模板中添加一个按钮和一个 `el-upload` 组件，用于选择和上传头像文件：

```
<template>
  <div>
    <el-button type="primary" @click="showUploadDialog">更改头像</el-button>
    <el-dialog :visible.sync="uploadDialogVisible" title="上传头像">
      <el-upload :action="uploadUrl" :on-success="handleUploadSuccess">
        <el-button slot="trigger">选择文件</el-button>
      </el-upload>
    </el-dialog>
  </div>
</template>
```

在这个示例中，我们添加了一个 `el-button` 组件，用于触发上传对话框的显示。当用户点击按钮时，会调用 `showUploadDialog` 方法，该方法会将上传对话框的可见性设置为 `true`，从而显示上传对话框。上传对话框中包含一个 `el-upload` 组件，用于选择和上传头像文件。在 `el-upload` 组件中，我们将 `action` 属性设置为上传地址，将 `on-success` 属性设置为上传成功后的回调方法，将 `slot="trigger"` 属性设置为触发上传的按钮。

接下来，在组件的 `data` 属性中定义上传对话框的可见性和上传地址：

```
<script>
export default {
  data() {
    return {
      uploadDialogVisible: false,
      uploadUrl: '/api/upload',
    };
  },
  methods: {
    showUploadDialog() {
      this.uploadDialogVisible = true;
    },
    handleUploadSuccess(response) {
      // 处理上传成功后的响应
      if (response.code === 0) {
        this.$message.success('头像上传成功');
        this.$store.commit('setUserAvatar', response.data.avatar);
        this.uploadDialogVisible = false;
      } else {
        this.$message.error('头像上传失败');
      }
    },
  },
};
</script>
```

在这个示例中，我们定义了两个方法：`showUploadDialog` 和 `handleUploadSuccess`。`showUploadDialog` 方法将上传对话框的可见性设置为 `true`，从而显示上传对话框。`handleUploadSuccess` 方法是上传成功后的回调方法，它会根据上传结果更新用户的头像。在这个示例中，我们假设上传成功后后端返回了一个 JSON 格式的响应，其中 `code` 字段表示操作结果，`data` 字段包含上传成功后的数据，例如头像地址。我们使用 Vuex 存储来保存用户的头像地址，通过调用 `$store.commit` 方法来更新用户的头像。最后，我们将上传对话框的可见性设置为 `false`，从而隐藏上传对话框。

需要注意的是，上传头像的具体实现方法可能会因后端技术栈不同而有所不同。你需要根据你的后端技术栈来实现上传接口和处理上传的逻辑。另外，如果需要显示用户的头像，你需要在模板中添加一个 `<img>` 标签，并将其 `src` 属性绑定到 Vuex 存储中的用户头像地址。




# 但是我没有后端，我只有本地，我想点击文件后，直接换头像就可以了
如果你没有后端，只是想在本地更改头像，那么你可以使用 `FileReader` 对象读取本地文件，并将其转换为 `data URL` 格式的字符串，然后将该字符串赋值给 `<img>` 标签的 `src` 属性，即可实现更改头像的效果。

以下是一个示例代码，用于实现点击更改头像按钮之后，选择头像文件，然后更改头像：

```
<template>
  <div>
    <el-button type="primary" @click="showUploadDialog">更改头像</el-button>
    <input type="file" ref="fileInput" style="display: none" @change="handleFileChange">
    <div v-if="userAvatar">
      <img :src="userAvatar" alt="头像">
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userAvatar: null,
    };
  },
  methods: {
    showUploadDialog() {
      this.$refs.fileInput.click();
    },
    handleFileChange(event) {
      const file = event.target.files[0];
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => {
        this.userAvatar = reader.result;
      };
    },
  },
};
</script>
```

在这个示例中，我们添加了一个 `input` 标签，用于选择本地文件。当用户点击更改头像按钮时，我们通过调用 `$refs.fileInput.click()` 方法来触发 `input` 标签的点击事件，从而显示文件选择对话框。当用户选择文件后，我们通过 `FileReader` 对象读取文件，并将其转换为 `data URL` 格式的字符串。最后，我们将该字符串赋值给 `<img>` 标签的 `src` 属性，从而实现更改头像的效果。

需要注意的是，`FileReader` 对象是 HTML5 中的新特性，可能不兼容一些老版本浏览器。另外，如果你需要将用户的头像保存到本地，你可以使用一些客户端存储技术，例如 `localStorage` 或 `IndexedDB`，将头像数据保存到浏览器的本地存储中。