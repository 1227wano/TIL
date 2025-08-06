T = int(input())
for test in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))
    maxi = 0
    mini = 1000000
    for i in range(N):
        if a[i] > maxi:
            maxi = a[i]
    for j in range(N):
        if a[j] < mini:
            mini = a[j]
    result = maxi - mini
    print(f'#{test}', result)
