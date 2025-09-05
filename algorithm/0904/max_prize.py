def dfs(n):  # 탐색 시작할 인덱스 받아 처음은 0
    global max_result

    # 종료조건: 주어진 교환횟수 모두 사용
    if n == cnt:
        # 현재 리스트를 숫자로 만들어서 최대값과 비교 후 갱신
        max_result = max(max_result, int("".join(li)))
        return

    # 모든 교환 조합 만들어서 검증
    # 0번부터 i번 카드, i+1번부터 j번 카드 뽑아 교환
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            # 두 카드 교환
            li[i], li[j] = li[j], li[i]

            # 중복 탐색 방지: 같은 깊이에서 같은 숫자가 나온적 있으면
            # 더이상 탐색할 필요 없음 (가지치기)
            state = (n, "".join(li))
            if state not in visited:
                visited.add(state)
                # 다음 교환을 위해 재귀 호출
                dfs(n+1)

            # 원래 상태로 복귀 (백트래킹)
            # 다른 조합을 시도하기 위해 교환했던 카드를 다시 원위치
            li[i], li[j] = li[j], li[i]


T = int(input())
for C in range(1, T+1):
    word, count = input().split()

    # 카드리스트와 교환횟수 저장
    li = list(word)
    cnt = int(count)

    max_result = 0      # 현재 인덱스
    visited = set()     # 방문 기록 초기화

    dfs(0)      # 0부터 탐색

    print(f'#{C} {max_result}')