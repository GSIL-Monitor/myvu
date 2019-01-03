#coding:utf8
__time__ = '2018/5/18 10:26'
__author__ = 'SYJ'

import pymysql,os,yaml
from common.log import Log
from common.orc import Uenoracle


class   managerMySql():

    def __init__(self):
        self.read=Uenoracle().read_config()
        self.host=self.read("DBTESTUAT","host")
        self.use=self.read("DBTESTUAT","user")
        self.pwd=self.read("DBTESTUAT","passwd")
        self.db=self.read("DBTESTUAT","db")
        self.utf=self.read("DBTESTUAT","charset")
        '''读取用例文件的路径以及名称'''
        script_path = os.path.realpath(__file__)
        filename = os.path.split(script_path)[1]
        self.log=Log(filename)


    def   connect(self):
        self.db=pymysql.connect(self.host,self.use,self.pwd,self.db,charset=self.utf)
        self.log.info("数据库连接")
        self.cursor=self.db.cursor()


    def  close(self):
        self.db.close()
        self.cursor.close()
        self.log.info("数据库关闭")

    def  seleSql(self,sql):
        result=()
        self.connect()
        try:
            self.cursor.execute(sql)
            result=self.cursor.fetchall()
            return   result
        except:
            self.log.info("查询失败")
        self.close()




    def  updaSql(self,sql):
        return self._mSql(sql)


    def inseSql(self,sql):
        return self._mSql(sql)


    def  deleSql(self,sql):
        return self._mSql(sql)


    def _mSql(self,sql):
        self.connect()
        rows=None
        try:
            rows=self.cursor.execute(sql)
            self.db.commit()
            self.log.info("数据操作完成")
        except:
            self.db.rollback()
            self.log.info("数据操作失败")
        self.close()
        return rows