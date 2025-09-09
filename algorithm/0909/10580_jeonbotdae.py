T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 1. N개의 새로운 선이 추가 (기존의 전선과 비교)
    wires = []          # 기존전선 저장 리스트
    answer_count = 0    # 교차점수

    for _ in range(N):
        s, e = map(int, input().split())

        # 기존 전선과 비교 (교차점 비교)
        for prey_start, prey_end in wires:
            # 1. 기존의 전선보다 시작점이 높고 도착점이 낮음
            if s > prey_start and e < prey_end:
                answer_count += 1
            # 2. 기존의 전선보다 시작점이 낮고 도착점이 높음
            if s < prey_start and e > prey_end:
                answer_count += 1

        # 목록에 추가
        wires.append((s,e))

    print(f'#{tc} {answer_count}')