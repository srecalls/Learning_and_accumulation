**（1）hash 模式的实现原理**

早期的前端路由的实现就是基于 location.hash 来实现的。其实现原理很简单，location.hash 的值就是 URL 中 # 后面的内容。比如下面这个网站，它的 location.hash 的值为 '#search'：

```js
https://www.word.com#search
```

hash 路由模式的实现主要是基于下面几个特性：

- URL 中 hash 值只是客户端的一种状态，也就是说当向服务器端发出请求时，hash 部分不会被发送；
- hash 值的改变，都会在浏览器的访问历史中增加一个记录。因此我们能通过浏览器的回退、前进按钮控制hash 的切换；
- 可以通过 a 标签，并设置 href 属性，当用户点击这个标签后，URL 的 hash 值会发生改变；或者使用  JavaScript 来对 loaction.hash 进行赋值，改变 URL 的 hash 值；
- 我们可以使用 **hashchange** 事件来监听 hash 值的变化，从而对页面进行跳转（渲染）。

在使用哈希模式（hash mode）时，当哈希值改变时，浏览器的历史记录是不会增加新的记录的。在哈希模式下，哈希值的改变只会触发浏览器的滚动位置调整，并不会生成新的历史记录。

当使用哈希模式时，URL 中的哈希值由 `#` 符号后面的部分组成，例如 `http://example.com/#/about`。在这种模式下，Vue Router 会通过**监听 `hashchange` 事件来捕获哈希值的变化，从而进行路由的切换。**

当你使用 `$router.push()` 方法去改变哈希值时，Vue Router 会调用 `window.location.hash` 来修改哈希值，但这并不会生成新的历史记录。相反，它只会更新现有的历史记录中的哈希部分，并将页面滚动到相应的位置。

因此，在哈希模式下，每次哈希值的改变都不会增加新的历史记录，整个页面的切换和导航都是在同一个历史记录中进行的。这使得在单页应用（SPA）中能够使用哈希作为路由的标识符，而不会影响浏览器的正常后退和前进行为。

**（2）history 模式的实现原理**

HTML5 提供了 History API 来实现 URL 的变化。其中做最主要的 API 有以下两个：history.pushState() 和 history.repalceState()。这两个 API 可以在不进行刷新的情况下，操作浏览器的历史纪录。唯一不同的是，前者是新增一个历史记录，后者是直接替换当前的历史记录，如下所示：

```js
window.history.pushState(null, null, path);
window.history.replaceState(null, null, path);
```

history 路由模式的实现主要基于存在下面几个特性：

- pushState 和 repalceState 两个 API 来操作实现 URL 的变化 ；
- 我们可以使用 popstate 事件来监听 url 的变化，从而对页面进行跳转（渲染）；
- history.pushState() 或 history.replaceState() 不会触发 popstate 事件，这时我们需要手动触发页面跳转（渲染）

**历史模式（history mode）** 是 Vue Router 的一种路由模式，它使用浏览器的 History API 来实现路由的切换和 URL 的管理。在历史模式下，URL 中不再包含哈希（#），而是使用普通的 URL 地址。

下面是历史模式的实现原理：

1. History API：浏览器提供了一组用于操作浏览器历史记录的 API，其中包括 `pushState()`、`replaceState()` 和 `popstate` 事件。这些 API 允许 JavaScript 修改浏览器的历史记录，并监听历史记录的变化。

2. URL 重写：在历史模式下，Vue Router 通过使用 **`pushState()` 或 `replaceState()` 方法来修改浏览器的历史记录**，从而实现 URL 的变化。同时，还需要在服务器端进行相应的配置，以确保在刷新页面或直接访问路由时能够正确地返回对应的页面。

3. 监听 URL 变化：Vue Router 在初始化时会注册一个全局的 `popstate` 事件监听器，用于监听浏览器历史记录的变化。当用户点击浏览器的**前进或后退按钮、调用 `pushState()` 或 `replaceState()` 方法时，会触发 `popstate` 事件**，Vue Router 会捕获该事件并根据当前 URL 进行路由的切换。

4. 服务器配置：在使用历史模式时，为了确保在刷新页面或直接访问路由时能够正确返回对应的页面，需要在服务器端进行配置。具体而言，当服务器接收到一个请求时，需要始终返回应用的根页面（如 `index.html`），然后由 Vue Router 根据请求的 URL 进行路由的切换。


**`popstate` 事件的主要用途是允许开发者在历史记录发生变化时执行相应的操作**。通过监听 `popstate` 事件，你可以捕获历史记录的变化，并根据需要执行特定的逻辑，例如：

当使用 `pushState()` 或 `replaceState()` 修改 URL 时，它们不会自动发起网络请求。它们仅仅是修改浏览器地址栏中的 URL，并更新浏览器的历史记录，**而不会引发实际的网络请求。**

- 根据历史记录切换页面内容或组件状态
- 更新页面的 URL、查询参数或哈希值
- 执行特定的操作或逻辑，例如重新加载数据或发送请求

总结起来，历史模式通过使用浏览器的 History API 来修改浏览器历史记录和监听历史记录的变化，从而实现 URL 的变化和路由的切换。同时，还需要在服务器端进行配置，以确保在刷新页面或直接访问路由时能够正确返回对应的页面。这样，就可以以普通 URL 地址的方式来管理路由，而不需要使用哈希（#）作为标识。


**在 Vue Router 中，可以使用以下方法进行前进、后退和替换操作：（hash模式和history模式都可以）**

## 1. 前进：使用 `$router.push()` 方法可以在当前路由基础上前进到一个新的路由。该方法接受一个路由对象或一个路由路径作为参数。例如：

