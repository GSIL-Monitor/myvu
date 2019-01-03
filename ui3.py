from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import hashlib,base64,json,re


BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]
class PrpCrypt(object):

    def __init__(self, ):
        key = base64.b64decode('y4fqVJFxKi6dwfaMHNgfAQ==')  # 密钥
        print (key)
        self.key = key
        self.mode = AES.MODE_ECB

    # 加密函数，如果text不足16位就用空格补足为16位，
    # 如果大于16当时不是16的倍数，那就补足为16的倍数。
    def encrypt(self, text):
        hash_256 = hashlib.sha256()
        hash_256.update(text.encode('utf-8'))
        hash_256_value = hash_256.hexdigest()
        print (hash_256_value)
        # text = text.encode('utf-8')
        # print (type(text))
        # text=str(text,encoding='utf-8')
        # text=json.dumps(text)
        # print (text)
        # text=bytes(text,encoding='utf-8')
        # print (text)
        # print (type(json.dumps(A)))
        cryptor = AES.new(self.key, self.mode)
        # 这里密钥key 长度必须为16（AES-128）,
        # 24（AES-192）,或者32 （AES-256）Bytes 长度
        # 目前AES-128 足够目前使用
        text = pad(text)
        length = 16
        count = len(text)
        print ('count:%s'%(count))
        # print (text)
        if count < length:
            add = (length - count)
            # print (add)
            # \0 backspace
            # text = text + ('\0' * add)
            text = text + ('\x04' * add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))
            # text = text + ('\0' * add)
            # text = text + ('\0' * add)    #先字符串补0，然后转字节
            # pad(text)
            # print (text)
            # print (text)
            # print (bytes(text,encoding='utf-8'))
            text=bytes(text,encoding='utf-8')
        print (type(text))
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        # return self.ciphertext
        # return b2a_hex(self.ci
        # phertext)
        return hash_256_value+str(base64.b64encode(self.ciphertext),encoding='utf-8')

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        # text=bytes(text,encoding='utf-8')
        text = text[64:]
        text = base64.b64decode(text)
        print(text)
        cryptor = AES.new(self.key, self.mode)
        # plain_text = cryptor.decrypt(a2b_hex(text))
        plain_text = cryptor.decrypt(text).decode('utf-8')
        print (plain_text)
        # print (plain_text[-1:])
        # str1=str(plain_text[-1:])
        # print (str1)
        # print (plain_text.split(b'"+str(str1)+"'))
        # print (bytearray(plain_text.split(b'clientVersion')))
        # num=re.findall("(\0)",str(bytearray(plain_text)))
        # print (num)
        # print ((plain_text))
        # print (unpad(bytes.decode(plain_text).rstrip('\0')))
        # return plain_text.rstrip('\0')
        return (unpad(plain_text))
        # return plain_text


if __name__ == '__main__':
    hash_256 = hashlib.sha256()
    key=base64.b64decode('y4fqVJFxKi6dwfaMHNgfAQ==')  #密钥
    # print (key.hex())
    # print ('密钥:%s'%(key))
    A = '{"meta":{"appKey":"vj5DYRpZ","clientVersion":"1.2.5","clientName":"IOS_11.4.1_qsj","username":"13764906431","accessToken":"fVJAAr1nT1eikxcAuU7oNg","transCode":"100100401","transDate":"20180907094020"},"data":{"orgId":"58205"}}'
    pc = PrpCrypt()  # 初始化密钥
    e = pc.encrypt(A)  # 加密
    # d = pc.decrypt(e)  # 解密
    # print("密文D:%s"%(e))  #密文D
    # print("解密:", d)
    hash_256.update(A.encode('utf-8'))
    hash_256_value = hash_256.hexdigest()
    obj = hashlib.new('ripemd160', hash_256_value.encode('utf-8'))
    ripemd_160_value = obj.hexdigest()
    # print("签名Ssha256:%s"%(hash_256_value))  # 16进制  签名S hexS
    # print (hash_256_value.hex())
    # baseD=base64.b64encode(e)
    # print (base64.b64decode(baseD))
    # print ('base64(D):%s'%(str(baseD,encoding='utf-8')))
    # print ('发送的报文:%s'%(hash_256_value+str(baseD,encoding='utf-8')))
    f=b"d61a479471f2942dc2dfe2ee047b91dd4ba458c811f529daa4c61933553e569cUNPXe9KZIHDs/EJfITME3AGSQBFBdpmC5z8FgzsXYKyUN9LYmSP+aC2qmHu80cT729ZOkWz2OztVD/8zhAF6OYHSjVflqXjAfmYmR/2Jw4xVZX2IbFFNnqeljud6/rl4WAsN4WRBCvOFqgeN/09BxQsyfw++xmFPJjKkuOI+/01aKCD+8G8Xwe7RWoOISrgMMqqbrCH3L/7+K9lddl/DyMEZpD1Vr+6xgNvd1EM5l+BsvMitXqfhhTL/V51LsfZL8XBOUbzG1+84IQp5DPwQ259+pxrR07HGiv8J9uaUIOW6iSVApjuH1v6eYYylMsYt"
    # r1=base64.b64decode(bytes(baseD))
    # print (base64.b64decode(r1))
    g=b"78ad14e0d18402b53b5d11c3cfee36e3d2c75e0a7688d215bbf9050c119e28d8bgmiopS4bxBuRXTu7Yfjwi5ZvPBm89YbvXfqYx5TBqe6Sy5U/o3Qi9TsB2P5YTGoGsaCmNUTID56mwhk/N/1BePx+CY9FzD90be16kBAWcshxF6YZnLXAVKtq+noWg6hbEd21Kt1CzibAaHxA+8A1sqmGmok+GJbHKlbKN3uuYjA3oiPfKKEjBkWMQrXbNXHdxcBtQlnMG5fWQrWjczD3pNyoJYLzhLi3EMQXTY6Uuud2az3geBUN0Y5NoqTTc/FJkXt11nUt+m9Ai/5sAzsymqvGLSDXI5BeBp3rAE3VbBqXHLMezuE2slQjAMXtztswndCPrd11VdseTt1XP0gNA=="
    # g=g[64:]
    # f = f[64:]
    print (g[63:])
    h=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    # print (base64.b64encode(h))
    # print (base64.b64decode(h))
    # r = base64.b64decode(f)
    # r1 = base64.b64decode(g)
    # print (pc.decrypt(bytes(f,encoding='utf-8')))
    # print('解密报文:%s'%(pc.decrypt(f)))
    print('解密报文:%s' % (pc.decrypt(g)))
    # print (pc.decrypt(g))
    result=(pc.decrypt(g))

    # print (result)
    # print (eval(result))
    # print (eval(pc.decrypt(g)))
    # result=pc.decrypt(g)
    print (json.loads(result))
    # for i in range(10):
    #     print (PrpCrypt())