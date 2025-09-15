import sys
sys.stdin = open("input.txt", "r")

from collections import deque
# deque 하는 이유 1. pop(0) 2. 중간을 검사 X


def bfs(start_node):
    # q의 의미: 다음에 방문해야 할 노드들 (후보열)
    q = deque([start_node])    # 시작점을 queue에 넣고 시작

    while q:
        # 1. 가장 앞의 노드를 뽑는다
        # 2. 해당 노드에서 갈 수 있는 노드들을 queue에 넣는다
        now = q.popleft()

        print(now, end=' ')

        for next_node in graph[now]:
            if visited[next_node]:
                continue

            visited[next_node] = 1
            q.append(next_node)


V, E = map(int, input().split())

# 인접 리스트 (연결된 간선만 저장)
graph = [[] for _ in range(V+1)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)    # 주의! 양방향일때 필요!!

visited = [0] * (V + 1)     # 방문 여부 기록
visited[1] = 1  # 출발점 초기화

bfs(1)

