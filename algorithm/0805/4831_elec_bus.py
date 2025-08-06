T = int(input())
for test in range(1, T + 1):
    # K = 거리 N = 길이 M = 충전기수
    K, N, M = map(int, input().split())         # 3 10 5
    stop = list(map(int, input().split()))      # 1 3 5 7 9
    result = 0
    bat = K     # 버스배터리

    if stop[0] > K:  # 첫번째 정류장이 거리보다 멀거나 배터리 없음 펑크
        print(f'#{test} 0')
        continue

    for i in range(M):       # 5번 충전기수로 반복 [1 3 5 7 9]
        if i > 0 and stop[i] - stop[i - 1] > K:  # 충전소간이 거리보다 길면 펑크
            result = 0
            break

        if i == 0:          # 첫번째 정류장
            bat -= stop[i]    # 지나온 거리만큼 배터리 삭제
            if stop[i+1] - stop[i] > bat:   # 다음충전소까지거리가 배터리잔량보다 크면 충전
                bat = K
                result += 1

        elif i < M-1:          # 두번째부터 마지막전 정류장
            bat -= (stop[i] - stop[i-1])     # 지나온 거리만큼 배터리 삭제
            if stop[i+1] - stop[i] > K:  # 다음충전소까지 가동거리보다 길면 펑크
                result = 0
                break
            elif stop[i+1] - stop[i] > bat:    # 다음충전소까지거리가 배터리잔량보다 크면 충전
                bat = K
                result += 1

        elif i == M-1:          # 마지막 정류장
            bat -= (stop[i] - stop[i - 1])  # 지나온 거리만큼 배터리 삭제
            if N - stop[i] > K:  # 다음충전소까지 가동거리보다 길면 펑크
                result = 0
                break
            elif N - stop[i] > bat:           # 마지막 정류장은 남은거리보다 잔량이 크면 충전
                bat = K
                result += 1

    print(f'#{test} {result}')

    # if stop[0] > K:  첫번째 정류장이 거리보다 멀거나 배터리 없음 펑크
    # 이 부분을 반복문 안에 넣어서 불필요한 반복이 돌아가서 두 개의 히든테케에서 오류 뜸
    # To-do 1. 통과거리만큼 배터리 삭제 2. 충전여부 3. 펑크요건확인