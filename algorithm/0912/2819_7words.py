import sys
sys.stdin = open("input.txt")

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def recur(y, x, number):
    if len(number) == 7:
        result.add(number)      # set이라 중복 제외하며 들어감
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # 범위 밖이면
        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue

        # 다음 위치로 이동
        recur(ny, nx, number+arr[ny][nx])   # 현재 숫자도 같이


T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]     # 숫자들을 문자처럼 더해야함
    result = set()

    for sy in range(4):
        for sx in range(4):
            recur(sy, sx, arr[sy][sx])

    print(f'#{tc} {len(result)}')   # set에 들어간 7자리수의 개수