container = []
for i in range(9):
    container.append(int(input()))
totalHeight = sum(container)


for j in range(len(container)):
    for z in range(j+1,len(container)):
        if totalHeight -(container[j]+container[z]) == 100:
            temp1 = container[j]
            temp2 = container[z]
            container.remove(temp1)
            container.remove(temp2)
            # print(container)
            container = sorted(container)
            # print(container)
            break
for k in container:
    print(k)