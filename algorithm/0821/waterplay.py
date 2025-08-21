T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ground = [list(input()) for _ in range(N)]
    cnt = 0     # 최소 이동 횟수

    # L 위치와 개수 저장
    lll = []
    l_count = 0
    # L 개수만큼 반복 위치 뽑아서 시작 포인트로
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 'L':
                l_count += 1
                lll.append([i,j])


    def bfs(i, j):
        visited = [[0] * M for _ in range(N)]
        q = [[i,j]]
        visited[i][j] = 1
        count = 0  # W 까지의 거리계산용

        while q:
            pi, pj = q.pop(0)   # 처음은 시작위치(L)
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ni = pi + di
                nj = pj + dj
                if ground[ni][nj] == 'W':
                    count += 1
                    return count
                elif 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                    q.append([ni, nj])      # 다음에 갈곳
                    visited[ni][nj] = 1
                    count += 1
        return count   # W 를 찾기까지 걸린

    for li, lj in lll:
        cnt += bfs(li, lj)

    print(f'#{tc} {cnt}')