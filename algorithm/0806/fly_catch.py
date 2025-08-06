T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    catch = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            di = 0
            for a in range(M):
                for b in range(M):
                    di += catch[i+a][j+b]
            if di > result:
                result = di

    print(f'#{test} {result}')