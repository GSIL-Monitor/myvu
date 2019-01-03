# coding:utf-8
import xlrd

class excel(object):
    def __init__(self,excelpath,sheetname):
        self.data = xlrd.open_workbook(excelpath)
        self.table = self.data.sheet_by_name(sheetname)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # print (self.rowNum)
        # 获取总列数
        self.colNum = self.table.ncols
        # print (self.colNum)
        me=self.data.sheets()[0]
        nrows = me.nrows

    def getdata(self):
        me = self.data.sheets()[0]
        nrows = me.nrows
        # print (nrows)
        data=[]
        num=[]
        fangshi=[]
        url=[]
        yuqi=[]
        for i in range(1,nrows):
            data.append(me.cell(i,3).value)
            url.append(me.cell(i, 4).value)
            fangshi.append(me.cell(i, 5).value)
            yuqi.append(me.cell(i,6).value)
            num.append(i)
        # print(yuqi)
        # print (type(data[0]))
        return data,url,fangshi,yuqi

    def makedata(self):
        listdata,listurl,listfangshi,listyuqi=excel.getdata(self)
        i=0
        makedata=[]
        for i in range(len(listdata)):
            makedata.append({'url':listurl[i],'data':listdata[i],'fangshi':listfangshi[i],'yuqi':listyuqi[i]})
            i +=i
        # print (makedata)
        return makedata




if __name__ == '__main__':
    path="D:\jiekou-python3-master\\test_case\case.xlsx"
    sheetname='Sheet1'
    excel1=excel(path,sheetname)
    data_test=excel1.makedata()
    print (data_test)
    # ex=excel(path,sheetname)
    # data_test=ex.makedata()


