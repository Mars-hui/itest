#coding = utf-8
#选择排序
#时间复杂度：n * n---O(n的平方)
#alist = [17, 20, 93, 54, 77, 31, 44, 55, 226]
def bubble_sort(alist):
    min_index = 0
    n = len(alist)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if alist[min_index] > alist[j]:
                min_index = j
        alist[i],alist[min_index] = alist[min_index],alist[i]


if __name__ == '__main__':
    li = [17, 20, 93, 54, 77, 31, 44, 55, 226]
    print(li)
    bubble_sort(li)
    print(li)