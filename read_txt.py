#coding:utf8
__time__ = '2018/7/20 14:39'
__author__ = 'SYJ'

import re,os
import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Series

class AA():
    def get_path(self):
        path = "E:\/123"  # 文件夹目录
        files = os.listdir(path)  # 得到文件夹下的所有文件名称
        s = []
        for file in files:  # 遍历文件夹
            print(file)
            if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
                with open(path + "/" + file, 'r') as f:
                    while True:
                        line=f.readline()
                        if line:
                            print (line)
                        # f.close()
                    # for line in f.readlines():
                    #     print (line)
                            s.append(line)
                # f = open(path + "/" + file, 'r')  # 打开文件
                # iter_f = iter(f)  # 创建迭代器
                # str = ""
                # for line in iter_f:  # 遍历文件，一行行遍历，读取文本
                    # str = str + line
                # s.append(str)  # 每个文件的文本存到list中
        print(len(s))  # 打印结果
        return s


if __name__ == '__main__':
    A=['IOS_11.3.1_1.2.5_zgb', 'IOS_11.2.5_1.4.1_zgb', 'IOS_10.3.2_1.4.1_zgb', 'IOS_11.4_1.4.1_zgb', 'IOS_11.2.5_1.4.1_zgb', 'IOS_11.4_1.2.5_zgb', 'IOS_11.2.6_1.2.5_zgb', 'IOS_11.3.1_1.4.1_zgb', 'IOS_10.0.2_1.4.1_zgb', 'IOS_11.4_1.4.1_zgb', 'IOS_11.4_2.2.7_jsd', 'IOS_10.3.2_1.4.1_zgb', 'IOS_11.4_1.4.1_zgb', 'IOS_11.3.1_1.4.1_zgb', 'IOS_11.4_1.2.5_zgb', 'IOS_11.4_1.4.1_zgb', 'IOS_11.4_1.2.5_zgb', 'IOS_10.3.3_1.4.1_zgb', 'IOS_11.2.6_2.1.4_jsd', 'IOS_10.3.3_1.4.1_zgb', 'IOS_11.4_1.4.1_zgb', 'IOS_10.2.1_1.4.0_zgb', 'IOS_11.4_1.2.3_zgb', 'IOS_11.4_1.2.5_zgb', 'IOS_11.4_1.4.1_zgb', 'IOS_11.4_1.4.1_zgb', 'IOS_10.3.3_1.4.0_zgb', 'IOS_11.3_2.2.7_jsd', 'IOS_10.3.3_1.4.1_zgb', 'IOS_11.4_1.4.1_zgb', 'IOS_11.4.1_1.2.5_zgb', 'IOS_11.4_1.2.5_zgb']
    a=Series(A)
    print (a.value_counts()[a.value_counts()>3])
    print ()

