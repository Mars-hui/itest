#coding = utf - 8
'''快速排序'''
#最优时间复杂度：
#最坏时间复杂度
#稳定性

def quick_sort(alist, first, last):

    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    #从循环退出时，low==high
    alist[low] = mid_value
    #对low左边的列表执行快速排序
    quick_sort(alist, first, low-1)
    #对low右边的列表排序
    quick_sort(alist, low+1, last)

if __name__ == '__main__':
    li = [17, 20, 93, 54, 77, 31, 44, 55, 226]
    print(li)
    quick_sort(li,0, len(li)-1)
    print(li)