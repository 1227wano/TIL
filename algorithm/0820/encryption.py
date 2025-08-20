T = 10
for tc in range(1, T+1):
    N = int(input())    # 테케번호
    arr = list(map(int, input().split()))
    stop = False

    while not stop:
        for x in range(1, 6):
            a = arr[0]
            for i in range(7):
                arr[i] = arr[i+1]
            if a-x <= 0:
                arr[7] = 0
                stop = True
                break
            else:
                arr[7] = a-x

    result = ' '.join(map(str, arr))

    print(f'#{tc} {result}')

    # -----------------------------------------------------------------
    # circular queue
    # front = 0
    # rear = 7

    # cq = deque(arr, maxlen=8) # arr라는 리스트로 고정길이 8인 원형 큐
    # flag = 0    # 원소 중 하나가 0이 될때까지 반복하기 위한 stopper
    # def circulation(n):
    #     global cq
    #     cq.rotate(-1)  # 왼쪽으로 값들을 회전
    #     cq = deque([(x - 1) % 10 for x in cq], maxlen=8)
    #     cq에서 하나씩 뽑아서 -1한 후 변환

    # -----------------------------------------------------------------
    # front = rear = 0
    # status
    # def is_empty():
    #     return front == rear
    #
    # def is_full():
    #     return (rear + 1) % len(arr) == front
    # # injection
    # def enqueue(item):
    #     global rear
    #     if is_full():
    #         print('queue_full')
    #     else:
    #         rear = (rear + 1) % len(arr)
    #         arr[rear] = item
    # # delete
    # def dequeue():
    #     global front
    #     if is_empty():
    #         print('queue_empty')
    #     else:
    #         front = (front + 1) % len(arr)
    #         return arr[front]
