T = int(input())
for test in range(1, T + 1):
    N = int(input())    # 5
    a = int(input())    # 49679
    c = [0] * 10

    # 숫자리스트에 각 숫자 담기
    for i in range(N):
        c[a % 10] += 1
        a //= 10

    # 숫자리스트 순회하며 최대 뽑기
    high = 0    # high count
    maxi = 0    # max idx
    for j in range(10):
        if c[j] > high:
            high = c[j]
            maxi = j
        elif c[j] == high:  # 카드 장수 동일시
            maxi = j        # 큰 숫자 카드로 갱신

    print(f'#{test}', maxi, high)