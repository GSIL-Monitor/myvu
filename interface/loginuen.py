#coding:utf8
__time__ = '2018/5/8 15:53'
__author__ = 'SYJ'

# -*- coding: utf-8 -*-
import requests, json,re,unittest,os,yaml
from common.log import Log
from common.orc import Uenoracle
from common.getexcel import excel



# 获取当前文件路径 D:/WorkSpace/StudyPractice/Python_Yaml/YamlStudy
filePath = 'H:\之前项目\pythonstudy\pythonstudy\python3\project1\project_config'
# 获取当前文件的Realpath  D:\WorkSpace\StudyPractice\Python_Yaml\YamlStudy\YamlDemo.py
fileNamePath = os.path.split(os.path.realpath(__file__))[0]
# 获取配置文件的路径 D:/WorkSpace/StudyPractice/Python_Yaml/YamlStudy\config.yaml
yamlPath = os.path.join(filePath, 'config.yaml')
'''读取用例文件的路径以及名称'''
script_path = os.path.realpath(__file__)
filename = os.path.split(script_path)[1]

class uenpay(object):
    def __init__(self, s,appname):
        self.s = s
        '''定义日志'''
        self.Log=Log(filename)
        self.read=Uenoracle(appname,'app_config','config.yaml').read_config()
        self.AppLoginBody = self.read['test_apilogin']['bodyAndheader']['Body']
        self.AppLoginHeader = self.read['test_apilogin']['bodyAndheader']['Header']
        self.AppLoginUrl = self.read['test_apilogin']['Host']+self.read['test_apilogin']['bodyAndheader']['Url']
        # self.Log.info(self.AppLoginBody)
        # self.Log.info(self.AppLoginHeader)
        # self.Log.info(self.AppLoginUrl)

        # print (self.AppLoginHeader)
        # self.bodyAndheader = self.read['bodyAndheader']
        # print (self.bodyAndheader['AppLoginBody'])
        # print(self.bodyAndheader['AppLoginHeader'])
        # self.f=open(yamlPath,'r',encoding='utf-8',)
        # self.cont=self.f.read()
        # self.yamlcont=yaml.load(self.cont)
        # self.f.close()

    def login(self,testhost,sys):
        '''登录接口'''
        requests.packages.urllib3.disable_warnings()  #屏蔽ssl警告
        url = testhost+'/'+str(sys)+'/'
        # print (url)
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "X-Requested-With": "XMLHttpRequest",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            # "Cookie":"JSESSIONID=CCE10C8EFB1519A1685093999CD19A4A;JSESSIONID=0B5C0B94703E18D7BC4B1373CB550F5A",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": "https://test.uenpay.com/uenams",
            "Origin": "https://test.uenpay.com"}
        req = requests.get(url, verify=False)
        # print(req.text)
        id = re.findall('jsessionid%(.*?)/', req.text)[0]
        jsid = 'jsessionid' + '=' + id
        # print(jsid)
        ur = re.findall('href=\'(.*?)\'</script>', req.text)
        # casjs=re.findall('jquery.min.js;(.*?)"',req.text)
        # jsid=casjs[0]
        # print (jsid)

        url1 = "" + (ur[0]) + ""
        header1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "X-Requested-With": "XMLHttpRequest",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            # "Cookie": "JSESSIONID=F2D7E3DAF172CD668AD5D6EB831F290D",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": "https://test.uenpay.com/uenams/",
            "Upgrade-Insecure-Requests": "1",
            "Host": "test.uenpay.com"}
        # "Cookie":""+(jsid)+""}
        #
        #
        req1 = requests.get(url1, headers=header1, verify=False)
        # print(req1.text)
        casjs = re.findall('jquery.min.js;(.*?)"', req1.text)
        re1 = re.findall('name=\"lt\" value="(.*?)"', req1.text)
        execution = re.findall('name="execution" value="(.*?)"', req1.text)[0]
        LT = re1[0]
        # print(re1[0])
        cas_js = casjs[0]
        # print(cas_js)
        # print(jsid)
        # print(ur[0])
        # print(execution)

        url2 = "https://test.uenpay.com/cas/login?service=https%3A%2F%2Ftest.uenpay.com%2F"+str(sys)+"%2F%3Bjsessionid%" + (
            id) + "/"
        header2 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Cookie": cas_js,
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": url2,
            "Origin": "https://test.uenpay.com",
            "Host": "test.uenpay.com",
            "Upgrade-Insecure-Requests": "1",
            "Cache-Control": "max-age=0"}
        body = {"username": "admin",
                "password": "123456",
                "code": "6666",
                "lt": "" + (LT) + "",
                "execution": execution,
                "_eventId": "submit",
                "submit": "登录"}
        # 获取验证码,必须获得验证码然后去cas验证服务器才认，否则就跳转回登录页面，这一步很关键，单点登录必须每一步都模拟尤其容易忘了获取验证码这步
        r1 = self.s.get('https://test.uenpay.com/cas/captcha.htm', headers=header2, verify=False)
        req2 = self.s.post(url2, headers=header2, data=body, verify=False)
        # print (req2.url)
        '''req3必须跳转，否则视为无效会话，坑坑坑！！！'''
        req3=self.s.get(''+str(req2.url)+'login',headers=header2,verify=False)
        # print (req2.text)
        # req3 = self.s.post('https://test.uenpay.com/uenams/common/menu/admin', verify=False)
        # print(req3.json()[0])


    @unittest.skip
    def chou(self, count):
        '''抽奖'''
        headers1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3230.0 Safari/537.36",
            "Origin": "http://192.168.1.133",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json;charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "http://192.168.1.133/bblc-web-v20/mall/list.html",
            "Upgrade-Insecure-Requests": "1"}
        url1 = 'http://192.168.1.133/bblc-web-v20/mall/drawRaffleAwards'
        body1 = {"data":
                     {"pondId": "e9a12d46-bfcb-4638-8d4d-e40b521ad11b",
                      "count": count,
                      },
                 "meta":
                     {"clientType": "0",
                      "pageCode": "mallList"}
                 }
        print(type(body1))
        data = json.dumps(body1)
        req1 = self.s.post(url1, headers=headers1, json=body1)
        # r=json.loads(req.text,encoding='utf-8')
        r1 = req1.json()
        print(r1)
        # response = opener.open(req)
        # print (r1['message']['content'])
        return r1

    # @unittest.skip
    def Uen(self, fangshi, url, param,headers):
        '''UenPOST,GET请求封装'''
        # headers = {
        #     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3230.0 Safari/537.36",
        #     "Origin": "http://192.168.1.133",
        #     "Accept-Language": "zh-CN,zh;q=0.9",
        #     "Accept-Encoding": "gzip, deflate",
        #     "Content-Type": "application/x-www-form-urlencoded",
        #     "X-Requested-With": "XMLHttpRequest",
        #     "Referer": "http://192.168.1.133/bblc-web-v20/mall/list.html",
        #     "Upgrade-Insecure-Requests": "1"}
        if fangshi == 'POST':
            if 'application/x-www-form-urlencoded; charset=UTF-8' in headers['Content-Type']:  #根据header的Content-Type判断传data还是json的body
                # print (headers['Content-Type'])
                try:
                    req = self.s.post(url, data=param, headers=headers)
                    # req = self.s.post(url)
                    res = req.json()
                    self.Log.info('POST请求成功')
                    return res
                except Exception as e:
                    self.Log.info('POST请求异常：%s' % (e))
                    return {'code': 1, 'result': 'POST请求出错，出错原因:%s' % (e)}
            else:
                try:
                    req = self.s.post(url, json=param, headers=headers)
                    # req = self.s.post(url)
                    res = req.json()
                    self.Log.info('POST请求成功')
                    return res
                except Exception as e:
                    self.Log.info('POST请求异常：%s'%(e))
                    return {'code': 2, 'result': 'POST请求出错，出错原因:%s' %(e)}
        elif fangshi == 'GET':
            try:
                req = self.s.get(url, headers=headers)
                res = req.text
                self.Log.info('GET请求成功')
                return res
            except Exception as e:
                self.Log.info('GET请求异常：%s' % (e))
                return {'code': 1, 'result': 'GET请求出错，出错原因:%s' % (e)}


    def applogin(self):
        headers = {"User-Agent": "JPjbp/2.6.1 (iPhone; iOS 10.2; Scale/3.00)",
                   "Accept-Language": "zh-Hans-CN;q=1",
                   "Accept-Encoding": "gzip, deflate",
                   "Content-Type": "application/json;charset=UTF-8"}
        req = self.s.post(self.AppLoginUrl, json=self.AppLoginBody,headers=self.AppLoginHeader)
        res = req.json()
        accessToken=res["meta"]["accessToken"]
        print (res)
        print(res["meta"]["accessToken"])
        return  res


if __name__ == '__main__':
    s = requests.session()
    # uenpay(s).login('uenrms','ams')
    # # BBLC(s).BBLCQQ('POST','http://192.168.1.133/bblc-web-v20/user/authenticate',param={"data":{"account":"13761917640","password":"a111111"},"meta":{"clientType":"0","pageCode":"userSignIn"}})
    # BBLC(s).chou(2)
    # uenpay(s)
    uenpay(s).applogin()
