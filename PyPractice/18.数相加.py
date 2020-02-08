#coding = utf - 8
# 题目18：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有
# 5个数相加)，几个数相加有键盘控制。
# count = int(input("要计算的数字："))
# num = int(input("几个数相加："))
# sum = 0
# counts = 0
# ele = count
# for i in range(1,num+1):
#     ele = ele + counts
#     counts = (10 ** i) * count
#     sum = ele + sum
# print(sum)

'''
① 10的n次方：10**n
② reduce()函数：对参数序列中元素进行累积
    reduce(add,list)=reduce(lambda x,y:x+y,list)
③ lambda x,y:x*y
'''

# 答案：
from functools import reduce

list=[2,4,5,7,5,3,7]
sn = reduce(lambda x,y:x+y,list)
print(sn)