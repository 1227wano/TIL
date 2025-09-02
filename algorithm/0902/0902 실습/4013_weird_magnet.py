from collections import deque
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for T in range(1, T+1):
    K = int(input())
    # mag = [list(map(int, input().split())) for _ in range(4)]
    mag_one = deque(list(map(int, input().split())))
    mag_two = deque(list(map(int, input().split())))
    mag_three = deque(list(map(int, input().split())))
    mag_four = deque(list(map(int, input().split())))

    moves = [list(map(int, input().split())) for _ in range(K)]

    for move in moves:
        to_visit = []
        to_visit.append(move)
        visited = [False for _ in range(5)]
        visited[move[0]] = True

        while to_visit:
            now, dir = to_visit.pop(0)

            left = now - 1
            right = now + 1

    total_score = 0
    score = 1
    for i in range(1, 5):
        total_score += score * mag[i][0]
        score *= 2

    print(f'#{T} {total_score}')