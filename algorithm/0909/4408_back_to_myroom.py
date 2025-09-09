T = int(input())
for T in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    time = 0                    # 기본 한시간
    visited = [False] * N        # 그 동선 통과 여부
    cnt = N                      # 학생수만큼 이동하고 종료

    arr = sorted(arr, key=lambda x: (x[0], x[1]))   # (시작시간이 같다면 종료시간으로 정렬)

    while cnt > 0:
        end_room = 0            # 마지막 방문방
        for i in range(N):
            s, e = arr[i][0], arr[i][1]     # s = start_time, e = end_time
            if not visited[i]:
                if end_room % 2 == 0 and s > end_room and end_room < e:
                    if s < e:
                        end_room = e
                    else:
                        end_room = s
                elif end_room % 2 == 1 and s > end_room+1 and end_room < e:
                    if s < e:
                        end_room = e
                    else:
                        end_room = s
                visited[i] = True
                cnt -= 1
        time += 1


    print(f'#{T} {time}')