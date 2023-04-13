组件从创建到销毁的过程就是它的生命周期  [[组件的生命周期]]
创建

	beforeCreate
		在这个阶段属性和方法都不能使用		
	created
		这里时实例创建完成之后，在这里完成了数据监测，可以使用数据，修改数据，不会触发updated，也不会更新视图		
挂载

	beforeMount
		完成了模板的编译，虚拟DOM也完成创建，即将渲染，修改数据，不会触发updated
		
	Mounted
		把编译好的模板挂载到页面，这里可以发送异步请求也可以访问DOM节点
更新

	beforeUpdate
		组件数据更新之前使用，数据是新的，页面上的数据时旧的，组件即将更新，准备渲染，可以改数据
		
	updated
		render重新做了渲染，这时数据和页面都是新的，避免在此更新数据
销毁

	beforeDestroy
		实例销毁前，在这里实例还可以用，可以清楚定时器等等
		
	destroyed
		组件已经被销毁了，全部都销毁
使用了keep-alive时多出两个周期:

	activited
		组件激活时
		
	deactivited
		组件被销毁时