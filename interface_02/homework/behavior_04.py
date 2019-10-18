#coding=utf-8

#创建 抢 类
class Gun():

    def __init__(self,number,add_number):
        self.number = number
        self.add_number = add_number
    #发射子弹
    def shoot(self):
        print("发射子弹")
        self.number -= 1
    #增加子弹的数量
    def add(self):
        print("增加子弹的数量")
        self.number += self.add_number

#创建 士兵 类，继承 抢
class Soldier(Gun):
    # 属性：名字，手枪
    def __init__(self,name,gun):
        self.name = name
        self.gun = gun
        #super.__init__(self.number,self.add_number) #若关联继承的类，则调用这个函数时需要传入相关参数

    def print_info(self):
        print('士兵'+ self.name + '有一把' + self.gun)

soldier_01 = Soldier('瑞恩','AK47')
soldier_01.print_info()
