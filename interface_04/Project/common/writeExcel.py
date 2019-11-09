#coding = utf-8
import xlrd
from xlutils.copy import copy
import os

class writeExcel(object):
    dir = 'testData'
    excel_dir = os.path.dirname(os.getcwd())+"\\"+dir
    rb = xlrd.open_workbook(excel_dir+"\\data.xls")
    wb =  copy(rb)
    ws = wb.get_sheet(2)
    # print(ws)
    def writeData(self,id,real,status):
        try:
            print("写入")
            # self.ws.write(id,2,real)
            self.ws.write(id,3,status)
            self.wb.save(self.excel_dir+"\\data.xls")
            return 'OK'
        except Exception as m:
            print(m)


if __name__ == '__main__':
    w = writeExcel()
