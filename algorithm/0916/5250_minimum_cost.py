import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for T in range(1, T+1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]

    cnt = (N-2)*2   # 초기값: 기본 이동 수







    print(f'#{T} {cnt}')