def merge(left, right):
    global cnt
    result = [0] * (len(left) + len(right))
    l = r = 0       # 인덱스 비교용

    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            result[l+r] = right[r]
            r += 1
        else:
            result[l+r] = left[l]
            l += 1
        if r == len(right):     # 오른쪽이 먼저 다 가면 카운트
            cnt += 1

    while l < len(left):
        result[l+r] = left[l]
        l += 1

    while r < len(right):
        result[l+r] = right[r]
        r += 1

    return result


def d_c(li):
    if len(li) == 1:
        return li

    # 1. 반으로 분할
    mid = len(li)//2
    left = li[:mid]
    right = li[mid:]

    # 2. 1개로 분할될때까지 재귀
    left_li = d_c(left)
    right_li = d_c(right)

    # 3. 분할완료 -> 병합
    merged_li = merge(left_li, right_li)
    return merged_li    # 최종 병합리스트 전까진 2번으로 감


T = int(input())
for T in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    lis = d_c(arr)
    r = lis[(N//2)]

    print(f'#{T} {r} {cnt}')