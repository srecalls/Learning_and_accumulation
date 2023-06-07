明文填充：

分组密码Block Cipher需要在加载前确保每个每组的长度都是分组长度的整数倍。一般情况下，明文的最后一个分组很有可能会出现长度不足分组的长度:

 ![](https://img2018.cnblogs.com/blog/1063309/201907/1063309-20190701163729141-914324832.png)

这个时候，普遍的做法是在最后一个分组后填充一个固定的值，这个值的大小为填充的字节总数。即假如最后还差3个字符，则填充3个0×03

![](https://img2018.cnblogs.com/blog/1063309/201907/1063309-20190701163820855-764150172.png)

 因为填充发生在最后一个分组，所以我们主要关注最后一个分组

![](https://img2018.cnblogs.com/blog/1063309/201907/1063309-20190701165149102-1362886443.png)

这里有个条件是服务器会对我们显示padding error的异常，如果不回显那么肯定无法判断进行利用

比如在web应用中，如果Padding不正确，则应用程序很可能会返回500的错误(程序执行错误)；如果Padding正确，但解密出来的内容不正确，则可能会返回200的自定义错误(这只是业务上的规定)，所以，这种区别就可以成为一个二值逻辑的”注入点”。

攻击成立的两个重要假设前提:

1. 攻击者能够获得密文（Ciphertext），以及附带在密文前面的IV（初始化向量）
2. 攻击者能够触发密文的解密过程，且能够知道密文的解密结果

我们的攻击流程实际上是不断地调整IV的值，以希望解密后，最后一个字节的值为正确的Padding Byte，因为padding正确时，这里padding正确是指最终解密并异或出来的明文最后一个字节在正确padding的范围内就是正确的，虽然最后明文不一定正确，但是padding是合法的，所以服务器才会返回200

![](https://img2018.cnblogs.com/blog/1063309/201907/1063309-20190701172108457-1214772788.png)

此时若我们输入的初始向量为：

![](https://img2018.cnblogs.com/blog/1063309/201907/1063309-20190701174122315-657054960.png)

这时候最后一组密文经过密钥解密后再和我们输入的初始向量异或以后将得到

![](https://img2018.cnblogs.com/blog/1063309/201907/1063309-20190701174501318-2135956034.png)

最后一位是0x3d，明显不满足padding的范围，所以肯定会返回500，那么此时假设padding为0x01，那么通过遍历初始向量最后一位将存在唯一一个初始向量值将于服务端解密得到的中间值异或以后得到0x01，直接遍历

IV值就可以得到该值，之后我们就可以利用以下的公式

![](https://img2018.cnblogs.com/blog/1063309/201907/1063309-20190702214548464-2065561512.png)

![](https://img2018.cnblogs.com/blog/1063309/201907/1063309-20190702214724083-971135812.png)

因此可以求出明文第八个字节，之后我们需要继续求出其第七个字节的明文值，那么此时假设填充了两个字节，那么为0x02，0x02，此时我们需要更新最后一位要输入的IV值为中间值第八位异或上0x02(第八位中间值根据明文第八位异或上原来的IV值第八位即可得到)，因为此时我们便利的后两位IV值，此时服务器期望得到是0x02

![](https://img2018.cnblogs.com/blog/1063309/201907/1063309-20190702220036494-1417692188.png)

此时继续遍历第七位IV值，直到得到0x02，此时可以得到明文第七位，依次类推可以得到所有的明文。




```python

import requests

  

# CBC模式密文blocks

cipher_text = # 待解密的CBC模式密文

  

# 接口地址,后端为Padding Oracle

url = "http://example.com/oracle"

  

# 重复发送相同密文实现错误填充,获取密文前面的一个byte

def get_byte(cipher_text,pos):

    byte = 0

    for i in range(256):    

        test_text = cipher_text[:pos] + chr(i) + cipher_text[pos+1:]

        res = requests.post(url,data=test_text).text  

        if res == 'Wrong padding':  

            byte = i  

            break

    return byte

  

# 解密密文,逐字节解密    

plain_text = b""

for i in range(len(cipher_text)):

    byte = get_byte(cipher_text, i)

    plain_text += bytes([byte])

    # 修改当前block中byte为已解密byte

    cipher_text = cipher_text[:i] + chr(byte) + cipher_text[i+1:]

print(plain_text.decode())
```