T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())        # NxN(20)의 문자배열 중에서 M(13)길이의 회문 찾기
    words = [list(input()) for _ in range(N)]   # 2차원 문자열 배열, 문자열은 split() 하지말자

    word = ''       # 회문확인용
    # 가로 회문 확인
    for i in range(N):                  # 세로줄 돌아 -> 20번 반복
        for j in range(N-M+1):          # 가로줄 돌아 -> 20-13 = 7번 반복
            for k in range(M):          # 회문체크할 길이만큼 단어 뽑아
                word = words[i][j+k]
            print(word)
            result = 0
            # 가로로 뽑은 문자열 회문 체크
            for a in range(M // 2):
                if word[a] == word[M-a-1]:  # 글자의 양끝 비교
                    result = 1
                    continue
                elif word[a] != word[M-a-1]:
                    result = 0
                    break
            if result == 1:
                print(f'#{test} {word}')
            else:
                break

    word = ''  # 회문확인용
    # 세로 회문 확인
    for i in range(N):              # 세로줄 돌아 -> 20번 반복
        for j in range(N-M+1):      # 가로줄 돌아 -> 20-13 = 7번 반복
            for k in range(M):      # 회문체크할 길이만큼 단어 뽑아
                word = words[j+k][i]
            result = 0
            # 세로로 뽑은 문자열 회문 체크
            for a in range(M // 2):
                if word[a] == word[M-a-1]:  # 글자의 양끝 비교
                    result = 1
                    continue
                elif word[a] != word[M-a-1]:
                    result = 0
                    break
            if result == 1:
                print(f'#{test} {word}')
            else:
                break

