T = 10
for test in range(1, T + 1):
    tc, N = map(int, input().split())       # 테케번호, 길의 개수(는 어따씀)
    arr = list(map(int, input().split()))   # 순서쌍

    visited = [False] * 100         # 방문여부
    visited[0] = True
    stack = [0]                     # 최근 방문한 노드
    node1 = [0] * 100               # 각 노드의 첫 번째 갈림길
    node2 = [0] * 100               # 각 노드의 두 번째 갈림길
    # point = 0                       # 현재 노드

    # 인접노드배열 저장 -> 0 1 0 2 1 4.. = (0,1) (0,2) (1,4) = 0번 노드는 1, 2번 노드와 연결
    # 홀수번호 인덱스에 짝수번호 값 입력
    for i in range(0, len(arr), 2):  # 0,2,4,6.. arr의 홀수번째인덱스 순회
        if node1[arr[i]] == 0:            # 비어있으면
            node1[arr[i]] = arr[i+1]
        else:
            node2[arr[i]] = arr[i+1]

    # 길 찾기
    # 노드배열로 연결된 길을 dfs하다 어떤 인덱스의 값이 99면 1출력
    # 끝까지 돌아도 99를 못만나면 0출력
    def dfs(n):                 # 0, 1
        if n == 99:
            return 1
        visited[n] = True       # 0번노드 방문

        # 튜플로 묶어서 반복 돌리기(new!)  <- 순차적으로 뽑아서 반복함
        for next_node in (node1[n], node2[n]):              # n이 0일때 1, 2 -> next_node =1후 =2로
            if next_node != 0 and not visited[next_node]:   # 연결노드 있고(0아님), 그 노드 방문 안했을때(not)
                if dfs(next_node) == 1:                     # 우선 1 보내서 재귀, 쭉돌리다가 n==99돼서 1리턴오면
                    return 1                                # 1 리턴
        return 0                                            # 반복 끝나도 1 안되면 걍 0 리턴

        # 무한재귀(RecursionError)걸린 내 노력들..
        # if stack and stack[-1] != n:      # stack이 비어있지 않고 최근값이 n과 다르면
        #     stack.append(n)               # 방문록작성 : 1번(1번없으면)
        #     if node1[n] != 0 and visited[node1[n]] is False:
        #         dfs(node1[n])             # 4 보내
        #     elif node2[n] != 0 and visited[node2[n]] is False:
        #         dfs(node2[n])
        #     else:
        #         stack.pop()
        #         dfs(stack[-1])
        # elif stack and stack[-1] == n:    # stack이 비어있지 않고 최근값이 n이면(복귀)
        #     if node2[n] != 0 and visited[node2[n]] is False:
        #         dfs(node1[n])
        #     else:
        #         stack.pop()
        #         if stack:
        #             dfs(stack[-1])
        #         elif stack == [] and visited[99] is False:
        #             print(f'#{tc} 0')

    result = dfs(0)         # 0번노드부터
    print(f'#{tc} {result}')