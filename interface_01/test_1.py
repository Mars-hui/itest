#coding=utf-8
'''
#1、输入一个数，判断该数的范围：90-100：等价为A……60以下：等级为E
a=input("请输入一个数：")
a = int(a)

if a >=90 and a<=100:
    print("A")
elif a >= 80 and a < 90:
    print("B")
elif a >= 70 and a < 80:
    print("C")
elif a >= 60 and a < 70:
    print("D")
else:
    print("E")

#2、定义一个列表，从键盘输入一个随机数，判断该数是否在列表中
list = [3,4,7,3,8,5]

print(type(list[0]))

a = input("请输入：")
a=float(a)
b=0
for i in list:
    if a == i:
        b=1
if b==1:
    print("在列表中")
else:
    print("不在列表中")

#3、求10阶乘
res=1
for i in range(1,11):
    for j in range(1,11):
        if i==j:
            res = res * j
            res_str=str(res)
            print(str(i)+"!"+"="+res_str)

#4、求100以内能被3整除的数，并将作为列表输出
list=[]
for i in range(1,101):
    if i%3==0:
        list.append(i)
print(list)

#5、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
List=[1,2,3,4,3,4,2,5,5,8,9,7]
list_new=list(set(List))
print(list_new)

#6、求斐波那契数列 1 1 2 3 5 8 13 ……
list=[1,1]
s=1
while True:
    n=list[-1]
    m=list[-2]
    s=m+n
    list.append(s)
print(list)

#7、求10000以内的质数
list=[1]
for i in range(1,1001):
    for j in range(2,1001):
        if i == j:
            list.append(i)
            break
        elif i%j==0:
            break
print(list)

l1=[]
n=2
m=2
for n in range(1,1001):
    while n<m:
        if n%m==0:
            l1=l1.append(n)

print("1000以内"l1)
'''
#8、预习后作业：输出100以内的所有质数（只能被1和其本身整除的数）
class ZhiShu():
    def zhishu(self,num):
        list=[1]
        num=num+1
        for i in range(1, num):
            for j in range(2, num):
                if i == j:
                    list.append(i)
                    break
                elif i % j == 0:
                    break
        return list

#实例化,创建一个对象
a=ZhiShu()
#调用
b=a.zhishu(100)
print(b)

