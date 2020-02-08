#coding = utf-8
li = [1,3,4,5,6,8,9,10,19]
n = len(li)
cur = 0

while cur < n-1:
    f = cur
    if li[cur + 1] - li[cur] != 1:
        print('[%d,%d]' % (li[f], li[cur]),end = '')
    else:
        li_1 = [li[f]]
        while cur < n-1 and li[cur + 1] - li[cur] == 1:
            cur += 1
            li_1.append(li[cur])
        print(li_1, end = '')
    cur += 1
if li[-1] - li[-2] != 1:
        print('[%d,%d]'%(li[-1], li[-1]))
'''
【总结】
1. 找到规律，哪个是变得，哪个是不变的
2. 利用游标

'''