#coding = utf - 8

import xlwt,os,xlrd
from xlutils.copy import copy

class WriteExcel(object):
    def write_xls(self, id, Except):
        testData_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\testData'
        print(testData_path)
        excel_dir = testData_path + '\\data.xls'
        rb = xlrd.open_workbook(excel_dir)
        wb = copy(rb)
        ws = wb.get_sheet(0)
        try:
            ws.write(id, 3, Except)
            wb.save(excel_dir)
            return 'OK'
        except Exception as m:
            print(m)

if __name__ == '__main__':
    w = WriteExcel()
    w.write_xls(1,1)


