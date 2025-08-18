T = int(input())
for T in range(1, T+1):
    word = input()
    stack = []
    ans = 1     # 실패하면 ans = 0

    for i in word:
        if i in '({':           # ( 이나 { 이면
            stack.append(i)     # stack 에 넣고
        elif i in ')}':         # ) 이나 } 일때
            if not stack:       # 일단 stack 비어있으면 실패
                ans = 0
                break
            top = stack.pop()   # 먼가 있으면 stack 최신값 뽑아서

            # ({)} 같은 케이스 방지
            if i == ')' and top != '(':     # 지금 ) 인데 최신값이 ( 이 아니면 실패
                ans = 0
                break
            if i == '}' and top != '{':     # 지금 } 인데 최신값이 { 이 아니면 실패
                ans = 0
                break
            # 위 조건 다 넘기면 괄호의 짝을 잘 찾은거라 ans 그대로 1

    if stack:       # 만약 stack에 괄호 남아있으면 실패
        ans = 0

    print(f'#{T} {ans}')