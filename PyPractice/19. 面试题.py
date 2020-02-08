#coding = utf - 8
# 1.	输出下面字符的类型
# str=“a, b, c, 1, 2, 3, -, +, =”
str_li = ['a', 1, '=']
for i in str_li:
    print(str(i),'的类型为：'+str(type(i)))


# list = [1,'a','b','=']
#
# for i in range(0, list.__len__()):
#     print (type(list[i]))

'''
2.逆序输出字符串

str=“a, b, c, d, e”————>edcba
'''
str_1 = ['a', 'b', 'c', 'd', 'e']
str_1.reverse()
for i in str_1:
    print(str(i), end = ' ')
    # print(i, end = '')

