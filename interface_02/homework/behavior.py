#coding=utf-8
#打印小猫爱吃鱼，小猫要喝水
class Behavior():

    def __init__(self,name,do):
        self.name = name
        self.do = do

    def action(self):
        print(self.name+self.do)

#小猫爱吃鱼
cat_01 = Behavior('小猫','爱吃鱼')
cat_01.action()
#小猫要喝水
cat_02 = Behavior('小猫','要喝水')
cat_02.action()


