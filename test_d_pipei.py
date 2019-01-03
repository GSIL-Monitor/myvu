# -*- coding: utf-8 -*-   
#导入各种库
import requests,arrow
import configparser
import json
import unittest
import pymysql
import xlrd
import re,datetime
import http.client
import logging,os,ddt,excel

@ddt.ddt
class AddPP(unittest.TestCase):
    '''投资理财计划'''
    global data
    testdata = excel.ExcelUtil("d:\\test.xlsx","Sheet1")
    data1 = testdata.dict_data()
    data = []
    for a in data1:
        print (a)
        if a['code'] is not '':
            # print ("不为空")
            data.append(a['code'])
    print (data)

    @classmethod
    def setUpClass(cls):
        '''初始化数据'''
        global cf, pk_id, logger, fh, ch
        utc = arrow.now()
        # utc = utc.replace(days=-1)
        nowtime = utc.format('YYYY-MM-DD')
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
        logger.info('开始执行AddPP---------------------------------------')



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
        sql = "SELECT * FROM fiz_plan WHERE dt_datetime_filled IS null AND dt_create_time LIKE '%"+nowtime+"%' GROUP BY dt_datetime_approved DESC LIMIT 5;'"     #直接找最近的一条审核通过的理财计划
        cur.execute(sql)
        cls.result = cur.fetchone()
        # print (self.result)
        # for data in self.result:
        #     print (data[0],data[1])
        # print ("pk_id:%s"%(self.result['pk_id']))
        # logger.info("pk_id:%s"%(self.result['pk_id']))
        # pk_id = cls.result['pk_id']
        # print (pk_id)
        # print ("pk_id:%s"%(cur.description[1][0]))
        # print ("pk_id:%s,nb_balance:%s,vc_name:%s,vc_account:%s,dc_type:%s"%(self.result['pk_id'],self.result['nb_balance'],self.result['vc_name'],self.result['vc_account'],self.result['dc_type']))

    @classmethod
    def tearDownClass(cls):
        '''关闭数据库'''
        cls.conn.close()
        logger.info('执行结束AddPP---------------------------------------')
        logger.removeHandler(fh)
        logger.removeHandler(ch)

    def test_1consloe_login(self):
        '''登录后台并断言是否登录成功'''
        global cookie,request
        request=requests.session()
        url = 'http://192.168.1.133/bbl-console/authenticate'
        body = {'account': 'admin',
                'password': 'admin4321'}
        # print (headers['cookie'])
        req=request.post(url,data=body)
        res = req.text
        # print (res)
        # res=req.text.encode(encoding='utf-8')
        self.assertIn('管理员', res)
        self.assertIn('修改', res)
        # logger.info('登录成功！')
        logger.info('test_1consloe_login用例通过！')


    # @unittest.skip('TZ用例调试停用')
    @ddt.data(*data)
    def test_2pipei(self,data):
        '''planMatch、planFilled匹配'''
        url = 'http://192.168.1.133/bbl-job/test-do-job'
        # "cookie": cookie1}
        date = cf.get('paopicode','date')
        # code0 = cf.get('paopicode','planmatch')
        # code1 = cf.get('paopicode','fangkuan')
        num = cf.get('paopicode','num')
        print (date)
        print (num)
        # if int(num)<=0:
        #     body = {"code": data}
        #     req = request.post(url, body)
        #     res = json.loads(req.text, encoding='utf-8')
        #     self.assertEqual(res['type'], 'SUCCESS')
        #     print(res)
        #     print(res['type'])
        #     num1 = int(num)
        #     num1 +=1
        #     if num1 == 1:
        #         print ('开始num1')
        body = {"code": data}
        req = request.post(url, body)
        res = json.loads(req.text, encoding='utf-8')
        self.assertEqual(res['type'], 'SUCCESS')
        print(res)
        print (res['messages'])
        logger.info('test_2pipei用例成功！')


if __name__ == '__main__':
     unittest.main