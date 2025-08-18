T = int(input())
for T in range(1, T + 1):
    word = input().strip()
    stack = []

    for i in range(len(word)):
        if stack and stack[-1] == word[i]:
            stack.pop()
        else:
            stack.append(word[i])

    print(f'#{T} {len(stack)}')