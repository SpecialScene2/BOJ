num = int(input())
container = []

for i in range(num):
    order = input().split()
    if order[0] == 'push':
        container.append(int(order[1]))
    elif order[0] == 'size':
        print(len(container))
    elif order[0] == 'pop':
        if container:
            print(container.pop())
        else:
            print(-1)
    elif order[0] == 'top':
        if container:
            print(container[-1])
        else:
            print(-1)
    elif order[0] =='empty':
        if container:
            print(0)
        else:
            print(1)
