# -*- coding: utf-8 -*-
import requests, json
from common.getexcel import excel


class BBLC(object):
    def __init__(self, s):
        self.s = s

    def login(self, account):
        '''登录接口'''
        url = 'http://192.168.1.133/bblc-web-v20/user/authenticate'
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3230.0 Safari/537.36",
            "Origin": "http://192.168.1.133",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json;charset=UTF-8"}
        # path = "D:\jiekou-python3-master\\test_case\case.xlsx"
        # sheetname = 'Sheet1'
        # get=excel(path,sheetname)
        # data,url,fangshi=get.makedata()
        # print (data['data'])
        # print (data['url'])
        # print ('num:%s'%(num))
        body = {"data":
                    {"account": account, "password": "a111111"},
                "meta":
                    {"clientType": "0", "pageCode": "userSignIn"}
                }
        req = self.s.post(url, headers=header, json=body)
        print(req.json())
        return req.json()

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

    def BBLCQQ(self, fangshi, url, param):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3230.0 Safari/537.36",
            "Origin": "http://192.168.1.133",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json;charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "http://192.168.1.133/bblc-web-v20/mall/list.html",
            "Upgrade-Insecure-Requests": "1"}
        if fangshi == 'POST':
            req = self.s.post(url, json=param, headers=headers)
            res = req.json()
            return res
        elif fangshi == 'GET':
            req = self.s.get(url, headers=headers)
            res = req.text
            return res

    def applogin(self):
        headers = {"User-Agent": "JPjbp/2.6.1 (iPhone; iOS 10.2; Scale/3.00)",
                   "Accept-Language": "zh-Hans-CN;q=1",
                   "Accept-Encoding": "gzip, deflate",
                   "Content-Type": "application/json;charset=UTF-8"}
        body = {"app_key": "2afXj9Rv",
                "cellphone": "18100000007",
                "password": "a111111",
                "pushId": "121c83f7601b4790a65",
                "secret_code": "22da848de43cc8cd893eae98ea519c18",
                "version": "2.6.1"}
        body1 = {"data":
                     {"password": "123456"
                      },
                 "meta":
                     {"appKey": "2afXj9Rv",
                      "accessToken": "mallList",
                      "clientName": "IOS_9.3.1",
                      "clientVersion": "v1.0",
                      "transCode": "1001",
                      "transDate": "20180-5-17 10:43:00",
                      "username": "18000000001",}
                 }
        req = self.s.post("http://192.168.1.108:8080/callisto-api/auth/login", json=body1)
        res = req.json()
        accessToken=res["meta"]["accessToken"]
        print (res)
        print(res["meta"]["accessToken"])
        return  accessToken


if __name__ == '__main__':
    s = requests.session()
    # BBLC(s).login()
    # # BBLC(s).BBLCQQ('POST','http://192.168.1.133/bblc-web-v20/user/authenticate',param={"data":{"account":"13761917640","password":"a111111"},"meta":{"clientType":"0","pageCode":"userSignIn"}})
    # BBLC(s).chou(2)
    BBLC(s).applogin()
