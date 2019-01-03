# -*- coding: utf-8 -*-
#导入各种库
import requests,random,arrow,os
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

class AddZQ(unittest.TestCase):
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
        logger.info('开始执行AddZQ---------------------------------------')

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
        # print (self.result)
        # for data in self.result:
        #     print (data[0],data[1])
        # print ("vc_sys_request_no:%s"%(self.result['vc_sys_request_no']))
        # print ("pk_id:%s"%(cur.description[1][0]))
        # print ("pk_id:%s,nb_balance:%s,vc_name:%s,vc_account:%s,dc_type:%s"%(self.result['pk_id'],self.result['nb_balance'],self.result['vc_name'],self.result['vc_account'],self.result['dc_type']))

    @classmethod
    def tearDownClass(cls):
        '''关闭数据库'''
        cls.conn.close()
        logger.info('执行结束AddZQ---------------------------------------')
        logger.removeHandler(ch)
        logger.removeHandler(fh)

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
        try:
            self.assertIn('管理员', req.text)
            self.assertIn('修改', req.text)
            # logger.info('登录成功！')
            logger.info('test_2consloe_login用例通过')
        except:
            logger.info('登录失败！')

        # print (res)

    # @unittest.skip
    def test_3uploadZQ(self):
        '''发布理财计划'''
        # name= cf.get('dbfb','name')
        anount=cf.get('dbfb','amount')
        fkAmount=cf.get('dbfb','amount')
        rate=cf.get('dbfb','rate')
        extraRate=cf.get('dbfb','extraRate')
        # contractNo=cf.get('dbfb','contractNo')
        repay=cf.get('dbfb','repay')
        deadline=cf.get('dbfb','deadline')
        period=cf.get('dbfb','period')
        periodType=cf.get('dbfb','periodType')
        loanType=cf.get('dbfb','period')
        qtMin = cf.get('dbfb', 'qtMin')
        activityId = cf.get('dbfb', 'activityId')
        activityType = cf.get('dbfb', 'activityType')
        isActivity = cf.get('dbfb', 'isActivity')
        publishType = cf.get('dbfb', 'publishType')
        # contractNo = cf.get('ZQ', 'contractNo')
        a = random.randint(1, 999)
        nowday = arrow.now().format('MMDD')
        nowtime=arrow.now().format('HHmmss')
        # name='loan'+'-'+nowday+'-'+nowtime
        # name = 'loan' + '-' + nowday
        name='邀请'
        contractNo_day =str(nowday)
        contractNo_time=str(nowtime)
        contractNo = contractNo_day + contractNo_time
        logger.info(contractNo_day)
        global loanID
        url1 = "http://192.168.1.133/bbl-console/loanv2/publish"
        headers1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Referer": "http://192.168.1.133/bbl-console/index",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Origin": " http://192.168.1.133",
            "Host": "192.168.1.133",
            "cookie": cookie}
        body1 = {'qtMin': qtMin,
                 'isActivity':isActivity,  #1为活动标
                 'activityType':activityType,   #匹配的活动类型
                'activityId':activityId, #数据库的活动的pkid
                 'loanTypeObj':period,
                 'rate':rate,
                 'period': period,
                 'deadline': deadline,
                 'repayOrigin': '第一还款来源：原债务人基于基础交易合同负有还款责任；\n第二还款来源：保理方上海奋雄商业保理有限公司，基于应收账款转让及回购协议负有还款责任；\n第三还款来源：原债权人基于保理合同中可追索条款负有还款责任。',
                 'financingUsage': '该笔借款主要用于企业生产经营的资金周转。',
                 'periodType':periodType,
                 'periodTypeName': '个月',
                 'repay': repay,
                 'matchTypeObj[code]': "match_type_default",
                 'matchTypeObj[createTime]': "0",
                 'matchTypeObj[id]': "216ffa97-40b4-11e5-bfb9-00163e001ddd",
                 'matchTypeObj[name]': '普通',
                 'matchTypeObj[order]': '1',
                 'matchTypeObj[parentId]': '0ad01f31-40b4-11e5-bfb9-00163e001ddd',
                 'matchTypeObj[status]': '00',
                 'matchTypeObj[updateTime]': '0',
                 'matchTypeObj[value]': '0',
                 'qxtimeObj[key]': '00',
                 'qxtimeObj[value]': '放款成功起息',  # 服务费
                 'activityTypeObj[key]': '00',  # 风险基金
                 'activityTypeObj[value]': '普通',
                 'enterpriseIdObj[account]': 'alllllll',
                 'enterpriseIdObj[bankCardNo]':'6222021001029770063',
                 'enterpriseIdObj[bankId]': '0102 ',
                 'enterpriseIdObj[bankName]': '中国工商银行',
                 'enterpriseIdObj[businessLicense]': '5101090000975000',
                 'enterpriseIdObj[cellphone]': '12000000002',
                 'enterpriseIdObj[cityId]': '3310',
                 'enterpriseIdObj[createTime]': '1504085833000',
                 'enterpriseIdObj[creator]': 'aad3247b-073d-11e4-855a-00ff24327431',
                 'enterpriseIdObj[formatNum]': '***************0063',
                 'enterpriseIdObj[id]': '14b740c9-af9f-407f-b471-fa2dc5c05b5e',
                 'enterpriseIdObj[idNo]': '310101199901014166',
                 'enterpriseIdObj[legalPerson]': '冰河',
                 'enterpriseIdObj[name]': '星星',
                 'enterpriseIdObj[organizationCode]':'zx001002',
                 'enterpriseIdObj[status]': '01',
                 'enterpriseIdObj[statusName]': '成功',
                 'enterpriseIdObj[taxId]': '321200776873168',
                 'enterpriseIdObj[updateTime]': '1504085833000',
                 'enterpriseIdObj[updater]': 'aad3247b-073d-11e4-855a-00ff24327431',
                 'enterpriseIdObj[userId]': '4d2d2e15-816d-48d8-b30a-04d31f1e9432',
                 'companyName': '星星',
                 'legalName':'冰河',
                 'legalIdNo': '310101199901014166',
                 'legalPhone': '12000000002',
                 'legalOrgNo': 'zx001002',
                 'legalBusNo': '5101090000975000',
                 'legalRegNo': '321200776873168',
                 'legalBankType': '中国工商银行',
                 'legalBankNo': '6222021001029770063',
                 'legalBankBranch': '',
                 'name': name,
                 'contractNo': contractNo,
                 'extraRate': extraRate,
                 'amount': anount,
                 'fkAmount': anount,
                 'desc': 'AAAAAAAAAA',
                 'loanType': period,
                 'qtMax': '',
                 'allowRedPacket': '0',  #0不允许使用投资红包，1允许使用投资红包
                 'garanteeType': '0',
                 'qxTime': '00',
                 'rank': 'A',
                 'enterpriseId': '14b740c9-af9f-407f-b471-fa2dc5c05b5e',
                 'bizInfoChecked': '1',
                 'bizLicenceChecked': '1',
                 'openLicenceChecked': '1',
                 'corpIdentityChecked': '1',
                 'corpBylawsChecked': '1',
                 'venueCertChecked': '1',
                 'publishType': publishType,        #1自动发布
                 'datetimePublish': '2017-12-06 16:35',
                 'images': '',
                 'expectPublish': '0'   #1前台预发布，0不前台预发布
                 }
        req = request.post(url1,body1)
        print (type(req.text))
        res = json.loads(req.text,encoding='utf-8')
        print (res)
        # response=opener.open(req)
        R = res
        # loanid = re.findall(r"\"id\":\"(.*?)\"", R)
        # print (R)
        # loanID = R['type']['id']
        # loanID = loanid[0]
        # print (loanID)
        self.assertEqual(R['type'],'SUCCESS')
        print('成功')
        print (R['type'])
        logger.info('test_3uploadZQ用例通过！')
        # return loanID

    @unittest.skip
    def test_4ZQYC(self):
        '''债券移池'''
        num = cf.get('LCJH','pipeileixing')
        url1 = "http://192.168.1.133/bbl-console/plan/doChangeLoanPool"
        body = {"loanItemId": loanID,
                "matchType": "22e6ed4a-f7e5-440b-a338-19ca43cc6bb" + str(num) + ""}
        req = request.post(url1,body)
        res = json.loads(req.text,encoding='utf-8')
        # logger.info(res)
        self.assertEqual(res['type'],'SUCCESS')
        logger.info('ZQYC用例通过！')

    @unittest.skip
    def test_5ZQSH(self):
        '''移池审核通过'''
        url1 = "http://192.168.1.133/bbl-console/plan/loan-approve-batch"
        body = {"loanId": loanID}
        req = request.post(url1,body)
        res = json.loads(req.text,encoding='utf-8')
        self.assertEqual(res['type'],'SUCCESS')
        logger.info('test_5ZQSH用例通过！')

    # @unittest.skip
    def test_6search(self):
        '''单标列表搜索'''
        global loanid
        url1 = "http://192.168.1.133/bbl-console/loanv2/search?page=0&size=20"
        body={"projectType": "",
              "loanName":"",
              "status":"00",
              "page":"0"}
        req = request.post(url1, body)
        res = json.loads(req.text, encoding='utf-8')
        # self.assertEqual(res['type'], 'SUCCESS')
        loanid=res["content"][0]['loan']['id']
        # print (json.dumps(a)['content'])
        # print(res["content"][0]['loan']['id'])
        print ("loanid=%s"%loanid)
        return loanid

    # @unittest.skip
    def test_7approved(self):
        '''单标审核'''
        # global loanid
        url1 = "http://192.168.1.133/bbl-console/loanv2/loan-approve"
        body={"loanId":loanid}
        req = request.post(url1, body)
        res = json.loads(req.text, encoding='utf-8')
        print (res)
        self.assertEqual(res['type'],'SUCCESS')


if __name__ == '__main__':
   unittest.main(warnings='ignore')




