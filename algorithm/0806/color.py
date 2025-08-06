T = int(input())
for test in range(1, T + 1):
    N = int(input())        # 색칠 개수
    color = [list(map(int, input().split())) for _ in range(N)]
    purple = 0
    white = [[0] * 10 for _ in range(10)]

    for i in range(N):      # 색칠한거 만큼 반복
        for a in range(color[i][2]-color[i][0]+1):        # 상하이동
            for b in range(color[i][3]-color[i][1]+1):    # 좌우이동
                h = color[i][0]+a   # 색칠 상하위치 2
                w = color[i][1]+b   # 색칠 좌우위치 2
                if color[i][4] == 1:
                    white[h][w] += 1
                if color[i][4] == 2:
                    white[h][w] += 2

    for a in range(10):
        for b in range(10):
            if white[a][b] >= 3:
                purple += 1

    print(f'#{test} {purple}')