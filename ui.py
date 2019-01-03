

from Crypto.Cipher import AES
import hashlib,base64

hash_256 = hashlib.sha256()
print("welcome python hashlib world!")
hash_str = '{"meta":{"appKey":"vj5DYRpZ","clientVersion":"1.2.3","clientName":"IOS_11.0.3_qsj","username":"13761913201","accessToken":"hgu-4rz-QluTO4iHO6iOHg","transCode":"100100401","transDate":"20180904174029"},"data":{"odName":"tgb","userId":"1705"},"page":{"pageSize":"10","pageNumber":"0"}}'
hash_256.update(hash_str.encode('utf-8'))
hash_256_value = hash_256.hexdigest()
obj = hashlib.new('ripemd160', hash_256_value.encode('utf-8'))
ripemd_160_value = obj.hexdigest()
print("sha256:", hash_256_value)  # 16进制
print("ripemd160 :", ripemd_160_value)


class MyAES:
    # def __init__(self, key, iv):
    #     self.key = bytes(key, encoding='utf8')
    #     self.iv = bytes(iv, encoding='utf8')
    #     self.mode = AES.MODE_CBC
    #
    # def my_encrypt(self, text):
    #     """加密函数"""
    #     # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）
    #     my_aes = AES.new(self.key, self.mode, self.iv)
    #     # 如果AES加密的text不是16的倍数，那就使用PKCS5Padding来为text填充（例如缺6位，则补6个6），如果刚好是16的倍数，则补16个bytes的16
    #     length = 16
    #     count = len(text)
    #     self.padding = length - (count % length)
    #     text = text + (chr(self.padding) * self.padding)
    #     text = bytes(text, encoding='utf8')  # 加密的文本必须是bytes
    #     cipher_text = my_aes.encrypt(text)
    #     # 统一把加密后的bytes转化为base64
    #     return str(base64.b64encode(cipher_text), encoding='utf8')
    #
    # def my_decrypt(self, text):
    #     """用base64解密后，用rstrip()去掉补足的字符"""
    #     my_aes = AES.new(self.key, self.mode, self.iv)
    #     plain_text = my_aes.decrypt(base64.b64decode(bytes(text, encoding='utf8')))
    #     return str(plain_text, encoding='utf8').rstrip(chr(self.padding))

    def my_to_base64(self,text):
        a=base64.b64decode(text)
        print (a)




if __name__ == '__main__':
    # sec=MyAES()
    # app_cryptic_secret_key = 'y4fqVJFxKi6dwfaMHNgfAQ'
    # sec.my_to_base64(app_cryptic_secret_key)
    print (base64.b64decode('y4fqVJFxKi6dwfaMHNgfAQ=='))