```javascript
// 前进到 /about 路由
this.$router.push('/about');

// 前进到命名路由
this.$router.push({ name: 'about' });

// 前进到带有参数的路由
this.$router.push({ path: '/user/123' });
```

## 2. 后退：使用 `$router.go()` 方法可以在路由历史记录中后退或前进指定的步数。如果步数为负数，则表示后退，如果步数为正数，则表示前进。例如：

```javascript
// 后退一步
this.$router.go(-1);

// 前进一步
this.$router.go(1);

// 后退两步
this.$router.go(-2);
```

## 3. 替换：使用 `$router.replace()` 方法可以替换当前路由，而不会生成新的历史记录。该方法的使用方式与 `$router.push()` 方法类似。例如：

```javascript
// 替换当前路由为 /about
this.$router.replace('/about');

// 替换当前路由为命名路由
this.$router.replace({ name: 'about' });

// 替换当前路由为带有参数的路由
this.$router.replace({ path: '/user/123' });
```

这些方法可以在 Vue 组件中使用，通过访问 `$router` 对象来调用。注意，为了使用这些方法，组件必须通过 Vue Router 进行路由配置，并且在根组件中注入了 `$router` 对象。

请注意，这些方法只适用于在 Vue 组件中进行路由操作。如果希望在 JavaScript 文件中进行路由操作，可以通过访问 Vue Router 实例来调用相应的方法。例如：

```javascript
import router from './router';

// 前进到 /about 路由
router.push('/about');

// 后退一步
router.go(-1);

// 替换当前路由为 /about
router.replace('/about');
```

这里的 `router` 是从 Vue Router 实例导出的路由实例。



hash模式：即地址栏 URL 中的 # 符号  
比如这个 URL：[http://www.abc.com/#/hello](https://link.zhihu.com/?target=http%3A//www.abc.com/%23/hello)， hash 的值为\#/hello  
它的特点在于：hash 虽然出现在 URL 中，但不会被包括在 HTTP 请求中，对后端完全没有影响，因此改变 hash 不会重新加载页面。

history模式：利用了 HTML5 History Interface 中新增的 pushState() 和 replaceState() 方法。（需要特定浏览器支持）  
这两个方法应用于浏览器的历史记录栈，在当前已有的 back()、forward()、go() 方法的基础之上，这两个方法提供了对历史记录进行修改的功能。当这两个方法执行修改时，只能改变当前地址栏的 URL，但浏览器不会向后端发送请求，也不会触发popstate事件的执行


`back()`、`forward()` 和 `go()` 是浏览器的 `history` 对象提供的方法，用于在浏览器的历史记录中进行导航。

1. `back()` 方法:
   - `back()` 方法用于将浏览器导航到历史记录中的前一个页面，实现后退功能。
   - 它相当于点击浏览器的后退按钮或调用 `history.go(-1)` 方法。
   - 示例：
     ```javascript
     // 后退一步
     history.back();
     ```

2. `forward()` 方法:
   - `forward()` 方法用于将浏览器导航到历史记录中的下一个页面，实现前进功能。
   - 它相当于点击浏览器的前进按钮或调用 `history.go(1)` 方法。
   - 示例：
     ```javascript
     // 前进一步
     history.forward();
     ```

3. `go()` 方法:
   - `go()` 方法用于在浏览器的历史记录中进行相对导航。
   - 它接受一个整数作为参数，表示导航的步数。
   - 正数表示向前导航，负数表示向后导航。
   - 示例：
     ```javascript
     // 前进一步
     history.go(1);

     // 后退一步
     history.go(-1);
     ```

这些方法可以在支持 JavaScript 的环境中使用，用于在浏览器的历史记录中实现前进和后退导航。它们对于控制浏览器的历史记录非常有用，在 Web 应用程序中可以实现页面的导航和状态管理。

**因此可以说，hash 模式和 history 模式都属于浏览器自身的特性，Vue-Router 只是利用了这两个特性（通过调用浏览器提供的接口）来实现前端路由.**

### vue中的router有两种模式：hash模式（默认）、history模式（需配置mode: 'history'）


`pushState()` 和 `replaceState()` 是浏览器的 History API 中的两个方法，用于操作浏览器的历史记录。它们的主要区别在于它们对浏览器历史记录的处理方式。

1. pushState():
   - `pushState()` 方法用于将新的状态（state）和 URL 添加到浏览器的历史记录中。
   - 它接受三个参数：`state`、`title` 和 `url`。
   - `state` 是一个表示状态的 JavaScript 对象，可以在后续的 `popstate` 事件中访问到。
   - `title` 是一个可选的字符串，表示新的历史记录的标题，目前大多数浏览器忽略该参数。
   - `url` 是新的 URL 地址，可以是相对路径或绝对路径。
   - 使用 `pushState()` 方法不会触发页面的刷新或导航，只是向浏览器历史记录中添加了一个新的条目。

2. replaceState():
   - `replaceState()` 方法用于替换当前的浏览器历史记录条目。
   - 它接受三个参数：`state`、`title` 和 `url`。
   - `state` 是一个表示状态的 JavaScript 对象，可以在后续的 `popstate` 事件中访问到。
   - `title` 是一个可选的字符串，表示新的历史记录的标题，目前大多数浏览器忽略该参数。
   - `url` 是新的 URL 地址，可以是相对路径或绝对路径。
   - 使用 `replaceState()` 方法会替换当前的历史记录条目，而不会添加新的条目，因此在浏览器的历史记录中只会保留一个条目。

总结起来，`pushState()` 方法用于添加新的历史记录条目，而 `replaceState()` 方法用于替换当前的历史记录条目。两者都可以修改 URL 地址，但 `pushState()` 会生成新的历史记录，而 `replaceState()` 则替换当前的历史记录，不会生成新的记录。