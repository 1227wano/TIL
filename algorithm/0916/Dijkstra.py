import sys
sys.stdin = open("input.txt", "r")
from heapq import heappop, heappush


def dijkstra(start_node):
    pq = [(0, start_node)]  # (누적거리, 노드번호)
    dists = [INF] * V       # 각 정점까지의 최단 거리 저장
    dists[start_node] = 0   # 시작노드 최단거리는 0

    while pq:
        dist, node = heappop(pq)

        # 이미 더 작은 값으로 온 적이 있으면 버린다
        # - (3, c) (4, c) 예시
        if dists[node] < dist:
            continue

        for next_dist, next_node in graph[node]:
            # 다음 노드로 가기 위한 누적 거리
            # 누적 거리 = 현재까지의 거리 + 다음 거리
            new_dist = dist + next_dist

            # 이미 크거나 같은 가중치로 온 적이 있다면 continue
            if dists[next_node] <= new_dist:
                continue

            # 누적거리, 새로운 노드를 pq에 저장 + dists에 갱신
            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

    return dists


INF = int(21e9)     # 무한대를 가정(문제의 최대)
                    # 손으로 다 더했을 때 최대값이 몇일까

V, E = map(int, input().split())
graph = [[] for _ in range(V)]  # 인접 리스트 (인접행렬도 사용할줄알도록)

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end))  # 주의! 다익스트라는 단방향

# 출발지로부터 모든 최단거리
result = dijkstra(0)
print(result)