
基于OpenSSL开源库，实现以下公钥应用：

1）RSA公钥加解密（使用RSA-OAEP模式）；

2）ECDSA数字签名（给定一个文件，给出该文件的签名，验证文件修改前后的签名有效性）；

3）SM2数字签名；

4）思考题：如果在ECDSA、SM2中用同样的随机数k签名两次，攻击者能否解出私钥？给出Python实验证明（本题为选做题，有兴趣同学可选做）
好的，下面是给这个Python代码加上注释的示例：

## 1）RSA公钥加解密（使用RSA-OAEP模式）；
```python
# 导入需要的模块
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# 定义RSA密钥长度和明文
key_size = 2048
plaintext = b'Hello, RSA!'

# 生成RSA密钥对
private_key = rsa.generate_private_key(
    public_exponent=65537, # 公钥指数
    key_size=key_size # 密钥长度
)

# 获取公钥
public_key = private_key.public_key()

# 加密
ciphertext = public_key.encrypt(
    plaintext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()), # 随机数生成函数
        algorithm=hashes.SHA256(), # 哈希算法
        label=None
    )
)

# 输出加密后的密文
print('Ciphertext:', ciphertext.hex())

# 解密
try:
    decryptedtext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()), # 随机数生成函数
            algorithm=hashes.SHA256(), # 哈希算法
            label=None
        )
    )
    # 输出解密后的明文
    print('Decrypted text:', decryptedtext.decode('utf-8'))
except ValueError as e:
    # 输出解密失败的错误信息
    print('Error decrypting message:', e)
```

注释如下：

1. 导入需要的模块：`rsa`和`padding`模块来实现RSA加解密，`serialization`和`hashes`模块用于密钥和哈希算法的处理。
2. 定义RSA密钥长度和明文。
3. 使用`rsa.generate_private_key()`函数生成一个RSA密钥对，设置公钥指数为65537，密钥长度为key_size。
4. 获取RSA密钥对的公钥。
5. 使用公钥对明文进行加密，使用RSA-OAEP填充模式，填充参数包括随机数生成函数（MGF1）和哈希算法。
6. 输出加密后的密文。
7. 使用私钥对密文进行解密，使用RSA-OAEP填充模式，填充参数同上。
8. 输出解密后的明文。
9. 如果解密失败，则输出错误信息。

请注意，这只是一个简单的示例，用于演示如何使用Python语言和`cryptography`模块实现RSA公钥加解密。在实际应用中，您需要更多的安全性措施，例如使用更长的密钥长度、使用更安全的填充模式、使用数字签名验证密文的完整性等。同时，您需要注意密钥的管理和保护，防止密钥泄漏或被攻击者获取。


## 2）ECDSA数字签名（给定一个文件，给出该文件的签名，验证文件修改前后的签名有效性）；

ECDSA（Elliptic Curve Digital Signature Algorithm）是一种基于椭圆曲线的数字签名算法，可以用于验证数字信息的完整性和真实性。下面是使用Python的OpenSSL库实现ECDSA数字签名和验证的示例代码：

```python
from OpenSSL.crypto import load_privatekey, load_publickey, PKey, TYPE_ECDSA, FILETYPE_PEM, sign, verify
from OpenSSL import crypto
import hashlib

# 读取私钥文件
with open("private_key.pem", "rb") as f:
    private_key = load_privatekey(FILETYPE_PEM, f.read())

# 读取公钥文件
with open("public_key.pem", "rb") as f:
    public_key = load_publickey(FILETYPE_PEM, f.read())

# 读取要签名的文件
with open("file.txt", "rb") as f:
    file_data = f.read()

# 计算文件哈希值
hash_value = hashlib.sha256(file_data).digest()

# 使用私钥对哈希值进行签名
signature = sign(private_key, hash_value, "sha256")

# 输出签名结果
print("Signature: ", signature.hex())

# 使用公钥对签名进行验证
is_valid = verify(public_key, signature, hash_value, "sha256")

# 输出验证结果
if is_valid:
    print("Signature is valid")
else:
    print("Signature is invalid")

# 修改文件内容
with open("file.txt", "wb") as f:
    f.write(b"This is a modified file.")

# 重新计算文件哈希值
with open("file.txt", "rb") as f:
    modified_file_data = f.read()
modified_hash_value = hashlib.sha256(modified_file_data).digest()

# 使用公钥对修改后的哈希值进行验证
is_valid = verify(public_key, signature, modified_hash_value, "sha256")

# 输出验证结果
if is_valid:
    print("The signature is still valid after file modification")
else:
    print("The signature is invalid after file modification")
```
![[Pasted image 20230606153129.png]]
![[Pasted image 20230606153119.png]]
## 3）SM2数字签名；
