iterateCount = int(input())

total = []
for i in range(1, 101):
    for j in range(1, 101):
        total.append((i,j))
total = set(total)

for i in range(iterateCount):
    xy = input().split(' ')
    x1 = int(xy[0])
    x2 = x1 + 10
    y1 = int(xy[1])
    y2 = y1 +10
    subtotal = []
    for j in range(x1+1, x2+1):
        for z in range(y1+1, y2+1):
            subtotal.append((j,z))
    subtotal = set(subtotal)
    total = total - subtotal
print(10000 - len(total))


