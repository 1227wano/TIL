import sys
sys.stdin = open("input.txt")


def d_c(li, n, direction):
    a = (len(li) - 1) // 2      # mid는 (시작 + 끝 인덱스) // 2 가 인덱스
    mid = li[a]

    # 타겟넘버 넘으면 종료
    if n == mid:
        return 1

    # 리스트 길이가 1인데 mid아니면 탐색불가
    if len(li) <= 1:
        return 0

    # 왼쪽 탐색
    if n < mid:
        # 이전에 왼쪽으로 갔는데 또 왼쪽으로 가면 실패
        if direction == 'left':
            return 0
        left = li[:a]
        # 다음 방향을 'left'로 지정하여 재귀 호출
        return d_c(left, n, 'left')

    # 오른쪽 탐색
    elif n > mid:
        # 이전에 오른쪽으로 갔는데 또 오른쪽으로 가면 실패
        if direction == 'right':
            return 0
        right = li[a+1:]
        # 다음 방향을 'right'로 지정하여 재귀 호출
        return d_c(right, n, 'right')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr_a = sorted(list(map(int, input().split())))     # 이진 탐색을 위해 A 배열은 정렬
    arr_b = list(map(int, input().split()))

    cnt = 0

    for i in arr_b:
        if i not in arr_a:
            continue

        c = d_c(arr_a, i, 'none')

        if c == 1:
            cnt += 1

    print(f'#{tc} {cnt}')