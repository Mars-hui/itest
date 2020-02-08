#coding = utf - 8
#插入排序
#时间复杂度：O（n的一次方）
def insert_sort(alist):
    #alist = [17, 20, 93, 54, 77, 31, 44, 55, 226]
    n = len(alist)
    for j in range(1,n):
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i-1],alist[i] = alist[i],alist[i-1]
            else:
                break
            i -= 1

if __name__ == '__main__':
    li = [17, 20, 93, 54, 77, 31, 44, 55, 226]
    print(li)
    insert_sort(li)
    print(li)