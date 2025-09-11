def partition(left, right):     # 피벗 맨 왼쪽
    pivot = arr[left]
    i = left + 1        # (맨왼쪽피벗)의 바로 왼쪽
    j = right           # 오른쪽 끝

    while i <= j:   # i가 j보다 왼쪽에 있는 동안
        while i <= j and arr[i] <= pivot:   # i번째 수가 pivot보다 작은 동안
            i += 1

        while i <= j and arr[j] >= pivot:  # i번째 수가 pivot보다 큰 동안
            j -= 1

        if i < j:   # i가 j보다 왼쪽에 있을 동안 계속 교체
            arr[i], arr[j] = arr[j], arr[i]

    # 마지막에 pivot과 j위치 교체
    arr[left], arr[j] = arr[j], arr[left]
    return j    # 피벗 위치만 리턴(그 좌우 배열은 정렬안된상태)


def quick(left, right):
    if left < right:
        pivot = partition(left, right)
        quick(left, pivot-1)
        quick(pivot+1, right)


T = int(input())
for T in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick(0, len(arr)-1)
    r = N//2
    print(f'#{T} {arr[r]}')