T = 10
for test in range(1, T + 1):
    dump = int(input())
    boxes = list(map(int, input().split()))
    result = 0
    maxi = 0  # 최고점 인덱스
    mini = 0  # 최저점 인덱스

    for i in range(dump):
        maxi = boxes.index(max(boxes))  # max인덱스 번호
        boxes[maxi] -= 1
        mini = boxes.index(min(boxes))  # min인덱스 번호
        boxes[mini] += 1

    result = max(boxes) - min(boxes)
    print(f'#{test} {result}')