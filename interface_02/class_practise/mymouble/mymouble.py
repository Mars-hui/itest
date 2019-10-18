#coding=utf-8
def fun1():
    print('fun1')

def fun2():
    print('fun2')

print('mymouble文件的name属性：',__name__)

if __name__ == '__main__':
    fun1()
    fun2()