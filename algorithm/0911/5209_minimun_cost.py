def recur(row, cur):
    global mini

    if cur >= mini:     # 가지치기용
        return

    if row == N:
        mini = cur
        return

    for i in range(N):
        if not checked[i]:
            checked[i] = True
            recur(row+1, cur+arr[row][i])
            checked[i] = False


T = int(input())
for x in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    checked = [False] * N   # 열 방문 check용
    mini = 15 * 99                # 최소 비용

    recur(0, 0)   # 시작인덱스와 시작비용 전달

    print(f'#{x} {mini}')