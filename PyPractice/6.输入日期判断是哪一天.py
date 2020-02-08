#coding=utf-8

# 题目6：输入某年某月某日，判断这一天是这一年的第几天？

year, month, day = input("请输入年-月-日:").split('-')
print(year, month, day)

months = (0,31,59,90,120,151,181,212,243,273,304,334,365)  #13
year = int(year)
month = int(month)
day = int(day)
sum = months[month - 1] + day
#若闰年则+1天
leap = 0
if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
    leap = 1
if month >= 2 and leap == 1:
    sum += 1

print("这一天是这一年的第%d天" %sum)




