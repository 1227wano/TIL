# def next_time(n):
#     global count
#     if n+count >= len(sor):   # 다음 탐색 타임이 없어지면
#         return -1
#     close = sor[n][1]-1           # 이전 종료시간 (1,4)니까 3
#     if not time[close]:           # 처음용
#         return n
#     elif close <= sor[n+count][0]:      # 이전 종료시간이 다음 타임 시작시간 이전이면
#         return n+count                  # 다음 탐색 타임 i인덱스 리턴
#     else:                       # 그게 아니면 다음 타임 탐색
#         count += 1
#         return next_time(n)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1. 끝나는 시간 기준 오름차순
    # 2. 빠르게 끝나는 회의 선택후 확정
    # 3. 이후로 가능한 회의중 빠르게 끝나는 회의 선택확정 반복

    sor = sorted(arr, key=lambda x: (x[1], x[0]))   # (종료 시간이 같다면 시작 시간으로 정렬)

    cnt = 1
    last_end_time = sor[0][1]

    for i in range(1, N):
        current_start_time = sor[i][0]

        if current_start_time >= last_end_time:
            cnt += 1
            last_end_time = sor[i][1]  # 마지막 종료 시간 업데이트

    print(f'#{tc} {cnt}')

    # 나의 아름다운 흔적들
    # time = [False] * 25
    # cnt = 0     # 최종 이용 가능수
    # num = 0     # 첫 종료 타임
    # count = 1   # 탐색용
    #
    # while True:
    #     num = next_time(num)   # 탐색해서 확정할 타임 들고와
    #     if num == -1:           # 돌아온게 -1이면 탐색할거없음
    #         break
    #
    #     s, e = sor[num][0], sor[num][1]     # 타임의 시작시간과 끝시간(1~4)
    #
    #     for i in range(s, e):   # 타임 확정(1~3)
    #         time[i] = True
    #     cnt += 1
    #
    #     if num == len(sor)-1:   # N=1일 경우를 대비한 탈출 조건
    #         break