def pre_order(node):
    if node:    # N(루트)가 0이 아니면
        global cnt
        cnt += 1
        pre_order(left[node])
        pre_order(right[node])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())        # E = 간선의 개수, N = 루트
    arr = list(map(int, input().split()))   # 부모자식 쌍   (2 1 2 5 1 6 5 3 6 4)
    cnt = 0

    # 노드 번호는 1번부터 E+1번 까지
    par = [0] * (E+2)         # 자식을 인덱스로 부모 저장
    left = [0] * (E+2)        # 부모를 인덱스로 왼쪽자식 저장
    right = [0] * (E+2)       # 부모를 인덱스로 오른쪽자식 저장

    # arr로 부모자식 만들어 이진트리니까 두개야
    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        par[c] = p
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    pre_order(N)

    print(f'#{tc} {cnt}')