#coding = utf - 8
'''归并排序
先分解再合并，运用递归
最优时间复杂度：O(nlogn)
最坏时间复杂度：O(nlogn)
稳定性：稳定
'''
def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2

    # left 采用归并排序后形成的有序的新的列表
    left_li = merge_sort(alist[:mid])

    # right 采用归并排序后形成的有序的新的列表
    right_li = merge_sort(alist[mid:])

    # 将两个有序的子序列合并为一个新的整体
    left_pointer,right_pointer = 0, 0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result

if __name__ == '__main__':
    # li = [17, 20, 93, 54, 77, 31, 44, 55, 226]
    li = [1, 2, 3, 4, 5, 6, 20, 7, 8]
    print(li)
    sorted_li = merge_sort(li)
    print(sorted_li)

