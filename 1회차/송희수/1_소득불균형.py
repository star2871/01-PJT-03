import sys

sys.stdin = open("_소득불균형.txt")

T= int(input())

for i in range(1,T+1):

    # 평균소득 보다 작거나 같으면 그 소득 명수를 적는다.
    pay =list(map(int, input().split()))
    print(pay)