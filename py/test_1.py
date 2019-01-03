#coding=utf-8
import pytest,requests,ddt
from common.loginBBLC import BBLC
from common.log import Log
from common.getexcel import excel


path = "D:\jiekou-python3-master\\test_case\case.xlsx"
sheetname = 'Sheet1'
ex = excel(path, sheetname)
data_test = ex.makedata()
print (data_test)
@ddt.ddt
class TestClass(object):
    params={"1","2"}
    def setup_class(cls):
        '''定义日志'''
        cls.log=Log()
        cls.log.info('执行开始---------------------------------------')
        s = requests.session()
        cls.login = BBLC(s)
        cls.login.login()

    @ddt.data(*params)
    def test_two(self):
        print (self.params)

if __name__ == '__main__':
    pytest.main()
