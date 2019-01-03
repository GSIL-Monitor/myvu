# coding:utf8
__time__ = '2018/7/20 12:30'
__author__ = 'SYJ'
import re, os
import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Series


class PaquPhone():
    def __init__(self, Wname):
        self.wenjianming = Wname

    def get_path(self):
        path = "E:\/123"  # 文件夹目录
        files = os.listdir(path)  # 得到文件夹下的所有文件名称
        s = []
        for file in files:  # 遍历文件夹
            # print(file)
            if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
                with open(path + "/" + file, 'r', encoding='utf-8') as f:
                    for line in f.readlines():
                        # print(line)
                        s.append(line)
                # f = open(path + "/" + file, 'r')  # 打开文件
                # iter_f = iter(f)  # 创建迭代器
                # str = ""
                # for line in iter_f:  # 遍历文件，一行行遍历，读取文本
                # str = str + line
                # s.append(str)  # 每个文件的文本存到list中
        print(len(s))  # 打印结果
        return s

    # def get_path(self):
    #     path = "E:\/123"  # 文件夹目录
    #     files = os.listdir(path)  # 得到文件夹下的所有文件名称
    #     s = []
    #     for file in files:  # 遍历文件夹
    #         print (file)
    #         if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
    #             f = open(path + "/" + file,'r')  # 打开文件
    #             iter_f = iter(f)  # 创建迭代器
    #             str = ""
    #             for line in iter_f:  # 遍历文件，一行行遍历，读取文本
    #                 str = str + line
    #             s.append(str)  # 每个文件的文本存到list中
    #     print(s)  # 打印结果
    #     return s

    def open_file(self):
        with open('E:\/123\/' + str(self.wenjianming) + '.' + 'txt') as f:
            lines = f.read()
            # print (lines)
            return lines
            # for line in lines:
            #     print (line)

    def search_phone_type(self, txtcontent):
        # txt=self.open_file()
        # print (str(txt))
        phone_type = re.findall('Dalvik/2.1.0 \(Linux; U; (.*?)\)', txtcontent)  # 搜索安卓下载机型
        # phone_type = re.findall('com.apple.appstored/1.0 (.*) model', txtcontent) #搜索ios系统版本
        # print (phone_type)
        return phone_type

    def search_android_or_ios(self, phone_list):
        Android_list = []
        Ios_list = []
        # print (phone_list[6])
        for i in range(len(phone_list)):
            if str('Android') in phone_list[i - 1]:
                # print (phone_list[i-1])
                Android_list.append(phone_list[i - 1])
            elif str('iOS') in phone_list[i - 1]:
                Ios_list.append(phone_list[i - 1])
        # print (Android_list,Ios_list)
        return Android_list, Ios_list

    def Android_type_totle(self, IOS_and_Android):
        Android_type_totle = []
        Ios_type_totle = []
        print('android用户7月8日-7月22日下载量:%s' % (len(IOS_and_Android[0])))
        for i in range(len(IOS_and_Android[0])):
            # print (IOS_and_Android[0][i - 1])
            android_juti_type = re.findall('Android.*?; (.*)', IOS_and_Android[0][i - 1])
            print (android_juti_type)
            if android_juti_type:
                Android_type_totle.append(android_juti_type[0])
        return Android_type_totle

    def Ios_type_totle(self, IOS_and_Android):
        Android_type_totle = []
        Ios_type_totle = []
        print('ios用户7月8日-7月22日下载量:%s' % (len(IOS_and_Android[1])))
        for i in range(len(IOS_and_Android[1])):
            # print (IOS_and_Android[1])
            ios_juti_type = re.findall('iOS/(.*)', IOS_and_Android[1][i - 1])
            # print (ios_juti_type)
            Ios_type_totle.append(ios_juti_type[0])
        return Ios_type_totle


if __name__ == '__main__':

    A = PaquPhone('2')
    list_A = A.get_path()  # 获取每个文件的内容加到list中
    # print(type(list_A))
    list_B = []  # 新增手机型号list
    for i in range(len(list_A)):
        phone_type = A.search_phone_type(list_A[i - 1])
        for i in range(len(phone_type)):
            # print (phone_type[i-1])
            list_B.append(phone_type[i - 1])
    # print(list_B)
    IOS_and_Android = A.search_android_or_ios(list_B)
    # print(IOS_and_Android)
    A.Android_type_totle(IOS_and_Android)  # 跑出所有的安卓机器型号，生成列表
    A.Ios_type_totle(IOS_and_Android)

    aa = Series(A.Ios_type_totle(IOS_and_Android))
    aa.value_counts()
    print(aa.value_counts())
    ss = Series(A.Android_type_totle(IOS_and_Android))
    ss.value_counts()
    print(ss.value_counts())

    # print (len(list_B))
    # list_B.append(phone_type)
    # print (list_B)
    # print (list_A[i-1])
