# -*- coding: utf-8 -*-
#导入各种库
import os,sys

class Gfile(object):
    def __init__(self):
        self.script_path = os.path.realpath(__file__)

    def filen(self):
        filename = os.path.split(self.script_path)[1]
        # filename=sys._getframe().f_code.co_filename
        # print (sys._getframe().f_code.co_filename)
        return filename


if __name__ == '__main__':
    filename=Gfile()
    filename.filen()
    print (filename.filen())