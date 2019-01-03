#coding:utf8
__time__ = '2018/9/7 15:29'
__author__ = 'SYJ'

import base64,hashlib
from Crypto.Cipher import AES

text='{"data":{"userId":"1721"},"meta":{"accessToken":"uf8NrD61SlG0pGGSeLv3og","appKey":"vj5DYRpZ","clientName":"Android_PACM00_8.1.0_qsj","clientVersion":"1.2.4","transCode":"100100401","transDate":"20180907144809","username":"13761911171"}}'
hash_256 = hashlib.sha256()
hash_256.update(text.encode('utf-8'))
hash_256_value = hash_256.hexdigest()
print (hash_256_value)

# str不是16的倍数那就补足为16的倍数
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes
#加密方法
def encrypt_oracle():
    # 秘钥
    # key = '123456'
    key = 'y4fqVJFxKi6dwfaMHNgfAQ=='  # 密钥base64.b64decode('y4fqVJFxKi6dwfaMHNgfAQ==')
    # 待加密文本
    text = '{"data":{"userId":"1721"},"meta":{"accessToken":"uf8NrD61SlG0pGGSeLv3og","appKey":"vj5DYRpZ","clientName":"Android_PACM00_8.1.0_qsj","clientVersion":"1.2.4","transCode":"100100401","transDate":"20180907144809","username":"13761911171"}}'
    # 初始化加密器
    aes = AES.new(base64.b64decode(add_to_16(key)), AES.MODE_ECB)
    #先进行aes加密
    print ((add_to_16(text)))
    encrypt_aes = aes.encrypt(add_to_16(text))
    #用base64转成字符串形式
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
    print(encrypted_text)
#解密方法
def decrypt_oralce(text):
    # 秘钥
    # key = '123456'
    key = base64.b64decode('y4fqVJFxKi6dwfaMHNgfAQ==')  # 密钥
    # 密文
    # text = 'UNPXe9KZIHDs/EJfITME3AGSQBFBdpmC5z8FgzsXYKyUN9LYmSP+aC2qmHu80cT729ZOkWz2OztVD/8zhAF6OYHSjVflqXjAfmYmR/2Jw4xVZX2IbFFNnqeljud6/rl4WAsN4WRBCvOFqgeN/09BxQsyfw++xmFPJjKkuOI+/01aKCD+8G8Xwe7RWoOISrgMMqqbrCH3L/7+K9lddl/DyMEZpD1Vr+6xgNvd1EM5l+BsvMitXqfhhTL/V51LsfZL8XBOUbzG1+84IQp5DPwQ259+pxrR07HGiv8J9uaUIOW6iSVApjuH1v6eYYylMsYt'
    # text='UNPXe9KZIHDs/EJfITME3AGSQBFBdpmC5z8FgzsXYKyUN9LYmSP+aC2qmHu80cT729ZOkWz2OztVD/8zhAF6OYHSjVflqXjAfmYmR/2Jw4xVZX2IbFFNnqeljud6/rl4WAsN4WRBCvOFqgeN/09BxQsyfw++xmFPJjKkuOI+/01aKCD+8G8Xwe7RWoOISrgMMqqbrCH3L/7+K9lddl/DyMEZpD1Vr+6xgNvd1EM5l+BsvMitXqfhhTL/V51LsfZL8XBOUbzG1+84IQp5DPwQ259+pxrR07HGiv8J9uaUIOXUYH5qvrKmpJsNLfICN2UQ'
    # 初始化加密器
    # print (text)
    aes = AES.new(key, AES.MODE_ECB)
    text=base64.b64decode(text)
    print (text)
    #优先逆向解密base64成bytes
    # base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
    #执行解密密并转码返回str
    # decrypted_text = str(aes.decrypt(base64_decrypted),encoding='utf-8').replace('\0','')
    decrypted_text = aes.decrypt(text)
    print(decrypted_text)

if __name__ == '__main__':
   # encrypt_oracle()
    text = 'UNPXe9KZIHDs/EJfITME3AGSQBFBdpmC5z8FgzsXYKyUN9LYmSP+aC2qmHu80cT729ZOkWz2OztVD/8zhAF6OYHSjVflqXjAfmYmR/2Jw4xVZX2IbFFNnqeljud6/rl4WAsN4WRBCvOFqgeN/09BxQsyfw++xmFPJjKkuOI+/01aKCD+8G8Xwe7RWoOISrgMMqqbrCH3L/7+K9lddl/DyMEZpD1Vr+6xgNvd1EM5l+BsvMitXqfhhTL/V51LsfZL8XBOUbzG1+84IQp5DPwQ259+pxrR07HGiv8J9uaUIOW6iSVApjuH1v6eYYylMsYt'
    text1 = b'78ad14e0d18402b53b5d11c3cfee36e3d2c75e0a7688d215bbf9050c119e28d8bgmiopS4bxBuRXTu7Yfjwi5ZvPBm89YbvXfqYx5TBqe6Sy5U/o3Qi9TsB2P5YTGoGsaCmNUTID56mwhk/N/1BePx+CY9FzD90be16kBAWcshxF6YZnLXAVKtq+noWg6hbEd21Kt1CzibAaHxA+8A1sqmGmok+GJbHKlbKN3uuYjA3oiPfKKEjBkWMQrXbNXHdxcBtQlnMG5fWQrWjczD3pNyoJYLzhLi3EMQXTY6Uuud2az3geBUN0Y5NoqTTc/FJkXt11nUt+m9Ai/5sAzsymqvGLSDXI5BeBp3rAE3VbBqXHLMezuE2slQjAMXtztswndCPrd11VdseTt1XP0gNA=='
    # decrypt_oralce(text)
    decrypt_oralce(text1)
