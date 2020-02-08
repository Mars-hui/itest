#coding = utf-8
import sys
# 题目11：要求输出国际象棋棋盘。
# 1.程序分析：用i控制行，j来控制列，根据i+j的和的变化来控制输出黑方格，还是白方格。

for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
            sys.stdout.write(chr(2019))
            sys.stdout.write(chr(2019))
        else:
            sys.stdout.write('  ')
    print('')




