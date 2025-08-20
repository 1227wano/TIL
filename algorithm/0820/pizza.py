from collections import deque

T = int(input())
for T in range(1, T+1):
    N, M = map(int, input().split())    # 화덕크기, 피자개수
    arr = list(map(int, input().split()))   # 각 피자의 치즈양 [7 2 6 5 3]
    result = 0

    fire = [0] * N      # 화덕
    out = [0] * M-N     # 남은애들

    rotate = True
    cnt = M-1           # 피자 하나남을때까지 카운트
    done = [0] * N      # 피자 방명록

    while rotate:
        for i in range(N):      # 화덕에 피자넣기  [7,2,6]
            fire[i] = arr[i]
        for j in range(M-N):    # 남은애들 [5,3]
            out[j] = arr[N+j]

        cq = deque(fire)        # 돌려돌려 화덕
        q = deque(out)

        if cnt == 0:            # 화덕에 하나 남았으면
            for x in range(N):
                if cq[x] != 0:
                    result = i
            rotate = False
        a = cq.popleft()                # a=7, arr = [2,6]
        if a == 0 and q:                # a가 0이고, q에 피자 남았으면
            cq.append(q.popleft())      # 남은거에서 빼서 넣어
        else:
            cq.append(a//2)     # [2,6,3]

