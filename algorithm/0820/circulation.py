from collections import deque

T = int(input())
for T in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    cq = deque(arr)

    for i in range(M):
        cq.rotate(-1)

    r = cq[0]

    print(f'#{T} {r}')