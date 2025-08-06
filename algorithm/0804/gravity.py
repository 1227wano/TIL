T = int(input())
for test in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))
    maxi = 0
    for i in range(N):
        same_box = 0
        for j in range(i+1, N):
            if a[j] >= a[i]:
                same_box += 1
        fall = (N - i - 1) - same_box   # 낙차=(전체길이-현재인덱스-인덱스니까1)-오른쪽동위치박스
        if maxi < fall:
            maxi = fall
    print(f'#{test}', maxi)
