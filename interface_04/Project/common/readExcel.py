#coding=utf-8
import os,xlrd

class ReadExcel():
    #1、打开Excel
    def openExcel(self):
        data ='testData'
        excel_dir = os.path.dirname(os.getcwd())+"\\"+data+"\\data.xls"
        # print(excel_dir)
        excel_values = xlrd.open_workbook(excel_dir)
        return excel_values

    #2、读取每个sheet
    def readSheet(self):
        excel_values = self.openExcel()
        url_sheet = excel_values.sheet_by_name("urlSheet")
        data_sheet = excel_values.sheet_by_name("paramSheet")
        assert_sheet = excel_values.sheet_by_name("assertSheet")
        # print(url_sheet)
        rownums = url_sheet.nrows
        return rownums,url_sheet,data_sheet,assert_sheet

    def getList(self):
        url_list = []
        rownums,url_sheet,data_sheet,assert_sheet = self.readSheet()
        for i in range(1, rownums):
            ele = url_sheet.row_values(i)
            url_list.append(ele)
        # print(type(url_list))

        data_list=[]
        for i in range(1,rownums):
            ele = data_sheet.row_values(i)
            data_list.append(ele)
        # print(data_list)

        assert_list=[]
        for i in range(1,rownums):
            ele = assert_sheet.row_values(i)
            assert_list.append(ele)
        # print(assert_list)
        return url_list,data_list,assert_list
    #3、将读取到的放到一个list
    def getExcelList(self):
        url_list, data_list, assert_list = self.getList()
        excel_list=[]
        for i in url_list:
            for j in data_list:
                for k in assert_list:
                    if i[0]==j[0]==k[0]:
                        ele = i+j[1:]+k[1:2]
                        excel_list.append(ele)
        return excel_list

# if __name__ == '__main__':
#     a = ReadExcel()
#     a.getExcelList()