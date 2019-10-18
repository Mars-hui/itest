#coding=utf-8
'''
#1、求1-100的和
i=1
sum=0
while i<101:
    sum= sum+i
    i+=1
print(sum)

sum=0
for i in range(101):
    sum=sum+i
print(sum)
#列表转换为字典
keys=['a','b','c']
values=[1,2,3]
dicts=dict(keys,values)
print(dicts)
'''
#
# def add(a,b):
#     return a+b
#
# def jian(a,b):
#     return a-b
#
# def cheng(a,b):
#     return a*b
#
# def chu(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("除数不能为0！")
#     except ValueError:
#         print("传入无效参数！")
#     except NameError:
#         print("该对象未声明")
#     finally:
#         print("程序执行完毕")
#
# a=float(input("第一个数："))
# b=input("运算符号：")
# c=float(input("第二个数："))
# if b=="+":
#     res=add(a,c)
# elif b=="-":
#     res=jian(a,c)
# elif b=="*":
#     res=cheng(a,c)
# elif b=="/":
#     res=chu(a,c)
# print("运算结果为："+str(res))

# def add_end(L=[]):
#     L.append('END')
#     return L
# print(add_end())
# print(add_end())

#函数传可变参数
# def calc(*numbers):
#     print(type(numbers))
#     print(*numbers)
#     for number in numbers:
#         print(number)
#
# numbers=[2,4,5,6,8]
# calc(numbers)
# calc(*numbers)

#关键字参数函数
# def d1(car,size,**info):
#     information={
#         'car':car,
#         'size':size
#     }
#     for key,value in info.items():
#         information[key]=value
#     print(information)
# info={
#     'color':'red',
#     'data':'50'
#            }
# d1('BMW','90',**info)

#try ...except
# def calc(a,b):
#     try:
#         print(a/b)
#     except BaseException:
#         print("除数不能为0")
#
# calc(1,0)
'''
#文件io练习
#1-读取文件
l=[]
with open('E:\\training\\code\\vip3test\\data.txt','r+') as f:
    info = f.readlines()
    print(info)
    for line in info:
        line=line.strip()
        l.append(line)
    print(l)
#2-将数据排序
l.sort()
print(l)
#3-将排序后的内容写入
with open('E:\\training\\code\\vip3test\\bakeup.txt')
'''
s='hello world'
print(s.split('l'))
print(s.split('l',2))
print(s.swapcase())
s='ab'
m='shdjabrjei'
print(s.join(m))
s=[1,3,4,5]
s1=[str(i) for i in s]
print('+'.join(s1))