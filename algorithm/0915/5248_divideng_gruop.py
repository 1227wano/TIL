import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for T in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))

    # 인접리스트
    li = [[] for _ in range(V+1)]

    for i in range(E):
        li[arr[i*2]].append(arr[i*2+1])
        li[arr[i*2+1]].append(arr[i*2])
    print(li)
    # 0
    # 1 [2]v
    # 2 [1, 3]v
    # 3 [2]v
    # 4 [5]v
    # 5 [4]v
    visited = [False] * (V+1)
    cnt = 0
    for j in range(1, V+1):
        if len(li[j]) > 0 and not visited[j]:
            visited[j] = True
            cnt += 1
            for k in range(len(li[j])):
                visited[li[j][k]] = True
        elif len(li[j]) > 0 and visited[j]:
            for k in range(len(li[j])):
                visited[li[j][k]] = True

    for l in range(1, V+1):
        if not visited[l]:
            cnt += 1

    print(f'#{T} {cnt}')