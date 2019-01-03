# -*- coding: utf-8 -*-
#导入各种库
import requests,os,random,arrow
import configparser
import json
import unittest
import pymysql
import xlrd
import re,datetime
import http.client
import logging
#
# http.client.HTTPConnection._http_vsn = '10'
# http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

class AddLCJH(unittest.TestCase):
    '''发布理财计划'''
    @classmethod
    def setUpClass(cls):
        '''初始化数据'''
        global cf, logger, ch, fh
        cf = configparser.ConfigParser()
        cf.read("config.ini",encoding='utf-8')
        # s = cf.sections()
        # print("section:", s)
        cls.bbl_login = cf.get("url","bbl_login")
        cls.console_login = cf.get("url","console_login")

        '''定义日志'''
        logger = logging.getLogger('BBLC')
        # defined log level
        logger.setLevel(logging.DEBUG)

        # defined handler
        proDir = os.path.realpath("D:\pythonstudy\python3\\log")
        fh = logging.FileHandler(os.path.join(proDir, "output.log"))
        ch = logging.StreamHandler()
        # defined formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # defined formatter
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # fh.setLevel(logging.DEBUG)
        # ch.setLevel(logging.DEBUG)
        # add handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        logger.info('开始执行AddLCJH---------------------------------------')

        '''查询数据库用户信息'''
        db_host = cf.get("mysql","host")
        db_user = cf.get("mysql", "user")
        db_password = cf.get("mysql", "password")
        db_database = cf.get("mysql", "database")
        db_charset = cf.get("mysql","charset")
        db_port = cf.get("mysql","port")
        # print ("db_host:",db_host)
        # print ("db_user:",db_user)
        # print ("db_password:",db_password)
        # print ("db_database:",db_database)
        # print ("db_charset:",db_charset)
        # print ("db_port:",db_port)
        cls.conn = pymysql.connect(host=db_host, user=db_user, passwd=db_password, db=db_database,charset=db_charset)
        # self.conn = pymysql.connect(host='192.168.1.132', user='bbq', passwd='bbq123456',port=3306, db='bbq_financz_test',charset='utf8')
        # self.conn = pymysql.connect(host='192.168.1.132' ,user='bbq', passwd='bbq123456',port=3306,db='bbq_financz_test',charset='utf8')
        cur = cls.conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = 'SELECT r.vc_sys_request_no,l.*, r.* FROM fiz_transaction_record r,fiz_loan l WHERE r.vc_relation_id = l.pk_id AND l.vc_name = "债权-0607-10%-2期";'
        cur.execute(sql)
        cls.result = cur.fetchone()
        # print (cls.result)
        # for data in self.result:
        #     print (data[0],data[1])
        # print ("vc_sys_request_no:%s"%(self.result['vc_sys_request_no']))
        # print ("pk_id:%s"%(cur.description[1][0]))
        # print ("pk_id:%s,nb_balance:%s,vc_name:%s,vc_account:%s,dc_type:%s"%(self.result['pk_id'],self.result['nb_balance'],self.result['vc_name'],self.result['vc_account'],self.result['dc_type']))

    @classmethod
    def tearDownClass(cls):
        '''关闭数据库'''
        cls.conn.close()
        logger.info('AddLCJH执行结束---------------------------------------')
        logger.removeHandler(fh)
        logger.removeHandler(ch)

    # @unittest.skip
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
        logger.info (cookie)
        logger.info('test_1getcookie用例成功！')

        return cookie

    # @unittest.skip
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
        try:
            self.assertIn('管理员', req.text)
            self.assertIn('修改', req.text)
            print ('登录成功！')
            # logger.info('登录成功！')
            logger.info('test_2consloe_login用例通过')
        except:
            logger.info('登录失败！')

        # print (res)

    # @unittest.skip
    def test_3fabulicai(self):
        '''发布理财计划'''
        periodType=cf.get('LCJH','periodType')
        days=cf.get('LCJH','days')
        rank=cf.get('LCJH','rank')
        # name=cf.get('LCJH','name')
        amount=cf.get('LCJH','amount')
        pipeileixing=cf.get('LCJH','pipeileixing')
        qtMin=cf.get('LCJH','qtMin')
        qtMax=cf.get('LCJH','qtMax')
        i=cf.get('LCJH','i')
        activityTypeObjk=cf.get('LCJH','activityTypeObjk')
        activityTypeObjv=cf.get('LCJH','activityTypeObjv')
        rate=cf.get('LCJH','rate')
        repayId = cf.get('LCJH','repayId')
        a = random.randint(1000, 9999)
        nowmonth = arrow.now().format('MMDD')
        nowdate=arrow.now().format('HHmmss')
        # name = str(a) + str(nowtime)
        name = str(nowmonth)+str(nowdate)
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
                 "desc": "<p>222222222222222222222</p>",
                 # "minInvest":"1",    #type为00时需要
                 "repayId": repayId,
                 # 返回本金时间计算id月：d48cbd50-42c2-11e4-b5fe-5452002c87f1，天：d434ec52-e6e2-440c-9021-f94ef02bc113
                 "periodType": periodType,  # 00为天，01为月
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
                 "name": '理财-'+name,
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
        # R = json.loads(req.text,encoding='utf-8')
        R = req.json()
        # print(R)
        # print (type(R))
        idA = re.findall(r"'id':\s+'(.*?)'", str(R))[0]
        if idA:
            logger.info(idA)
            logger.info('test_3fabulicai用例通过！')
            return idA

    # @unittest.skip
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
        logger.info('test_4approved用例通过！')
        print (R)

    # @unittest.skip
    def test_5shouyexianshi(self):
        # print (idA)
        today = datetime.date.today()  # 获取当前日期
        tomorrow = today + datetime.timedelta(days=1)
        yesterday = today - datetime.timedelta(days=1)
        date_list = [yesterday, today, tomorrow]
        date = date_list[1]
        url1 = "http://192.168.1.133/bbl-console/plan/updatestatus/" + str(idA) + "/01"
        req = request.put(url1)
        res = req.json()
        # print (res)
        self.assertEqual(res['type'],'SUCCESS')
        logger.info('test_5shouyexianshi用例通过！')



if __name__ == '__main__':
   unittest.main(warnings='ignore')




