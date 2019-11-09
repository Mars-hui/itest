#coding=utf-8
import xlrd,xlwt

'''
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

'''



'''教学版'''
#打开Excel
#读取
#汇整成一个
import os
class ReadExcel():
    dir = 'testData'
    excel_dir = os.path.dirname(os.getcwd()) + '\\'+dir
    workbook = xlrd.open_workbook(excel_dir+'\\'+'data.xls')
    #sheet1 = workbook.sheet_by_index(0)
    urlSheet = workbook.sheet_by_name('urlSheet')
    paramSheet = workbook.sheet_by_name('paramSheet')
    assertSheeet = workbook.sheet_by_name('assertSheet')

    rownum = urlSheet.nrows
    #print(rownum)

    def getInterfaceList(self):
        urllist=[]
        for i in range(1,self.rownum):
            rowvalue = self.urlSheet.row_values(i)
            urllist.append(rowvalue)
        return urllist
    def getParamList(self):
        paramlist = []
        for i in range(1,self.rownum):
            rowvalue = self.paramSheet.row_values(i)
            paramlist.append(rowvalue)
        return paramlist

    def getAssertList(self):
        '''assertlist属于方法内的属性'''
        assertlist = []
        for i in range(1,self.rownum):
            row_value = self.assertSheeet.row_values(i)
            assertlist.append(row_value)
        return assertlist
    '''不能直接调用方法内的属性，需调用方法，将返回值传给他'''
    def excleList(self):
        excellist = []
        urllist = self.getInterfaceList()
        paramlist = self.getParamList()
        assertlist = self.getAssertList()
        for i in urllist:
            for j in paramlist:
                for m in assertlist:
                    if i[0] == j[0] == m[0]:
                        #print(type(i))
                        ele = i + j[1:]+ m[1:2]
                        print(type(ele))
                        excellist.append(ele)

                        break

        return excellist


#
if __name__ == '__main__':
    readexcel = ReadExcel()
    # print (readexcel.getInterfaceList())
    # print(readexcel.getParamList())
    # print(readexcel.getAssertList())
    print(readexcel.excleList())





