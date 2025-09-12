import sys
sys.stdin = open("input.txt")

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N * N + 1)   # 1번 ~ N^2번 방 번호

    # 현 위치 기준 상하좌우 확인
    # 1 큰게 있으면 visited에 1 체크
    for y in range(N):
        for x in range(N):
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue

                if arr[ny][nx] == arr[y][x] + 1:
                    # 현재 숫자 다음으로 이동 가능
                    visited[arr[y][x]] = 1
                    break

    maxi = 0    # 최종 답
    cnt = 0     # 하나하나 마다 몇개가 연속되는지
    start = 0   # 숫자를 세기 시작한 위치

    for i in range(1, N*N+1):
        if visited[i] == 1:
            cnt += 1
        else:
            if maxi < cnt:
                maxi = cnt          # 최대값 갱신
                start = i - cnt     # 시작점 찾기
            cnt = 0

    print(f'#{tc} {start} {maxi+1}')