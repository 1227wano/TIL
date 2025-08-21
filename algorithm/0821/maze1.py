T = 10
for tc in range(1, T+1):
    tc = int(input())        # 테케번호!
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]

    # 시작점 도착점 찾기
    def find_start():          # 시작점 찾아줘
        for i in range(N):
            for j in range(N):
                if maze[i][j] == 2:
                    return i, j

    def bfs(i, j, N):
        visited = [[0] * N for _ in range(N)]
        q = [[i, j]]
        visited[i][j] = 1
        while q:
            pi, pj = q.pop(0)
            if maze[pi][pj] == 3:
                return 1
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ni = pi + di
                nj = pj + dj
                if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                    q.append([ni, nj])
                    visited[ni][nj] = 1
        return 0

    si, sj = find_start()
    result = bfs(si, sj, N)
    print(f'#{tc} {result}')