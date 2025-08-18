T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split('+')))
    result = 0

    for i in range(len(arr)):
        result += arr[i]

    print(f'#{tc} {result}')