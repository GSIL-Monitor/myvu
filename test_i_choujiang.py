# -*- coding: utf-8 -*-
#导入各种库
import requests,arrow,os,ddt,sys,pymysql
import configparser
import unittest
from common.loginBBLC import BBLC
from common.log import Log
from common.getexcel import excel
from common.getfile import Gfile

path = "H:\jiekou-python3\\test_case_data\case.xlsx"
sheetname = 'Sheet1'
ex = excel(path, sheetname)
data_test = ex.makedata()
# print (data_test)


@ddt.ddt
class Addchoujiang(unittest.TestCase):
    """投资理财计划"""



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
        # cls.bbl_login = cf.get("url","bbl_login")
        # cls.console_login = cf.get("url","console_login")

        '''读取用例文件的路径以及名称'''
        script_path = os.path.realpath(__file__)
        filename = os.path.split(script_path)[1]

        '''定义日志'''
        cls.log=Log(filename)
        cls.log.info('执行开始---------------------------------------')


        '''查询数据库用户信息'''
        # db_host = cf.get("mysql","host")
        # db_user = cf.get("mysql", "user")
        # db_password = cf.get("mysql", "password")
        # db_database = cf.get("mysql", "database")
        # db_charset = cf.get("mysql","charset")
        # db_port = cf.get("mysql","port")
        # cls.conn = pymysql.connect(host=db_host, user=db_user, passwd=db_password, db=db_database,charset=db_charset)
        # self.conn = pymysql.connect(host='192.168.1.132', user='bbq', passwd='bbq123456',port=3306, db='bbq_financz_test',charset='utf8')
        # self.conn = pymysql.connect(host='192.168.1.132' ,user='bbq', passwd='bbq123456',port=3306,db='bbq_financz_test',charset='utf8')
        # cur = cls.conn.cursor(cursor=pymysql.cursors.DictCursor)
        # sql = "SELECT * FROM fiz_plan WHERE dt_datetime_filled IS null AND dt_create_time LIKE '%"+nowtime+"%' GROUP BY dt_datetime_approved DESC LIMIT 5;'"     #直接找最近的一条审核通过的理财计划
        # cur.execute(sql)
        # cls.result = cur.fetchone()
        '''调用登录方法保持session'''
        s=requests.session()
        cls.login=BBLC(s)
        cls.login.login('13761917640')



    @classmethod
    def tearDownClass(cls):
        '''关闭数据库'''
        cls.conn.close()
        cls.log.info('执行结束---------------------------------------')

    @ddt.data(*data_test)
    def test_api(self,data_test):
        '''excel封装接口'''
        self.log.info('请求数据:%s'%(data_test['data']))
        print(data_test['url'])
        req=self.login.BBLCQQ(fangshi=data_test['fangshi'],url=data_test['url'],param=eval(data_test['data']))#str要转成dict，req里才能用json
        if req['message']['code'] == '0':
            print('请求返回:%s' % (req['message']['code']))
            self.assertIn(data_test['yuqi'], req['message']['code'])
        else:
            print('请求返回:%s' % (req['message']['content']))
            self.assertIn(data_test['yuqi'],req['message']['content'])


    # @ddt.data(*data)
    # def test_1QT_chou(self,data):
    #     '''宝箱商城抽奖'''
    #     self.log.info('start------------------------------------')
    #     self.log.info('投资钥匙个数:%s'%(data))
    #     req1 = self.login.chou(data)
    #     if int(data)<0:
    #         self.log.info('返回:%s'%(req1)
    #         self.assertIn('参数异常',req1['message']['content'])
    #     elif int(data)==0:
    #         self.log.info('返回:%s' % (req1))
    #         self.assertIn('参数异常', req1['message']['content'])
    #     elif 0<int(data)<=10:
    #         self.log.info('返回:%s' % (req1))
    #         self.assertIn('钥匙不足',req1['message']['content'])
    #     elif int(data)>10:
    #         self.log.info('返回:%s' % (req1))
    #         self.assertIn('参数异常',req1['message']['content'])
    #     self.log.info(('end-------------------------------------'))



if __name__ == '__main__':
     unittest.main()