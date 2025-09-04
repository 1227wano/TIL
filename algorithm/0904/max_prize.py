def where_is_maxi(n):  # 탐색 시작할 인덱스 받아 처음은 0
    # n부터 리스트 끝까지 가장 큰 숫자가 무엇인지 찾음
    max_num = max(li[n:])

    # 만약 n번째 위치의 숫자가 이미 최대값이면, 바꿀 필요가 없으므로
    # 현재 위치인 n을 그대로 반환해서 아무것도 안 하도록 신호를 줌
    if li[n] == max_num:
        return n

    # 만약 최대값이 여러 개 있으면 가장 뒤(오른쪽)에 있는 것과 바꿔야 유리함
    # 따라서 리스트를 뒤에서부터 거꾸로 탐색
    for i in range(len(li)-1, n-1, -1):
        if li[i] == max_num:
            return i  # 최대값의 '절대 인덱스'를 찾으면 바로 반환


# def what_can_change(y):
#     if y == 0:
#         return -1
#
#     min_num = min(li[y:-1:-1])
#     return li[y:-1:-1].index(min_num)


T = int(input())
for C in range(1, T+1):
    word, count = input().split()

    # 카드리스트와 교환횟수 저장
    li = list(word)
    cnt = int(count)

    ni = 0          # 현재 인덱스

    while cnt > 0 and ni < len(li):
        maxi = where_is_maxi(ni)  # 최대값 인덱스

        # where_is_maxi의 결과가 현재 위치(ni)와 다르다면 교환이 필요함
        if maxi != ni:
            li[ni], li[maxi] = li[maxi], li[ni]
            cnt -= 1

        # 다음 위치를 확인하러 이동
        ni += 1

        # 최적화가 끝난 후에도 교환 횟수(cnt)가 남았을 경우 처리
        # 중복된 숫자가 있는지 확인
        check = len(set(li)) < len(li)

        # 남은 횟수가 홀수이고, 중복된 숫자가 없다면
        if cnt % 2 == 1 and not check:
            # 가장 손해가 적은 마지막 두 숫자를 교환
            li[-1], li[-2] = li[-2], li[-1]

    result = "".join(li)
    print(f'#{C} {result}')
