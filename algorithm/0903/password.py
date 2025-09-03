import sys
sys.stdin = open("sample_input.txt", "r")


# 암호 인식 메서드
def password(s, bi):
    patterns = {
        '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
    }

    # 입력된 s를 비율(bi)에 따라 패턴찾기
    normal = ''
    i = 0
    while i < len(s):
        normal += s[i]
        i += bi

    return patterns.get(normal, -1)   # 암호아니면 -1


def next_pass(n):
    global last_pass
    for i in range(n, N):
        for j in range(M):
            if arr[i][j] != '0':
                return i, j
    return -1, -1


def is_pass(a, b):

    # 위치 전달받아 16진수 블록의 시작과 끝 찾기
    stb = b
    while stb > 0 and arr[a][stb-1] != '0':
        stb -= 1
    eb = stb
    word = ''
    while eb < M and arr[a][eb] != '0':
        word += arr[a][eb]
        eb += 1

    def del_block():
        for i in range(a, N):  # 암호는 여러 줄에 걸쳐 같은 모양일 수 있으므로 아래 줄도 지웁니다.
            zero = True
            for j in range(stb, eb):
                if arr[i][j] != arr[a][j]:
                    zero = False
                    break
            if zero:
                for j in range(stb, eb):
                    arr[i][j] = '0'
            else:
                break

    del_block()

    if not word:
        return None

    # 2진수로
    two = bin(int(word, 16))[2:].zfill(len(word) * 4)
    two = two.rstrip('0')

    # 마지막 0빼기
    while two and two[-1] == '0':
        two = two[:-1]

    if not two:
        del_block()
        return None

    # 앞 0빼기
    if len(two) % 56 != 0:
        del_block()
        return None

    # 비율을 몇배로 볼까나
    bi = len(two) // 56
    if bi == 0:
        del_block()
        return None

    li = []
    st = ''
    for x in two:  # 가로길이만큼
        st += x
        if len(st) == (7 * bi):
            pass_num = password(st, bi)
            if pass_num == -1:
                del_block()
                return None
            li.append(pass_num)
            st = ''

    result = ((li[0] + li[2] + li[4] + li[6]) * 3) + (li[1] + li[3] + li[5]) + li[7]

    del_block()     #  처리한 블록 지우기

    if result % 10 == 0:
        return li
    else:
        return None


# T = 1
T = int(input())
for C in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input().strip()) for _ in range(N)]

    code = set()    # 처리한 암호 저장
    final = 0   # 유효한 암호의 총합을 더해가는 변수
    a = 0       # next_pass 에 보낼용

    while True:
        sa, sb = next_pass(a)

        if sa == -1:
            break

        ans = is_pass(sa, sb)

        if ans:
            # 중복된 암호인지 확인
            code_tuple = tuple(ans)
            if code_tuple not in code:
                final += sum(ans)
                code.add(code_tuple)

        a = sa

    print(f'#{C} {final}')