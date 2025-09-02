# 암호 인식 메서드
def password(s):
    if s == '0001101':
        return 0
    elif s == '0011001':
        return 1
    elif s == '0010011':
        return 2
    elif s == '0111101':
        return 3
    elif s == '0100011':
        return 4
    elif s == '0110001':
        return 5
    elif s == '0101111':
        return 6
    elif s == '0111011':
        return 7
    elif s == '0110111':
        return 8
    elif s == '0001011':
        return 9

T = int(input())
for C in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input().strip()) for _ in range(N)]

    # 역순으로 탐색해서 암호부터 뽑아내
    a = b = 0   # 암호뭉탱이 꼭지점
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                a = i
                b = j
                break
    b -= 55     # 꼭지점에서 출발점으로

    li = []    # 암호코드 담아
    st = ''
    for x in range(56):     # 가로길이만큼
        st += arr[a][b+x]
        if len(st) == 7:
            li.append(password(st))
            st = ''

    result = ((li[0]+li[2]+li[4]+li[6])*3) + (li[1]+li[3]+li[5]+li[7])
    if result % 10 == 0:
        result = (li[0]+li[2]+li[4]+li[6]+li[1]+li[3]+li[5]+li[7])
        print(f'#{C} {result}')
    else:
        print(f'#{C} 0')