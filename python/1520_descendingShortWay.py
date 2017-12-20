map_row, map_col = map(int, input().split(' '))
# print(map_col, map_row)

Map = []
for i in range(map_row):
    element = map(int, input().split(' '))
    Map.append(list(element))
print('Map', Map)

current = [Map[0][0], 0, 0]
target = [Map[map_row-1][map_col-1], map_row-1, map_col-1]
solution = 0
count = 0

# print('현재',current,'목표', target)
def findWay(current, target):
    # print('시작')
    global count
    if current == target:
        count += 1
        # print('@@@@@@@@@@@@끝@@@@@@@@@@')
        return
    if current[1] + 1 <= map_row-1 and current[0] > Map[current[1]+1][current[2]]:
        # print('before1', current)
        newCurrent1 = ['','','']
        newCurrent1[0] = Map[current[1] + 1][current[2]]
        # print(Map)
        # print(Map[current[1]+1][current[2]])
        newCurrent1[1] = current[1] + 1
        newCurrent1[2] = current[2]
        # print('after1', newCurrent1)
        findWay(newCurrent1, target)
    if current[1] - 1 >= 0 and current[0] > Map[current[1]-1][current[2]]:
        # print('before2', current)
        newCurrent2 = ['','','']
        newCurrent2[0] = Map[current[1] - 1][current[2]]
        newCurrent2[1] = current[1] - 1
        newCurrent2[2] = current[2]
        # print('after2', newCurrent2)
        findWay(newCurrent2, target)
    if current[2] + 1 <= map_col-1 and current[0] > Map[current[1]][current[2]+1]:
        # print('before3', current)
        newCurrent3 = ['', '', '']
        newCurrent3[0] = Map[current[1]][current[2] + 1]
        newCurrent3[1] = current[1]
        newCurrent3[2] = current[2] + 1
        # print('after3', newCurrent3)
        findWay(newCurrent3, target)
    if current[2] - 1 > 0 and current[0] > Map[current[1]][current[2]-1]:
        # print('before4', current)
        newCurrent4 = ['', '', '']
        newCurrent4[0] = Map[current[1]][current[2] - 1]
        newCurrent4[1] = current[1]
        newCurrent4[2] = current[2] - 1
        # print('after4', newCurrent4)
        findWay(newCurrent4, target)

findWay(current, target)
print(count)

