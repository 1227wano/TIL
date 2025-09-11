def recur(row, cur):
    global maxi

    if cur <= maxi:     # 가지치기용. 확률은 점점 낮아지므로 현재 확률이 현 최고확률보다 낮다면 종료
        return

    if row == N:
        maxi = cur      # 일 배정 다 끝날때마다 최대 확률 갱신
        return

    for i in range(N):
        if not checked[i]:
            checked[i] = True
            recur(row+1, cur*(arr[row][i] / 100.0))        # 현재 확률을 곱해서 전달
            checked[i] = False


T = int(input())
for x in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    checked = [False] * N   # 열 방문 check용
    maxi = 0.0              # 확률

    recur(0, 1.0)   # 시작인덱스와 시작확률 전달

    result = maxi * 100

    print(f'#{x} {result:.6f}')     # 소수점 6자리