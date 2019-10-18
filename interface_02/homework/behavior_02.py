#coding=utf-8

class Person():

    #属性：名字，体重
    def __init__(self,name,weight):
        self.name = name
        self.weight = float(weight)
    #打印某人的体重
    def print_weight(self):
        print(self.name+"体重是"+str(self.weight)+"公斤")

    #跑步，跑步后体重减0.5公斤
    def run(self):
        self.weight -= 0.5
    #吃东西，吃东西体重增加1公斤
    def eat(self):
        self.weight += 1

#小明体重75.0公斤
xiaoming = Person('小明','75.0')
xiaoming.print_weight()
#小美的体重是45.0公斤
xiaomei = Person('小美','45.0')
xiaomei.print_weight()
#小明跑步后体重多少？
xiaoming.run()
xiaoming.print_weight()

#注意：传数据的类型时字符串类型还是整数型？那么在调用时需要转换类型，运算时用的是float或int