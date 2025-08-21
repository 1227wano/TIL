T = int(input())
for tc in range(1, T+1):
    n, e = map(int, input().split())    # 점의 개수, 선의 개수

    # 먼저 그래프를 데이터로 표현해야함
    # 선들을 일단 입력받자
    edges = [list(map(int, input().split())) for _ in range(e)]

# 인접 행렬   <- ..이거 씀?
    # 2차원 배열을 만들고,
    # arr[i][j]가 True라면 i->j로 통하는 길이 있음을 나타내도록
    # 값을 채운다.
    # 1. 일단 전체 배열을 만든다
    # N개의 점이 있다면 최소 N * N의 2차원 배열이 필요
    adj_mat = [
        [0] * (n + 1) for _ in range(n + 1)
    ]
    # 2. 각 간선을 살펴보면서 adj_mat을 채운다
    for edge in edges:
        # edge[0]에서 edge[1]까지는 길이 존재함을 의미하므로
        adj_mat[edge[0]][edge[1]] = 1
        # 양방향이라면
        # edge[1]에서 edge[0]까지 길도 존재함을 의미하므로
        # adj_mat[edge[1]][edge[0]] = 1
    # for row in adj_mat:
    #     print(row)

# 인접 리스트
    # 2차원 배열을 만들고,
    # arr[i]에 리스트(또는 다른 컬렉션)을 할당한 다음
    # i에 저장된 리스트에 연결된 정점들을 넣는다
    # 1. 각 i와 연결된 점들 보관을 위한 리스트를 만든다
    adj_list = [
        [] for _ in range(n+1)
    ]
    # 2. 각 간선을 살펴보면서, adj_list를 갱신한다.
    for edge in edges:
        # edge[0]에서 edge[1]이 도달 가능함을 의미하므로
        adj_list[edge[0]].append(edge[1])
        # 양방향이면
        # adj_list[edge[1]].append(edge[0])

    # for row in adj_list:
    #     print(row)

# -------------------------------------------------------------------------------

    # DFS를 해보자
    # 1. 재방문 방지를 위한 방문 배열을 만든다
    visited = [0 for _ in range(n+1)]
    # 2. 출발지점과 끝 지점을 기록한다
    start, goal = map(int, input().split())
    visited[start] = 1

    # 3. (덤) 진행 경로를 저장할 리스트를 만든다
    route = []

    # 4. stack을 만든다
    stack = [start]

    # stack이 비어있지 않은 동안 반복함
    while stack:
        # 1. 이번 방문 지점을 가져온다
        now = stack.pop()
        # 2. (덤) 방문 순서를 기록한다 ( 문제마다 다름 )
        route.append(now)
        # 3. 다음 방문 가능 점들을 넣는다
        for next_node in adj_list[now]:
            # 연결되어 있고, 방문한 적 없으면 stack에 넣고 방문표시
            if visited[next_node] == 0:
                stack.append(next_node)
                visited[next_node] = 1

    # print('DFS')
    # print(route)
    # print(visited[goal])

    # BFS
    for i in range(n+1):        # 방문기록 리셋
        visited[i] = 0
    visited[start] = 1

    # 3. (덤) 진행 경로를 저장할 리스트를 만든다
    route = []

    # 4. queue를 만든다
    queue = [start]

    # queue가 비어있지 않은 동안 반복함
    while queue:
        # 1. 이번 방문 지점을 가져온다
        now = queue.pop(0)
        # 2. (덤) 방문 순서를 기록한다 ( 문제마다 다름 )
        route.append(now)
        # 3. 다음 방문 가능 점들을 큐에 넣는다
        for next_node in adj_list[now]:
            # 연결되어 있고, 방문한 적 없으면 stack에 넣고 방문표시
            if visited[next_node] == 0:
                queue.append(next_node)
                visited[next_node] = 1

    # print('BFS')
    # print(route)
    # print(visited[goal])

    print(f'#{tc} {visited[goal]}') # goal번째에 방문했으면 1이, 아니면 0이 출력