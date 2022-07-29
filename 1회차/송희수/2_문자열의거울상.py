import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())
for i in range(1,T+1):
    n = list(str(input()))
    a = n[::-1]
    result = ""
    # p 를 q로 q를 p로 d를 a로 a를 d로
    for t in range(len(a)):
        if a[t] == 'b':
         result += 'd'
        elif a[t] == 'd':
            result += 'b'
        elif a[t] == 'p':
            result += 'q'
        else :
            result += 'p'
    print(f'#{i} {result}')
    