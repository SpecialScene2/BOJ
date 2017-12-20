totalNumber = int(input())

container = []
for i in range(totalNumber):
    a = int(input())
    container.append(a)
# print(container)

for z in range(totalNumber):
    for j in range(totalNumber-z-1):
        if container[j] > container[j+1]:
            container[j], container[j+1] = container[j+1], container[j]
for k in container:
    print(k)
