T = 10
for tc in range(1, T+1):
    N = int(input())
    words = list(input().strip())
    result = 0

    # strip -> 9, +, 5, *, 3, *, 2, ...
    # * 만나면 앞뒤 곱해서 *의 뒤칸에 재할당(다음도 곱하기 일수도니까), 나머진 0으로
    # + 빼고 다 더하기

    for i in range(1, N-1):
        if words[i] == '*':
            words[i+1] = int(words[i-1]) * int(words[i+1])
            words[i-1] = 0
            words[i] = 0

    for j in range(N):
        if words[j] == '+':
            words[j] = 0

    for k in words:
        result += int(k)

    print(f'#{tc} {result}')