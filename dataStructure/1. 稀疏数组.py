#coding = utf - 8
'''
五子棋棋盘的存储的使用
思路：棋盘→二维数组→稀疏数组→文件

'''

import numpy
#1.构建二维数组
Arrlist1 = numpy.zeros((11,11))
print(type(Arrlist1))
Arrlist1[1][1] = 1
Arrlist1[2][2] = 2
Arrlist1[5][7] = 1

#2.将二维数组转化为稀疏数组
    #①得到有值的个数sum
sum = 0
for i in range(11):
   for j in range(11):
       if Arrlist1[i][j] != 0:
           sum += 1
print(sum)
    #②创建稀疏数组
sparseArr = numpy.zeros((sum+1,3))
sparseArr[0][0] = 11
sparseArr[0][1] = 11
sparseArr[0][2] = sum
# print(sparseArr)
count = 0
for i in range(11):
   for j in range(11):
       if Arrlist1[i][j] != 0:
           count += 1
           sparseArr[count][0] = i
           sparseArr[count][1] = j
           sparseArr[count][2] = Arrlist1[i][j]
print(sparseArr)
#3.稀疏数组→二维数组
    #①创建二位数组
Arrlist2 = numpy.zeros((int(sparseArr[0][0]),int(sparseArr[0][1])))
print(Arrlist2)
print(len(sparseArr))
for i in range(1,len(sparseArr)):
    Arrlist2[int(sparseArr[i][0])][int(sparseArr[i][1])] = sparseArr[i][2]
print(Arrlist2)
