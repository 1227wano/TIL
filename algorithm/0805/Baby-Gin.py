T = int(input())
for test in range(1, T + 1):
    N = int(input())        # 054060
    a = [0] * 10
    tri = 0
    ron = 0

    for i in range(6):     # 받은 숫자열 배열에 담아
        a[N % 10] += 1
        N //= 10

    for j in range(10):
        while a[j] >= 3:
            a[j] -= 3
            tri += 1

    for j in range(8):
        while a[j] >= 1 and a[j+1] >= 1 and a[j+2] >= 1:
            a[j] -= 1
            a[j+1] -= 1
            a[j+2] -= 1
            ron += 1

    if tri + ron == 2:
        print(f'#{test} 1')
    else:
        print(f'#{test} 0')