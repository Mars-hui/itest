#coding = utf - 8
#lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，
# 也就是指匿名函数。
#1、直接使用lambda函数
from functools import reduce

add = lambda x,y:x+y
print(add(1,2))
#2、应用在函数式编程
#将列表中的元素按照绝对值大小进行升序排列
list1 = [3,4,-3,44,0,-99]
# list2 = sorted(list1, key=lambda x : abs(x))
# print(list2)

#3、Python提供了很多函数式编程的特性，如：map、reduce、filter、sorted等这些函数都
# 支持函数作为参数，lambda函数就可以应用在函数式编程中

# ① map() 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
#在python3X  中map（）返回的为解释器



res = map(lambda x:x ** 2,list1)
print(map(lambda x:x ** 2,list1))

# ② reduce()函数：对参数序列中元素进行累积
from functools import reduce

list=[2,4,5,7,5,3,7]
sn = reduce(lambda x,y:x+y,list)
print(sn)

# ③filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中。


