import time, os
import sys
import unittest
from HTMLTestRunner import HTMLTestRunner     #引入HTMLTestRunner模板
from BeautifulReport import BeautifulReport
from tomorrow import threads


now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
filename = now + "report.html"
def add_case():
    test_dir = './project1'  # 指定当前文件夹下的Interface目录
    file = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')  # 匹配开头为test的py文件
    # now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))  # 取当前时间
    public_path = os.path.dirname(os.path.abspath(sys.argv[0]))  # 获取当前运行的.py文件所在的绝对路径
    # filename = now + "report.html"
    print (file)
    print(filename)
    return file

@threads(3)
def run_cast(file,nth=0):
    result = BeautifulReport(file)
    result.report(filename=filename, description='接口测试报告', log_path='report')

if __name__=="__main__":
    a=add_case()
    # for i,j in zip(a,range(len(list(a)))):
    #     run_cast(i,nth=j)
    # run_cast(a[0],a[1])
    i=0
    for i in range(1):
    # file = unittest.load_tests(tests="test_a_addLCJH.py")
    #     test_dir = './'  # 指定当前文件夹下的Interface目录
    #     file = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')  # 匹配开头为test的py文件
    #     now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))    # 取当前时间
    #     public_path = os.path.dirname(os.path.abspath(sys.argv[0]))       # 获取当前运行的.py文件所在的绝对路径
    #     print (file)
    #     filename = public_path + "\\Report\\" + now + "report.html"   #保存的报告路径和名称
        filename=now + "report.html"
        print (filename)
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(stream=fp,
                                title="接口自动化报告",
                                description="详细描述如下："
                                )
        runner.run(a)     #执行测试套件
        fp.close()
        report=HTMLTestRunner(a)
        # result.report(filename=filename, description='接口测试报告', log_path='report')