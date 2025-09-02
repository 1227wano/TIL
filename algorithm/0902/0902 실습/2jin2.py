T = int(input())
for T in range(1, T+1):
    num = float(input())    # 0.625
    # 소수부분 2진수 -> 10진수
    # 0.625 x 2 = 1.25 -> 정수 1
    # 0.25 x 2 = 0.5 -> 정수 0
    # 0.5 x 2 = 1.0 -> 정수 1

    result = ''
    for i in range(12):     # 13자리 이상이면 x
        num *= 2
        if num >= 1:
            result += '1'
            num -= 1     # num = 0.25
        else:
            result += '0'

        if num == 0:    # num이 0되면 연산 끝
            break

    if num != 0:    # 12자리 까지 연산해도 num이 남았으면
        print(f'#{T} overflow')
    else:
        print(f'#{T} {result}')