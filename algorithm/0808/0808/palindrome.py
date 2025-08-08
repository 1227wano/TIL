T = int(input())
for test in range(1, T + 1):
    word = input()      # level
    le = len(word)      # 글자수
    result = 0

    for j in range(le//2):   # 전체길이 / 2
        if word[j] == word[le-j-1]:   # level의 0번째(l)이랑 4번째(l) 비교
            result = 1
            continue
        elif word[j] != word[le-j-1]:
            result = 0
            break
    print(f'#{test} {result}')