T = int(input())
for x in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxi = 0
    rich = 0

    for i in range(N-1, -1, -1):
        if maxi > arr[i]:
            rich += maxi - arr[i]
        elif maxi <= arr[i]:
            maxi = arr[i]

    print(f'#{x} {rich}')