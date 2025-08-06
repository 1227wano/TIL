for test in range(1, 11):
    T = int(input())
    N = 100
    delta = [list(map(int, input().split())) for _ in range(N)]

    hap = 0

    # 가로
    for i in range(N):
        now = 0                 # 각 행마다의 비교값
        for j in range(N):
            now += delta[i][j]
        if now > hap:
            hap = now

    # 세로
    for a in range(N):
        now = 0                 # 각 행마다의 비교값
        for b in range(N):
            now += delta[b][a]
        if now > hap:
            hap = now

    # 대각선 좌우
    now = 0
    for i in range(100):
        now += delta[i][i]
    if now > hap:
        hap = now

    # 대각선 우좌
    now = 0
    for i in range(100):
        now += delta[i][N-1-i]
    if now > hap:
        hap = now

    print(f'#{test} {hap}')