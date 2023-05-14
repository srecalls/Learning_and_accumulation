### mutations使用方式修改

# 方式1: 组件内 - **直接**使用
    
- 原语法:

		 this.$store.commit("mutations里的函数名", 具体值)

-    开命名空间后语法:

		  this.$store.commit("模块名/mutations里的函数名", 具体值)

# 方式2: 组件内 - **映射**使用


- 原语法:

		...mapMutations(['mutations里方法名'])

 -   开命名空间后语法:
 
	...mapMutations("模块名", ['mutations里方法名'])