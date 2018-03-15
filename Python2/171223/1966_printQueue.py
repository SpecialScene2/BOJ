from sys import stdin

read = lambda : stdin.readline().rstrip()
element = int(read())
print(element)

for i in range(element):
    read = lambda: stdin.readline().rstrip()

    element = list(map(int,read().split()))
    print(element)
    totalCount = element[0]
    target = element[1]

    if totalCount == 1 and target == 0:
        read2 = lambda: stdin.readline().rstrip()
        element2 = list(map(int, read2().split()))
        print('element2',element2)
        print(1)
    else:
        read2 = lambda: stdin.readline().rstrip()

        element2 = list(map(int,read2().split()))
        print('element2', element2)
        targetValue = element2[target]
        print('totalcount', totalCount)
        for j in range(totalCount):
            first = element2[j]
            maxValue = max(element2[j:])
            idx = element2.index(maxValue)
            if first == target:
                if first == maxValue:
                    print('haha1', j+1)
                    break
                else:
                    element2 = element2[idx:] +element2[:idx]
                    print('haha2', element2, target)
                    if target < idx:
                        target = len(element2) - idx
                    else:
                        target -= idx
            else:
                element2 = element2[idx:] + element2[:idx]
                print('haha2', element2, target)
                if target < idx:
                    target = len(element2) - idx
                else:
                    target -= idx
