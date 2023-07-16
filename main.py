from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def encrypt_cbc(key, iv, plaintext):
    # 初始化 AES 密码器和 CBC 模式
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    # 创建加密器
    encryptor = cipher.encryptor()
    # 如果最后一个分组不足 16 个字节，则需要填充
    if len(plaintext) % 16 != 0:
        padding_size = 16 - len(plaintext) % 16
        plaintext += bytes([padding_size] * padding_size)
    # 加密明文
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext


def decrypt_cbc(key, iv, ciphertext):
    # 初始化 AES 密码器和 CBC 模式
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    # 创建解密器
    decryptor = cipher.decryptor()
    # 解密密文
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    # 如果最后一个明文分组被填充了，需要将填充数据删除
    if plaintext[-1] <= 16:
        padding_size = plaintext[-1]
        plaintext = plaintext[:-padding_size]
    return plaintext


def test():
    key = b"1234567891011123"
    iv = b"8888888888888888"
    plaintext = b"qwertyuiopasdfgh"
    encrypt_text = encrypt_cbc(key, iv, plaintext)
    print(encrypt_text)
    decrypt_text = decrypt_cbc(key, iv, encrypt_text)
    print(decrypt_text)
    return 0


test()
