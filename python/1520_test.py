map_row, map_col = map(int, input().split(' '))
# print(map_col, map_row)

Map = []
checkMap = []
for i in range(map_row):
    element = map(int, input().split(' '))
    Map.append(list(element))

for j in range(map_row):
    temp = []
    for k in range(map_col):
        temp.append(1)
    checkMap.append(temp)

# print('Map', Map)
# print(checkMap)

checkMap[0][0] = 0
current = [Map[0][0], 0, 0]
target = [Map[map_row-1][map_col-1], map_row-1, map_col-1]
solution = 0
count = 0

# print('현재',current,'목표', target)
def findWay(current, target):
    # print('시작')
    global count
    global checkMap
    if current == target:
        count += 1
        # print('@@@@@@@@@@@@끝@@@@@@@@@@')
        checkMap = []
        for j in range(map_row):
            temp = []
            for k in range(map_col):
                temp.append(1)
            checkMap.append(temp)
        return
    if current[1] + 1 <= map_row-1 and current[0] > Map[current[1]+1][current[2]]:
        if checkMap[current[1] + 1][current[2]] != 0:
            # print('before1', current)
            newCurrent1 = ['','','']
            newCurrent1[0] = Map[current[1] + 1][current[2]]
            checkMap[current[1] + 1][current[2]] = 0
            # print(Map)
            # print(Map[current[1]+1][current[2]])
            newCurrent1[1] = current[1] + 1
            newCurrent1[2] = current[2]
            # print('after1', newCurrent1)
            findWay(newCurrent1, target)
    if current[1] - 1 >= 0 and current[0] > Map[current[1]-1][current[2]]:
        if checkMap[current[1] - 1][current[2]] != 0:
            # print('before2', current)
            newCurrent1 = ['','','']
            newCurrent1[0] = Map[current[1] - 1][current[2]]
            checkMap[current[1] - 1][current[2]] = 0
            newCurrent1[1] = current[1] - 1
            newCurrent1[2] = current[2]
            # print('after2', newCurrent2)
            findWay(newCurrent1, target)
    if current[2] + 1 <= map_col-1 and current[0] > Map[current[1]][current[2] + 1] :
        if checkMap[current[1]][current[2] + 1] != 0:
            # print('before3', current)
            newCurrent1 = ['', '', '']
            newCurrent1[0] = Map[current[1]][current[2] + 1]
            checkMap[current[1]][current[2] + 1] = 0
            newCurrent1[1] = current[1]
            newCurrent1[2] = current[2] + 1
            # print('after3', newCurrent3)
            findWay(newCurrent1, target)
    if current[2] - 1 > 0 and current[0] > Map[current[1]][current[2] - 1]:
        if checkMap[current[1]][current[2] - 1] != 0:
            # print('before4', current)
            newCurrent1 = ['', '', '']
            newCurrent1[0] = Map[current[1]][current[2] - 1]
            checkMap[current[1]][current[2] - 1] = 0
            newCurrent1[1] = current[1]
            newCurrent1[2] = current[2] - 1
            # print('after4', newCurrent4)
            findWay(newCurrent1, target)
    else:
        return

findWay(current, target)
print(count)
