# def div(t, num):      # 타겟수와 나눌수
#     if t == 1:
#         return 0
#     if t % num == 0:
#         number[num] += 1
#         div(t/num, num)
#     else:
#         num += 1
#         div(t, num)

T = int(input())
for T in range(1, T+1):

    target = int(input())         # 27
    # number = [0] * 1000000      # 어떤수로 몇번 나눴는지 세는용?
    # num = 2                     # 나눌 어떤 수
    #
    # result = div(target, num)
    #
    # if result == 0:
    #     number

    for i in range(1, 1000002):
        if i ** 3 == target:
            print(f'#{T} {i}')
            break
        elif i == 1000001:
            print(f'#{T} -1')