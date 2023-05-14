###   actions使用方式修改

# 方式1: 组件内 - **直接**使用

-   原语法:

        this.$store.dispatch("actions里的函数名", 具体值)

-   开命名空间后语法:

        this.$store.dispatch("模块名/actions里的函数名", 具体值)

# 方式2: 组件内 - **映射**使用

-   原语法:

	    ...mapActions(['actions里方法名'])

 -   开命名空间后语法:

    ...mapActions("模块名", ['actions里方法名'])