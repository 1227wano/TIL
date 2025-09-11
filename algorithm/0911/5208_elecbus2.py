def recur(n, cnt):

    if cnt > result:   # 충전횟수가 현 최저횟수를 넘으면 종료
        return

    if n == N:  # 도착하면 끝
        return

    for i in range()


T = int(input())
for x in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr.pop(0)  # 정류장수.
    # 이제 arr = 배터리 정보 arr[N-1]까지 가야함

    result = 0      # 총 충전횟수
    bat = arr[0]    # 시작 배터리 (2)
    cnt = 0

    # for i in range(N):
    #     if bat == 0:
    #         bat = arr[i]
    #         cnt += 1
    #     bat -= 1

    recur(0, 0)

    print(f'#{x} {cnt}')