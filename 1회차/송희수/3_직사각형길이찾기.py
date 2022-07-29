import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())
for i in range(1,T+1):
    lenth =list(map(int, input().split()))
    # 일단 모든 값을 정렬 하였다.
    lenth.sort()
    # 112 344 555 이렇게 나온다
    # 첫번째자리에수와 두번째자리에수가 같지않으면 첫번째자리수를 프린트한다. 나머지는 세번째자리수를 프린트한다.
    if lenth[0] != lenth[1]:
        print(f'#{i} {lenth[0]}')
    else:
        print(f'#{i} {lenth[2]}')

   
        