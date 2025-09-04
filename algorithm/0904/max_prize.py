def where_is_maxi(n):  # 탐색 시작할 인덱스 받아 처음은 0
    if n >= len(li):
        return

    max_num = max(li[n:])       # 제일 큰 숫자 머야
    if max_num == li[n]:        # 근데 탐색한 범위의 첫번째 인덱스야?
        where_is_maxi(n+1)      # 다음 인덱스부터 다시
    else:
        max_index = li[n:].index(max_num)
        # 반복돌려서 max_index 뒤에 같은 값 없나 확인
        return max_index


def what_can_change(y):
    min_num = min(li[y:0:-1])
    return li[y:0:-1].index(min_num)


T = int(input())
for C in range(1, T+1):
    word = input().split()

    # 카드리스트와 교환횟수 저장
    li = []
    for i in word[0]:
        li.append(i)
    cnt = int(word[1])

    result = 0      # 최종 출력 숫자
    ni = 0          # 맥시 탐색 인덱스

    a = 0
    while cnt != 0:
        maxi = where_is_maxi(ni)  # 최대값 인덱스
        min_index = what_can_change(maxi)   # 최대값인덱스 보낼테니까 내 앞에있는 최소값 인덱스 내놔
        if li[min_index] < li[maxi]:
            li[min_index], li[maxi] = li[maxi], li[min_index]
            a = min_index
        else:
            li[min_index], li[maxi] = li[maxi], li[min_index]
            a = min_index
        cnt -= 1

    result = int("".join(map(str, li)))
    print(f'#{C} {result}')
