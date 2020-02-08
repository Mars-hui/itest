#coding = utf - 8
#题目7：输入三个整数x,y,z，请把这三个数由小到大输出。

x,y,z = input("请输入三个整数：").split(',')
l = [x,y,z]
l.sort()
print(l)

