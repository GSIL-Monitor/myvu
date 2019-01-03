# -*- coding: utf-8 -*-
#导入各种库
import requests,arrow,os,ddt,sys
import configparser
import unittest
from common.loginBBLC import BBLC
from common.log import Log
from common.getexcel import excel

# path = "D:\jiekou-python3-master\\test_case\case.xlsx"
# sheetname = 'Sheet1'
# ex = excel(path, sheetname)
# data_test = ex.makedata()
# print (data_test)

CurrentPath = os.getcwd()
print(CurrentPath)
# print(os.path)
print(sys.argv[0])
# print(os.path.split(os.path.realpath(sys.argv[0]))[1])
filename = os.path.split(os.path.realpath(sys.argv[0]))[1]
print (filename)