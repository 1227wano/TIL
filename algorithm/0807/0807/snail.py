T = int(input())
for test in range(1, T + 1):
    N = int(input())

    # 달팽이가 가는 빈 배열
    result = [[0 for _ in range(N)] for _ in range(N)]

    # 진행방향의 순서(우하좌상)가 반영되도록 만드는 델타
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 숫자를 적을 위치를 정하는 변수를 설정
    now_i = 0
    # 이동하고 숫자를 적을 것이므로 -1 시작
    now_j = -1
    # 현재 진행방향을 기록, 벽을 만날때마다 1씩 커지며, N 이상이 되면 0으로
    d = 0
    # N * N 반복하면서 그 숫자를 넣기
    for n in range(1, N * N + 1):
        # 진행방향으로 이동
        now_i += di[d]
        now_j += dj[d]

        # 현재 위치에 숫자를 넣어준다
        result[now_i][now_j] = n

        # 다음 진행할 곳이 막혀있는지 확인
        if not (
            # 다음 진행할 인덱스가 범위내인지
            0 <= now_i + di[d] < N and
            0 <= now_j + dj[d] < N and
            # 해당 위치에 숫자가 적혀있는지
            result[now_i + di[d]][now_j + dj[d]] == 0
        ):
            # 막혀있다면 진행 방향을 바꿔주기
            d = (d + 1) % 4
        # 결과 출력
        for row in result:
            print(test, ' '.join(map(str, row)))