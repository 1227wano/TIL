import sys
sys.stdin = open("input.txt")


def recur(m_index, total_cost):
    global mini

    if m_index > 12:
        # Todo : 최소값 갱신
        mini = min(total_cost, mini)
        return

    # 1일 이용권으로 사는 경우
    recur(m_index + 1, total_cost + (days[m_index] * day))

    # 1달 이용권으로 사는 경우
    recur(m_index + 1, total_cost + month)

    # 3달 이용권으로 사는 경우
    recur(m_index + 3, total_cost + month3)

    # 1년 이용권으로 사는 경우
    recur(m_index + 12, total_cost + year)     # 12월 넘어가서 끝


T = int(input())
for tc in range(1, T+1):
    day, month, month3, year = map(int, input().split())    # 이용권
    days = [0] + list(map(int, input().split()))    # 1월 = 1인덱스
    mini = 3000 * 12 * 31   # 이용권 최대가격 3000
    recur(1, 0)
    print(f'#{tc} {mini}')