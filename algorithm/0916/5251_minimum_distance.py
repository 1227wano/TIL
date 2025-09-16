import sys
sys.stdin = open("input.txt", "r")
from heapq import heappop, heappush


def dijkstra(start_node):
    priority_q = [(0, start_node)]
    distance_list = [inf] * (N+1)
    distance_list[start_node] = 0

    while priority_q:
        distance, node = heappop(priority_q)

        if distance_list[node] < distance:  # 이미 저장된 최소 거리가 있으면 넘어가
            continue

        for next_node in range(N+1):   # 현재 노드의 거리들 뽑아
            # 거리 없으면 넘어가
            if graph[node][next_node] == 0:
                continue

            new_dist = distance + graph[node][next_node]

            # 이미 크거나 같은 거리로 왔으면 넘어가
            if distance_list[next_node] <= new_dist:
                continue

            distance_list[next_node] = new_dist
            heappush(priority_q, (new_dist, next_node))

    return distance_list[N]


T = int(input())
for T in range(1, T+1):
    N, E = map(int, input().split())

    start_node = 0
    graph = [[0] * (N+1) for _ in range(N+1)]
    inf = int(21e9)

    for _ in range(E):
        start, end, dis = map(int, input().split())
        graph[start][end] = dis

    result = dijkstra(0)
    print(f'#{T} {result}')