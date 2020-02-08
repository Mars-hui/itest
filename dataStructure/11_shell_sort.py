#coding = utf-8
'''希尔排序'''
#时间复杂度：n的平方
#不稳定
def shell_sort(alist):

    n = len(alist)
    gap = n//2
    while gap > 0:
        for j in range(gap,n):
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2

if __name__ == '__main__':
    li = [17, 20, 93, 54, 77, 31, 44, 55, 226]
    print(li)
    shell_sort(li)
    print(li)