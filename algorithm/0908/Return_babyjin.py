def run_check(li):          # 리스트 받아서 '연속수' 잇나 확인
    for a in li:            # [5,2,1,2,9,0]
        if a == 0:
            if 1 in li and 2 in li:
                return True
        elif 0 < a < 9:
            if (a-1) in li and (a+1) in li:
                return True
        elif a == len(li):
            if (a-2) in li and (a-1) in li:
                return True
        else:
            continue
    return False


def tri_check(li):      # 리스트 받아서 '동일수' 잇나 확인
    for a in li:
        if li.count(a) >= 3:
            return True
        else:
            continue
    return False


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    fst = arr[0:len(arr)-1:2]   # [5,2,1,2,9,0]
    sec = arr[1:len(arr):2]     # [3,9,5,0,2,0]

    result = 0
    turn = 1
    for i in range(4, 7):
        if run_check(fst[:i]):
            result = 1
            break
        elif tri_check(fst[:i]):
            result = 1
            break
        elif run_check(sec[:i]):
            result = 2
            break
        elif tri_check(sec[:i]):
            result = 2
            break

    print(f'#{tc} {result}')