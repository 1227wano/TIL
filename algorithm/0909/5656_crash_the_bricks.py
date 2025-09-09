from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def shoot(cnt, remains, now_arr):
    global min_blocks
    # 종료 조건 : N개의 구슬을 모두 발사 or 남은 벽돌이 0이면
    if cnt == N or remains == 0:
        min_blocks = min(min_blocks, remains)
        return

    # 모든 열에 한 줄 씩 떨구자
    for col in range(W):
        # 기존 벽돌들의 상태를 저장해야함
        # 방법1. 원본을 복사해두고, 재귀시키기
        # 1. col 위치에 떨구기 전 상태를 복사 (얕은 복사 주의)
        # 2. 원본 리스트의 col 위치에 떨구고
        # 3. cnt +1 번 재귀 상태로 이동
        # 4. 떨구기 전 상태로 복귀

        # 방법2. 복구 시간이 없는 방식 (채택)
        # 1. col 위치에 떨구기 전 상태를 복사
        # 2. 복사한 리스트의 col위치에 떨군다
        # 3. cnt+1 번 상태로 이동할 때,
        copy_arr = [row[:] for row in now_arr]

        row = -1
        # 가장 위 벽돌을 검색
        for r in range(H):
            if copy_arr[r][col]:
                row = r
                break

        if row == -1:   # 벽돌이 없는 열은 pass
            continue

        # 해당 row, col의 숫자부터 시작해서 BFS
        q = deque([(row, col, copy_arr[row][col])])
        now_remains = remains - 1
        copy_arr[row][col] = 0   # 구슬이 처음 만나는 벽돌 자리

        # 주변 벽돌들을 순차적으로 파괴
        while q:
            r, c, p = q.popleft()
            # 상하좌우의 p칸을 모두 제거
            for k in range(1, p):
                for i in range(4):
                    nr = r + (dy[i] * k)
                    nc = c + (dx[i] * k)

                    if nr < 0 or nr >= H or nc < 0 or nc >= W:
                        continue

                    if copy_arr[nr][nc] == 0:
                        continue

                    q.append((nr, nc, copy_arr[nr][nc]))
                    copy_arr[nr][nc] = 0
                    now_remains -= 1

        # 빈칸 메우기
        for c in range(W):
            idx = H - 1
            for r in range(H-1, -1, -1):
                if copy_arr[r][c]:
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -= 1

        shoot(cnt+1, now_remains, copy_arr)


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_blocks = 1e9  # 최소 벽돌수 (1억부터시작)
    blocks = 0

    # 남은 벽돌 수
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                blocks += 1

    shoot(0, blocks, arr)
    print(f'#{tc} {min_blocks}')