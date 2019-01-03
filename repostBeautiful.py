#coding:utf8
__time__ = '2018/5/10 17:18'
__author__ = 'SYJ'

import time, os
import sys
import unittest
from HTMLTestRunner import HTMLTestRunner     #引入HTMLTestRunner模板
from BeautifulReport import BeautifulReport
from tomorrow import threads


now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
filename = now + "report.html"
def add_case(project):
    test_dir = './project/'+str(project)+''  # 指定当前文件夹下的Interface目录
    top_level_dir='./project'       #定义项目用例顶级目录，不设置的话第二次调用discover会报错
    # print (test_dir)
    # test_dir = './project'  # 指定当前文件夹下的Interface目录
    file = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py', top_level_dir = top_level_dir)  # 匹配开头为test的py文件
    # print (file)
    # now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))  # 取当前时间
    public_path = os.path.dirname(os.path.abspath(sys.argv[0]))  # 获取当前运行的.py文件所在的绝对路径
    # filename = now + "report.html"
    # print (file)
    # print(filename)
    return file

@threads(1)
def run_cast(file):
    result = BeautifulReport(file)
    result.report(filename=filename, description='代理商APP接口测试报告', log_path='report')

if __name__=="__main__":
    pro=['project_ams']  #需要运行的项目文件夹，下面存放用例
    for project in pro:
        cases=add_case(project)
    # add_case((pro[1]))
        for case in cases:
            print (case)
            run_cast(case)
    # for i,j in zip(a,range(len(list(a)))):
    #     run_cast(i,nth=j)
    # run_cast(a[0],a[1])
    # i=0
    # for i in range(1):
    # file = unittest.load_tests(tests="test_a_addLCJH.py")
    #     test_dir = './'  # 指定当前文件夹下的Interface目录
    #     file = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')  # 匹配开头为test的py文件
    #     now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))    # 取当前时间
    #     public_path = os.path.dirname(os.path.abspath(sys.argv[0]))       # 获取当前运行的.py文件所在的绝对路径
    #     print (file)
    #     filename = public_path + "\\Report\\" + now + "report.html"   #保存的报告路径和名称
    #     filename=now + "report.html"
    #     print (filename)
    #     fp = open(filename, 'wb')
    #     runner = HTMLTestRunner(stream=fp,
    #                             title="接口自动化报告",
    #                             description="详细描述如下："
    #                             )
    #     runner.run(a)     #执行测试套件
    # #     fp.close()
    #     result=BeautifulReport(a)
    #     result.report(filename=filename, description='接口测试报告', log_path='report')