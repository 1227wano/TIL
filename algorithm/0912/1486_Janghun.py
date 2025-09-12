import sys
sys.stdin = open("input.txt")


def recur(idx, total_height):
    global mini

    if total_height >= B:
        mini = min(mini, total_height)
        return

    if idx == N:
        return

    recur(idx+1, total_height+heights[idx])     # 탑에 점원 포함
    recur(idx+1, total_height)                  # 탑에 점원 미포함


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())

    heights = list(map(int, input().split()))
    mini = 10000 * N
    recur(0, 0)
    print(f'#{tc} {mini - B}')