#coding = utf - 8

# 题目14：判断101-200之间有多少个素数，并输出所有素数。
# 思路：只能被1和他本身整除
l = []
for i in range(101,201):
    for j in range(2,i):
        if i % j == 0:
            break
        elif j+1 == i:
            l.append(i)
print(l)
