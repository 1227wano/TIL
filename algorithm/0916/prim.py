from heapq import heappush, heappop
import sys
sys.stdin = open("input.txt", "r")


# 특정 정점 기준으로 시작해서 갈수있는 노드 중 가중치가 최소인 노드부터
# -> 작은 노드를 먼저 꺼내기 위해 우선순위큐(heapq)를 활용
def prim(start_node):
    pq = [(0, start_node)]  # (가중치, 시작노드) <- 힙큐는 앞에있는걸로 정렬하니까 이 순서로
    MST = [0] * V   # visited와 동일
    min_weight = 0  # 최소 비용(가중치)

    while pq:
        weight, node = heappop(pq)  # 최소 가중치 꺼냄
        # 이미 방문한 노드라면 continue
        if MST[node]:
            continue

        MST[node] = 1           # node로 가는 최소 비용이 선택됨
        min_weight += weight    # 누적합 추가

        for next_node in range(V):
            # 갈 수 없으면 continue
            if graph[node][next_node] == 0:
                continue

            # 이미 방문했으면 continue
            if MST[next_node]:
                continue

            # 원래 BFS에서는 여기서 방문 처리 -> 최소 비용 x

            heappush(pq, (graph[node][next_node], next_node))

    return min_weight


V, E = map(int, input().split())
# 인접 행렬
graph = [[0] * V for _ in range(V)]

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start][end] = weight
    graph[end][start] = weight  # 양방향이라

result = prim(0)     # 출발 정점과 함께 시작 (출발 점정을 바꿔도 최소비용은 동일)
print(f'최소비용 = {result}')