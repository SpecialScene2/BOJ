from sys import stdin, stdout

read = lambda: stdin.readline().rstrip()
element = list(read())
# element = ['(', '(', ')', '[', '[', ']', ']', ')', '(', '[', ']', ')']
# print(element)

def checker(element):
    stack1 = []
    stack2 = []
    for i in element:
        if i == '(':
            stack1.append(i)
        elif i == '[':
            stack2.append(i)
        elif i == ')':
            # if i>0 and element[-1] == '[':
            #     print(0)
            #     return
            # elif stack1:
            #     stack1.pop()
            # else:
            #     print(0)
            #     return
            try:
                stack1.pop()
            except:
                continue
            break
        elif i == ']':
            # if i>0 and element[-1] == '(':
            #     print(0)
            #     return
            # elif stack2:
            #     stack2.pop()
            # else:
            #     print(0)
            #     return
            try:
                stack2.pop()
            except:
                continue
            break
    if stack1 or stack2:
        print(0)
    else:
        calculator(element)

def calculator(element):
    stack1 = []
    top = element[0]
    for i in element:
        if i == '(' or i == '[':
            stack1.append(i)
            top = i
        elif i == ')' and top == '(':
            stack1.pop()
            stack1.append(2)
            top = stack1[-1]
        elif i == ']' and top == '[':
            stack1.pop()
            stack1.append(3)
            top = stack1[-1]
        elif i == ')' and type(top) == int:
            temp = 0
            for i in reversed(stack1):
                if i == '(':
                    temp *= 2
                    stack1.remove(i)
                    stack1.append(temp)
                    top = stack1[-1]
                    break
                elif type(i) == int:
                    temp += i
                    stack1.remove(i)

        elif i == ']' and type(top) == int:
            temp = 0
            for i in reversed(stack1):
                if i == '[':
                    temp *= 3
                    stack1.remove(i)
                    stack1.append(temp)
                    top = stack1[-1]
                    break
                elif type(i) == int:
                    temp += i
                    stack1.remove(i)
    try:
        print(sum(stack1))
    except:
        print(0)
        return
checker(element)