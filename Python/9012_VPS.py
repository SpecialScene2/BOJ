Number = int(input())

for i in range(Number):
    stack = []
    stack2 = []
    element = list(input())
    # print(element)
    for j in element:
        if j == '(':
            stack.append(j)
        else:
            if not stack:
                # print(1)
                stack2.append(j)
            else:
                stack.pop()
    # print('Stack1:',stack)
    # print('Stack2:',stack2)
    if stack or stack2:
        print('NO')
    if not stack and not stack2:
        print('YES')