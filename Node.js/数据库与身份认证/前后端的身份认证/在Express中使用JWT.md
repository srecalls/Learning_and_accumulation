## 安装JWT相关的包
![[Pasted image 20230314162642.png]]

## 导入JWT相关的包 jsonwebtoken
![[Pasted image 20230314162659.png]]

## 定义secret密钥
![[Pasted image 20230314162759.png]]
![[Pasted image 20230314162742.png]]

## 在登录成功后生产JWT字符串 jwt.sign
![[Pasted image 20230314162823.png]]
![[Pasted image 20230314162919.png]]
## 将JWT字符串还原为JSON对象 expressJWT
![[Pasted image 20230314163020.png]]

## 使用req.user获取用户信息 req.user
![[Pasted image 20230314163129.png]]
![[Pasted image 20230314163216.png]]
![[Pasted image 20230314163227.png]]

## 捕获解析JWT失败后产生的错误
![[Pasted image 20230314163414.png]]
