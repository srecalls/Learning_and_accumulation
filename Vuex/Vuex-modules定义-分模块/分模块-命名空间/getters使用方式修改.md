###   getters使用方式修改

# 方式1: 组件内 - **直接**使用
    
-   原语法:

        this.$store.getters.计算属性名
        
-   开命名空间后语法:

        this.$store.getters['模块名/计算属性名']     

# 方式2: 组件内 - **映射**使用
    
-   原语法:

		   ...mapGetters(['getters里计算属性名'])
 -  开命名空间后语法:

        ...mapGetters("模块名", ['getters里计算属性名'])