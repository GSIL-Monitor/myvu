from cryptography.fernet import Fernet
import base64,hashlib
import ui3,json
# cipher_key = base64.b64decode('YmluYXJ5AHN0cmluZw==')
# base64.b64encode('i\xb7\x1d\xfb\xef\xff')
# print (base64.b64decode('y4fqVJFxKi6dwfaMHNgfAQ=='))
# print (base64.b64decode('YmluYXJ5AHN0cmluZw=='))
# print (base64.b64encode(b'\xcb\x87\xeaT\x91q*.\x9d\xc1\xf6\x8c\x1c\xd8\x1f\x01'))
# print (cipher_key)

# -*- coding: utf-8 -*-
# __author__ = 'Carry'

# key=base64.b64decode('y4fqVJFxKi6dwfaMHNgfAQ==')  #密钥
data = '{"data":{"userId":"1721"},"meta":{"accessToken":"uf8NrD61SlG0pGGSeLv3og","appKey":"vj5DYRpZ","clientName":"Android_PACM00_8.1.0_qsj","clientVersion":"1.2.4","transCode":"100100401","transDate":"20180907144809","username":"13761911171"}}'
data1 =  {"data":{"phoneNumber":"13764906431"},"page":{"pageNumber":"0","pageSize":"10"},"meta":{"appKey":"vj5DYRpZ","accessToken":"w6IUpEuSTVi2a9s9JxqL0Q","clientName":"IOS_10.3.3_qsj","clientVersion":"1.2.4","transCode":"100100401","transDate":"20180907144809","username":"13764906431"}}
data2=  {"data":{"parentCode":"0"},"page":{"pageNumber":1,"pageSize":10},"meta":{"appKey":"vj5DYRpZ","accessToken":"mallList","clientName":"IOS_9.3.1","clientVersion":"v1.0","transCode":"1001","transDate":"2018-5-1710:50:00","username":13764906431}}
# print (type(data))
# print (data)
# print (json.dumps(data1).replace(' ',''))

# print (type(json.dumps(data1)))
# print (type(str(data)))
A=ui3.PrpCrypt()
# e = A.encrypt(json.dumps(data1).replace(' ',''))
# e = A.encrypt(data)
f = A.encrypt(json.dumps(data1).replace(' ',''))
# print (e)
print (f)

a={"aa":[{"b":1,"c":2}]}
print (a['aa'][0].keys())

# print (hash_256_value)

# correct_json=str(hash_256_value)+e
# print (correct_json)

