T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    W_arr = list(map(int, input().split()))     # N개의 화물 무게
    T_arr = list(map(int, input().split()))     # M대의 트럭 적재가능양
    # 10 12
    # 10 13 14 6 19 11 5 20 11 14
    # 5 18 17 8 9 17 18 4 1 16 15 13

    result = 0
    W_arr.sort(reverse=True)
    T_arr.sort(reverse=True)
    nj = 0  # 탐색 인덱스 저장
    end = 0

    for i in range(M):
        if end == N-1:          # 종료조건
            break
        for j in range(nj, N):
            if T_arr[i] >= W_arr[j]:
                result += W_arr[j]
                nj = j+1
                if j == N-1:    # 마지막 컨테이너 운반했으면 종료
                    end = j
                break


    print(f'#{tc} {result}')