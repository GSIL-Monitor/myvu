# -*- coding: utf-8 -*-
#导入各种库
import requests
import json
import unittest
import pymysql
import xlrd
import re,datetime
import http.client
#
# http.client.HTTPConnection._http_vsn = '10'
# http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

class AddLCJH(unittest.TestCase):
    ''''增加理财计划'''

    def setUp(self):
        '''初始化数据'''
        self.bbl_login = 'http://192.168.1.133/bbl-web/authenticate'
        self.console_login = 'http://192.168.1.133/bbl-console/sign-in'

        # '''查询数据库用户信息'''
        # self.conn = pymysql.connect(host='192.168.1.132', user='bbq', password='bbq123456', database='bbq_financz_test',charset='utf8')
        # cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        # sql = 'SELECT r.vc_sys_request_no,l.*, r.* FROM fiz_transaction_record r,fiz_loan l WHERE r.vc_relation_id = l.pk_id AND l.vc_name = "债权-0607-10%-2期";'
        # cur.execute(sql)
        # self.result = cur.fetchone()
        # # print (self.result)
        # # for data in self.result:
        # #     print (data[0],data[1])
        # print ("pk_id:%s"%(self.result['vc_sys_request_no']))
        # # print ("pk_id:%s"%(cur.description[1][0]))
        # # print ("pk_id:%s,nb_balance:%s,vc_name:%s,vc_account:%s,dc_type:%s"%(self.result['pk_id'],self.result['nb_balance'],self.result['vc_name'],self.result['vc_account'],self.result['dc_type']))


    def tearDown(self):
        '''关闭数据库'''
        # self.conn.close()

    def test_1getcookie(self):
        '''用户登录后台，获取cookie'''
        global cookie
        request = requests.session()
        req = request.get(self.console_login)
        # res = json.loads(req.text.encode('utf-8'))
        # print (req.headers['Set-Cookie'][0:43])
        cookie=req.headers['Set-Cookie'][0:43]
        # print (req.text)
        # print (res['type'])
        # self.assertEqual(res['type'],'SUCCESS')  #验证登录是否成功
        # self.assertIs(res['type'],'SUCCESS')
        # self.assertIn('管理员',req.text)
        # self.assertIn('修改',req.text)
        # print (req.headers)
        # cookie = res["Cookies"]
        print (cookie)
        return cookie

    def test_2consloe_login(self):
        '''登录后台并断言是否登录成功'''
        global cookie,request
        request=requests.session()
        url = 'http://192.168.1.133/bbl-console/authenticate'
        body = {'account': 'admin',
                'password': 'admin4321'}
        # print (headers['cookie'])
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate",
            "cookie": cookie}
        req=request.post(url,data=body)
        res = req.text
        # res=req.text.encode(encoding='utf-8')
        self.assertIn('管理员', req.text)
        self.assertIn('修改', req.text)
        # print (res)

    def test_3fabulicai(self):
        '''发布理财计划'''
        days='1'
        rank="A"
        name="sam0703-2期"
        amount='1000'
        pipeileixing='7'
        qtMin='1000'
        qtMax='0'
        i='1'
        activityTypeObjk='00'
        activityTypeObjv='普通'
        rate='10'
        global request,idA
        qxtimeObj_list = ["满标即起息", "投资当天即起息", "T+1工作日", "T+2工作日", "T+3工作日"]
        qxtimeObj = qxtimeObj_list[0]
        url1 = 'http://192.168.1.133/bbl-console/plan/publish'
        headers1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "http://192.168.1.133/bbl-console/index",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-Hans-CN,zh-Hans;q=0.5",
            "Host": "192.168.1.133",
            "cookie": cookie}
        body1 = {"rate": rate,
                 "period": days,  # 红包个数
                 "rank": rank,
                 "desc": "<p>2</p>",
                 # "minInvest":"1",    #type为00时需要
                 "repayId": "d434ec52-e6e2-440c-9021-f94ef02bc113",
                 # 返回本金时间计算id月：d48cbd50-42c2-11e4-b5fe-5452002c87f1，天：d434ec52-e6e2-440c-9021-f94ef02bc113
                 "periodType": "00",  # 00为天，01为月
                 "periodTypeName": "天",
                 "matchTypeObj[code]": "match_type_default_" + str(pipeileixing) + "",
                 "matchTypeObj[createTime]": "0",
                 "matchTypeObj[id]": "22e6ed4a-f7e5-440b-a338-19ca43cc6bb" + str(pipeileixing) + "",
                 "matchTypeObj[name]": "普通_" + str(pipeileixing) + "",
                 "matchTypeObj[order]": "1",
                 "matchTypeObj[parentId]": "0ad01f31-40b4-11e5-bfb9-00163e001ddd",
                 "matchTypeObj[status]": "00",
                 "matchTypeObj[updateTime]": "0",
                 "matchTypeObj[value]": "2" + str(pipeileixing) + "",
                 "activityTypeObj[key]": activityTypeObjk,  # 02:红包新人计划，03:普通新人计划
                 "activityTypeObj[value]": activityTypeObjv,
                 "name": name,
                 "amount": amount,
                 "summary": "" + str(pipeileixing) + "",
                 "matchType": "22e6ed4a-f7e5-440b-a338-19ca43cc6bb" + str(pipeileixing) + "",
                 "activityType": activityTypeObjk,
                 "qxtimeObj[value]": qxtimeObj,
                 "qtMin": qtMin,
                 "qtMax": qtMax,
                 "qxtimeObj[key]": "0" + str(i) + "",
                 "qxTime": "0" + str(i) + ""}
        req=request.post(url1,data=body1)
        # # response=opener.open(req)
        R = json.loads(req.text,encoding='utf-8')
        print(R)
        # print (type(R))
        idA = re.findall(r"'id':\s+'(.*?)'", str(R))[0]
        print(idA)
        return idA

    def test_4approved(self):
        '''理财计划通过审核'''
        # print idA
        today = datetime.date.today()  # 获取当前日期
        tomorrow = today + datetime.timedelta(days=1)
        yesterday = today - datetime.timedelta(days=1)
        date_list = [yesterday, today, tomorrow]
        date=date_list[1]
        url1 = 'http://192.168.1.133/bbl-console/plan/approve'
        headers1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "http://192.168.1.133/bbl-console/index",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-Hans-CN,zh-Hans;q=0.5",
            "Host": "192.168.1.133",
            "cookie": cookie}
        body1 = {"id": idA,
                 "passOrReject": "01",  # 红包个数
                 "desc": "<p>2</p>",
                 "platForm":"01","publishType": "00","planBeginDate": str(date)+" 00:00:00","planEndDate": str(date)+" 00:00:00","activityNum": 5}
        req=request.post(url1,data=body1)
        R=json.loads(req.text,encoding='utf-8')
        print (R)


if __name__ == '__main__':
   unittest.main




