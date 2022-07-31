import sys

sys.stdin = open("_소득불균형.txt")

T= int(input())

for tc in range(1,T+1):
    N = int(input())

    pay =list(map(int, input().split()))
    

    # 전체 평균을 구해줍니다.
    avg = int(sum(pay) / len(pay))

    cnt = 0

     # 평균소득 보다 작거나 같으면 그 소득 명수를 적는다.

    for i in pay:
        if i <= avg:
            cnt += 1

    print(f'#{tc} {cnt}')