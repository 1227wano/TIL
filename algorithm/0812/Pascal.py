T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cnt = 0

    arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr[i][j] = 1
            if i == 0:
                break
            if j == 0:
                continue
            elif arr[i-1][j] == 0:
                break
            elif arr[i-1][j] != 0:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    # 숫자 -> 문자열로 출력형식 맞추기
    print(f'#{t}')
    for a in range(N):
        word = ''
        for b in range(N):
            if arr[a][b] != 0 and b == 0:
                word += str(arr[a][b])
            elif arr[a][b] != 0 and b > 0:
                word += ' ' + str(arr[a][b])
        print(word)