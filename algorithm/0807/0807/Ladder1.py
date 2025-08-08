for test in range(1, 11):
    T = int(input())
    N = 100
    lad = [list(map(int, input().split())) for _ in range(N)]
    goal = 0   # 출발점의 x좌표

    # 1. y=0 중에서 lad[x][y]가 1인 출발점들 선택해서 반복
    # 1-1. y=0인 행을 range(100) 돌려서 출발점(1인) departure에 넣어
    # 2. departure 반복 돌려서 그 안에 while y != 99 반복
    # 2-2. delta로 [0,1],[0,-1](좌우)가 0이라면 [1,0](아래)로 이동
    # 3. lad[x][y]가 2면 goal에 x 담아

    # 1
    departure = []      # 출발점리스트
    for i in range(N):
        if lad[0][i] == 1:
            departure.append(i)     # [2, 13, 33] 이런식으로 출발점 x좌표리스트?

    # 2

    for a in departure:
        x = a                   # a를 직접 수정해나가는거보다 x에 담아서 조작이 안정적
        y = 0
        d = 0                   # 방향 0=아래, 1=좌, 2=우
        while y != N-1:         # [0, 1], [0, -1](좌우)가 0이라면[1, 0](아래)로 이동

            # 좌우 이동 먼저 확인
            if x > 0 and lad[y][x - 1] == 1 and d != 2:  # 왼쪽에 길이 있고 이전 방향이 오른쪽이 아닐 때
                x -= 1
                d = 1
            elif x < N - 1 and lad[y][x + 1] == 1 and d != 1:  # 오른쪽에 길이 있고 이전 방향이 왼쪽이 아닐 때
                x += 1
                d = 2
            else:  # 아래로 내려감
                y += 1
                d = 0

        if lad[y][x] == 2:
            goal = a

    print(f'#{test} {goal}')