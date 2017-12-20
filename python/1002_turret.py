testNum = int(input())

for i in range(testNum):
    result = []
    element = input().split(' ')
    x1 = int(element[0])
    y1 = int(element[1])
    r1 = int(element[2])

    x2 = int(element[3])
    y2 = int(element[4])
    r2 = int(element[5])

    d = ((((x2-x1)**2) + ((y2-y1)**2))) ** 0.5

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        #1 접점이 1개인 경우
        if r1 + r2 == d: # 내접은 아니지만 한점에서 만나는 경우
            print(1)
        elif r1 - r2 == d or r2 - r1 == d: # 내접하면서 한점에서 만나는 경우
            print(1)
        elif abs(r1-r2)< d < abs(r1 +r2):
            print(2)
        elif abs(r1-r2) > d:
            print(0)
        elif r1 + r2 < d: # 못 만나는 경우
            print(0)