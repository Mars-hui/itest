#coding=utf-8

class Person():

    #构造方法，初始化方法
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
        print("执行init方法")

    def eat(self,food):
        print('吃',food)

    def sleep(self):
        print('睡觉')
#实例化
a = Person('张三'，'')
#调用类中的方法
a.eat('uuu')
a.sleep()
