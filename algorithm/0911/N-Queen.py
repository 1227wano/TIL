# N-Queen
def check(row, col):
    # (row, col) 좌표 기준
    # 1. 같은 열에 놓은 적이 잇는가
    for i in range(row):
        if visited[i][col]:
            return False

    # 2. 좌상단 대각선에 놓은 적이 있는가 (\)
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if visited[i][j]:
            return False

        i -= 1
        j -= 1

    # [참고] for문으로 하고싶다다
    # for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
    #     if visited[i][j]:
    #         return False
    # zip이 머더라...

    # 3. 상단 대각선에 놓은 적이 있는가 (/)
    i, j = row-1, col+1
    while i >= 0 and j < N:
        if visited[i][j]:
            return False

        i -= 1
        j += 1

    return True


# 종료조건 : N개의 행을 모두 고려하면 종료
# 가지의 수 : N개의 열
def recur(row):
    global answer

    if row == N:
        answer += 1
        return

    for col in range(N):
        # 가지치기 : 같은 열을 못고르도록
        # --> 유망하지 않은 케이스를 모두 삭제(세로, 대각선)
        if not check(row, col):
            continue

        # col을 선택
        visited[row][col] = 1
        recur(row+1)
        visited[row][col] = 0


N = 8
answer = 0  # 가능한 정답수
visited = [[0] * N for _ in range(N)]
recur(0)
print(f'N={N} / answer={answer}')