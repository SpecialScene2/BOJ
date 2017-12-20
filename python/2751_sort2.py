# N = int(input())
#
# container = []
# for i in range(N):
#     element = int(input())
#     container.append(element)
#
# result = []
# for j in range(N):
#     Min = container[j]
#     for k in range(j+1, N):
#         if Min > container[k]:
#             Min, container[k] = container[k], Min
#     container[j] = Min
#
# for k in container:
#     print(k)

N = int(input())

container = []
for i in range(N):
    element = int(input())
    container.append(element)
print(container)
def quickSort(list):
    center=''
    if len(list) == 1:
        print(list[0])
    elif len(list) % 2== 0:
        center = len(list) % 2
    else:
        center = int(len(list)/2) + 1
    standard = list[center]
    left = []
    right = []

    for i in list:
        if center >= i:
            right.append(i)
        else:
            left.append(i)
    quickSort(left)
    print(standard)
    quickSort(right)
quickSort(container)



