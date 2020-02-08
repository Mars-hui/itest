#coding = utf - 8
#二分查找，使用递归的方法
#递归版本

# def binary_search(alist,item):
#     n = len(alist)
#     if n > 0:
#         mid = n // 2
#         if alist[mid] == item:
#             return True
#         elif alist[mid] > item:
#             return binary_search(alist[:mid], item)
#         else:
#             return binary_search(alist[mid+1:], item)
#     return False

#非递归版本
def binary_search(alist,item):
    n = len(alist)
    first = 0
    last = n-1

    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == '__main__':
    li = [17, 20, 31, 44, 54, 55, 77, 93, 226]
    print(li)
    res = binary_search(li, 44)
    print(res)


