import sys
sys.stdin = open("input.txt", "r")
from heapq import heappop, heappush


def prim(start_node):
    priority_q = [(0, start_node)]
    mst = [0] * (V+1)
    min_w = 0

    while priority_q:
        wei, node = heappop(priority_q)
        if mst[node]:
            continue

        mst[node] = 1
        min_w += wei

        for next_wei, next_node in graph[node]:
            if mst[next_node]:
                continue

            heappush(priority_q, (next_wei, next_node))

    return min_w


T = int(input())
for T in range(1, T+1):
    V, E = map(int, input().split())

    start_node = 0
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        start, end, weight = map(int, input().split())
        graph[start].append((weight, end))
        graph[end].append((weight, start))

    result = prim(0)
    print(f'#{T} {result}')