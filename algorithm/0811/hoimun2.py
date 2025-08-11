T = 10
for test in range(1, T + 1):
    N = int(input())
    words = [list(input()) for _ in range(100)]
    maxi = 0

    for i in range(100):
        for j in range(100):

            # 가로 회문
            if 0 <= j <= 97:    # 97인 이유는 회문 최소 길이가 3이어서 97,98,99인덱스로 가능하기때문
                for a in range(3, 101-j):       # 따라서 회문최소길이인 3부터 반복
                    word = ''.join(words[i][j:j+a])     # 3~한계까지 글자를 join으로 단어에 대입
                    if word == word[::-1] and a > maxi:     # 회문체크일때 그 범위(a)가 maxi보다 크면
                        maxi = a

            # 세로 회문
            if 0 <= i <= 97:
                for b in range(3, 101-i):
                    word = ''.join(words[i+d][j] for d in range(b))     # 세로는 슬라이싱이 안되니까
                    if word == word[::-1] and b > maxi:
                        maxi = b

    print(f'#{N} {maxi}')