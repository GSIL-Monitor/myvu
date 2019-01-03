#coding:utf8
__time__ = '2018/5/8 16:49'
__author__ = 'SYJ'

import requests,re

requests.packages.urllib3.disable_warnings()

url='https://test.uenpay.com/uenams/'
header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "X-Requested-With":"XMLHttpRequest",
            "Accept":"application/json, text/javascript, */*; q=0.01",
            # "Cookie":"JSESSIONID=CCE10C8EFB1519A1685093999CD19A4A;JSESSIONID=0B5C0B94703E18D7BC4B1373CB550F5A",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer":"https://test.uenpay.com/uenams",
            "Origin":"https://test.uenpay.com"}
req=requests.get(url,verify=False)
print (req.text)
id=re.findall('jsessionid%(.*?)/',req.text)[0]
jsid='jsessionid'+'='+id
print (jsid)
ur=re.findall('href=\'(.*?)\'</script>',req.text)
# casjs=re.findall('jquery.min.js;(.*?)"',req.text)
# jsid=casjs[0]
# print (jsid)

url1=""+(ur[0])+""
header1={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "X-Requested-With":"XMLHttpRequest",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            # "Cookie": "JSESSIONID=F2D7E3DAF172CD668AD5D6EB831F290D",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer":"https://test.uenpay.com/uenams/",
            "Upgrade-Insecure-Requests":"1",
            "Host":"test.uenpay.com"}
            # "Cookie":""+(jsid)+""}
#
#
req1=requests.get(url1,headers=header1,verify=False)
# print (req1.text)
casjs=re.findall('jquery.min.js;(.*?)"',req1.text)
re1=re.findall('name=\"lt\" value="(.*?)"',req1.text)
execution=re.findall('name="execution" value="(.*?)"',req1.text)[0]
LT=re1[0]
print (re1[0])
cas_js=casjs[0]
print (cas_js)
print (jsid)
print (ur[0])
print (execution)

url2="https://test.uenpay.com/cas/login?service=https%3A%2F%2Ftest.uenpay.com%2Fuenams%2F%3Bjsessionid%"+(id)+"/"
header2={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Cookie":cas_js,
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer":url2,
            "Origin":"https://test.uenpay.com",
            "Host":"test.uenpay.com",
            "Upgrade-Insecure-Requests":"1",
            "Cache-Control":"max-age=0"}
body={"username":"admin",
      "password":"123456",
      "code":"6666",
      "lt":""+(LT)+"",
      "execution":execution,
      "_eventId":"submit",
      "submit":"登录"}
#获取验证码,必须获得验证码然后去cas验证服务器才认，否则就跳转回登录页面，这一步很关键
r=requests.session()
r1=r.get('https://test.uenpay.com/cas/captcha.htm',headers=header2,verify=False)
req2=r.post(url2,headers=header2,data=body,verify=False)
# print (req2.headers)
# print (req2.text)
req3=r.post('https://test.uenpay.com/uenams/common/menu/admin',verify=False)
print (req3.json()[0])