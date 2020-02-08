#coding = utf-8

def bubble_sort(alist):
    n = len(alist)
    #如果列表本身就是有序的，那么则不用交换，用count记录交换的次数，若第一次比较均未交换，说明列表为有序列表
    for i in range(n-1):
        count = 0
        for j in range(n-1-i):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count += 1
        if count == 0:
            return

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31]
    print(li)
    bubble_sort(li)
    print(li)