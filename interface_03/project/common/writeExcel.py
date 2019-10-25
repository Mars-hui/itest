#coding=utf-8
from copy import copy

import xlwt,xlrd
real =1
rb = xlrd.open_workbook(r'E:\training\code\vip3test\interface_03\project\testData\data.xls')
wb = copy(rb)
ws = wb.get_sheet(2)
ws.write(1,1,1)