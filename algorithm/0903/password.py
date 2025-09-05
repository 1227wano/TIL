import sys
sys.stdin = open("../../TIL/algorithm/0903/sample_input.txt", "r")


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

    found_codes = []
    p = len(two)  # 탐색 위치를 가리키는 포인터 (오른쪽 끝에서 시작)

    while p >= 56:          # 최소 암호 길이(56)보다 길 때만 탐색
        sub_two = two[:p]   # 현재 포인터까지의 부분 문자열

        # 부분 문자열의 끝부분 패턴을 분석해 비율(bi)을 찾습니다.
        p_temp = len(sub_two) - 1
        c1, c2, c3 = 0, 0, 0  # 1의 개수, 0의 개수, 1의 개수
        while p_temp >= 0 and sub_two[p_temp] == '1':
            c1 += 1
            p_temp -= 1
        while p_temp >= 0 and sub_two[p_temp] == '0':
            c2 += 1
            p_temp -= 1
        while p_temp >= 0 and sub_two[p_temp] == '1':
            c3 += 1
            p_temp -= 1

        if c1 == 0 or c2 == 0 or c3 == 0:
            p -= 1      # 유효한 패턴이 아니면 포인터를 한 칸 왼쪽으로 옮겨 다시 탐색
            continue

        bi = min(c1, c2, c3)

        # 찾은 비율(bi)을 바탕으로 56*bi 길이의 암호 후보를 추출합니다.
        expected_len = 56 * bi
        if len(sub_two) < expected_len:
            p -= 1
            continue
        candidate = sub_two[-expected_len:]

        # 암호 후보를 해독하고 검증합니다.
        li = []
        is_valid_candidate = True
        for i in range(8):
            digit_bin = candidate[i * 7 * bi:(i + 1) * 7 * bi]
            pass_num = password(digit_bin, bi)
            if pass_num == -1:
                is_valid_candidate = False
                break
            li.append(pass_num)

        if not is_valid_candidate:
            p -= 1                      # 해독 실패 시 포인터를 한 칸 이동
            continue

        result = ((li[0] + li[2] + li[4] + li[6]) * 3) + (li[1] + li[3] + li[5]) + li[7]
        if result % 10 == 0:
            found_codes.append(tuple(li))
            p -= expected_len           # 성공 시, 찾은 암호 길이만큼 포인터를 이동
        else:
            p -= 1                      # 검증 실패 시 포인터를 한 칸 이동

    return found_codes if found_codes else None


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

        # 중복된 암호인지 확인
        if ans:
            for code_tuple in ans:
                if code_tuple not in code:
                    final += sum(code_tuple)
                    code.add(code_tuple)

        a = sa

    print(f'#{C} {final}')