#coding=utf-8
import math
# 一个整数，它加上100后是一个完全平方数，再加上268又是一个完全平方数，请问该数是多少？
# 1.程序分析：在10万以内判断，先将该数加上100后再开方，再将该数加上268后再开方，如果开方后
# 　　　　　　的结果满足如下条件，即是结果。请看具体分析：

for i in range(10000):
    x = int(math.sqrt(i+100))
    y = int(math.sqrt(i+268))
    if x * x == i+100 and y * y == i+268:
        print(x,y,i)
'''
math.sqrt()方法计算完成后数据为小数，
'''