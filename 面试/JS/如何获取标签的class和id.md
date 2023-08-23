要修改元素的 class 属性，可以使用以下方法：
## class
1. `element.classList.add(className)`: 将指定的类名添加到元素的 class 属性中。

   用法示例：

   ```javascript
   const element = document.getElementById('my-element');
   element.classList.add('new-class');
   ```

   上述代码将在具有 ID 为 "my-element" 的元素上添加名为 "new-class" 的类。

2. `element.classList.remove(className)`: 从元素的 class 属性中移除指定的类名。

   用法示例：

   ```javascript
   const element = document.getElementById('my-element');
   element.classList.remove('old-class');
   ```

   上述代码将从具有 ID 为 "my-element" 的元素的 class 属性中移除名为 "old-class" 的类。

3. `element.classList.toggle(className)`: 如果元素的 class 属性中包含指定的类名，则移除该类名；如果不包含，则添加该类名。

   用法示例：

   ```javascript
   const element = document.getElementById('my-element');
   element.classList.toggle('active');
   ```

   上述代码将在具有 ID 为 "my-element" 的元素上切换名为 "active" 的类，即如果类名存在，则移除它；如果不存在，则添加它。

4. `element.classList.replace(oldClass, newClass)`: 将元素的 class 属性中的一个类名替换为另一个类名。

   用法示例：

   ```javascript
   const element = document.getElementById('my-element');
   element.classList.replace('old-class', 'new-class');
   ```

   上述代码将在具有 ID 为 "my-element" 的元素的 class 属性中将名为 "old-class" 的类替换为 "new-class"。

5. `element.className = newClassName`: 直接通过赋值方式修改元素的 class 属性。这会完全替换元素的 class 属性，因此需要注意不会保留原有的类名。

   用法示例：

   ```javascript
   const element = document.getElementById('my-element');
   element.className = 'new-class';
   ```

   上述代码将将具有 ID 为 "my-element" 的元素的 class 属性设置为 "new-class"。

注意事项：

- 在使用 `classList` 方法时，无需担心重复添加或移除类名，因为它们会自动处理重复操作。
- 使用 `classList` 方法修改类名，不会影响元素之前已有的类名，而是在现有的类名基础上进行操作。
- `classList` 方法在现代浏览器中得到广泛支持，但在一些旧版本的浏览器中可能不完全支持。在使用时需注意浏览器的兼容性。


## id

要修改元素的 ID 属性，可以直接通过赋值方式来修改。

例如，假设你有一个元素的引用 `element`，你可以使用以下方法来修改其 ID 属性：

```javascript
element.id = "new-id";
```

上述代码将该元素的 ID 属性设置为 "new-id"。

注意事项：

- 修改元素的 ID 属性后，将会更新文档中对应的元素 ID。
- 确保新的 ID 值在文档中是唯一的，不与其他元素的 ID 冲突。
- 修改 ID 属性时，最好遵循命名规范，使用有意义的、能够描述元素用途的名称。
- 修改 ID 属性后，相关的 CSS 和 JavaScript 代码可能需要相应地进行更新，以反映新的 ID 值。
- 可以通过 `document.getElementById` 方法来获取具有新 ID 的元素的引用，以进一步操作或访问该元素。