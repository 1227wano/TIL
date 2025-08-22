def in_order(n):
    if n < N+1:
        in_order(n*2)    # 왼쪽 끝까지 이동
        global result
        result += words[n]
        in_order(n*2+1)    # 오른쪽으로 이동

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    result = ''     # 최종 출력

    words = [0] * (N+1)     # 글자들 넣어갈 리스트

    for i in range(N):
        node, word = int(arr[i][0]), arr[i][1]
        words[node] = word  # 몇번 노드에 무슨 글자가

    in_order(1)
    print(f'#{tc} {result}')