T = int(input())
for test in range(1, T + 1):
    N = int(input())        # 다 5?
    delta = [list(map(int, input().split())) for _ in range(N)]

    hap = 0
    # for i in range(N):
    #     for j in range(N):
    #         # 9개의 영역으로 조건문 돌리기... 이게 맞아?
    #         # 피자 맛난 영역
    #         if 0<i<4 and 0<j<4:
    #             hap += abs(delta[i][j] - delta[i-1][j])
    #             hap += abs(delta[i][j] - delta[i][j-1])
    #             hap += abs(delta[i][j] - delta[i+1][j])
    #             hap += abs(delta[i][j] - delta[i][j+1])
    #
    #         # 치즈크러스트 영역
    #         if i==0 and 0<j<4:
    #             hap += abs(delta[i][j] - delta[i][j-1])
    #             hap += abs(delta[i][j] - delta[i+1][j])
    #             hap += abs(delta[i][j] - delta[i][j+1])
    #         if j==0 and 0<i<4:
    #             hap += abs(delta[i][j] - delta[i-1][j])
    #             hap += abs(delta[i][j] - delta[i+1][j])
    #             hap += abs(delta[i][j] - delta[i][j+1])
    #         if i==4 and 0<j<4:
    #             hap += abs(delta[i][j] - delta[i-1][j])
    #             hap += abs(delta[i][j] - delta[i][j-1])
    #             hap += abs(delta[i][j] - delta[i][j+1])
    #         if j==4 and 0<i<4:
    #             hap += abs(delta[i][j] - delta[i-1][j])
    #             hap += abs(delta[i][j] - delta[i+1][j])
    #             hap += abs(delta[i][j] - delta[i][j-1])
    #
    #         # 꼬다리 영역
    #         if i==0 and j==0:
    #             hap += abs(delta[i][j] - delta[i+1][j])
    #             hap += abs(delta[i][j] - delta[i][j+1])
    #         if i==0 and j==4:
    #             hap += abs(delta[i][j] - delta[i+1][j])
    #             hap += abs(delta[i][j] - delta[i][j-1])
    #         if i==4 and j==0:
    #             hap += abs(delta[i][j] - delta[i-1][j])
    #             hap += abs(delta[i][j] - delta[i][j+1])
    #         if i==4 and j==4:
    #             hap += abs(delta[i][j] - delta[i-1][j])
    #             hap += abs(delta[i][j] - delta[i][j-1])

    for i in range(N):
        for j in range(N):
            now = delta[i][j]                           # 기준
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:  # 각 방향으로 반복
                ni, nj = i + di, j + dj                 # 현 위치
                if 0 <= ni < N and 0 <= nj < N:         # 인덱스 범위 조건
                    hap += abs(delta[ni][nj] - now)

    print(f'#{test} {hap}')