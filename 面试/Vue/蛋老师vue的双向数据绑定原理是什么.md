```js


```
![[Pasted image 20230524011930.png]]
![[Pasted image 20230524011913.png]]
![[Pasted image 20230524013755.png]]
![[Pasted image 20230524015014.png]]

Document.createDocumentFragment
https://developer.mozilla.org/zh-CN/docs/Web/API/Document/createDocumentFragment

append
# Element.append()
https://developer.mozilla.org/zh-CN/docs/Web/API/Element/append












通过数据劫持和发布订阅者模式来实现，同时利用O
![[Pasted image 20230410124428.png]]
通过数据劫持和发布订阅者模式来实现，同时利用object . defineProperty()劫持各个属性的setter和getter,
在数据发生改变的时候发布消息给订阅者，触发对应的监听回调演染视图，也就是说数据和视图时同步的，数据发生改变，视图跟着发生改变，视图改变，数据也会发生改变。
第一步:需要observer的数据对象进行递归遍历，包括子属性对象的属性，都加上setter和getter
第二步: compile模板解析指令，把模板中的变量替换成数据，然后初始化渲染视图，同时把每个指令对应的节点绑定上更
新函数，添加订阅者，如果数据变化，收到通知，更新视图
第三步: Watcher订阅者是observer和Compile之间的通信桥梁，作用:

	1.在自身实例化的时候忘订阅器内添加自己
	2.自身要有一个update()方法
	3.等待属性变动时，调用自身的update方法，触发compile这种的回调
	
第四步: MVWM作 为数据绑定的入口，整合了observer. compile 和Iwatcher三者，通过observer来 监听自己的数据变化，
通过compile解析模板指令，最后利用watcherbal



