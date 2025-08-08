T = int(input())
for test in range(1, T + 1):
    N, le = input().split()
    case = input().split()

    # 2차원 숫자 배열 만들어서 각 숫자에 맞게 넣고 뽑을때 반복으로 1차원처럼 출력

    result = [0] * 10
    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in case:
        if i == 'ZRO':
            result[0] += 1
        if i == 'ONE':
            result[1] += 1
        if i == 'TWO':
            result[2] += 1
        if i == 'THR':
            result[3] += 1
        if i == 'FOR':
            result[4] += 1
        if i == 'FIV':
            result[5] += 1
        if i == 'SIX':
            result[6] += 1
        if i == 'SVN':
            result[7] += 1
        if i == 'EGT':
            result[8] += 1
        if i == 'NIN':
            result[9] += 1

    print(N)
    last = ''
    for b in range(10):     # num 별로 반복
          last += ((num[b] + ' ') * result[b])    # 각 result에 담긴 숫자만큼 반복append
    print(last)