T = int(input())
for T in range(1, T+1):
    N, st = input().split()

    # int(n, 16) : 16진수인 n을 정수로 변환
    # bin(n) : 2진수로 바꾸는 함수
    # zfill(n) : 왼쪽에 0을 붙여서 총 길이를 n으로 맞춤

    n = int(st, 16)
    result = bin(n)[2:].zfill(int(N)*4)
    # [2:]로 앞의 '0b' 자르고, 2진수 글자수 = N*4

    print(f'#{T} {result}')