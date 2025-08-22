def in_order(node, tree):
    global cnt
    if node < len(tree):
        in_order(node * 2, tree)    # 왼쪽 끝까지 이동
        tree[node] = cnt            # 현재 넣을 값 넣기
        cnt += 1
        in_order(node*2+1, tree)    # 오른쪽으로 이동

T = int(input())
for tc in range(1, T+1):
    N = int(input())     # 노드 개수
    tree = [0] * (N+1)   # 노드가 들어가는 빈 트리 생성
    cnt = 1              # 지금 몇번째 수를 넣어야 하는지

    in_order(1, tree)    # 노드 1부터

    print(f'#{tc} {tree[1]} {tree[N//2]}')