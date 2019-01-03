# coding:utf8
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'  # oracle数据库版本是10g，字符集是AL32UTF8,否则中文返回显示乱码
__time__ = '2018/5/8 15:20'
__author__ = 'SYJ'

import cx_Oracle, yaml


class Uenoracle():

    def __init__(self,project,configname,confignYaml):
        # 获取当前文件路径 D:/WorkSpace/StudyPractice/Python_Yaml/YamlStudy
        self.filePath = 'H:\之前项目\pythonstudy\pythonstudy\python3\project\\'+(project)+'\\'+(configname)+''
        # 获取当前文件的Realpath  D:\WorkSpace\StudyPractice\Python_Yaml\YamlStudy\YamlDemo.py
        fileNamePath = os.path.split(os.path.realpath(__file__))[0]
        # 获取配置文件的路径 D:/WorkSpace/StudyPractice/Python_Yaml/YamlStudy\config.yaml
        # yamlPath = os.path.join(filePath, 'config.yaml')
        self.yamlPath = os.path.join(self.filePath, ''+(confignYaml)+'')
        # 加上 ,encoding='utf-8'，处理配置文件中含中文出现乱码的情况。
        f = open(self.yamlPath,'r',encoding='utf-8')
        cont=f.read()
        a=yaml.load(cont)
        f.close()


    def read_config(self):
        f = open(self.yamlPath, 'r', encoding='utf-8')
        cont = f.read()
        a = yaml.load(cont)
        f.close()
        return a



    @staticmethod       #定义在同一个类可以进行方法调用
    def orc_connect(self,oraclename):
        '''连接oracle数据库'''
        # filePath = 'H:\之前项目\pythonstudy\pythonstudy\python3\project\project_ams/ams_config'
        # 获取当前文件的Realpath  D:\WorkSpace\StudyPractice\Python_Yaml\YamlStudy\YamlDemo.py
        fileNamePath = os.path.split(os.path.realpath(__file__))[0]
        # 获取配置文件的路径 D:/WorkSpace/StudyPractice/Python_Yaml/YamlStudy\config.yaml
        # yamlPath = os.path.join(filePath, 'config.yaml')
        # self.yamlPath = os.path.join(self.filePath, 'config.yaml')
        # 加上 ,encoding='utf-8'，处理配置文件中含中文出现乱码的情况。
        f = open(self.yamlPath, 'r', encoding='utf-8')
        cont = f.read()
        a = yaml.load(cont)
        f.close()
        self.host=a[''+(oraclename)+'']['host']
        self.username = a[''+(oraclename)+'']['username']
        # self.host=a['ORACLE']['host']
        # self.username = a['ORACLE']['username']
        oracle_tns = cx_Oracle.makedsn(self.host, 1521, self.username)
        db = cx_Oracle.connect(self.username, 'qwer1234', oracle_tns)
        cur = db.cursor(cx_Oracle)
        return db

    def orc_select(self,sql):
        '''封装查询语句'''
        # cursor=db.cursor()
        cursor=self.orc_connect(self,'ORACLE')  #调用同类中的方法
        cursor.execute(sql)
        result = cursor.fetchall()
        index = cursor.description  # 字段描述便利添加到row形成字典返回结果
        re = []
        for res in result:
            # print (res[0])
            row = {}
            # print (len(index))
            for i in range(len(index)):
                row[index[i][0]] = res[i]
                re.append(row)
            # print (re)
        return re


    def read_valid_code(self):
        '''读取数据库最新短信验证码'''
        sql1 = "select * from AGENT_SEND_MSG_LOG order by CREATE_DATE desc "
        message = self.orc_select(sql1, 'ORACLE')[0][
            'LAST_VALIDATOR_CODE']
        return message

    def delete_registeruser(self,phone):
        '''删除注册手机号'''
        db=self.orc_connect(self, 'ORACLE')
        cursor = db.cursor(cx_Oracle) # 调用同类中的方法
        sql1 = "delete from AGENT_REGISTER_USER where USER_NAME="+str(phone)+""
        # sql1 = "select * from AGENT_SEND_MSG_LOG order by CREATE_DATE desc "
        print (sql1)
        cursor.execute(sql1)
        db.commit()
        # result = cursor.fetchall()
        # print (result)

        # return message


if __name__ == '__main__':
    sql1 = "select * from AGENT_SEND_MSG_LOG order by CREATE_DATE desc "
    # a=Uenoracle(project='DailiApp',configname='app_config',confignYaml='config.yaml').orc_select(sql1)[0]['LAST_VALIDATOR_CODE']
    # print (a)
    a = Uenoracle(project='DailiApp', configname='app_config', confignYaml='config.yaml').delete_registeruser(13700000006)
    # # sql1=a['Test_Apilogin']['bodyAndheader']['Body']
    # # sql1="select * from RSK_EXTRACT_AUDIT where AGENT_NAME='吴桂平分润三级机构'"
    # print (list(a))
    # db=Uenoracle('DailiApp', 'app_config', 'config.yaml').orc_connect('ORACLE')
    # sql1 = "select * from AGENT_SEND_MSG_LOG order by CREATE_DATE desc "





