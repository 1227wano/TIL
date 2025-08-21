T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    def find_start(N):          # 시작점 찾아줘
        for i in range(N):
            for j in range(N):
                if maze[i][j] == 2:
                    return i, j

    def bfs(i, j, N):           
        visited = [[0] * N for _ in range(N)]
        q = [[i,j]]             # 시작점 넣기
        visited[i][j] = 1       # 1부터 1씩 증가하며 방문처리
        while q:
            ti, tj = q.pop(0)
            if maze[ti][tj] == 3:
                return visited[ti][tj] - 2
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                wi, wj = ti + di, tj + dj
                if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                    q.append([wi,wj])
                    visited[wi][wj] = visited[ti][tj] + 1   # 인큐표시
        return 0

    si, sj = find_start(N)
    ans = bfs(si, sj, N)
    print(f'#{tc} {ans}')