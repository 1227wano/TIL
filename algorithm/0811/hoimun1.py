T = 10
for test in range(1, T + 1):
    N = int(input())            # 회문길이
    words = [list(input()) for _ in range(8)]
    cnt = 0

    for i in range(8):
        for j in range(8):

            if 0 <= j <= 8-N:
                word = ''
                for a in range(N):
                    word += words[i][j + a]
                rev = word[::-1]
                if word == rev:
                    cnt += 1

            if 0 <= i <= 8-N:
                word = ''
                for b in range(N):
                    word += words[i + b][j]
                rev = word[::-1]
                if word == rev:
                    cnt += 1

    print(f'#{test} {cnt}')