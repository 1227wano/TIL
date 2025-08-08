T = int(input())
for test in range(1, T + 1):
    word = input()      # bdppq
    le = len(word)      # 글자수 5

    mirror = [''] * le
    for i in range(le):
        if word[i] == 'b':
            mirror[le-i-1] = 'd'
        elif word[i] == 'd':
            mirror[le-i-1] = 'b'
        elif word[i] == 'p':
            mirror[le-i-1] = 'q'
        else:
            mirror[le-i-1] = 'p'

    last = ''
    for j in mirror:
        last += j
    print(f'#{test} {last}')