#coding:utf8
__time__ = '2019/1/8 11:54'
__author__ = 'SYJ'

import requests ,json

url='http://auth.matafy.com/mtfy/user/login/send/sms'
body={
	"countryCode": "+86",
	"mobile": "13761917640",
	"language": "cn"
}

req=requests.post(url,json=body)
print (req.json())



