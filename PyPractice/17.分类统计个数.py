#coding = utf - 8
# 题目17：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
from pip._vendor.distlib.compat import raw_input

s = raw_input("输入一行字符：")
letters = 0
digit = 0
space = 0
others = 0

for i in s:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        space += 1
    else:
        others += 1
print("letters = %d,digit = %d,space = %d,others = %d" %(letters,digit,space,others))
'''
i.isalpha()
i.isdigit()
i.isspace()
'''
