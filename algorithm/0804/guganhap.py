T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    maxi = 0
    mini = N * 10000
    for i in range(N-M+1):
        hap = 0
        for q in range(M):
            hap += li[i+q]
        if hap > maxi:
            maxi = hap

    for j in range(N-M+1):
        hap = 0
        for w in range(M):
            hap += li[j+w]
        if hap < mini:
            mini = hap

    result = maxi - mini
    print(f'#{test}', result)