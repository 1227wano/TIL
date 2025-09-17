import sys
sys.stdin = open("input.txt")


def recur(start_ham, kal):
    global point, ham_kal

    if start_ham == N:
        return

    if kal >= L:
        return

    maxi = 0    # 비교용 점수
    for i in range(N):
        # 아직 안쓴 재료고, 햄부기칼로리에 더해도 제한 이하일때
        if not visited[i] and kal + sor[i][1] <= L:
            visited[i] = True
            maxi += sor[i][0]
            kal += sor[i][1]
            recur(start_ham+1, kal)
            visited[i] = False

    if maxi > point:
        point = maxi


T = int(input())
for T in range(1, T+1):
    N, L = map(int, input().split())    # 재료수, 제한칼로리
    hamburgers = [list(map(int, input().split())) for _ in range(N)]

    # 맛-칼로리 적은 순으로 정렬해서 넣어갈때 빠를듯?
    sor = sorted(hamburgers, key=lambda x: (abs(x[0] - x[1]), -x[1]))

    point = 0       # 햄부기 최종 점수
    ham_kal = 0     # 햄부기 칼로리
    visited = [False] * N     # 재료 소진 여부

    recur(0, 0)     # 시작 인덱스와 시작 칼로리

    print(f'#{T} {point}')