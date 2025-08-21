T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())    # 노드 개수, 간선 개수
    edges = [list(map(int, input().split())) for _ in range(E)]  # 간선 정보
    S, G = map(int, input().split())    # 출발노드, 도착노드
    cnt = 0

    # 인접리스트
    ad_li = [[] for _ in range(V+1)]    # 인덱스번호 = 노드번호 니까+1
    for edge in edges:
        ad_li[edge[0]].append(edge[1])
        ad_li[edge[1]].append(edge[0])  # 양방향이니

    # 도착노드까지의 간선의 개수
    def bfs():
        visited = [0] * (V+1)
        q = [S]
        while q:
            p = q.pop(0)
            for a in ad_li[p]:          # 해당노드의 인접노드 뽑고
                if visited[a] == 0:     # 방문 안했으면
                    q.append(a)         # 큐(다음노드)에 담고
                    visited[a] = visited[p] + 1   # 시작노드에서 거리만큼 기록

        return visited[G]   # 도착노드의 거리

    print(f'#{tc} {bfs()}')