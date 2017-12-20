command = input().split(' ')

mapSize = []
mapSize.append(int(command[0]))
mapSize.append(int(command[1]))
print(mapSize, type(mapSize))

mapSize_x = mapSize[0]
mapSize_y = mapSize[1]

diceLocate = []
diceLocate.append(int(command[2]))
diceLocate.append(int(command[3]))
dice_x = diceLocate[0]
dice_y = diceLocate[1]
print(dice_x,type(dice_x), dice_y, type(dice_y) )

#좌,우,위,아래,앞,뒤 순서
diceShape = [0,0,0,0,0,0]

grid = []
for i in range(int(command[0])):
    temp = []
    num = input().split(' ')
    for j in range(int(command[1])):
        temp.append(int(num[j]))
    grid.append(temp)
print(grid)

command2 = input().split(' ')
for j in range(len(command2)):
    command2[j] = int(command2[j])
    if command2[j] == 1:
        dice_y = dice_y + 1
        if dice_y > mapSize_y - 1:
            dice_y = dice_y - 1
            continue
        # print(dice_x, dice_y)
        if grid[dice_x][dice_y] !=0 :
            diceShape = [diceShape[3], diceShape[2], diceShape[0], diceShape[1], diceShape[4], diceShape[5]]
            diceShape[3] = grid[dice_x][dice_y]
            grid[dice_x][dice_y] = 0
            print(diceShape[2])
        elif grid[dice_x][dice_y] ==0 :
            diceShape = [diceShape[3], diceShape[2], diceShape[0], diceShape[1], diceShape[4], diceShape[5]]
            grid[dice_x][dice_y] = diceShape[3]
            print(diceShape[2])
    elif command2[j] == 2:
        dice_y = dice_y - 1
        if dice_y < 0:
            dice_y = dice_y + 1
            continue
        if grid[dice_x][dice_y] !=0 :
            diceShape = [diceShape[2], diceShape[3], diceShape[1], diceShape[0], diceShape[4], diceShape[5]]
            diceShape[3] = grid[dice_x][dice_y]
            grid[dice_x][dice_y] = 0
            print(diceShape[2])
        elif grid[dice_x][dice_y] ==0 :
            diceShape = [diceShape[2], diceShape[3], diceShape[1], diceShape[0], diceShape[4], diceShape[5]]
            grid[dice_x][dice_y] = diceShape[3]
            print(diceShape[2])
    elif command2[j] == 3:
        dice_x = dice_x - 1
        if dice_x < 0:
            dice_x = dice_x + 1
            continue
        if grid[dice_x][dice_y] !=0 :
            diceShape = [diceShape[0], diceShape[1], diceShape[4], diceShape[5], diceShape[3], diceShape[2]]
            diceShape[3] = grid[dice_x][dice_y]
            grid[dice_x][dice_y] = 0
            print(diceShape[2])
        elif grid[dice_x][dice_y] ==0 :
            diceShape = [diceShape[0], diceShape[1], diceShape[4], diceShape[5], diceShape[3], diceShape[2]]
            grid[dice_x][dice_y] = diceShape[3]
            print(diceShape[2])
    elif command2[j] == 4:
        dice_x = dice_x + 1
        if dice_x > mapSize_x - 1:
            dice_x = dice_x -1
            continue
        if grid[dice_x][dice_y] !=0 :
            diceShape = [diceShape[0], diceShape[1], diceShape[5], diceShape[4], diceShape[2], diceShape[3]]
            diceShape[3] = grid[dice_x][dice_y]
            grid[dice_x][dice_y] = 0
            print(diceShape[2])
        elif grid[dice_x][dice_y] ==0 :
            diceShape = [diceShape[0], diceShape[1], diceShape[5], diceShape[4], diceShape[2], diceShape[3]]
            grid[dice_x][dice_y] = diceShape[3]
            print(diceShape[2])
