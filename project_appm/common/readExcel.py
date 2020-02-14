#coding = utf - 8
import os
import xlrd

class getExcelList(object):
    def get_excel(self):
        testData_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\testData'
        print(testData_path)
        excel_dir = testData_path + '\\data.xls'
        print(excel_dir)
        excel_values = xlrd.open_workbook(excel_dir)
        return excel_values

    def get_excel_list(self):
        excel = self.get_excel()
        sheet = excel.sheet_by_index(0)
        nrows = sheet.nrows
        ncols = sheet.ncols

        row_2 = []
        for i in range(1, nrows):
            row_1 = []
            for j in range(0, ncols - 1):
                ele = sheet.cell(i, j).value
                # print(type(ele))
                row_1.append(ele)
            row_2.append(row_1)
        print(row_2)
        return row_2

if __name__ == '__main__':
    g = getExcelList()
    g.get_sheet()