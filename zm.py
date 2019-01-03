#coding:utf8
import sys

set('utf-8')
import binascii
__time__ = '2018/12/4 16:18'
__author__ = 'SYJ'



def hex_to_str(s):
    return ''.join([chr(i) for i in [int(b, 16) for b in s.split(' ')]])

if __name__ == '__main__':
    a = 'i am request,\x44\x88\x91\xE6\x98\xAF\xE8\xAF\xB7\xE6\xB1\x82'.encode('utf-8').decode('gbk')
    # print (hex_to_str(a))
    print (a)

    # print (chardet.detect(a))
    # a.encode('gbk').decode('GBK')
    # print (a)