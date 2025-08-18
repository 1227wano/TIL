# maze
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    result = 0

    # 시작점 찾기
    si = sj = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
                break

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # 상하좌우
    visited = [[False] * N for _ in range(N)]

    def dfs(si, sj):
        stack = [(si, sj)]      # 첫방문지 & 다음방문지 저장
        visited[si][sj] = True  # 방문여부

        while stack:            # 스택에 가능방문지 저장하고
            i, j = stack.pop()  # 빼면서 첫 방문지까지 빠지면 반복끝

            if arr[i][j] == 3:  # 도착점
                return 1

            for di, dj in dirs:     # 인접 가능방문지 찾고
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if not visited[ni][nj] and arr[ni][nj] != 1:  # 방문 안했고, 벽이 아닌곳이면
                        visited[ni][nj] = True                    # push 시점에 방문 처리
                        stack.append((ni, nj))
        return 0

    result = dfs(si, sj)
    print(f'#{tc} {result}')
