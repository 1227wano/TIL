import sys
sys.stdin = open("input.txt", "r")


def dfs(node):
    print(node, end=' ')

    # 다음 재귀 호출
    # node로 부터 갈 수 있는 노드들을 모두 확인
    # --> 그 중에서 한 곳으로 진행
    for next_node in graph[node]:
        # 이미 방문한 지점은 가지마라
        if visited[next_node]:
            continue

        visited[next_node] = 1  # 방문처리
        dfs(next_node)


V, E = map(int, input().split())

# 인접 리스트 (연결된 간선만 저장)
graph = [[] for _ in range(V+1)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)    # 주의! 양방향일때 필요!!

visited = [0] * (V + 1)     # 방문 여부 기록
visited[1] = 1  # 출발점 초기화

dfs(1)