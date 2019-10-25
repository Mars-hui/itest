#coding=utf-8
import xlrd,xlwt

#打开xls文件
class Excel():
    def read_excell(url):
        #readbook = xlrd.open_workbook(r'E:\training\code\vip3test\interface_03\project\testData\data.xls')
        readbook = xlrd.open_workbook(url)
        sheet1 = readbook.sheet_by_index(0)
        sheet2 = readbook.sheet_by_index(1)
        sheet3 = readbook.sheet_by_index(2)

        nrows = sheet1.nrows
        ncols = sheet1.ncols
        # print(sheet1)
        # print(nrows)
        # print(ncols)

    #读取xls文件存入xls_values

        xls_values =[]
        for i in range(1,nrows):
            row_values = sheet1.row_values(i)
            row_value_sheet2 = sheet2.row_values(i)
            row_value_sheet3 = sheet3.row_values(i)
            row_values.pop(0)
            row_values.extend(row_value_sheet2)
            row_values.extend(row_value_sheet3)
            row_values.pop(3)
            row_values.pop(-1)
            row_values.pop(-1)
            row_values.pop(-2)
            xls_values.append(row_values)
        print(xls_values)
        return xls_values





