1. webpack 默认只能打包处理.js 结尾的文件，处理不了其它后缀的文件
2. 由于代码中包含了index.css 这个文件，因此 webpack默认处理不了
3. 当 webpack 发现某个文件处理不了的时候，会查找 webpack.config,js 这个配置文件看 module.rules 数组中，是否配置了对应的loader 加载器
4. webpack把index.css 这个文件，先转交给最后一个loader 进行处理 (先转交给css-loader)
5. 当css-loader 处理完毕之后，会把处理的结果，转交给下一个loader (转交给 style-loader)
6. 当style-loader 处理完毕之后，发现没有下一个loader了，于是就把处理的结果，转交给了 webpack
7. webpack 把style-loader 处理的结果，合并到/dist/bundlejs 中，最终生成打包好的文件。


![[Pasted image 20230226185401.png]]
![[Pasted image 20230226185744.png]]
![[Pasted image 20230226185808.png]]
![[Pasted image 20230226190016.png]]
![[Pasted image 20230226190717.png]]
![[Pasted image 20230226191922.png]]
![[Pasted image 20230226193735.png]]
![[Pasted image 20230226194424.png]]
![[Pasted image 20230226195318.png]]
![[Pasted image 20230226195427.png]]
![[Pasted image 20230226195913.png]]
![[Pasted image 20230226200022.png]]
