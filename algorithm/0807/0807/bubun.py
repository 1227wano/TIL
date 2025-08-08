T = int(input())
for test in range(1, T + 1):
    arr = list(map(int, input().split()))

    n = len(arr)        # [7 7 19 1 -18 5 -9 -11 19 18]
    power_set = []      #

    for i in range(1 << n):         # 부분집합수만큼 반복
        subset = []                 # ON 된 arr[j]들을 넣을 부분합수집합
        for j in range(n):          # list 원소의 수만큼 비트를 비교함
            if i & (1 << j):        # ex) i=1,j=0 -> i&(1<<j) = 001&001 동일?
                subset.append(arr[j])   # => arr[j] ON 포함시켜
        if sum(subset) == 0 and subset != []:
            power_set.append(subset)

    if power_set:
        print(f'#{test} 1')
    else:
        print(f'#{test} 0')