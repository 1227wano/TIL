T = 10
for test in range(1, T + 1):
    N = int(input())    # 건물개수
    li = list(map(int, input().split()))    # 건물높이들
    count = 0
    for i in range(2, N-2):
        maxi = 0                # 현재건물기준 5범위내에서 젤높은거
        for j in range(-2, 3):
            if li[i+j] > maxi:
                maxi = li[i+j]

        if li[i] == maxi:       # 내가젤높으니까 이제 다른거랑 비교할거야
            dif = 0             # 각 건물과의 고차
            min_dif = li[i]     # 젤 차이 적은 고차
            for a in range(-2, 3):
                if a == 0:
                    continue
                dif = li[i] - li[i+a]
                if dif < min_dif:
                    min_dif = dif
            count += min_dif

    print(f'#{test}', count)