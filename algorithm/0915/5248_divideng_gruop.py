import sys
sys.stdin = open("input.txt", "r")


def dfs(node):
    for next_node in li[node]:
        if visited[next_node]:
            continue
        visited[next_node] = True
        dfs(next_node)


T = int(input())
for T in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))

    # 인접리스트
    li = [[] for _ in range(V+1)]

    for i in range(E):
        li[arr[i*2]].append(arr[i*2+1])
        li[arr[i*2+1]].append(arr[i*2])

    visited = [False] * (V+1)
    cnt = 0
    for j in range(1, V+1):
        if not visited[j]:
            cnt += 1
            dfs(j)

    print(f'#{T} {cnt}')