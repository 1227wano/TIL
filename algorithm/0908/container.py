T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    W_arr = list(map(int, input().split()))     # N개의 화물 무게
    T_arr = list(map(int, input().split()))     # M대의 트럭 적재가능양
    # 3 2
    # 1 5 3
    # 8 3

    result = 0
    W_arr.sort()    # 5 3 1
    T_arr.sort()    # 8 3

    count = abs(len(W_arr) - len(T_arr))

    for i in range(count):
        if T_arr[i] >= W_arr[i]:
            result += W_arr[i]

    print(f'#{tc} {result}')