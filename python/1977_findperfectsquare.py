first = int(input())
last = int(input())

container = []
if first <= last:
    # 두 수 모두 완전 제곱근이 아닌 경우
    if first ** (0.5) != int(first ** (0.5))  and last ** (0.5) != int(last ** (0.5)):
        first = int(first ** (0.5))
        last = int(last ** (0.5))
        if not list(range(first,last)):
            print(-1)
        else:
            for i in range(first+1, last+1):
                container.append(i**2)
            print(sum(container))
            print(container[0])
    # 두 수 모두 완전 제곱근인 경우
    elif first ** (0.5) == int(first ** (0.5)) and last ** (0.5) == int(last ** (0.5)):
        first = int(first ** (0.5))
        last = int(last ** (0.5))
        if not list(range(first,last)):
            print(-1)
        else:
            for i in range(first, last+1):
                container.append(i**2)
            print(sum(container))
            print(container[0])
    elif first ** (0.5) == int(first ** (0.5)) and last ** (0.5) != int(last ** (0.5)):
        first = int(first ** (0.5))
        last = int(last ** (0.5))
        if not list(range(first,last)):
            print(-1)
        else:
            for i in range(first, last + 1):
                container.append(i**2)
            print(sum(container))
            print(container[0])
    elif first ** (0.5) != int(first ** (0.5)) and last ** (0.5) == int(last ** (0.5)):
        first = int(first ** (0.5))
        last = int(last ** (0.5))
        if not list(range(first,last)):
            print(-1)
        else:
            for i in range(first + 1, last+1):
                container.append(i**2)
            print(sum(container))
            print(container[0])
else:
    print(-1)