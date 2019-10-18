#coding=utf-8

#1、定义一个1-9的元组，1、输出倒数第3个元素；2、输出值468
tup = list(range(1,10))
print("倒数第三个元素：",tup[-3])
print(tup[3:10:2])

# 练习：列表[11,13,5,7,0,56,23,34,72]，
li = [11,13,5,7,0,56,23,34,72]
# 求该列表中的最大值，最小值及列表中一共有几个元素
print("最大值：",max(li))
print("最小值：",min(li))
print("几个元素：",len(li))
# 获取56元素在列表的位置
print("56元素在列表的位置:",li.index(56))#取下标时，传递的是元素，不用额外加单引号，加单引号后就变成字符串了。
# 追加元素7
li.append(7)
# 删除元素0
li.remove(0)
print(li)

#练习：计算1 + 2 + 3 + 4……+100的和
sum = 0
for i in range(1,101):
    sum = sum + i
print("1 + 2 + 3 + 4……+100的和:",sum)

# 求10阶乘
sum = 1
for i in range(1,11):
    sum = sum * i
    print(str(i)+"!=",sum)#每次计算都用到了上一个数
# 求100以内能被3整除的数，并将作为列表输出
li_1 = []
for i in range(1,101):
    if i % 3 == 0:
        li_1.append(i)
print(li_1)
# 列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
'''
创建两个列表，将元素放到新的列表中，用  not in  判断，不在新列表中，则append
或者用set（）方法，集合中的元素不能重复

'''
li_2 = [1,2,3,4,3,4,2,5,5,8,9,7]
li_3 = []
for i in li_2:
    if i not in li_3:
        li_3.append(i)
    else:
        pass
print(li_3)
li_3 = set(li_2)
print(li_3)
# 求斐波那契数列 1 1 2 3 5 8 13 ……
li_4 = [1,1]
while len(li_4) < 100:
    num = li_4[-1]+li_4[-2]
    li_4.append(num)
print(li_4)
# 求10000以内的质数
'''
创建一个flag，满足条件则flag为t，放在每次做计算前的循环
'''
li_5 = []

for i in range(2,1001):
    j = 2
    flag = "t"
    while j < i :
        if i%j == 0:
            flag = "f"
            break
        else:
            j += 1
    if flag == "t":
        li_5.append(i)
print(li_5)

#设计一个计算器，输入两个数，自动实现加减乘除（进阶：根据用户输入的计算符号计算结果）

#练习关键字

# a、定义一个学生类：Student、内部含有一个方法：study，实现打印：xx学习xx课程
class Student():

    def __init__(self,name,curriculum):
        self.name = name
        self.curriculum = curriculum
    def study(self):
        print(self.name+"学习"+self.curriculum)

# b、定义一个类名：Student—学生、类内部含有一个属性：sno—学号，一个方法：study—学习，实现打印：学号为xx的学生，学习xx课程
class Student():
    def __init__(self,sno,curriculum):
        self.sno = sno
        self.curriculum = curriculum
    def study(self):
        print("学号为"+str(self.sno)+"的学生，学习"+self.curriculum+"课程")

# 		定义一个Teacher类，继承Person类，拥有自身的属性工号：gh，自身的方法：teach教课（课程）；
class Person():

    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print('%s吃%s' %(self.name,food))

    def sleep(self):
        print('睡觉')

class Teacher(Person):
    def __init__(self,gh,name):
        self.gh = gh
        self.name = name
        super().__init__(self.name)
    def teach(self,curiiculm):
        print('%s教课%s' %(self.gh,curiiculm))
    def job(self,company,salary):
        print("在%s上班，工资%s"%(company,salary))

# 1、实现gh为xx的老师，教xx课
mis_1 = Teacher('001','小明')
mis_1.teach('python')

# 2、实现gh为xx老师，在xx上班，一月工资xx
mis_1.job('FBI','20000元')
# 3、名字是xx，工号为xx的老师，吃饭
print("名字是%s工号为%s的老师，吃饭"%(mis_1.name,mis_1.gh))
# 有这样一个文件，文件内容如下：
# Lucy|18601914231|男|19890218
# Jack|18101913132|女|19810311
# Tom|18201912533|女|19830713
# Lily|18301911734|男|19870210

# 任务1-找出所有L开头的人名
#打开文件
with open("E:\\training\code\\vip3test\\interface_02\\homework\\人员信息.txt") as f:
    #读取文件内容
    info = f.readlines()
    print(info)
#找到所有L开头的人名
'''
srring.split("+")将字符串按照+分隔开
'''
name_L = []
li_old = []
li_nv = []
for i in info:
    li = i.split("|")
    if "L" in i[0]:
        name_L.append(li[0])
    if "女" in li[2]:
        li_nv.append(li)

print(name_L)
# 任务3-找出所有女性用户的信息l
print(li_nv)
# 任务2-按照年龄进行排序
'''
排序问题：两两比较，大的数放到后面，写两个循环，第二个循环次数会每次少一个，因为最大的数已经在最后，
循环部分：两个位置互换，把最大的放到后面info_2[j],info_2[j+1] = info_2[j+1],info_2[j]
若列表中的元素还为列表，则可找元素中的元素
'''
info = [i.strip() for i in info]
info_2 = [i.split("|") for i in info]
n = len(info)
for i in range(n):
    for j in range(n-i-1):
        if info_2[j][-1] > info_2[j+1][-1]:
            info_2[j],info_2[j+1] = info_2[j+1],info_2[j]
print(info_2)


# 目录下有这些文件：
# A1.txt
# B2.txt
# C1.doc
# D1.excel
# 任务1-将该目录下的文件按照后缀进行分类，然后分别新建且放入不同的文件夹内，比如txt文件放入txt目录下等




