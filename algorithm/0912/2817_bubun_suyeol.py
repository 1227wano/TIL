from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0

    for i in range(N):  # 각 인덱스를 기준으로 순회
        d = deque(arr)
        d.rotate(-i)
        now = d[0]      # 기준 값
        for j in range(1, N):
            if now == K:
                break
            else:
                now += d[j]
        if now == K:
            cnt += 1

    print(f'#{tc} {cnt}')