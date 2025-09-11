def recur(n, cnt):
    global count

    if cnt > count:   # 충전횟수가 최종 충전횟수를 넘으면 나가
        return

    # 골 넘어가면, 최소횟수 저장후 종료
    if n >= N:
        count = min(count, cnt-1)   # 처음에 1번일때 cnt+1한거 빼서 비교
        return

    # 다음은 어디로 갈까
    # 현위치 다음칸부터 배터리를 추가한 곳까지
    for nex in range(n+1, n+arr[n]+1):
        recur(nex, cnt+1)   # 다음갈수있는 곳과 (1번빼고)충전하면서 가니까 cnt+1


T = int(input())
for x in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]      # 정류장수.
    count = N       # 충전횟수. 초기값은 최대충전수

    recur(1, 0) # 출발점 1, 현재 충전수 0

    print(f'#{x} {count}')