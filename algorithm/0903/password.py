import sys
sys.stdin = open("sample_input.txt", "r")


# 암호 인식 메서드
def password(s, bi):
    if s == '000'*bi+'11'*bi+'0'*bi+'1'*bi:
        return 0
    elif s == '00'*bi+'11'*bi+'00'*bi+'1'*bi:
        return 1
    elif s == '00'*bi+'1'*bi+'00'*bi+'11'*bi:
        return 2
    elif s == '0'*bi+'1111'*bi+'0'*bi+'1'*bi:
        return 3
    elif s == '0'*bi+'1'*bi+'000'*bi+'11'*bi:
        return 4
    elif s == '0'*bi+'11'*bi+'000'*bi+'1'*bi:
        return 5
    elif s == '0'*bi+'1'*bi+'0'*bi+'1111'*bi:
        return 6
    elif s == '0'*bi+'111'*bi+'0'*bi+'11'*bi:
        return 7
    elif s == '0'*bi+'11'*bi+'0'*bi+'111'*bi:
        return 8
    elif s == '000'*bi+'1'*bi+'0'*bi+'11'*bi:
        return 9
    else:
        return -1


def next_pass(n):
    global last_pass
    for i in range(n, N):
        for j in range(M):
            if arr[i][j] != '0' and arr[i][j:j+3] != last_pass:
                last_pass = arr[i][j:j+3]
                return i, j
    return -1, -1


def can_igo(q, w):
    for e in range(w, M):
        if arr[q][e] != '0':
            return True
        else:
            continue
    return False


def is_pass(a, b):
    word = ''  # 16진수 암호
    while True:
        if arr[a][b] == '0':
            if can_igo(a, b):
                word += arr[a][b]
            else:
                break
        else:
            word += arr[a][b]
        b += 1

    # 2진수로
    num = int(word, 16)
    two = bin(num)[2:].zfill(len(word) * 4)

    # 마지막 0빼기
    while True:
        if two[-1] == '0':
            two = two[:-1]
        else:
            break
    # 앞 0빼기
    while True:
        if len(two) % 56 != 0:
            two = two[1:]
        else:
            break

    # 비율을 몇배로 볼까나
    bi = len(two) // 56
    li = []
    st = ''
    for x in two:  # 가로길이만큼
        st += x
        if len(st) == (7 * bi):
            pass_num = password(st, bi)

            if pass_num == -1:
                return 0

            li.append(pass_num)
            st = ''

    if len(li) != 8:
        return 0

    result = ((li[0] + li[2] + li[4] + li[6]) * 3) + (li[1] + li[3] + li[5]) + li[7]
    if result % 10 == 0:
        result = sum(li)
        return result
    else:
        return 0


# T = 1
T = int(input())
for C in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input().strip()) for _ in range(N)]
    last_pass = ''

    code = set()    # 처리한 암호 저장
    final = 0   # 유효한 암호의 총합을 더해가는 변수
    a = 0       # next_pass 에 보낼용

    while True:
        sa, sb = next_pass(a)

        if sa == -1:
            break

        ans = is_pass(sa, sb)

        if ans == 0:
            a = sa + 1
            continue

        # 중복된 암호인지 확인
        code_tuple = tuple(ans)
        if code_tuple not in code:
            final += sum(ans)
            code.add(code_tuple)

        a = sa + 1

    print(f'#{C} {final}')