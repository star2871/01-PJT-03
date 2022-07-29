from re import A
import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
for i in range(T):
    n = str(input())
    a = list(n)
    # if a == '3' and '4' and '5' and '6' and '9':
    #     print(1)
    # else:
    #     print(0)
    print(a)
