#coding = utf - 8
# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
# 思路：1)输入的正整数正好为素数不可分解
# 2）找因数，2，打印出，然后将n/2后的商再进行从2开始的找因数
# 3）2不是因数就找3...

from sys import stdout
n = int(input("请输入一个正整数：\n"))

stdout.write("%d= " %n)
for i in range(2,n+1):
    while n != i:
        if n % i == 0:
            # print("%d *" %i)
            stdout.write(str(i))
            stdout.write(" * ")
            n = n/i
        else:
            break
print(int(n))

'''
sys.stdin(),解释器的标准输入
sys.stdout(),解释器的标准输出
sys.stderr(),解释器的标准出错流
'''